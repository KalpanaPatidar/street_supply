import streamlit as st
import pandas as pd

# Load data
products = pd.read_csv('products.csv')

# Set page config
st.set_page_config(page_title="Bhojan Bazaar", layout="wide")

# Header
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>Bhojan Bazaar 🛒</h1>", unsafe_allow_html=True)
st.markdown("### India's Trusted Raw Material Marketplace for Street Food Vendors")

# Sidebar Navigation
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3595/3595455.png", width=100)
st.sidebar.title("📦 Menu")
menu = st.sidebar.radio("Navigate", ["Home", "Search", "Departments", "Cart", "Wishlist", "Orders"])

# Session State Setup
if 'cart' not in st.session_state: st.session_state.cart = []
if 'wishlist' not in st.session_state: st.session_state.wishlist = []

# Home Page
if menu == "Home":
    st.success("Welcome to Bhojan Bazaar. Find trusted suppliers, compare prices, and save time!")
    st.image("https://cdn.pixabay.com/photo/2021/05/26/04/43/grocery-6284031_960_720.png", use_column_width=True)

# Search Page
elif menu == "Search":
    query = st.text_input("🔍 Search raw materials by name")
    if query:
        results = products[products['name'].str.contains(query, case=False)]
        results = results.sort_values(by='price')
        st.write("Search Results:")
        st.dataframe(results)

# Departments
elif menu == "Departments":
    dept = st.selectbox("Choose Category", products['category'].unique())
    filtered = products[products['category'] == dept]
    st.write(f"🛒 {dept} Products")
    for i, row in filtered.iterrows():
        st.markdown(f"""
        **{row['name']}**  
        ₹{row['price']} | ⭐ {row['rating']} | 🏪 {row['supplier']}  
        Discount: {row['discount']}% | Final: ₹{row['price']*(1-row['discount']/100):.2f}  
        """)
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button(f"Add to Cart 🛒 ({row['product_id']})"):
                st.session_state.cart.append(row['product_id'])
        with col2:
            if st.button(f"Add to Wishlist 💖 ({row['product_id']})"):
                st.session_state.wishlist.append(row['product_id'])

# Cart Page
elif menu == "Cart":
    st.subheader("🛍 Your Cart")
    total = 0
    for pid in st.session_state.cart:
        item = products[products['product_id'] == pid].iloc[0]
        price = item['price'] * (1 - item['discount'] / 100)
        st.write(f"{item['name']} - ₹{price:.2f}")
        total += price
    st.info(f"🧾 Total: ₹{total:.2f}")

    pay_mode = st.radio("Choose Payment Method", ["Cash on Delivery", "UPI/Online"])
    if st.button("✅ Place Order"):
        st.success(f"Order Placed with {pay_mode}!")
        st.session_state.cart = []

# Wishlist Page
elif menu == "Wishlist":
    st.subheader("💖 Wishlist")
    for pid in st.session_state.wishlist:
        item = products[products['product_id'] == pid].iloc[0]
        st.write(f"{item['name']} - ₹{item['price']}")

# Orders Page
elif menu == "Orders":
    st.info("📦 This is your order history. (Simulation only in MVP)")
    st.warning("Coming soon: Delivery tracking, cancellation, and reviews!")

st.markdown("""
<style>
h1 {
    font-size: 42px;
    color: #FF4B4B;
    font-weight: bold;
}
.sidebar .sidebar-content {
    background-color: #f7f7f7;
}
</style>
""", unsafe_allow_html=True)
