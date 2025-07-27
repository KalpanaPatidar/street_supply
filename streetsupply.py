import streamlit as st
import pandas as pd
from streamlit.components.v1 import html
location = st.text_input("Or Enter Location Manually", placeholder="Indore")


st.markdown("### 📍 Detecting your location...")
html(open("location_helper.html").read(), height=200)

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

#Home page
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


import streamlit as st
import pandas as pd

# Load updated product data
products = pd.read_csv("india_products_with_locations.csv")

st.title("🔍 Search by Location and Product")

# Step 1: Ask for location
location_input = st.text_input("📍 Enter your location (e.g., Bhawarkua, Indore)")

# Step 2: Ask for product keyword
keyword_input = st.text_input("🔎 Enter product name (e.g., Oil, Rice, Milk)")

# Step 3: Filter results
if location_input or keyword_input:
    filtered = products.copy()
    if location_input:
        filtered = filtered[filtered['supplier_location'].str.contains(location_input, case=False)]
    if keyword_input:
        filtered = filtered[filtered['name'].str.contains(keyword_input, case=False)]

    if not filtered.empty:
        st.success(f"✅ Found {len(filtered)} matching products.")
        st.dataframe(filtered[['name', 'supplier', 'supplier_location', 'price', 'discount', 'rating', 'delivery_charge']])
    else:
        st.warning("⚠️ No matching products found.")
# --- Checkout Form ---
st.subheader("📦 Delivery Details")
with st.form("checkout_form"):
    name = st.text_input("👤 Full Name")
    phone = st.text_input("📞 Phone Number")
    address = st.text_area("🏠 Delivery Address")
    city = st.text_input("🏙️ City")
    pincode = st.text_input("📮 Pincode")
    pay_mode = st.radio("💳 Payment Mode", ["Cash on Delivery", "Pay Online (Razorpay)"])
    submitted = st.form_submit_button("🛍️ Confirm & Pay")

    if submitted:
        if name and phone and address and city and pincode:
            st.success("✅ Order confirmed! Redirecting to payment..." if pay_mode == "Pay Online (Razorpay)" else "✅ Order placed with COD.")
            if pay_mode == "Pay Online (Razorpay)":
                st.markdown("Visit [Razorpay Demo Payment Page](https://rzp.io/l/NF6yVOS) to simulate payment.")  # Replace with your live URL
        else:
            st.error("❌ Please fill all the required fields.")
import razorpay

# Replace with your test keys
client = razorpay.Client(auth=("YOUR_KEY_ID", "YOUR_SECRET"))

order_data = {
    "amount": 5000,  # ₹50.00 in paise
    "currency": "INR",
    "payment_capture": "1"
}
order = client.order.create(data=order_data)
st.write("✅ Razorpay Order ID:", order['id'])

st.markdown(f"""
<a href="https://rzp.io/l/YOUR_PAYMENT_LINK" target="_blank">
    <button style="background-color:#4CAF50;color:white;padding:10px;border:none;border-radius:5px;">💳 Proceed to Pay with Razorpay</button>
</a>
""", unsafe_allow_html=True)
products = pd.read_csv("products.csv")

query = st.text_input("🔍 Search for raw material (e.g., plate, oil)")
user_location = st.text_input("📍 Your Location (e.g., Indore)")

if query:
    results = products[products['name'].str.contains(query, case=False)]
    if user_location:
        results = results[results['supplier_location'].str.contains(user_location, case=False)]
    st.dataframe(results[['name', 'price', 'rating', 'supplier', 'supplier_location', 'reviews']])

payment_method = st.radio("💳 Choose Payment Method", ["Cash on Delivery", "Pay Online"])

if st.button("✅ Place Order"):
    if payment_method == "Cash on Delivery":
        st.success("Order Placed! Delivery in progress.")
    else:
        st.markdown("""
        <a href="https://rzp.io/l/YOUR_PAYMENT_LINK" target="_blank">
            <button style="background-color:#4CAF50;color:white;padding:10px;border:none;border-radius:5px;">💳 Pay with Razorpay / UPI</button>
        </a>
        """, unsafe_allow_html=True) st.markdown("### 📊 Price and Reviews Comparison")

if query:
    compare = products[products['name'].str.contains(query, case=False)].sort_values(by=["price", "rating"])
    for _, row in compare.iterrows():
        st.markdown(f"""
        - *{row['name']}* from {row['supplier']}
        - Price: ₹{row['price']} | Discount: {row['discount']}%
        - ⭐ {row['rating']} | 📍 {row['supplier_location']}
        - 💬 Review: {row['reviews']}
        """)
        st.markdown("---")   

from streamlit_lottie import st_lottie
import json

with open("lottie/animation.json") as f:
    lottie_anim = json.load(f)
 


import razorpay

# Use your Test Keys
client = razorpay.Client(auth=("rzp_test_xxxxxx", "xxxxxxxxxxxxx"))

order_data = {
    "amount": 5000,  # ₹50 in paise
    "currency": "INR",
    "payment_capture": "1"
}
order = client.order.create(data=order_data)
st.write("🧾 Razorpay Order ID:", order['id'])

# Payment button
st.markdown(f"""
<a href="https://rzp.io/l/YOUR_PAYMENT_LINK" target="_blank">
    <button style="background-color:#4CAF50;color:white;padding:10px 20px;border:none;border-radius:5px;">💳 Pay Now</button>
</a>
""", unsafe_allow_html=True)
st_lottie(lottie_anim, height=300)
