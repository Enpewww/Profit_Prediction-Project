import streamlit as st
import pandas as pd
import pickle
import os
from custom_date import DateExtractor

def run():
    # load and save model
    model_path = os.path.join(os.path.dirname(__file__), "..", "src/best_model_pred.pkl")
    with open(model_path, "rb") as f:
        best_model = pickle.load(f)

    # Title and Description
    st.title('E-Commerce Profit Prediction App')
    st.markdown('''
    This application predicts the profit for e-commerce orders based on user inputs. 
    Enter the order details below, and the app will predict the profit.
    ''')

    # Form for user input
    with st.form("Order Form"):
        st.subheader("Enter Transactions Details")

        # Create column for better layout
        col1, col2 = st.columns(2)

        with col1:
            order_id = st.number_input("Order ID", min_value=1, value=1000, step=1)
            order_date = st.text_input('Order Date (mm/dd/yyyy)', value='mm/dd/yyyy')
            customer_name = st.text_input('Customer Name', value=None)
            city = st.text_input('City', value='Groningen')
            country = st.selectbox('Country', ['Sweden', 'United Kingdom', 'France', 'Italy', 'Austria', 'Spain', 'Germany', 'Netherlands', 'Denmark', 'Belgium', 'Norway', 'Portugal', 'Switzerland', 'Ireland', 'Finland'])
            state = st.selectbox("State", ["Stockholm", "England", "Auvergne-Rhône-Alpes", "Provence-Alpes-Côte d'Azur", "Languedoc-Roussillon-Midi-Pyrénées", "Liguria", "Vienna", "Murcia", "Lower Saxony", "South Holland", "Västra Götaland", "Hovedstaden", "Valenciana", "South Denmark", "Lombardy", "Sicily", "Ile-de-France", "North Rhine-Westphalia", "Flemish Brabant", "Tuscany", "Emilia-Romagna", "Madrid", "Oslo", "Lisboa", "Saxony", "Andalusía", "Catalonia", "Alsace-Champagne-Ardenne-Lorraine", "Bavaria", "Uppsala", "Nord-Pas-de-Calais-Picardie", "Hesse", "Overijssel", "Basel-Stadt", "Bourgogne-Franche-Comté", "Zürich", "Dublin", "Lazio", "Namur", "North Holland", "Berlin", "Baden-Württemberg", "Aquitaine-Limousin-Poitou-Charentes", "Uusimaa", "Apulia", "Saxony-Anhalt", "Rogaland", "Sardinia", "Drenthe", "Mecklenburg-Vorpommern", "North Brabant", "Umbria", "Geneva", "Veneto", "Normandy", "Scotland", "Coimbra", "Castile and León", "Gelderland", "Hamburg", "Brandenburg", "Pays de la Loire", "Antwerp", "Bremen", "Thuringia", "Porto", "Utrecht", "Castile-La Mancha", "Brittany", "Campania", "Cork", "Groningen", "East Flanders", "Ceuta", "Halland", "Navarra", "Rhineland-Palatinate", "Limburg", "Upper Austria", "Schleswig-Holstein", "Tyrol", "Corsica", "Trentino-Alto Adige", "Vaud", "Piedmont", "Calabria", "Galicia", "Buskerud", "Centre-Val de Loire", "Styria", "Abruzzi", "Basque Country", "Cantabria", "Asturias", "Finland Proper", "Central Jutland", "Wales", "Kymenlaakso", "Friesland", "Braga", "Aveiro", "Marche", "Saarland", "Skåne", "Friuli-Venezia Giulia", "Balearic Islands", "Extremadura", "Basilicata", "Hedmark", "Hainaut", "Melilla", "Salzburg", "Carinthia", "Zeeland", "Hordaland", "Lucerne", "Liège", "West Flanders", "Bern", "Brussels", "Södermanland", "Zealand", "Galway", "Värmland", "Vest-Agder", "St. Gallen", "Setúbal"])
            region = st.selectbox("Region", ['Central', 'South', 'North'])

        with col2:
            segment = st.selectbox("Segment", ['Home Office', 'Corporate', 'Consumer'])
            category = st.selectbox("Category", ['Office Supplies', 'Furniture', 'Technology'])
            ship_mode = st.selectbox("Ship Mode", ['Economy Plus', 'Immediate', 'Economy', 'Priority'])
            sub_category = st.selectbox("Sub-Category", ['Paper', 'Bookcases', 'Art', 'Binders', 'Tables', 'Chairs', 'Appliances', 'Labels', 'Fasteners', 'Envelopes', 'Accessories', 'Furnishings', 'Copiers', 'Storage', 'Supplies', 'Phones', 'Machines'])
            product_name = st.text_input("Product Name", value='Ikea Classic Bookcase, Metal')
            quantity = st.number_input("Quantity", min_value=1, value=2, step=1)
            cost = st.number_input("Cost", min_value=0.0, value=28.0, step=0.1)
            sales = st.number_input("Sales", min_value=0.0, value=30.0, step=0.1)

        # Submit button
        submitted = st.form_submit_button("Predict Profit")

    # Process submit form
    if submitted:
        input_data = {
        'Order_ID': [order_id],
        'Order_Date': [order_date],
        'Customer_Name': [customer_name],
        'City': [city],
        'Country': [country],
        'State': [state],
        'Region': [region],
        'Segment': [segment],
        'Category': [category],
        'Ship_Mode': [ship_mode],
        'Sub_Category': [sub_category],
        'Product_Name': [product_name],
        'Quantity': [quantity],
        'Cost': [cost],
        'Sales': [sales]
    }

        # Convert to DataFrame
        df_input = pd.DataFrame(input_data)

        try:
        # Predict profit using the model
            predicted_profit = best_model.predict(df_input)[0]
            st.success(f"**Predicted Profit: ${predicted_profit:.2f}**")

            # Display input data
            st.markdown("### Input Data")
            st.dataframe(df_input)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.write("Please ensure all inputs are valid and try again.")

if __name__ == "main":
    run()