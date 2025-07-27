# Updated Streamlit UI Design for Bhojan Bazaar (Enhanced with Changes) --> MORE BEAUTIFUL BUT6 NOT COMPLETE

# import streamlit as st
# import pandas as pd
# from streamlit.components.v1 import html
# from datetime import datetime, timedelta

# # Config
# st.set_page_config(page_title="Bhojan Bazaar", layout="wide")

# # Replace Lottie animation with a static banner image
# st.image(
#     "https://cdn.pixabay.com/photo/2021/05/26/04/43/grocery-6284031_960_720.png",
#     caption="Welcome to Bhojan Bazaar - Your Trusted Raw Material Marketplace",
#     use_column_width=True
# )

# # Session Setup
# if 'cart' not in st.session_state: st.session_state.cart = []
# if 'wishlist' not in st.session_state: st.session_state.wishlist = []
# if 'menu' not in st.session_state: st.session_state.menu = "Home"
# if 'orders' not in st.session_state:
#     st.session_state.orders = [
#         {"name": "Onion 5kg", "status": "Delivered", "delivered_date": "2025-07-25"},
#         {"name": "Rice 10kg", "status": "Out for Delivery", "estimated_date": (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')},
#         {"name": "Oil 1L", "status": "Shipped", "estimated_date": (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')}
#     ]

# # Load Data
# products = pd.read_csv("india_products_with_locations.csv")

# # Header Bar
# col1, col2, col3, col4, col5 = st.columns([4, 2, 1, 1, 1])
# with col1:
#     search = st.text_input("🔍 Search products", placeholder="e.g. Onion, Oil")
# with col2:
#     st.toggle("📍 Nearest Location", key="location_filter")
# with col3:
#     if st.button("🛒", help="Cart"):
#         st.session_state.menu = "Cart"
# with col4:
#     if st.button("❤️", help="Wishlist"):
#         st.session_state.menu = "Wishlist"
# with col5:
#     if st.button("📦", help="Orders"):
#         st.session_state.menu = "Orders"

# # Sidebar Menu
# menu = st.sidebar.radio("Navigate", ["Home", "Search Results", "Account"])
# if menu:
#     st.session_state.menu = menu

# # Account Section
# if st.session_state.menu == "Account":
#     st.subheader("👤 Your Profile")
#     if st.button("✏️ Edit Profile"):
#         st.session_state.edit_mode = not st.session_state.get("edit_mode", False)

#     edit = st.session_state.get("edit_mode", False)

#     name = st.text_input("Full Name", value="Kishan Vendor", disabled=not edit)
#     phone = st.text_input("Phone", value="9876543210", disabled=not edit)
#     email = st.text_input("Email", value="kishan@example.com", disabled=not edit)
#     address = st.text_area("Address", value="Indore", disabled=not edit)
#     if edit:
#         st.button("Save Changes")

# # Search Results Page
# elif st.session_state.menu == "Search Results" and search:
#     results = products[products['name'].str.contains(search, case=False)]
#     if st.session_state.location_filter:
#         results = results[results['supplier_location'].str.contains("Indore", case=False)]
#     st.subheader(f"🔍 Results for '{search}'")
#     for _, row in results.iterrows():
#         st.markdown(f"""
#         **{row['name']}** from **{row['supplier']}**  
#         Price: ₹{row['price']} | Discounted: ₹{row['price']*(1-row['discount']/100):.2f}  
#         ⭐ {row['rating']} | 📍 {row['supplier_location']} | 🚚 ₹{row['delivery_charge']}  
#         💬 {row['reviews']}
#         """)
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             st.button("Add to Cart", key=f"cart_{row['product_id']}")
#         with col2:
#             st.button("❤️ Wishlist", key=f"wish_{row['product_id']}")
#         with col3:
#             st.button("Place Order (COD)", key=f"order_{row['product_id']}")
#         st.markdown("---")

# # Home Page with Categories
# elif st.session_state.menu == "Home":
#     st.subheader("🏬 Browse by Category")
#     depts = products['category'].unique()
#     for dept in depts:
#         st.markdown(f"### 🏷️ {dept}")
#         dept_items = products[products['category'] == dept]
#         for _, row in dept_items.iterrows():
#             st.markdown(f"**{row['name']}** (₹{row['price']} → ₹{row['price']*(1-row['discount']/100):.2f})")
#             st.markdown(f"⭐ {row['rating']} | 📍 {row['supplier_location']} | 🚚 ₹{row['delivery_charge']}")
#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 st.button("Add to Cart", key=f"dept_cart_{row['product_id']}")
#             with col2:
#                 st.button("❤️ Wishlist", key=f"dept_wish_{row['product_id']}")
#             with col3:
#                 st.button("Order Now", key=f"dept_order_{row['product_id']}")
#             st.markdown("---")

# # Cart Page
# elif st.session_state.menu == "Cart":
#     st.subheader("🛍 Your Cart")
#     total = 0
#     for pid in st.session_state.cart:
#         item = products[products['product_id'] == pid].iloc[0]
#         price = item['price'] * (1 - item['discount'] / 100)
#         st.write(f"{item['name']} - ₹{price:.2f}")
#         total += price
#         st.button("❌ Remove", key=f"remove_{pid}")
#         st.button("💖 Save for Later", key=f"save_{pid}")
#     st.markdown(f"### Total Payable: ₹{total:.2f}")
#     st.radio("Payment Mode", ["Cash on Delivery"], key="pay_mode")
#     if st.button("✅ Place Order"):
#         st.success("Order Placed with Cash on Delivery!")
#         st.session_state.cart = []

# # Wishlist Page
# elif st.session_state.menu == "Wishlist":
#     st.subheader("💖 Wishlist")
#     for pid in st.session_state.wishlist:
#         item = products[products['product_id'] == pid].iloc[0]
#         st.write(f"{item['name']} - ₹{item['price']}")
#         st.button("Add to Cart", key=f"wish_to_cart_{pid}")
#         st.button("Remove", key=f"wish_remove_{pid}")

# # Orders Page
# elif st.session_state.menu == "Orders":
#     st.subheader("📦 Your Orders")

#     for order in st.session_state.orders:
#         st.markdown(f"### {order['name']}")
#         if order['status'] == "Delivered":
#             st.success(f"✅ Delivered on {order['delivered_date']}")
#         else:
#             st.warning(f"🚚 Status: {order['status']}, Estimated Delivery: {order['estimated_date']}")
#             st.progress(["Order Placed", "Shipped", "Out for Delivery", "Delivered"].index(order['status']) / 3.0)

#         with st.expander("View Tracking Details"):
#             steps = ["Order Placed", "Shipped", "Out for Delivery", "Delivered"]
#             for step in steps:
#                 if steps.index(step) <= steps.index(order['status']):
#                     st.markdown(f"✅ {step}")
#                 else:
#                     st.markdown(f"🔲 {step}")
#         st.markdown("---")

# NEW WITH PICTURES
# Updated Streamlit UI with Category Cards like CHF Mart

# import streamlit as st
# import pandas as pd
# from streamlit.components.v1 import html
# from datetime import datetime, timedelta

# # Page Configuration
# st.set_page_config(page_title="Bhojan Bazaar", layout="wide")

# # Banner Image
# st.image(
#     "https://cdn.pixabay.com/photo/2021/05/26/04/43/grocery-6284031_960_720.png",
#     caption="Welcome to Bhojan Bazaar - Your Trusted Raw Material Marketplace",
#     use_column_width=True
# )

# # Session Setup
# if 'cart' not in st.session_state: st.session_state.cart = []
# if 'wishlist' not in st.session_state: st.session_state.wishlist = []
# if 'menu' not in st.session_state: st.session_state.menu = "Home"
# if 'orders' not in st.session_state:
#     st.session_state.orders = [
#         {"name": "Onion 5kg", "status": "Delivered", "delivered_date": "2025-07-25"},
#         {"name": "Rice 10kg", "status": "Out for Delivery", "estimated_date": (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')},
#         {"name": "Oil 1L", "status": "Shipped", "estimated_date": (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')}
#     ]

# # Load Data
# products = pd.read_csv("india_products_with_locations.csv")


# # Header Navigation Bar
# col1, col2, col3, col4, col5 = st.columns([4, 2, 1, 1, 1])
# with col1:
#     search = st.text_input("🔍 Search products", placeholder="e.g. Onion, Oil")
# with col2:
#     st.toggle("📍 Nearest Location", key="location_filter")
# with col3:
#     if st.button("🛒", help="Cart"):
#         st.session_state.menu = "Cart"
# with col4:
#     if st.button("💖", help="Wishlist"):
#         st.session_state.menu = "Wishlist"
# with col5:
#     if st.button("📦", help="Orders"):
#         st.session_state.menu = "Orders"

# # Sidebar Navigation (Optional)
# menu = st.sidebar.radio("Navigate", ["Home", "Search Results", "Account"])
# if menu:
#     st.session_state.menu = menu

# # Account Section
# if st.session_state.menu == "Account":
#     st.subheader("👤 Your Profile")
#     if st.button("✏️ Edit Profile"):
#         st.session_state.edit_mode = not st.session_state.get("edit_mode", False)

#     edit = st.session_state.get("edit_mode", False)

#     name = st.text_input("Full Name", value="Kishan Vendor", disabled=not edit)
#     phone = st.text_input("Phone", value="9876543210", disabled=not edit)
#     email = st.text_input("Email", value="kishan@example.com", disabled=not edit)
#     address = st.text_area("Address", value="Indore", disabled=not edit)
#     if edit:
#         st.button("Save Changes")

# # Search Results Page
# elif st.session_state.menu == "Search Results" and search:
#     results = products[products['name'].str.contains(search, case=False)]
#     if st.session_state.location_filter:
#         results = results[results['supplier_location'].str.contains("Indore", case=False)]
#     st.subheader(f"🔍 Results for '{search}'")
#     for _, row in results.iterrows():
#         st.markdown(f"""
#         **{row['name']}** from **{row['supplier']}**  
#         Price: ₹{row['price']} | Discounted: ₹{row['price']*(1-row['discount']/100):.2f}  
#         ⭐ {row['rating']} | 📍 {row['supplier_location']} | 🚚 ₹{row['delivery_charge']}  
#         💬 {row['reviews']}
#         """)
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             st.button("Add to Cart", key=f"cart_{row['product_id']}")
#         with col2:
#             st.button("💖 Wishlist", key=f"wish_{row['product_id']}")
#         with col3:
#             st.button("Place Order (COD)", key=f"order_{row['product_id']}")
#         st.markdown("---")

# # Home Page with Category Cards
# elif st.session_state.menu == "Home":
#     st.subheader("🗂️ Categories")
#     categories = products['category'].unique()
#     cols = st.columns(4)

#     for index, category in enumerate(categories):
#         with cols[index % 4]:
#             st.image("https://cdn-icons-png.flaticon.com/512/263/263115.png", width=100)
#             if st.button(category, key=f"cat_{category}"):
#                 st.session_state.selected_category = category

#     # If a category is selected
#     if st.session_state.get("selected_category"):
#         selected = st.session_state.selected_category
#         st.subheader(f"🛍️ Products in '{selected}'")
#         filtered = products[products['category'] == selected]
#         for _, row in filtered.iterrows():
#             st.markdown(f"**{row['name']}** (₹{row['price']} → ₹{row['price']*(1-row['discount']/100):.2f})")
#             st.markdown(f"⭐ {row['rating']} | 📍 {row['supplier_location']} | 🚚 ₹{row['delivery_charge']}")
#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 st.button("Add to Cart", key=f"dept_cart_{row['product_id']}")
#             with col2:
#                 st.button("💖 Wishlist", key=f"dept_wish_{row['product_id']}")
#             with col3:
#                 st.button("Order Now", key=f"dept_order_{row['product_id']}")
#             st.markdown("---")

# # Cart Page
# elif st.session_state.menu == "Cart":
#     st.subheader("🛍 Your Cart")
#     total = 0
#     for pid in st.session_state.cart:
#         item = products[products['product_id'] == pid].iloc[0]
#         price = item['price'] * (1 - item['discount'] / 100)
#         st.write(f"{item['name']} - ₹{price:.2f}")
#         total += price
#         st.button("❌ Remove", key=f"remove_{pid}")
#         st.button("💖 Save for Later", key=f"save_{pid}")
#     st.markdown(f"### Total Payable: ₹{total:.2f}")
#     st.radio("Payment Mode", ["Cash on Delivery"], key="pay_mode")
#     if st.button("✅ Place Order"):
#         st.success("Order Placed with Cash on Delivery!")
#         st.session_state.cart = []

# # Wishlist Page
# elif st.session_state.menu == "Wishlist":
#     st.subheader("💖 Wishlist")
#     for pid in st.session_state.wishlist:
#         item = products[products['product_id'] == pid].iloc[0]
#         st.write(f"{item['name']} - ₹{item['price']}")
#         st.button("Add to Cart", key=f"wish_to_cart_{pid}")
#         st.button("Remove", key=f"wish_remove_{pid}")

# # Orders Page
# elif st.session_state.menu == "Orders":
#     st.subheader("📦 Your Orders")
#     for order in st.session_state.orders:
#         st.markdown(f"### {order['name']}")
#         if order['status'] == "Delivered":
#             st.success(f"✅ Delivered on {order['delivered_date']}")
#         else:
#             st.warning(f"🚚 Status: {order['status']}, Estimated Delivery: {order['estimated_date']}")
#             st.progress(["Order Placed", "Shipped", "Out for Delivery", "Delivered"].index(order['status']) / 3.0)

#         with st.expander("View Tracking Details"):
#             steps = ["Order Placed", "Shipped", "Out for Delivery", "Delivered"]
#             for step in steps:
#                 if steps.index(step) <= steps.index(order['status']):
#                     st.markdown(f"✅ {step}")
#                 else:
#                     st.markdown(f"🔲 {step}")
#         st.markdown("---")


# EVEN BETTER
# Updated Streamlit UI Design for Bhojan Bazaar (Inspired by CHF Mart)

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Config
st.set_page_config(page_title="Bhojan Bazaar", layout="wide")

# Static Banner Image
st.image(
    "https://cdn.pixabay.com/photo/2021/05/26/04/43/grocery-6284031_960_720.png",
    caption="Welcome to Bhojan Bazaar - Your Trusted Raw Material Marketplace",
    use_column_width=True
)

# Session Setup
if 'cart' not in st.session_state: st.session_state.cart = []
if 'wishlist' not in st.session_state: st.session_state.wishlist = []
if 'menu' not in st.session_state: st.session_state.menu = "Home"
if 'orders' not in st.session_state:
    st.session_state.orders = [
        {"name": "Onion 5kg", "status": "Delivered", "delivered_date": "2025-07-25"},
        {"name": "Rice 10kg", "status": "Out for Delivery", "estimated_date": (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')},
        {"name": "Oil 1L", "status": "Shipped", "estimated_date": (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')}
    ]

# Load Data
products = pd.read_csv("india_products_with_locations.csv")


# Header Bar - Centered Search
st.markdown("""
    <style>
    .search-bar {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .search-bar input {
        width: 50% !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="search-bar">', unsafe_allow_html=True)
search = st.text_input("", placeholder="Search 9000+ products")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<div style='text-align:right;'>", unsafe_allow_html=True)
st.toggle("📍 Nearest Location", key="location_filter")
st.markdown("</div>", unsafe_allow_html=True)

# Navigation Buttons
cols = st.columns([8, 1, 1, 1])
with cols[1]:
    if st.button("🛒", help="Cart"): st.session_state.menu = "Cart"
with cols[2]:
    if st.button("💗", help="Wishlist"): st.session_state.menu = "Wishlist"
with cols[3]:
    if st.button("📦", help="Orders"): st.session_state.menu = "Orders"

# Profile
with st.sidebar:
    if st.button("👤 Account"):
        st.session_state.menu = "Account"

# Account Page
if st.session_state.menu == "Account":
    st.subheader("👤 Your Profile")
    if st.button("✏️ Edit Profile"):
        st.session_state.edit_mode = not st.session_state.get("edit_mode", False)
    edit = st.session_state.get("edit_mode", False)
    name = st.text_input("Full Name", value="Kishan Vendor", disabled=not edit)
    phone = st.text_input("Phone", value="9876543210", disabled=not edit)
    email = st.text_input("Email", value="kishan@example.com", disabled=not edit)
    address = st.text_area("Address", value="Indore", disabled=not edit)
    if edit:
        st.button("Save Changes")

# Search Results Page (dynamic)
if search:
    st.subheader(f"🔍 Search Results for '{search}'")
    st.markdown("<div style='text-align:right;'>📍 Nearest Location Filter Applied: " + str(st.session_state.location_filter) + "</div>", unsafe_allow_html=True)
    results = products[products['name'].str.contains(search, case=False)]
    if st.session_state.location_filter:
        results = results[results['supplier_location'].str.contains("Indore", case=False)]
    if results.empty:
        st.info("No products found matching the search criteria.")
    for _, row in results.iterrows():
        st.markdown(f"""
        **{row['name']}** from **{row['supplier']}**  
        Price: ₹{row['price']} | Discounted: ₹{row['price']*(1-row['discount']/100):.2f}  
        ⭐ {row['rating']} | 📍 {row['supplier_location']} | 🚚 ₹{row['delivery_charge']}  
        💬 {row['reviews'] if 'reviews' in row and pd.notna(row['reviews']) else 'No reviews available'}

        """)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button("Add to Cart", key=f"cart_{row['product_id']}")
        with col2:
            st.button("💗 Wishlist", key=f"wish_{row['product_id']}")
        with col3:
            st.button("Order Now", key=f"order_{row['product_id']}")
        st.markdown("---")

# Home Page - Categories with Images
elif st.session_state.menu == "Home":
    st.subheader("🛒 Categories")
    categories = products['category'].unique()
    image_map = {
        "Vegetables": "https://cdn-icons-png.flaticon.com/512/135/135620.png",
        "Dairy Products": "https://cdn-icons-png.flaticon.com/512/3174/3174880.png",
        "Grocery": "https://cdn-icons-png.flaticon.com/512/1046/1046784.png",
        "Spices": "https://cdn-icons-png.flaticon.com/512/1999/1999625.png",
        "Cleaning Supplies": "https://cdn-icons-png.flaticon.com/512/679/679922.png",
        "Meat": "https://cdn-icons-png.flaticon.com/512/1046/1046785.png",
        "Beverages": "https://cdn-icons-png.flaticon.com/512/1046/1046789.png"
    }

    for cat in categories:
        with st.container():
            st.image(image_map.get(cat, "https://cdn-icons-png.flaticon.com/512/1046/1046784.png"), width=100)
            if st.button(cat):
                st.session_state.selected_category = cat

    if st.session_state.get("selected_category"):
        cat = st.session_state.selected_category
        st.subheader(f"Items in {cat}")
        cat_items = products[products['category'] == cat]
        for _, row in cat_items.iterrows():
            st.markdown(f"**{row['name']}** (₹{row['price']} → ₹{row['price']*(1-row['discount']/100):.2f})")
            st.markdown(f"⭐ {row['rating']} | 📍 {row['supplier_location']} | 🚚 ₹{row['delivery_charge']}")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.button("Add to Cart", key=f"dept_cart_{row['product_id']}")
            with col2:
                st.button("💗 Wishlist", key=f"dept_wish_{row['product_id']}")
            with col3:
                st.button("Order Now", key=f"dept_order_{row['product_id']}")
            st.markdown("---")

# Cart Page
elif st.session_state.menu == "Cart":
    st.subheader("🛍 Your Cart")
    total = 0
    for pid in st.session_state.cart:
        item = products[products['product_id'] == pid].iloc[0]
        price = item['price'] * (1 - item['discount'] / 100)
        st.write(f"{item['name']} - ₹{price:.2f}")
        total += price
        st.button("❌ Remove", key=f"remove_{pid}")
        st.button("💗 Save for Later", key=f"save_{pid}")
    st.markdown(f"### Total Payable: ₹{total:.2f}")
    st.radio("Payment Mode", ["Cash on Delivery"], key="pay_mode")
    if st.button("✅ Place Order"):
        st.success("Order Placed with Cash on Delivery!")
        st.session_state.cart = []

# Wishlist Page
elif st.session_state.menu == "Wishlist":
    st.subheader("💗 Wishlist")
    for pid in st.session_state.wishlist:
        item = products[products['product_id'] == pid].iloc[0]
        st.write(f"{item['name']} - ₹{item['price']}")
        st.button("Add to Cart", key=f"wish_to_cart_{pid}")
        st.button("Remove", key=f"wish_remove_{pid}")

# Orders Page
elif st.session_state.menu == "Orders":
    st.subheader("📦 Your Orders")
    for order in st.session_state.orders:
        st.markdown(f"### {order['name']}")
        if order['status'] == "Delivered":
            st.success(f"✅ Delivered on {order['delivered_date']}")
        else:
            st.warning(f"🚚 Status: {order['status']}, Estimated Delivery: {order['estimated_date']}")
            st.progress(["Order Placed", "Shipped", "Out for Delivery", "Delivered"].index(order['status']) / 3.0)
        with st.expander("View Tracking Details"):
            steps = ["Order Placed", "Shipped", "Out for Delivery", "Delivered"]
            for step in steps:
                if steps.index(step) <= steps.index(order['status']):
                    st.markdown(f"✅ {step}")
                else:
                    st.markdown(f"🔲 {step}")
        st.markdown("---")

