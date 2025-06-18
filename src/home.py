import pandas as pd
import streamlit as st
import os

def home():    
    # Title
    st.title("E-Commerce Profit Prediction using Machine Learning")
    st.markdown("---")

    # Background
    st.markdown("# Background")
    st.markdown('''
    In today’s competitive e-commerce landscape, understanding profitability drivers is essential for growth and strategic decision-making. Profit is influenced by various factors including customer segmentation, shipping modes, product performance, and order characteristics. Different customer segments like corporate, home office, and individual consumers exhibit unique buying behaviors, enabling targeted pricing and promotions. Shipping choices affect both customer satisfaction and operational costs, requiring a balance between speed and efficiency. Product categories perform differently across regions, highlighting the importance of local preferences. Additionally, order size and cost of goods directly impact margins. By applying regression models to historical sales data, businesses can forecast profit more accurately. This enables smarter inventory planning, tailored marketing, and improved logistics, ultimately driving operational efficiency and competitive advantage.
    ''')

    # Problem Statement
    st.markdown("# Problem Statement")
    st.markdown('''
    The main objective is to make prediction of e-commerce profitablity using machine learning algorithms, based on historical e-commerce sales data. Given the dynamic and competitive nature of the digital marketplace, the ability to understand and predict profit enables businesses to make data-driven decisions that improve operational efficiency, customer targeting, and sustainability.
    ''')

    st.markdown("---")

    # Dataset
    st.markdown("# Dataset")
    dataset_path = os.path.join('src', 'Shop Direct Sale Data For Research (1).csv')
    try:
        data_ecommerce = pd.read_csv(dataset_path)
        st.dataframe(data_ecommerce.head(5))
        st.markdown(f"**Dataset Size**: {data_ecommerce.shape[0]} rows, {data_ecommerce.shape[1]} columns")
    except FileNotFoundError:
        st.error(f"Dataset file '{dataset_path}' not found. Please ensure the file exists in the 'src' directory.")
    except pd.errors.ParserError:
        st.error("Error parsing the dataset. Please check the CSV file format.")

    st.markdown("---")

    # Data Overview
    st.markdown("### Data Overview", unsafe_allow_html=True)

    st.markdown(f"""
    <h3>📊 Dataset Overview</h3>
    <p>
    This section provides a comprehensive overview of the dataset used in this project. The dataset contains detailed transactional records from a retail environment, spanning order-level details, customer demographics, geographic distribution, product categorization, cost and revenue-related features, and logistical information. Each column contributes to forming a holistic view of how retail operations influence profitability.
    </p>

    <table style="width:100%; border-collapse: collapse; font-size: 14px;" border="1">
        <thead>
            <tr style="background-color: #f2f2f2; text-align: left;">
                <th style="padding: 8px;">Column</th>
                <th style="padding: 8px;">Information</th>
            </tr>
        </thead>
        <tbody>
            <tr><td style="padding: 8px;"><code>Order_ID</code></td><td style="padding: 8px;">Unique identifier for each order (integer).</td></tr>
            <tr><td style="padding: 8px;"><code>Order_Date</code></td><td style="padding: 8px;">Date of the order in mm/dd/yyyy format (string).</td></tr>
            <tr><td style="padding: 8px;"><code>Customer_Name</code></td><td style="padding: 8px;">Name of the customer placing the order (string).</td></tr>
            <tr><td style="padding: 8px;"><code>City</code></td><td style="padding: 8px;">City where the order was placed (string, e.g., Eindhoven).</td></tr>
            <tr><td style="padding: 8px;"><code>Country</code></td><td style="padding: 8px;">Country of the order (string, e.g., Netherlands, France).</td></tr>
            <tr><td style="padding: 8px;"><code>State</code></td><td style="padding: 8px;">State or province of the order (string, e.g., North Brabant).</td></tr>
            <tr><td style="padding: 8px;"><code>Region</code></td><td style="padding: 8px;">Geographical region: <code>Central</code>, <code>South</code>, <code>North</code>.</td></tr>
            <tr><td style="padding: 8px;"><code>Segment</code></td><td style="padding: 8px;">Customer segment: <code>Home Office</code>, <code>Corporate</code>, <code>Consumer</code>.</td></tr>
            <tr><td style="padding: 8px;"><code>Category</code></td><td style="padding: 8px;">Product category: <code>Office Supplies</code>, <code>Furniture</code>, <code>Technology</code>.</td></tr>
            <tr><td style="padding: 8px;"><code>Ship_Mode</code></td><td style="padding: 8px;">Shipping method: <code>Economy Plus</code>, <code>Immediate</code>, <code>Economy</code>, <code>Priority</code>.</td></tr>
            <tr><td style="padding: 8px;"><code>Sub_Category</code></td><td style="padding: 8px;">Product sub-category (e.g., <code>Art</code>, <code>Paper</code>, <code>Chairs</code>).</td></tr>
            <tr><td style="padding: 8px;"><code>Product_Name</code></td><td style="padding: 8px;">Name of the product (string, e.g., BIC Pencil Sharpener).</td></tr>
            <tr><td style="padding: 8px;"><code>Quantity</code></td><td style="padding: 8px;">Number of items ordered (integer, min 1).</td></tr>
            <tr><td style="padding: 8px;"><code>Cost</code></td><td style="padding: 8px;">Cost of goods (float, e.g., 28.0).</td></tr>
            <tr><td style="padding: 8px;"><code>Sales</code></td><td style="padding: 8px;">Revenue generated from the order (float, e.g., 30.0).</td></tr>
            <tr><td style="padding: 8px;"><code>Profit</code></td><td style="padding: 8px;">Profit from the order transaction (float, target variable).</td></tr>
        </tbody>
    </table>

                
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Model Used
    st.markdown("## Algorithm and Metrics Evaluation")
    st.markdown('''
    Random Forest Algorithm is selected to be the based model for this profitability prediction. Metrics Evaluation used to select the best model is R-Squared Score (R2), Mean Absolute Error (MAE), and Mean Absolute Percentage Erros (MAPE).
    ''')

    st.markdown("---")

if __name__ == "__main__":
    home()