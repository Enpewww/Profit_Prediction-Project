import streamlit as st
import plot as ep

def eda():
    # isi page
    # title
    st.title("Exploratory Data Analysis")
    eda = st.selectbox('Pilih EDA',['How the distribution of Profit based on transaction in Year, Month, and Day of Week?', 'How the correlation of Profit to Sales, Quantity, and Cost?', 'How the yearly and monthly trend of Profit, Sales, and Cost being compared?', 'How much the difference between Sales and Revenue based on Country, Region, and State?', 'How the performance of Profit and Sales in States in particular Countries?', 'How much Profit and Cost distinct by the shipping methods?'])

    st.markdown("---")

    # EDA
    if eda == 'How the distribution of Profit based on transaction in Year, Month, and Day of Week?':
        # EDA 1 
        st.markdown("The Distribution of profit in a Year, Month, and Day of Week")
        st.pyplot(ep.eda1())
        st.markdown('''
                    This distribution graph is very crucial into our analysis because it consist the pattern when the peak of the profit generated. The graph generated the mean of all year and compare it to each other by periodes.

                    1. Profit by Order Year (Transaction per Year) -> Figure 1:

                    - Insight:

                        - 2018 was the most profitable year on average.

                        - Profit seems to declined in 2020, likely due to market disruptions of pandemic (Covid-19).

                        - The standard deviation bars suggest that year-to-year variance is relatively stable, but drop in 2020 is consistent.

                    - Business Implication:

                        - The company should be investigate what been done in peak year as 2018. As the bar shows in 2020 the cyclical begin to show because of Pandemic Era.

                        - Plan mitigation for similar downturns or seasonal shifts in future years.

                    2. Profit by Order Month (Transaction per Month) -> Figure 2:

                    - Insight:

                        - November is the peak month for profit, this might be due to seasonal sales events like Black Friday, 11.11, or pre-holiday shopping (where customer have more higher income compare to other month).

                        - February and August show lower profits, possibly due to post-holiday slumps or vacation periods.

                        - June, July, September, and October also show strong profit performance.

                    - Business Implication:

                        - Focus marketing and inventory planning on high-profit months (Nov, Oct, Jun).

                        - Promotions or bundled sales to boost performance.

                        - Cost control strategies.

                        - Customer re-engagement campaigns.

                    3. Profit by Week (Transaction per Week) -> Figure 3

                    - Insight: 

                        - Sunday (6) shows the highest profit, significantly outperforming other days.

                        - Monday (0) and Friday (4) are also strong performers.

                        - Tuesday (1) and Thursday (3) are the lowest, consistently underperforming.

                        - Sunday has higher variation in profit (likely due to sales spikes or campaign effects).

                        - Weekdays show less variance, possibly indicating stable but modest performance.

                    - Business Implication:

                        - Focus promotions, exclusive releases, or email campaigns on Sunday, Monday, and Friday to amplify high-profit behavior.

                        - For Tuesday and Thursday, try limited-time deals, bundled products, or free shipping offers to lift profits.

                        - Sunday’s success might be linked to consumer free time or payday weekends, the company could leverage this with social ads or reminders.
                    ''')
        st.markdown("---")

    elif eda == 'How the correlation of Profit to Sales, Quantity, and Cost?':
        # EDA 2
        st.markdown("The Distribution of profit in a Year, Month, and Day of Week")
        st.pyplot(ep.eda2())
        st.markdown('''
                    | Features Corr. | Correlation Value | Intepretation |
| --- | --- | ---|
| Cost - Sales | 0.83 | Strong Correlation and Positive |
| Cost - Profit | 0.44 | Moderate Correlation and Positive |
| Profit - Sales | 0.82 | Strong Correlation and Positive |
| Quantity - Sales | 0.41 | Moderate Correlation and Positive |
| Quantity - Profit | 0.33 | Weak Correlation and Positive |
| Quantity - Cost | 0.35 | Weak Correlation and Positive |

Business Insight:

1. Cost has a stronger correlation with Sales (0.83) than with Profit (0.44).

  - This indicates that as Cost increases, Sales tend to increase significantly, suggesting that higher operational or marketing spending maybe contributing to more sales volume as it shows on the graph.

  - However, Profit is only moderately correlated with Cost, meaning that not all increased Cost leads to increased Profit. Some of the additional Cost may not convert efficiently into bottom-line gains due to factors like discounts, returns, or operational inefficiencies. Which means, it indicates that if company generate more sales and make some profit it will increase the cost either but not that significant.

2. Profit is strongly correlated with Sales (0.82).

  - A higher Sales figure tends to directly relate to higher Profit, which is expected in most businesses.

  - This suggests that strategies to increase sales volume may effectively improve profitability, assuming costs are controlled (back to the correlation of cost with sales it directly positive).

3.  Quantity has a weaker relationship with both Profit (0.33) and Sales (0.41).

  - Selling more units does not always guaranteed increase profit and sales proportionally.

  - This might implied the discount or even promotional campaign that company applied doesn't seem to scale profitablity even more.
''')

    elif eda == 'How the yearly and monthly trend of Profit, Sales, and Cost being compared?':
        # EDA 3
        st.markdown("Trend by Sales, Profit, and Cost")
        st.pyplot(ep.eda3())
        st.markdown('''
Summing up from the trend graph above we can conclude that:

1. Yearly Trend: Sales, Profit, and Cost
  
    - Sales is constantly increase from 2017 and 2020 it indicates consistent growth overtime.
  
    - Profit increase in early year of the dataset, but the growth seems to decrease in more recent year (2019-2020).

    - Cost is significantly increasing from 171747 to 214715 dollar (2019 and 2020), it even overlap profit growth in those particular year.

- Business Insight:

    - Although sales seemingly to increase, margin of profit is shows to decline because of the cost increasing overtime.

    - Need to relocate the cost in the recent year to increase the perfomance of the profit.

    - Company could discussed to apply some automation in the business process, or even efficiency of operational cost overtime.

2. Monthly Trend: Sales, Profit, and Cost

    - For the month trend there is a clear seasonal pattern.

    - Sales peak significantly in June (6), August (8), and November (11).

    - The increase in sales is consistently accompanied by the rises in both of profit and cost, with the highest peak indicates in August (8), and November (11).

    - March (3) and April (4) show the lowest performance across all metrics.

- Business Insight:

  - June (6), August (8), and November (11) hold high business potential to sell.

  - It is recommended to strengthen marketing campaigns and stock preparation in the weeks leading up to these peak months.

  - March (3) and April (4) could be ideal or focusing on internal improvements and operational efficiency, as market demand tends to decreasing.

''')
    elif eda == 'How much the difference between Sales and Revenue based on Country, Region, and State?':
        # EDA 4
        st.markdown("Sales and Revenue Based on Country, Region, and State")
        st.pyplot(ep.eda4())
        st.markdown('''
From the graph that compares total sales (`tot_sales`) and total profit (`tot_profit`) across three regions, we can conclude that:

1. Descriptive Analysis: 

  - Central Region plays a crucial role for sales generated and profit generated compared to other Regions. 

    - Sales: Reaching 698,245 dollar, which is more double the sales either he North or South region. This indicates very strong market dominance of this region.

    - Profit: Generating 345,216 dollar, and also the highest in absolute terms. This is the company's main cash flow of performance.

  - North Region this region holds the second position in sales but the last position in profit.

    - Sales: Reach for the certain amount of 289,019 dollar.

    - Profit: Reach for the certain amount of 139,782 dollar.

  - South Region is interesting because although it has the lowest sales, its profit slightly outperforms the North Regions.

    - Sales: South region shows the lowest of sales of the three, 280,300 dollar.

    - Profit: At 141,969 dollar, it is slightly higher than the North's

2. Profitability (Profit Margin):

- To gain deeper business insight from the metrics, we cannot only look to the absolute values. We need to calculate the Profit Margin (Profit Efficiency) for each region using the formula (total_profit/total_sales*100):

  - Central: (345,216 / 698,245) * 100% = 49.44%
  
  - North: (139,782 / 289,019) * 100% = 48.36%
  
  - South: (141,969 / 280,300) * 100% = 50.65%
  
- From this calculation: Although Central is the largest region, it is not the most efficient at converting sales into profit. The South is the most efficient/profitable region. Every 100 dollar in sales in the South generates 50.6 dollar in profit, higher than any other region. The North is the region with the lowest profitability.

3. Business Insights and Recommendations: Based on the analysis above, we can draw several strategic conclusions and provide actionable recommendations.

- The company has two types of regions with distinct characteristics:
    
    - The High-Volume Region: The Central region is the main actor that serving as the backbone of the company's revenue and profit.
    
    - The High-Efficiency Region: The South region is a most consistent in the term of profit, with the most profitable growth potential.
    
    - The Area for Improvement: The North region is lagging slightly, both in terms of sales (compared to Central) and efficiency (compared to the South).

- Strategic Recommendation:

  - For the Central Region: the objective is to protect the main revenue stream (Maintain & Optimize).

  - For the South Region: the objective is to increase sales in the most profitable area (Invest & Grow).

  - For the North Region: the objective is to identify the causes of the low performance (Analyze & Improve).
''')
        
    elif eda == 'How the performance of Profit and Sales in States in particular Countries?':
        # EDA 5
        st.markdown("Profit and Sales performance by State and Countries")
        st.pyplot(ep.eda5())
        st.markdown('''
From the graph above I could inferred with the explanation below:

- This figure shows Healthy Business Model: The scatter plot indicates a strong positive correlation between sales and profit as sales increase, the profits follows consistently, indicating a good consistent business.

- Although it has a good consistent business performance, unprofitable a andreas still exist. Location are on or below the "red-line" which indicates ther are several geographical area that still unprofitable and still costly on the resources.

- The market dominance still appear and it has a pattern. As seen explicitly shows that country like united kingdom is kind of like a "Superstar" in this dataset. Therefore, to gain this pattern and insight is crucial to out analysis and output.
''')
        
    elif eda == 'How much Profit and Cost distinct by the shipping methods?':
        # EDA 6
        st.markdown("Profit and Cost Comparisons by Ship Mode")
        st.pyplot(ep.eda6())
        st.markdown('''
Summary:

The economy shipping mode is the company's primary generating profit, it has indicators that customer using economy ship mode means it drives the vast majority of sales, cost, and profits. While all shipping methods appears to be profitable, the Priority shipping mode stands out to be the most efficient, and it demonstrating the best ratio of profit to cost. Although of the terms of "profitable", The Immediate shipping mode is suggesting the high value, but it is count as the smallest and least impactful channel.

Business Recommendation:

1. Try to protect and optimze the economy shipping mode. Any small improvement in its cost efficiency could lead to significant gains for the company.

2. The company should analyze and investigate the type of product that customer bought using this ship mode. There is a clear opportunity to grow this highly efficient channel by promoting its value to more customer (through shipping promotions).

3. Lastly, company try to review the Economy Plus shipping mode for less efficient output. From the base assumptions, this shipping mode costs really to high for the product, or are the products sold through it lower-margin.
''')

if __name__ == "main":
    eda()