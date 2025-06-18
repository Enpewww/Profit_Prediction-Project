import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_new = pd.read_csv('src/Data_Deploy.csv')
numeric_cols = ['Quantity', 'Cost', 'Sales']

year_tre = df_new.groupby('Order_Year')[['Sales', 'Profit', 'Cost']].sum().reset_index()
year_tre = year_tre.sort_values('Order_Year')
month_tre = df_new.groupby('Order_Month')[['Sales', 'Profit', 'Cost']].sum().reset_index()
month_tre = month_tre.sort_values('Order_Month')
region_performance = df_new.groupby('Region').agg(
    tot_sales = ('Sales', 'sum'),
    tot_profit = ('Profit', 'sum')
).reset_index()

region_melted = pd.melt(
    region_performance,
    id_vars=['Region'], # Unpivot Column
    value_vars=['tot_sales', 'tot_profit'], # Column that combined
    var_name='Comparison Metrics', # New Column named metrics
    value_name='Value' # Show value
)
geo_metrics = pd.pivot_table(
    df_new,
    index=['Country', 'State'],
    values=['Sales', 'Profit'],
    aggfunc='sum'
)

ship_mode = df_new.groupby('Ship_Mode').agg(
       tot_profit = ('Profit', 'sum'),
    tot_cost = ('Cost', 'sum'),
    tot_sales = ('Sales', 'sum')
)

def eda1():
 
    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(24, 6))

    # Plot 1: Order_Year vs Profit
    sns.barplot(data=df_new, x='Order_Year', y='Profit', ax=ax1)
    ax1.bar_label(ax1.containers[0])
    ax1.set_title('Profit per Year')

    # Plot 2: Order_Month vs Profit
    sns.barplot(data=df_new, x='Order_Month', y='Profit', ax=ax2)
    ax2.bar_label(ax2.containers[0])
    ax2.set_title('Profit per Month')

    # Plot 3: Order_DayOfWeek vs Profit
    sns.barplot(data=df_new, x='Order_DayOfWeek', y='Profit', ax=ax3)
    ax3.bar_label(ax3.containers[0])
    ax3.set_title('Profit per Day of Week')

    return fig


def eda2():
    # Subset hanya kolom numerik
    df_corr = df_new[numeric_cols]

    # Hitung matriks korelasi Spearman
    corr_mat = df_corr.corr(method='spearman')

    # Buat plot
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr_mat, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    ax.set_title('Heatmap Correlation (Spearman)')

    return fig

def eda3():
    # Make it one axis for 1 row and 2 columns
    fig, ax = plt.subplots(1, 2, figsize=(18,10))

    # Subplot for year
    sns.lineplot(ax=ax[0], data=year_tre, x='Order_Year', y='Sales', label='Sales', marker='o')
    sns.lineplot(ax=ax[0], data=year_tre, x='Order_Year', y='Profit', label='Profit', marker='o')
    sns.lineplot(ax=ax[0], data=year_tre, x='Order_Year', y='Cost', label='Cost', marker='o')

    # Loop for marker value
    for col in ['Sales', 'Profit', 'Cost']:
        for i in range(len(year_tre)):
            x = year_tre['Order_Year'].iloc[i]
            y = year_tre[col].iloc[i]
            ax[0].text(x, y, f"{int(y)}", ha='center', va='bottom', fontsize=8)

    ax[0].set_title('Yearly Trend: Sales, Profit, and Cost')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Value')
    ax[0].set_xticks(year_tre['Order_Year'].unique())
    ax[0].legend()
    ax[0].grid(True)

    # Subplot for month
    sns.lineplot(ax=ax[1], data=month_tre, x='Order_Month', y='Sales', label='Sales', marker='o')
    sns.lineplot(ax=ax[1], data=month_tre, x='Order_Month', y='Profit', label='Profit', marker='o')
    sns.lineplot(ax=ax[1], data=month_tre, x='Order_Month', y='Cost', label='Cost', marker='o')

    # Loop for marker value
    for col in ['Sales', 'Profit', 'Cost']:
        for i in range(len(month_tre)):
            x = month_tre['Order_Month'].iloc[i]
            y = month_tre[col].iloc[i]
            ax[1].text(x, y, f"{int(y)}", ha='center', va='bottom', fontsize=8)

    ax[1].set_title('Monthly Trend: Sales, Profit, and Cost')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Value')
    ax[1].set_xticks(month_tre['Order_Month'].unique())
    ax[1].legend()
    ax[1].grid(True)

    return fig

def eda4():
    fig = plt.figure(figsize=(10, 6))
    ax = sns.barplot(
        x='Region',
        y='Value',
        hue='Comparison Metrics',
        data=region_melted,
        palette='pastel'
    )

    # Setting the position of the annot
    for bar in ax.patches:
        y_val = bar.get_height()    # value for y setting height position
        x_pos = bar.get_x() + bar.get_width() / 2.0  # half of the width settings
        label = f"{int(y_val)}" # label using the value from the group data
        if y_val >= 0:
            ver_position = 'bottom'
        else:
            ver_position = 'top'
        plt.text(x_pos, y_val, label, ha='center', va=ver_position, fontsize=9, weight='bold')
    
    plt.title('Comparison of Sales vs Profit in each Region')
    plt.xlabel('Region', fontsize=12)
    plt.ylabel('Sales vs Profit (Value)', fontsize=12)
    plt.legend(title='Metrics')

    return fig 

def eda5():
    fig = plt.figure(figsize=(10, 8))
    scat_plot = sns.scatterplot(
        data=geo_metrics,
        x='Sales',
        y='Profit',
        hue='Country',  
        size='Sales',   
        sizes=(50, 1500), # Define the range of point sizes
        alpha=0.7,      # Use slight transparency to see overlapping points
        palette='viridis',
        legend='full'
    )

    # Add Horizontal Line
    plt.axhline(0, color='red', linestyle='--', linewidth=1.5, label='Profit')

    # Setting the Legend
    handles, labels = scat_plot.get_legend_handles_labels()
    size_legend_index = labels.index('Sales')
    country_handles = handles[1:size_legend_index]
    country_labels = labels[1:size_legend_index]
    plt.legend(handles=country_handles, labels=country_labels, bbox_to_anchor=(1.02, 1), loc='upper left') # bbox to anchor to set the location set for the legend following the pixels

    # Final touch
    plt.title('Sales vs Profit Geographical')
    plt.xlabel('Total Sales', fontsize=12)
    plt.ylabel('Total Profit', fontsize=12)

    return fig

def eda6():
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot stacked bar dengan Pandas plot, arahkan ke ax yang dibuat
    ship_mode.plot(
        kind='bar',
        stacked=True,
        ax=ax,
        color=['darkblue', 'lightgreen', 'red'],
        title='Ship Mode: Profit vs Cost vs Sales',
    )

    # Ambil container untuk setiap bar segment
    cost = ax.containers[0]
    profit = ax.containers[1]
    sales = ax.containers[2]

    # Tambahkan label ke setiap segmen
    ax.bar_label(cost, label_type='center', fontsize=8, color='white', weight='bold') 
    ax.bar_label(profit, label_type='center', fontsize=8, color='black', weight='bold')
    ax.bar_label(sales, label_type='center', fontsize=8, color='white', weight='bold')

    # Tambahan format
    ax.set_ylabel('Profit vs Cost vs Sales')
    ax.set_xlabel('Ship Mode', fontsize=9)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.legend(['Profit', 'Cost', 'Sales'], loc='center left', bbox_to_anchor=(1.02, 0.5))

    return fig