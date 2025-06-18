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
            city = st.text_input('City', value=None)
            country = st.selectbox('Country', ['Sweden', 'United Kingdom', 'France', 'Italy', 'Austria', 'Spain', 'Germany', 'Netherlands', 'Denmark', 'Belgium', 'Norway', 'Portugal', 'Switzerland', 'Ireland', 'Finland'])
            state = st.text_input("State", value=None)
            region = st.selectbox("Region", ['Central', 'South', 'North'])

        with col2:
            segment = st.selectbox("Segment", ['Home Office', 'Corporate', 'Consumer'])
            category = st.selectbox("Category", ['Office Supplies', 'Furniture', 'Technology'])
            ship_mode = st.selectbox("Ship Mode", ['Economy Plus', 'Immediate', 'Economy', 'Priority'])
            sub_category = st.selectbox("Sub-Category", ['Paper', 'Bookcases', 'Art', 'Binders', 'Tables', 'Chairs', 'Appliances', 'Labels', 'Fasteners', 'Envelopes', 'Accessories', 'Furnishings', 'Copiers', 'Storage', 'Supplies', 'Phones', 'Machines'])
            product_name = st.text_input("Product Name", value=None)
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