

# import streamlit as st
# import pandas as pd
# from datetime import datetime, timedelta
# # st.set_page_config(page_title="Bhojan Bazaar", layout="wide")
# st.set_page_config(page_title="Bhojan Bazaar", layout="wide")

# # Static Banner Image (no caption)
# st.image("https://cdn.pixabay.com/photo/2021/05/26/04/43/grocery-6284031_960_720.png", use_column_width=True)

# # Stylish Heading & Subheading
# st.markdown("""
#     <h1 style='
#         text-align: center;
#         font-weight: 700;
#         color: #2c3e50;
#         font-size: 40px;
#         margin-top: 20px;
#         margin-bottom: 0px;
#         font-family: "Segoe UI", "Roboto", sans-serif;
#     '>
#         Welcome to Bhojan Bazaar
#     </h1>
#     <h3 style='
#         text-align: center;
#         color: #7f8c8d;
#         font-size: 20px;
#         font-weight: 400;
#         margin-bottom: 30px;
#     '>
#         Your Trusted Raw Material Marketplace
#     </h3>
# """, unsafe_allow_html=True)

# # Styling for search box
# st.markdown("""
#     <style>
#     .stTextInput input {
#         font-size: 16px;
#         padding: 8px;
#     }
#     </style>
# """, unsafe_allow_html=True)

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
# if 'back_to_home' not in st.session_state: st.session_state.back_to_home = False
# if 'selected_category' not in st.session_state: st.session_state.selected_category = None

# # Load Data
# products = pd.read_csv("india_products_with_locations.csv")

# # # Header Row: Home | Search | Account
# col_home, col_search, col_account = st.columns([1, 6, 1])

# with col_home:
#     if st.button("🏠", help="Home"):
#         st.session_state.menu = "Home"
#         st.session_state.selected_category = None
#         st.rerun()

# with col_search:
#     search = st.text_input("Search 9000+ products", key="search_query")

# with col_account:
#     if st.button("👤 Account"):
#         st.session_state.menu = "Account"

# # Functional buttons for 🏠 and 👤
# col1, col2, col3 = st.columns([1, 8, 1])
# with col1:
#     if st.button("🏠", key="home_actual"):
#         st.session_state.menu = "Home"
#         st.session_state.selected_category = None
#         st.rerun()
# with col3:
#     if st.button("👤 Account", key="account_actual"):
#         st.session_state.menu = "Account"

# # Capture the search query
# search = st.text_input("", placeholder="Search 9000+ products", key="search_real")

# # Nearest Location Toggle (only if something is searched)
# if search:
#     st.markdown("<div style='text-align:right;'>", unsafe_allow_html=True)
#     st.toggle("📍 Nearest Location", key="location_filter")
#     st.markdown("</div>", unsafe_allow_html=True)

# # Navigation Buttons
# cols = st.columns([8, 1, 1, 1])
# with cols[1]:
#     if st.button("🛒", help="Cart"): st.session_state.menu = "Cart"
# with cols[2]:
#     if st.button("💗", help="Wishlist"): st.session_state.menu = "Wishlist"
# with cols[3]:
#     if st.button("📦", help="Orders"): st.session_state.menu = "Orders"

# # Helper function
# def add_to_cart(pid):
#     if pid not in st.session_state.cart:
#         st.session_state.cart.append(pid)
#         st.success("✅ Product added to cart!")

# def add_to_wishlist(pid):
#     if pid not in st.session_state.wishlist:
#         st.session_state.wishlist.append(pid)
#         st.success("💗 Product added to wishlist!")

# # Account Page
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
#     st.button("🚪 Logout")

# # Search Results Page (dynamic)
# if search:
#     st.subheader(f"🔍 Search Results for '{search}'")
#     if st.session_state.get("location_filter"):
#         st.markdown("<div style='text-align:right;'>📍 Nearest Location Filter Applied: True</div>", unsafe_allow_html=True)
#     if st.button("🔙 Back to Home"):
#         st.session_state.menu = "Home"
#         st.session_state.selected_category = None
#         st.rerun()
#     results = products[products['name'].str.contains(search, case=False)]
#     if st.session_state.get("location_filter"):
#         results = results[results['supplier_location'].str.contains("Indore", case=False)]
#     if results.empty:
#         st.info("No products found matching the search criteria.")
#     for _, row in results.iterrows():
#         st.markdown(f"""
#         *{row['name']}* from *{row['supplier']}*  
#         Price: ₹{row['price']} | Discounted: ₹{row['price']*(1-row['discount']/100):.2f}  
#         ⭐ {row['rating']} | 📍 {row['supplier_location']} | 🚚 ₹{row['delivery_charge']}
#         """)
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             if st.button("Add to Cart", key=f"cart_{row['product_id']}"):
#                 add_to_cart(row['product_id'])
#         with col2:
#             if st.button("💗 Wishlist", key=f"wish_{row['product_id']}"):
#                 add_to_wishlist(row['product_id'])
#         with col3:
#             st.button("Order Now", key=f"order_{row['product_id']}")
#         st.markdown("---")


# # Stylish Heading & Subheading
# st.markdown("""
#     <h1 style='
#         text-align: center;
#         font-weight: 700;
#         color: #2c3e50;
#         font-size: 40px;
#         margin-top: 20px;
#         margin-bottom: 0px;
#         font-family: "Segoe UI", "Roboto", sans-serif;
#     '>
#         Welcome to Bhojan Bazaar
#     </h1>
#     <h3 style='
#         text-align: center;
#         color: #7f8c8d;
#         font-size: 20px;
#         font-weight: 400;
#         margin-bottom: 30px;
#     '>
#         Your Trusted Raw Material Marketplace
#     </h3>
# """, unsafe_allow_html=True)
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
# if 'back_to_home' not in st.session_state:
#     st.session_state.back_to_home = False
# if 'selected_category' not in st.session_state:
#     st.session_state.selected_category = None

# # Load Data
# products = pd.read_csv("india_products_with_locations.csv")

# # Header Bar
# # header_cols = st.columns([1, 7, 1, 1, 1, 1])
# # with header_cols[0]:
# #     if st.button("🏠", help="Home"):
# #         st.session_state.menu = "Home"
# #         st.session_state.selected_category = None
# #         st.rerun()
# # with header_cols[4]:
# #     if st.button("👤 Account"):
# #         st.session_state.menu = "Account"

# # Centered Search
# # st.markdown("""
# #     <style>
# #     .search-bar {
# #         display: flex;
# #         justify-content: center;
# #         # margin-bottom: 20px;
# #     }
# #     .search-bar input {
# #         width: 50% !important;
# #     }
# #     </style>
# """, unsafe_allow_html=True)


# # ---------- 📌 Top Bar Layout ----------
# top_col1, top_col2, top_col3 = st.columns([1, 5, 1.2])

# with top_col1:
#     if st.button("🏠 Home"):
#         st.session_state.menu = "Home"
#         st.session_state.selected_category = None
#         st.rerun()

# # with top_col2:
# #     search_query = st.text_input("Search products...", "", key="search_input", label_visibility="collapsed")

#    # with top_col3:
#     if st.button("👤 Account"):
#         st.session_state.menu = "Account"



# # ---- Load Product Data ----
# products = pd.read_csv("india_products_with_locations.csv")


# st.markdown('<div class="search-bar">', unsafe_allow_html=True)
# search = st.text_input("", placeholder="Search 9000+ products")
# st.markdown('</div>', unsafe_allow_html=True)

# # Nearest Toggle Only for Search
# if search:
#     st.markdown("<div style='text-align:right;'>", unsafe_allow_html=True)
#     st.toggle("📍 Nearest Location", key="location_filter")
#     st.markdown("</div>", unsafe_allow_html=True)
# # --- Navigation Buttons ---
# cols = st.columns([8, 1, 1, 1])
# with cols[1]:
#     if st.button("🛒", help="Cart"): st.session_state.menu = "Cart"
# with cols[2]:
#     if st.button("💗", help="Wishlist"): st.session_state.menu = "Wishlist"
# with cols[3]:
#     if st.button("📦", help="Orders"): st.session_state.menu = "Orders"




# # --- Helper Functions ---
# def add_to_cart(pid):
#     if pid not in st.session_state.cart:
#         st.session_state.cart.append(pid)
#         st.success("✅ Product added to cart!")

# def add_to_wishlist(pid):
#     if pid not in st.session_state.wishlist:
#         st.session_state.wishlist.append(pid)
#         st.success("💗 Product added to wishlist!")

# # --- Account Page ---
# if st.session_state.menu == "Account":
#     st.subheader("👤 Your Profile")
#     if st.button("✏️ Edit Profile"):
#         st.session_state.edit_mode = not st.session_state.get("edit_mode", False)
#     edit = st.session_state.get("edit_mode", False)
#     name = st.text_input("Full Name", value="Kishan Vendor", disabled=not edit)
#     phone = st.text_input("Phone", value="9876543210", disabled=not edit)
#     email = st.text_input("Email", value="kishan@example.com", disabled=not edit)
#     address = st.text_area("Address", value="Indore", disabled=not edit)
#     if edit: st.button("Save Changes")
#     st.button("🚪 Logout")

# # --- Search Results Page ---
# if search:
#     st.subheader(f"🔍 Search Results for '{search}'")
#     if st.session_state.get("location_filter"):
#         st.markdown("<div style='text-align:right;'>📍 Nearest Location Filter Applied: True</div>", unsafe_allow_html=True)
#     if st.button("🔙 Back to Home"):
#         st.session_state.menu = "Home"
#         st.session_state.selected_category = None
#         st.rerun()
#     results = products[products['name'].str.contains(search, case=False)]
#     if st.session_state.get("location_filter"):
#         results = results[results['supplier_location'].str.contains("Indore", case=False)]
#     if results.empty:
#         st.info("No products found matching the search criteria.")
#     for _, row in results.iterrows():
# st.markdown(f"""
# **{row['name']}** from *{row['supplier']}*  
# Price: ₹{row['price']} | Discounted: Rs{row['price'] * (1 - row['discount'] / 100):.2f}  
# Rating: {row['rating']} | Location: {row['supplier_location']} | Delivery: ₹{row['delivery_charge']}
# """)

#         col1, col2, col3 = st.columns(3)
#         with col1:
#             if st.button("Add to Cart", key=f"cart_{row['product_id']}"):
#                 add_to_cart(row['product_id'])
#         with col2:
#             if st.button("💗 Wishlist", key=f"wish_{row['product_id']}"):
#                 add_to_wishlist(row['product_id'])
#         with col3:
#             st.button("Order Now", key=f"order_{row['product_id']}")
#         st.markdown("---")


# # Home Page - Categories with Grid
# elif st.session_state.menu == "Home":
#     if st.session_state.back_to_home:
#         st.session_state.back_to_home = False

#     st.subheader("🛒 Categories")
#     categories = products['category'].unique()
#     image_map = {
#          "Edible Oil": "https://www.jiomart.com/images/product/original/490000052/fortune-sunlite-refined-sunflower-oil-870-g-product-images-o490000052-p490000052-0-202504081953.jpg?im=Resize=(360,360)",
#         "Grains": "https://www.jiomart.com/images/product/original/rvdtr0vthp/manna-instant-health-mix-200g-spinach-carrot-daal-with-milk-baby-cereal-baby-food-product-images-orvdtr0vthp-p594806042-0-202210261433.jpg?im=Resize=(420,420)",
#         "Spices": "https://www.jiomart.com/images/product/original/rvlfuumgzv/chokhi-dhani-bombay-biryani-masala-100gm-product-images-orvlfuumgzv-p611552031-0-202505292308.jpg?im=Resize=(360,360)",
#         "Cleaning Supplies": "https://www.jiomart.com/images/product/original/494263706/gebi-ecogin-clean-o-brush-toilet-brush-pack-of-2-product-images-o494263706-p605498198-0-202310311821.jpg?im=Resize=(360,360)",
#         "Dairy": "data:image/webp;base64,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",
#         "Sauces": "data:image/jpeg;base64,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",
#         # "Packaging Material": "data:image/jpeg;base64,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",
#         "Packaging Material": "https://www.jiomart.com/images/product/original/rvjz09yn4t/agroha-plastic-polythene-clear-bags-small-size-pouches-transparent-self-adhesive-bopp-bags-for-jewellery-packing-pack-of-100-pieces-4-5-inch-10-12-5-cm-product-images-orvjz09yn4t-p609367969-0-202406171609.jpg?im=Resize=(360,360)",
#         "Sweetener": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZVGa6EsitJTY_V6o-y1szbfFwvn12LzijQA&s"
#     }

#     for i in range(0, len(categories), 4):
#         category_cols = st.columns(4)
#         for j, cat in enumerate(categories[i:i+4]):
#             with category_cols[j]:
#                 st.image(image_map.get(cat, "https://cdn-icons-png.flaticon.com/512/1046/1046784.png"), width=100)
#                 if st.button(cat):
#                     st.session_state.selected_category = cat
#                     st.session_state.menu = "Category"
#                     st.rerun()

# elif st.session_state.menu == "Category" and st.session_state.get("selected_category"):
#     cat = st.session_state.selected_category
#     st.subheader(f"Items in {cat}")
#     cat_items = products[products['category'] == cat]
#     for _, row in cat_items.iterrows():
#         st.markdown(f"**{row['name']}** (₹{row['price']} → ₹{row['price']*(1-row['discount']/100):.2f})")
#         st.markdown(f"⭐ {row['rating']} | 📍 {row['supplier_location']} | 🚚 ₹{row['delivery_charge']}")
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             if st.button("Add to Cart", key=f"dept_cart_{row['product_id']}"):
#                 add_to_cart(row['product_id'])
#         with col2:
#             if st.button("💗 Wishlist", key=f"dept_wish_{row['product_id']}"):
#                 add_to_wishlist(row['product_id'])
#         with col3:
#             st.button("Order Now", key=f"dept_order_{row['product_id']}")
#         st.markdown("---")

# # Cart Page
# elif st.session_state.menu == "Cart":
#     st.subheader("🛍 Your Cart")

#     if not st.session_state.cart:
#         st.info("Your cart is empty.")
#     else:
#         total_mrp = 0
#         total_discount = 0
#         delivery_charge_total = 0

#         for pid in st.session_state.cart:
#             item = products[products['product_id'] == pid].iloc[0]

#             # Extract all required fields
#             name = item['name']
#             mrp = item['price']
#             discount_percent = item['discount']
#             discount_amount = mrp * (discount_percent / 100)
#             final_price = mrp - discount_amount
#             delivery_charge = item['delivery_charge']
#             supplier = item['supplier']
#             rating = item['rating']
#             stock = item['stock']

#             if stock <= 0:
#                 st.warning(f"⚠️ {name} is currently out of stock.")
#                 continue

#             # Totals
#             total_mrp += mrp
#             total_discount += discount_amount
#             delivery_charge_total += delivery_charge

#             # Product display
#             st.markdown(f"""
#             ### 🛒 {name}
#             - 🏷 **Supplier**: {supplier}
#             - ⭐ **Rating**: {rating}/5
#             - 📦 **Stock Available**: {stock}
#             - 💰 **MRP**: ₹{mrp:.2f}
#             - 🎯 **Discount ({discount_percent}%):** ₹{discount_amount:.2f}
#             - 🔖 **Price After Discount**: ₹{final_price:.2f}
#             - 🚚 **Delivery Charge**: ₹{delivery_charge:.2f}
#             """)

#             # Remove / Wishlist options
#             col1, col2 = st.columns(2)
#             with col1:
#                 if st.button("❌ Remove", key=f"remove_{pid}"):
#                     st.session_state.cart.remove(pid)
#                     st.success("🗑️ Removed from cart!")
#                     st.rerun()
#             with col2:
#                 if st.button("💗 Save for Later", key=f"save_{pid}"):
#                     if pid not in st.session_state.wishlist:
#                         st.session_state.wishlist.append(pid)
#                     st.session_state.cart.remove(pid)
#                     st.success("💗 Moved to Wishlist!")
#                     st.rerun()

#             st.markdown("---")

#         # Final total payable
#         final_total = total_mrp - total_discount + delivery_charge_total

#         # Order Summary
#         st.markdown("## 🧾 Order Summary")
#         st.markdown(f"- **Total MRP:** ₹{total_mrp:.2f}")
#         st.markdown(f"- **Total Discount:** ₹{total_discount:.2f}")
#         st.markdown(f"- **Delivery Charges:** ₹{delivery_charge_total:.2f}")
#         st.markdown(f"### ✅ Total Payable: ₹{final_total:.2f}")

#         st.radio("Payment Mode", ["Cash on Delivery"], key="pay_mode")

#         if st.button("✅ Place Order"):
#             today = datetime.now()
#             for pid in st.session_state.cart:
#                 item = products[products['product_id'] == pid].iloc[0]
#                 st.session_state.orders.append({
#                 "product_id": item['product_id'],
#                 "name": item['name'],
#                 "status": "Order Placed",
#                 "estimated_date": (today + timedelta(days=3)).strftime('%Y-%m-%d')
#         })
#             st.success("🎉 Order Placed Successfully with Cash on Delivery!")
#             st.session_state.cart = []
   

# # Wishlist Page
# elif st.session_state.menu == "Wishlist":
#     st.subheader("💗 Wishlist")
#     for pid in st.session_state.wishlist:
#         item = products[products['product_id'] == pid].iloc[0]
#         st.write(f"{item['name']} - ₹{item['price']}")
#         if st.button("Add to Cart", key=f"wish_to_cart_{pid}"):
#             if pid not in st.session_state.cart:
#                 st.session_state.cart.append(pid)
#             st.session_state.wishlist.remove(pid)
#             st.success("🛒 Moved to Cart!")
#             st.rerun()
#         if st.button("Remove", key=f"wish_remove_{pid}"):
#             st.session_state.wishlist.remove(pid)
#             st.success("❌ Removed from Wishlist!")
#             st.rerun()
# # Orders Page
# elif st.session_state.menu == "Orders":
#     st.subheader("📦 Your Orders")

#     if not st.session_state.orders:
#         st.info("You have no orders yet.")
#     else:
#         for order in st.session_state.orders:
#             st.markdown(f"### 🧺 {order['name']}")
#             current_status = order['status']
#             steps = ["Order Placed", "Shipped", "Out for Delivery", "Delivered"]

#             if current_status == "Delivered":
#                 st.success(f"✅ Delivered on {order.get('delivered_date', 'N/A')}")
#             else:
#                 st.warning(f"🚚 Status: {current_status}, Estimated Delivery: {order['estimated_date']}")
#                 st.progress(steps.index(current_status) / 3.0)

#             with st.expander("📍 View Tracking Details"):
#                 for step in steps:
#                     if steps.index(step) <= steps.index(current_status):
#                         st.markdown(f"✅ {step}")
#                     else:
#                         st.markdown(f"🔲 {step}")
#             st.markdown("---")








# import streamlit as st
# import pandas as pd
# from datetime import datetime
# import json
# import os

# # ========================== CONFIG ==========================

# st.set_page_config(page_title="Bhojan Bazaar", layout="wide")

# # ====================== Load Product Data ===================

# @st.cache_data
# def load_data():
#     return pd.read_csv("products.csv")

# products = load_data()

# # ==================== Session State =========================

# for key in ['cart', 'wishlist']:
#     if key not in st.session_state:
#         st.session_state[key] = []

# # ====================== Header ==============================

# st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>Bhojan Bazaar 🛒</h1>", unsafe_allow_html=True)
# st.markdown("### India’s Trusted Raw Material Marketplace for Street Food Vendors")

# # =================== Sidebar Menu ===========================

# st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3595/3595455.png", width=100)
# st.sidebar.title("📦 Menu")
# menu = st.sidebar.radio("Navigate", ["Home", "Search", "Departments", "Cart", "Wishlist", "Orders"])

# # =================== Helper Functions =======================

# def add_to_cart(pid):
#     if pid not in st.session_state.cart:
#         st.session_state.cart.append(pid)
#         st.success("✅ Added to cart!")

# def add_to_wishlist(pid):
#     if pid not in st.session_state.wishlist:
#         st.session_state.wishlist.append(pid)
#         st.success("💖 Added to wishlist!")

# # ====================== Pages ===============================

# if menu == "Home":
#     st.success("Welcome to Bhojan Bazaar. Browse fresh raw materials.")
#     st.image("https://cdn.pixabay.com/photo/2021/05/26/04/43/grocery-6284031_960_720.png", use_column_width=True)

# elif menu == "Search":
#     query = st.text_input("🔍 Search products")
#     if query:
#         filtered = products[products['name'].str.contains(query, case=False)]
#         for _, row in filtered.iterrows():
#             st.markdown(f"**{row.name}** - ₹{row.price} | ⭐ {row.rating}")
#             c1, c2 = st.columns(2)
#             with c1:
#                 st.button("Add to Cart", key=f"cart_{row.product_id}", on_click=add_to_cart, args=(row.product_id,))
#             with c2:
#                 st.button("💗 Wishlist", key=f"wish_{row.product_id}", on_click=add_to_wishlist, args=(row.product_id,))

# elif menu == "Departments":
#     dept = st.selectbox("Select Category", products['category'].unique())
#     filtered = products[products['category'] == dept]
#     for _, row in filtered.iterrows():
#         final_price = row.price * (1 - row.discount / 100)
#         st.markdown(f"**{row.name}** | ₹{final_price:.2f} | ⭐ {row.rating} | 🏪 {row.supplier}")
#         c1, c2 = st.columns(2)
#         with c1:
#             st.button("Add to Cart", key=f"dept_cart_{row.product_id}", on_click=add_to_cart, args=(row.product_id,))
#         with c2:
#             st.button("💗 Wishlist", key=f"dept_wish_{row.product_id}", on_click=add_to_wishlist, args=(row.product_id,))

# elif menu == "Cart":
#     st.subheader("🛍️ Your Cart")
#     total = 0
#     for pid in st.session_state.cart:
#         item = products[products.product_id == pid].iloc[0]
#         price = item.price * (1 - item.discount / 100)
#         total += price
#         st.write(f"{item.name} - ₹{price:.2f}")
#     st.markdown(f"**Total: ₹{total:.2f}**")
#     if st.button("✅ Place Order"):
#         st.success("🎉 Order Placed Successfully!")
#         st.session_state.cart.clear()

# elif menu == "Wishlist":
#     st.subheader("💖 Your Wishlist")
#     for pid in st.session_state.wishlist:
#         item = products[products.product_id == pid].iloc[0]
#         st.write(f"{item.name} - ₹{item.price}")
#         c1, c2 = st.columns(2)
#         with c1:
#             st.button("🛒 Add to Cart", key=f"wish_cart_{pid}", on_click=add_to_cart, args=(pid,))
#         with c2:
#             st.button("❌ Remove", key=f"wish_remove_{pid}", on_click=lambda pid=pid: st.session_state.wishlist.remove(pid))

# elif menu == "Orders":
#     st.subheader("📦 Your Orders")


# # ========================== CONFIG ==========================

# st.set_page_config(page_title="Bhojan Bazaar", layout="wide")

# # ===================== User Management =======================

# USERS_FILE = "users.json"

# def load_users():
#     if os.path.exists(USERS_FILE):
#         with open(USERS_FILE, "r") as f:
#             return json.load(f)
#     return {}

# def save_users(users):
#     with open(USERS_FILE, "w") as f:
#         json.dump(users, f, indent=4)

# def signup_user(email, password):
#     users = load_users()
#     if email in users:
#         return False, "User already exists."
#     users[email] = {"password": password, "cart": [], "wishlist": [], "orders": []}
#     save_users(users)
#     return True, "Account created successfully."

# def login_user(email, password):
#     users = load_users()
#     if email in users and users[email]["password"] == password:
#         return True
#     return False

# # ====================== Load Product Data ====================

# @st.cache_data

# def load_data():
#     return pd.read_csv("products.csv")

# products = load_data()

# # ===================== Session Initialization ===============

# for key in ['authenticated', 'user_email', 'page']:
#     if key not in st.session_state:
#         st.session_state[key] = None if key != 'page' else 'Login'

# # ========== AUTH UI: SIGN UP / LOGIN SYSTEM ==================

# if not st.session_state.authenticated:
#     st.title("🔐 Welcome to Bhojan Bazaar")

#     tab1, tab2 = st.tabs(["Login", "Sign Up"])

#     with tab1:
#         login_email = st.text_input("Email", key="login_email")
#         login_pass = st.text_input("Password", type="password", key="login_pass")
#         if st.button("Login"):
#             if login_user(login_email, login_pass):
#                 st.session_state.authenticated = True
#                 st.session_state.user_email = login_email
#                 st.success("Logged in successfully!")
#                 st.experimental_rerun()
#             else:
#                 st.error("Invalid credentials.")

#     with tab2:
#         signup_email = st.text_input("New Email", key="signup_email")
#         signup_pass = st.text_input("New Password", type="password", key="signup_pass")
#         if st.button("Sign Up"):
#             ok, msg = signup_user(signup_email, signup_pass)
#             if ok:
#                 st.success(msg)
#             else:
#                 st.error(msg)

#     st.stop()

# # ====================== Header ==============================

# st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>Bhojan Bazaar 🛒</h1>", unsafe_allow_html=True)
# st.markdown("### India’s Trusted Raw Material Marketplace for Street Food Vendors")

# # =================== Sidebar Menu ===========================

# st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3595/3595455.png", width=100)
# st.sidebar.title("📦 Menu")
# menu = st.sidebar.radio("Navigate", ["Home", "Search", "Departments", "Cart", "Wishlist", "Orders", "Logout"])

# # =================== Helper Functions =======================

# def add_to_list(pid, list_name):
#     users = load_users()
#     email = st.session_state.user_email
#     if pid not in users[email][list_name]:
#         users[email][list_name].append(pid)
#         save_users(users)
#         st.success(f"✅ Added to {list_name}!")

# def remove_from_list(pid, list_name):
#     users = load_users()
#     email = st.session_state.user_email
#     if pid in users[email][list_name]:
#         users[email][list_name].remove(pid)
#         save_users(users)

# # ====================== Pages ===============================

# users = load_users()
# user_data = users[st.session_state.user_email]

# if menu == "Home":
#     st.success("Welcome to Bhojan Bazaar. Browse fresh raw materials.")
#     st.image("https://cdn.pixabay.com/photo/2021/05/26/04/43/grocery-6284031_960_720.png", use_column_width=True)

# elif menu == "Search":
#     query = st.text_input("🔍 Search products")
#     if query:
#         filtered = products[products['name'].str.contains(query, case=False)]
#         for _, row in filtered.iterrows():
#             st.markdown(f"**{row.name}** - ₹{row.price} | ⭐ {row.rating}")
#             c1, c2 = st.columns(2)
#             with c1:
#                 st.button("Add to Cart", key=f"cart_{row.product_id}", on_click=add_to_list, args=(row.product_id, 'cart'))
#             with c2:
#                 st.button("💗 Wishlist", key=f"wish_{row.product_id}", on_click=add_to_list, args=(row.product_id, 'wishlist'))

# elif menu == "Departments":
#     dept = st.selectbox("Select Category", products['category'].unique())
#     filtered = products[products['category'] == dept]
#     for _, row in filtered.iterrows():
#         final_price = row.price * (1 - row.discount / 100)
#         st.markdown(f"**{row.name}** | ₹{final_price:.2f} | ⭐ {row.rating} | 🏪 {row.supplier}")
#         c1, c2 = st.columns(2)
#         with c1:
#             st.button("Add to Cart", key=f"dept_cart_{row.product_id}", on_click=add_to_list, args=(row.product_id, 'cart'))
#         with c2:
#             st.button("💗 Wishlist", key=f"dept_wish_{row.product_id}", on_click=add_to_list, args=(row.product_id, 'wishlist'))

# elif menu == "Cart":
#     st.subheader("🛍️ Your Cart")
#     total = 0
#     for pid in user_data['cart']:
#         item = products[products.product_id == pid].iloc[0]
#         price = item.price * (1 - item.discount / 100)
#         total += price
#         st.write(f"{item.name} - ₹{price:.2f}")
#     st.markdown(f"**Total: ₹{total:.2f}**")
#     if st.button("✅ Place Order"):
#         user_data['orders'].append({"items": user_data['cart'], "timestamp": datetime.utcnow().isoformat()})
#         user_data['cart'] = []
#         save_users(users)
#         st.success("🎉 Order Placed Successfully!")

# elif menu == "Wishlist":
#     st.subheader("💖 Your Wishlist")
#     for pid in user_data['wishlist']:
#         item = products[products.product_id == pid].iloc[0]
#         st.write(f"{item.name} - ₹{item.price}")
#         c1, c2 = st.columns(2)
#         with c1:
#             st.button("🛒 Add to Cart", key=f"wish_cart_{pid}", on_click=add_to_list, args=(pid, 'cart'))
#         with c2:
#             st.button("❌ Remove", key=f"wish_remove_{pid}", on_click=remove_from_list, args=(pid, 'wishlist'))

# elif menu == "Orders":
#     st.subheader("📦 Your Orders")
#     for order in user_data['orders']:
#         st.markdown(f"📅 {order['timestamp']}")
#         st.write("🛒 Items:", order['items'])

# elif menu == "Logout":
#     st.session_state.authenticated = False
#     st.session_state.user_email = None
#     st.success("You have been logged out.")
#     st.experimental_rerun()


# import streamlit as st
# import pandas as pd
# from datetime import datetime, timedelta

# # ---------------- HEADER ----------------
# st.markdown("""
#     <h1 style='text-align: center; font-weight: 700; color: #2c3e50; font-size: 40px; margin-top: 20px; margin-bottom: 0px; font-family: "Segoe UI", "Roboto", sans-serif;'>Welcome to Bhojan Bazaar</h1>
#     <h3 style='text-align: center; color: #7f8c8d; font-size: 20px; font-weight: 400; margin-bottom: 30px;'>Your Trusted Raw Material Marketplace</h3>
# """, unsafe_allow_html=True)

# # ---------------- SESSION ----------------
# if 'cart' not in st.session_state: st.session_state.cart = []
# if 'wishlist' not in st.session_state: st.session_state.wishlist = []
# if 'menu' not in st.session_state: st.session_state.menu = "Home"
# if 'orders' not in st.session_state:
#     st.session_state.orders = [
#         {"name": "Onion 5kg", "status": "Delivered", "delivered_date": "2025-07-25"},
#         {"name": "Rice 10kg", "status": "Out for Delivery", "estimated_date": (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')},
#         {"name": "Oil 1L", "status": "Shipped", "estimated_date": (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')}
#     ]
# if 'selected_category' not in st.session_state: st.session_state.selected_category = None

# # ---------------- CSS ----------------
# st.markdown("""
#     <style>
#     .top-bar { display: flex; align-items: center; justify-content: space-between; padding: 12px 20px; background-color: #f9f9f9; border-radius: 12px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08); margin-bottom: 30px; }
#     .top-bar .stButton>button { background-color: #3498db; color: white; padding: 10px 22px; border-radius: 25px; border: none; font-size: 15px; font-weight: bold; transition: 0.2s; }
#     .top-bar .stButton>button:hover { background-color: #2980b9; }
#     .top-bar .stTextInput>div>input { width: 100%; padding: 12px 20px; border-radius: 30px; border: 1px solid #ccc; font-size: 16px; outline: none; }
#     </style>
# """, unsafe_allow_html=True)

# # ---------------- NAV BAR ----------------
# col1, col2, col3 = st.columns([1.2, 5, 1.2])
# with col1:
#     if st.button("🏠 Home"):
#         st.session_state.menu = "Home"
#         st.session_state.selected_category = None
#         st.rerun()
# with col2:
#     search_query = st.text_input("Search products...", "", key="search_input", label_visibility="collapsed")
# with col3:
#     if st.button("👤 Account"):
#         st.session_state.menu = "Account"
#         st.rerun()

# # ---------------- LOAD DATA ----------------
# products = pd.read_csv("india_products_with_locations.csv")

# # TEMP DEBUG: Show columns
# # st.write("Available columns:", products.columns.tolist())

# # Normalize column names
# products.columns = products.columns.str.strip()

# # Check if expected columns exist
# required_columns = ['Product Name', 'Location', 'Price']
# if not all(col in products.columns for col in required_columns):
#     st.error("❌ CSV is missing required columns: 'Product Name', 'Location', or 'Price'")
#     st.stop()

# # ---------------- ACCOUNT PAGE ----------------
# if st.session_state.menu == "Account":
#     st.markdown("## 👤 Account Info")
#     st.write("Name: Kalpana Patidar")
#     st.write("Email: kalpana@example.com")
#     st.markdown("### 📦 Order History")
#     for order in st.session_state.orders:
#         st.write(f"**{order['name']}** - {order['status']}")
#         if order['status'] == "Delivered":
#             st.write(f"Delivered on: {order['delivered_date']}")
#         else:
#             st.write(f"Expected by: {order['estimated_date']}")
#     st.stop()

# # ---------------- HOME PAGE ----------------
# if st.session_state.menu == "Home":
#     st.markdown("## 🛍️ Products")
#     if search_query:
#         filtered_products = products[products['Product Name'].str.contains(search_query, case=False, na=False)]
#     else:
#         filtered_products = products

#     for idx, row in filtered_products.iterrows():
#         with st.container():
#             cols = st.columns([2, 4, 2])
#             with cols[0]:
#                 st.image("https://via.placeholder.com/150", width=120)
#             with cols[1]:
#                 st.subheader(row['Product Name'])
#                 st.write(f"📍 Location: {row['Location']}")
#                 st.write(f"💰 Price: ₹{row['Price']}")
#             with cols[2]:
#                 if st.button("Add to Cart", key=f"cart_{idx}"):
#                     st.session_state.cart.append(row['Product Name'])
#                     st.success(f"{row['Product Name']} added to cart!")
#                 if st.button("Add to Wishlist", key=f"wishlist_{idx}"):
#                     st.session_state.wishlist.append(row['Product Name'])
#                     st.info(f"{row['Product Name']} added to wishlist!")

# # ---------------- CART & WISHLIST ----------------
# st.markdown("## 🛒 Your Cart")
# if st.session_state.cart:
#     for item in st.session_state.cart:
#         st.markdown(f"- {item}")
# else:
#     st.info("Your cart is empty.")

# st.markdown("## ❤️ Your Wishlist")
# if st.session_state.wishlist:
#     for item in st.session_state.wishlist:
#         st.markdown(f"- {item}")
# else:
#     st.info("Your wishlist is empty.")

# You said:

# import streamlit as st
# import pandas as pd
# from datetime import datetime, timedelta
# st.set_page_config(page_title="Bhojan Bazaar", layout="wide")

# # Static Banner Image (no caption)
# st.image("https://cdn.pixabay.com/photo/2021/05/26/04/43/grocery-6284031_960_720.png", use_column_width=True)

# # Bold, centered heading using HTML
# st.markdown("""
# <h1 style='text-align: center; font-weight: bold; color: #333333; font-size: 32px; margin-top: 10px;'>
#     Welcome to Bhojan Bazaar - Your Trusted Raw Material Marketplace
# </h1>
# """, unsafe_allow_html=True)

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
# if 'back_to_home' not in st.session_state:
#     st.session_state.back_to_home = False
# if 'selected_category' not in st.session_state:
#     st.session_state.selected_category = None

# # Load Data
# products = pd.read_csv("india_products_with_locations.csv")

# # Header Bar
# header_cols = st.columns([1, 7, 1, 1, 1, 1])
# with header_cols[0]:
#     if st.button("🏠", help="Home"):
#         st.session_state.menu = "Home"
#         st.session_state.selected_category = None
#         st.rerun()
# with header_cols[4]:
#     if st.button("👤 Account"):
#         st.session_state.menu = "Account"

# # Centered Search
# st.markdown("""
#     <style>
#     .search-bar {
#         display: flex;
#         justify-content: center;
#         margin-bottom: 20px;
#     }
#     .search-bar input {
#         width: 50% !important;
#     }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown('<div class="search-bar">', unsafe_allow_html=True)
# search = st.text_input("", placeholder="Search 9000+ products")
# st.markdown('</div>', unsafe_allow_html=True)

# # Nearest Toggle Only for Search
# if search:
#     st.markdown("<div style='text-align:right;'>", unsafe_allow_html=True)
#     st.toggle("📍 Nearest Location", key="location_filter")
#     st.markdown("</div>", unsafe_allow_html=True)
# # --- Navigation Buttons ---
# cols = st.columns([8, 1, 1, 1])
# with cols[1]:
#     if st.button("🛒", help="Cart"): st.session_state.menu = "Cart"
# with cols[2]:
#     if st.button("💗", help="Wishlist"): st.session_state.menu = "Wishlist"
# with cols[3]:
#     if st.button("📦", help="Orders"): st.session_state.menu = "Orders"

# # --- Helper Functions ---
# def add_to_cart(pid):
#     if pid not in st.session_state.cart:
#         st.session_state.cart.append(pid)
#         st.success("✅ Product added to cart!")

# def add_to_wishlist(pid):
#     if pid not in st.session_state.wishlist:
#         st.session_state.wishlist.append(pid)
#         st.success("💗 Product added to wishlist!")

# # --- Account Page ---
# if st.session_state.menu == "Account":
#     st.subheader("👤 Your Profile")
#     if st.button("✏️ Edit Profile"):
#         st.session_state.edit_mode = not st.session_state.get("edit_mode", False)
#     edit = st.session_state.get("edit_mode", False)
#     name = st.text_input("Full Name", value="Kishan Vendor", disabled=not edit)
#     phone = st.text_input("Phone", value="9876543210", disabled=not edit)
#     email = st.text_input("Email", value="kishan@example.com", disabled=not edit)
#     address = st.text_area("Address", value="Indore", disabled=not edit)
#     if edit: st.button("Save Changes")
#     st.button("🚪 Logout")

# # --- Search Results Page ---
# if search:
#     st.subheader(f"🔍 Search Results for '{search}'")
#     if st.session_state.get("location_filter"):
#         st.markdown("<div style='text-align:right;'>📍 Nearest Location Filter Applied: True</div>", unsafe_allow_html=True)
#     if st.button("🔙 Back to Home"):
#         st.session_state.menu = "Home"
#         st.session_state.selected_category = None
#         st.rerun()
#     results = products[products['name'].str.contains(search, case=False)]
#     if st.session_state.get("location_filter"):
#         results = results[results['supplier_location'].str.contains("Indore", case=False)]
#     if results.empty:
#         st.info("No products found matching the search criteria.")
#     for _, row in results.iterrows():
#         st.markdown(f"""
#         *{row['name']}* from *{row['supplier']}*  
#         Price: ₹{row['price']} | Discounted: ₹{row['price']*(1-row['discount']/100):.2f}  
#         ⭐ {row['rating']} | 📍 {row['supplier_location']} | 🚚 ₹{row['delivery_charge']}
#         """)
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             if st.button("Add to Cart", key=f"cart_{row['product_id']}"):
#                 add_to_cart(row['product_id'])
#         with col2:
#             if st.button("💗 Wishlist", key=f"wish_{row['product_id']}"):
#                 add_to_wishlist(row['product_id'])
#         with col3:
#             st.button("Order Now", key=f"order_{row['product_id']}")
#         st.markdown("---")


# # Home Page - Categories with Grid
# elif st.session_state.menu == "Home":
#     if st.session_state.back_to_home:
#         st.session_state.back_to_home = False

#     st.subheader("🛒 Categories")
#     categories = products['category'].unique()
#     image_map = {
#          "Edible Oil": "https://www.jiomart.com/images/product/original/490000052/fortune-sunlite-refined-sunflower-oil-870-g-product-images-o490000052-p490000052-0-202504081953.jpg?im=Resize=(360,360)",
#         "Grains": "https://www.jiomart.com/images/product/original/rvdtr0vthp/manna-instant-health-mix-200g-spinach-carrot-daal-with-milk-baby-cereal-baby-food-product-images-orvdtr0vthp-p594806042-0-202210261433.jpg?im=Resize=(420,420)",
#         "Spices": "https://www.jiomart.com/images/product/original/rvlfuumgzv/chokhi-dhani-bombay-biryani-masala-100gm-product-images-orvlfuumgzv-p611552031-0-202505292308.jpg?im=Resize=(360,360)",
#         "Cleaning Supplies": "https://www.jiomart.com/images/product/original/494263706/gebi-ecogin-clean-o-brush-toilet-brush-pack-of-2-product-images-o494263706-p605498198-0-202310311821.jpg?im=Resize=(360,360)",
#         "Dairy": "data:image/webp;base64,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",
#         "Sauces": "data:image/jpeg;base64,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",
#         # "Packaging Material": "data:image/jpeg;base64,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",
#         "Packaging Material": "https://www.jiomart.com/images/product/original/rvjz09yn4t/agroha-plastic-polythene-clear-bags-small-size-pouches-transparent-self-adhesive-bopp-bags-for-jewellery-packing-pack-of-100-pieces-4-5-inch-10-12-5-cm-product-images-orvjz09yn4t-p609367969-0-202406171609.jpg?im=Resize=(360,360)",
#         "Sweetener": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZVGa6EsitJTY_V6o-y1szbfFwvn12LzijQA&s"
#     }

#     for i in range(0, len(categories), 4):
#         category_cols = st.columns(4)
#         for j, cat in enumerate(categories[i:i+4]):
#             with category_cols[j]:
#                 st.image(image_map.get(cat, "https://cdn-icons-png.flaticon.com/512/1046/1046784.png"), width=100)
#                 if st.button(cat):
#                     st.session_state.selected_category = cat
#                     st.session_state.menu = "Category"
#                     st.rerun()

# elif st.session_state.menu == "Category" and st.session_state.get("selected_category"):
#     cat = st.session_state.selected_category
#     st.subheader(f"Items in {cat}")
#     cat_items = products[products['category'] == cat]
#     for _, row in cat_items.iterrows():
#         st.markdown(f"**{row['name']}** (₹{row['price']} → ₹{row['price']*(1-row['discount']/100):.2f})")
#         st.markdown(f"⭐ {row['rating']} | 📍 {row['supplier_location']} | 🚚 ₹{row['delivery_charge']}")
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             if st.button("Add to Cart", key=f"dept_cart_{row['product_id']}"):
#                 add_to_cart(row['product_id'])
#         with col2:
#             if st.button("💗 Wishlist", key=f"dept_wish_{row['product_id']}"):
#                 add_to_wishlist(row['product_id'])
#         with col3:
#             st.button("Order Now", key=f"dept_order_{row['product_id']}")
#         st.markdown("---")

# # Cart Page
# elif st.session_state.menu == "Cart":
#     st.subheader("🛍 Your Cart")
#     total = 0
#     for pid in st.session_state.cart:
#         item = products[products['product_id'] == pid].iloc[0]
#         price = item['price'] * (1 - item['discount'] / 100)
#         st.write(f"{item['name']} - ₹{price:.2f}")
#         if st.button("❌ Remove", key=f"remove_{pid}"):
#             st.session_state.cart.remove(pid)
#             st.success("🗑️ Removed from cart!")
#             st.rerun()
#         if st.button("💗 Save for Later", key=f"save_{pid}"):
#             if pid not in st.session_state.wishlist:
#                 st.session_state.wishlist.append(pid)
#             st.session_state.cart.remove(pid)
#             st.success("💗 Moved to Wishlist!")
#             st.rerun()
#     st.markdown(f"### Total Payable: ₹{total:.2f}")
#     st.radio("Payment Mode", ["Cash on Delivery"], key="pay_mode")
#     if st.button("✅ Place Order"):
#         st.success("Order Placed with Cash on Delivery!")
#         st.session_state.cart = []

# # Wishlist Page
# elif st.session_state.menu == "Wishlist":
#     st.subheader("💗 Wishlist")
#     for pid in st.session_state.wishlist:
#         item = products[products['product_id'] == pid].iloc[0]
#         st.write(f"{item['name']} - ₹{item['price']}")
#         if st.button("Add to Cart", key=f"wish_to_cart_{pid}"):
#             if pid not in st.session_state.cart:
#                 st.session_state.cart.append(pid)
#             st.session_state.wishlist.remove(pid)
#             st.success("🛒 Moved to Cart!")
#             st.rerun()
#         if st.button("Remove", key=f"wish_remove_{pid}"):
#             st.session_state.wishlist.remove(pid)
#             st.success("❌ Removed from Wishlist!")
#             st.rerun()
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
#         st.markdown("---") make css file to design it in best way

# NEW OLD CODE


import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
st.set_page_config(page_title="Bhojan Bazaar", layout="wide")

# Static Banner Image (no caption)
st.image("https://cdn.pixabay.com/photo/2021/05/26/04/43/grocery-6284031_960_720.png", use_column_width=True)

# Bold, centered heading using HTML
st.markdown("""
<h1 style='text-align: center; font-weight: bold; color: #333333; font-size: 32px; margin-top: 10px;'>
    Welcome to Bhojan Bazaar - Your Trusted Raw Material Marketplace
</h1>
""", unsafe_allow_html=True)

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
if 'back_to_home' not in st.session_state:
    st.session_state.back_to_home = False
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = None

# Load Data
products = pd.read_csv("india_products_with_locations.csv")

# Header Bar
header_cols = st.columns([1, 7, 1, 1, 1, 1])
with header_cols[0]:
    if st.button("🏠", help="Home"):
        st.session_state.menu = "Home"
        st.session_state.selected_category = None
        st.rerun()
with header_cols[4]:
    if st.button("👤 Account"):
        st.session_state.menu = "Account"

# Centered Search
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

# Nearest Toggle Only for Search
if search:
    st.markdown("<div style='text-align:right;'>", unsafe_allow_html=True)
    st.toggle("📍 Nearest Location", key="location_filter")
    st.markdown("</div>", unsafe_allow_html=True)
# --- Navigation Buttons ---
cols = st.columns([8, 1, 1, 1])
with cols[1]:
    if st.button("🛒", help="Cart"): st.session_state.menu = "Cart"
with cols[2]:
    if st.button("💗", help="Wishlist"): st.session_state.menu = "Wishlist"
with cols[3]:
    if st.button("📦", help="Orders"): st.session_state.menu = "Orders"

# --- Helper Functions ---
def add_to_cart(pid):
    if pid not in st.session_state.cart:
        st.session_state.cart.append(pid)
        st.success("✅ Product added to cart!")

def add_to_wishlist(pid):
    if pid not in st.session_state.wishlist:
        st.session_state.wishlist.append(pid)
        st.success("💗 Product added to wishlist!")

# --- Account Page ---
if st.session_state.menu == "Account":
    st.subheader("👤 Your Profile")
    if st.button("✏ Edit Profile"):
        st.session_state.edit_mode = not st.session_state.get("edit_mode", False)
    edit = st.session_state.get("edit_mode", False)
    name = st.text_input("Full Name", value="Kishan Vendor", disabled=not edit)
    phone = st.text_input("Phone", value="9876543210", disabled=not edit)
    email = st.text_input("Email", value="kishan@example.com", disabled=not edit)
    address = st.text_area("Address", value="Indore", disabled=not edit)
    if edit: st.button("Save Changes")
    st.button("🚪 Logout")

# --- Search Results Page ---
if search:
    st.subheader(f"🔍 Search Results for '{search}'")
    if st.session_state.get("location_filter"):
        st.markdown("<div style='text-align:right;'>📍 Nearest Location Filter Applied: True</div>", unsafe_allow_html=True)
    if st.button("🔙 Back to Home"):
        st.session_state.menu = "Home"
        st.session_state.selected_category = None
        st.rerun()
    results = products[products['name'].str.contains(search, case=False)]
    if st.session_state.get("location_filter"):
        results = results[results['supplier_location'].str.contains("Indore", case=False)]
    if results.empty:
        st.info("No products found matching the search criteria.")
    for _, row in results.iterrows():
        st.markdown(f"""
        {row['name']} from {row['supplier']}  
        Price: ₹{row['price']} | Discounted: ₹{row['price']*(1-row['discount']/100):.2f}  
        ⭐ {row['rating']} | 📍 {row['supplier_location']} | 🚚 ₹{row['delivery_charge']}
        """)
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Add to Cart", key=f"cart_{row['product_id']}"):
                add_to_cart(row['product_id'])
        with col2:
            if st.button("💗 Wishlist", key=f"wish_{row['product_id']}"):
                add_to_wishlist(row['product_id'])
        with col3:
            st.button("Order Now", key=f"order_{row['product_id']}")
        st.markdown("---")


# Home Page - Categories with Grid
elif st.session_state.menu == "Home":
    if st.session_state.back_to_home:
        st.session_state.back_to_home = False

    st.subheader("🛒 Categories")
    categories = products['category'].unique()
    image_map = {
         "Edible Oil": "https://www.jiomart.com/images/product/original/490000052/fortune-sunlite-refined-sunflower-oil-870-g-product-images-o490000052-p490000052-0-202504081953.jpg?im=Resize=(360,360)",
        "Grains": "https://www.jiomart.com/images/product/original/rvdtr0vthp/manna-instant-health-mix-200g-spinach-carrot-daal-with-milk-baby-cereal-baby-food-product-images-orvdtr0vthp-p594806042-0-202210261433.jpg?im=Resize=(420,420)",
        "Spices": "https://www.jiomart.com/images/product/original/rvlfuumgzv/chokhi-dhani-bombay-biryani-masala-100gm-product-images-orvlfuumgzv-p611552031-0-202505292308.jpg?im=Resize=(360,360)",
        "Cleaning Supplies": "https://www.jiomart.com/images/product/original/494263706/gebi-ecogin-clean-o-brush-toilet-brush-pack-of-2-product-images-o494263706-p605498198-0-202310311821.jpg?im=Resize=(360,360)",
        "Dairy": "data:image/webp;base64,UklGRvQVAABXRUJQVlA4IOgVAAAwUgCdASqcAJwAPmUokUWkIiGVTZX4QAZEtABoREUo1+986m1/6f8Xey7vfjN9p/8/7nfnR/svVp+i/9d7g/6wfrL62n6ze8TzIfsx+znuw/7j9pvdZ6AH9D/w/Wc/3H/N+wj+wHpr/ud8Hv9u/4n7h+1b///YAy8bjD+v8K/Kz8A/cuLt095kfzH8A/tf8B7W/6HwZ+RGoR7S/zviO/1Hez2d/43qF92v+F/c/WE+q81fsh7AH88/q//M9e/+H4ff4H/l+wH/L/8L/4fU5/8v9H6Ifpr/z/6T4C/53/av+t66fsq9Hz9omYgbTZ3ZYdYKAeTdhNzF/vOQB8I1/BgJHX/w6aFqT/7icupyaA71/eaR9g/UAasq9sVasX3f+fyW1CTYucV8PRIvrpCuhc+j1rFFeB+9y58/V44B2ee1oNvc3NdEH0NIA3bj9DR/e+f43OY/Y2E0UB/XLDHz+i7kGurVr1SY7l4t5yYA7vwRj2o/T5bDOx1k8trm07xi0AAPVIi9jYnYYjF1NCnBzb9xXrulCVuvj7+FHD34fgv7/IFCCmjBSpvUvXBYsZbBtB+senE0jvCoqIgy4CzxAaz7LNkpGF8I/VZwtJNMrsxExBe+cmjhNSXli8Gi8npZxxJDecA3hPsKi25VhUN1v/69YHjCqQ2iCfl1Yjo2ujrw3weoBals8wHvrFx/cDhursT9cOEU33SIvGneSbv+f1GTc5OYFJ5hMOnSxaM+SRW/ZZMu1/yWHmfAbmOuteqYrNzK2zE3JdjMLpVRiX0jU40/AhontsBDTzU72zko/Ki6o+Cnis99aprEBKpOg2HrG3QlTtiYI/k6qqyz2k4TV3aKz4EPoK0YsQ6z1dbRXKWATThv9jKwmbfxSEAA/v/b9b7RKQ/L3OZtoE50tXKUwJ98k+VoK4SQCV769NGixsroMydd7jVxGgqVSZekSFncnY/ioQNfhFQDG573Foc+/mfzJDRUj8BN+5HnS+BSiCreoadrRgt1+FZSSBW8rXolI4/UDN2bA/bel2YQTx8ImdsI+DJo+5jH+JdayYS1lKIB2FN2XlFWVzykaJ6UJNgThlMs/U1xeMn+TpN5Q2+399E6+w2u2GuP5JYj8onuqlCvAHgfIT3X8J0T+CqyDWntFnM+akuf7ebOJ13kbEF4fbvw8K+Mzz6DZ8y+CnEv8utkVvbA86sYgjXKirZGzlMzZ83hj1ds2PAtc8tTFfZJ+TLaKFCNyMH2DKVGUTcXBHHgrpOscxP5e41UmmiePWjOLGLkpoj/67kekpPBuQVUWwd8BeNdHQVWb/+h8fYs4Is/l4X1/wfoxx/+PFe0MGC0Ng7igbTdUoNt/lEzkdQVadsI32ydD4cAW+ZGROOcbVTMvqh+9PBoXXr8IKQftUNw0EgcPx2sn+fxyBP2aCA+hkz0Uf0rvT2ZxKXxKnGJOA2xssk6SKIoiz49ncaNFdtYKv+nF4G88fcK0wioV+sppLxwEaP9MrIlfguW2ABYAtf6KHkVPMy6L5qRDVfJavnVGFWDrA++owxUU9o0oX1Tji36BsIzT0mU0Cb+UxitVQvF2LlHNyLJQeDuO1Liti8IyqYB6o3VW9muUlTDmI+A2z8H/Q/AjYfDJgEmGu/QZvm6pN6qZVxB7te/z6C/YK4e4I5UfEcDzb4vicemjRmZNieaO8HGbtQLsRNG33n7ev2dkUsMBdO4ov0OaopsUAIei0hPFOY8vkhioqDPNNayIzi2oAMJ1B/AWW/+T54yoRXMzCmjfYGG8mcVZXVpmDuyhWDgMIYF5NZyK6kloKkIln0EXlEjxt/hYa+ERgDtDsTeLJm5HjfPdzPLOTdMaTKjsLtNTB52cRRncdjoq3Aba0TmT8mQX8jxe+FkeP2k4yt4Gsw0wYGf5abfAioOaCJE1a+AwE90oGoqDjZnJvv62aRxUv8cs66JK6FKkGOvEfLk4zfYhP6yoIOOpWtw4/qwS8zcauAcMTdmyOoRmDEOwdGBymzt9UGTtVZlbewfIpqHwYPhhfXeIuMjNu2N0dDaOCVizygTkJ/cRKNx15ov7ZM5d/VlXyyPclm47Gb+FIkfXWJG9oU6rd/mBbaTLNj22DLJ/IZGee0gZKOxDzKICInDty0x/DitfTvEF6PgKhoULI+sB90cwEq4AnhNJiyP4SQHzDOBpgjK33cNY94EIYs88+Ffd0Q3dyt/CxFz9QmJPZMDsThIJYafV3+XkFqT9+oar/VU502doxrFcs6eO0huUEf4aPtN6pe13zv38nqkmK2S8uFHZQCNcEWW9b/zbtbtfpaATEGMWS5rvHmaH0Gu0RqEfoN2T4zUB8f4KJhHaK+ii+2idS18Aank77wcrmQNzO3TXuNvvFsO3La1vy7VnAvnM5zJ61TmQZIeMucQLeXhUKlVxMw3A68XxXe0p+JPvC9Fq/Bfcmh9TW9hTQYgA6YlPAk+XsMs7yLnoxP8WCEsAKlkF+3h/opQe5T0ebLBKLjOb/gea0pBzeTcb5hqlX+hofhrHvoA2f4yeH1yOlJyiNT8SdlwkC8VjYOsmWtGwjX/cDtqpgb4JW5cnRy376IJYG4MeNEzwjWJixfZzGbihbxuHwBpOKfaxyipwdU2IKxNPCtqNCvuYjTutzzwxnZ4fhZYezIOP3Jnu8mqUHKplEbjnzJZNxpu/vPJN2CffNvoA0OgOqPWMcH3xL2GD23p8GXQCldXamRCHiUaGApDKSZq0vEY4rsJbSwLMiKtCq0rgH2h2wJLM32UFdjSChybfu/hKrVvmspqcJIsjdzPnxV/71T0Zsx4NUbimMUzE1E1Qi3Iivm8x6AB2r0Lrr0XfZ8RwcYzfM6YARm4T3Ozu0LZZNu/I88rHQQpwm8Y+GgSm01O2o7UENPmquK2eNKvyGCMN5eluM7I9o0NqWPbX9zl4JX0QahRz8tu9DxKTMNF42F08H4hNw/SYNrOWtmvlYDsHl+EjtXsBgUPdPawYumotdlMub9GD3FP7nV4McB5MQ0jzAHHDU+sJlt4qeL/wMvGoY5ic+rTZXKXYmaitm2U7Vh+z11cMyeDhCVCbvj/uRBoQO4cJ/jSBvzm/beHEvmJxyHlfbAk2qngGRMN1d4SwJ98dakw3Hwfo4QWoz057tsvKJ2p2ppwU1Aez5uBgRq51ALTZUeZZvgW3p+1bsJbcQE1YGVPG2W/PoRm4NH3xSVVPrhMRr+eO5TM7ccjkpL/urOosqOZMrAbNA2Pod/N+LU8wZsHEl4FuaZsVMfFc1aoRsMsZnwP4Wt4vtPe+AwQzb1gWUxa8pNpEfmOUoX92b30A2RV1nRqp0AbE11hm9BcfNyH4YzzDEB+8NsydIrFuekfFj7aE82hmZR2JYzoCppyxuvh3G4XZVE1/KnZD2Vp6E9fATS8QZuGaVIeKEVIJhhAf/drYxiQipoGCyh5E7VdH7EhQl7TWS7r7YIo9fh6rYKhnxw32GUq2t9FWjlCwp6/0dXUsghGE3/J7+SRDpLMfP5KzxV1rWj+TUIGQ0eUj2M7/AMqMBCkEeBuIIlz8Mh9hgm4bTJR8rz+2LBgQy9JOyQrhsh4dgY+FKO9VO4aWuPC4XeJABEGB8dkFIToiMsL09ZRSkyN2TDNrvL+QAqVuf+5bWbPIsUQewKM6u3PlBPFLBhd0jEltSUWk8W5o9cw/hfUHuOVB1FgmioLmRJa1k5P36HrqmqL6c7el8Dyowna1JFvx3hQ86o8w2ZBzip7xRLfYXLzjxu2EYxTuR11EyDnKFHtG6fn7LV3/D5+qPWIHtSKWuI6FWu4FEQLwzIYZ3SumTCo/dPOIr//bsEjVdUqPocXJMTrnrIkcvfsFp5G7CM3EyKJxORM6s1lebR1lyf5UC5cCwOmUC6/uyBOGhRD/y9VRRBQGRuLgiVNpX4KJwfenYgur3t9HPa7DNE9O+5czFoAtvv5ZSDDl/enqyjuewr9YiOS/gHHsEjiq1hFSQLNgrqOkNxSdK9PZmZmXM540oAZeY5pk5d7EPrpAPfg1W9G7CLrl+7+pq6MSle/J62s9NDIb9MkYQ6kwAhpuQOdvp6HLv7orvRs37XkYlnBL2gePv2nwKqI3yqfxDbRO2v+ay1wp85y8sieuqPcIz/VO1DbM1Tx5NekZhH4YhDwzQY0aRH53sYOoeC7BMyxux4VsjTb8i0tv32b7VGJ8+/ct9TKPwCikM8xRDtXmxul07juhYpb+ZGXzbQxL0U9yW1bwIdD7WwaMJ35nmfU1uA93MdU7azy41jDzTUTVqyyClS8bzsHOUfSWrFqwyb1U265QqZTNNuNv/0uJNaZxLoVJoQovmQi+u0ui5N5LdTQ4ijkUbqwiJkz1i7rKQBPM0HalNqgo6zUUZJhmlPbtOvewPrGhZ8S7RMm3NNh1hEOnpTg/bPpzA5M9cXEyTiRiD21XWvhmGdH+0nXBRyt9+pKCza/I9d70FVuHJ7ilC+Y7+LNEEU3wYKm9QCJJXptzd0mchuTJ7IA7jEANYcrLWVGd8zXA17C/O5be3QTgdqwEE5TalVF4zNHXHpwEjvirXyqL7iFrz4ijDP0i7sfqT8WHUkzu6Ap8c9cBXkGpnfW/9/iVsioq/pkRBUug4fIfmCl9N1alwcCUc5K2VzKUcdvz7fA0c4n52ARnPTm0ThJJIBMxfqcP5w/HsOqNchpfYsTWsuStARis+2888iZ/s32/in8kmF2pYoAnt3mxQ8h96DKQZWL9xcIYNo3ixZGJ1jK4MLuc20Omsp3KzOxvX9DK+29os2IY7w9DVy9fdA/8SAd/gMIDFj6xRKuJd+47+e6oBjaBrAk8lsq2GlDs6gb2fUIRmTGM7xjORPqdAYNrIgUiequoYhuTF9f2mlCz7Z793eLYt3tJNXtQ7c6fKYfhCr9OR0WIP3EXR9R9s8yQ1hrWpMWLH/vFyOI3S0JDeEEAO7kk8eu8ULbYkBa9bdbznTKKBHINqWUNDxQGdlj51/MsmCAER6u7qpn/mx8pkIoO6euYNLm3O57SXGDMAVtKtPsPrI6xKmk11bpK4bwlRKSajKCrf7YheXj2k0uf47SKImuHrwb7J+vjzpFUKBc9EEUFfW9hOyOGoEuusLYfdqOXAoDVjtxJYoUKZyG3zdfWeFJ3+wiCNiNQN1Yb2CpY/8L8UjgW7NvUNeJUp+Q5DHWQN0NgO5J6Hvo17OinJEkd21vcL9R/D+ruDRGdwLxm7eO3i9JXgP/qqdXcMhGRvBAFhgLGenmh5cdpT9XguLTERuNLJGUdkSZpr11W9cCbzLKRrHeoq+4NekW+jbBgUV7WVURkDDshhrdwbhEU0h8zxCPmVmU69crArWqGWU7PQ2msieRp6QRJcTI20DiYvx4SvH8JCZu2ilcOWgqNKUQPofalFGChzYtsb8exs0xP9IetwLPDNtDAICMNSdMqGFxDiqehdHzJZf6pa2um4lqiEhvU4NAsv3rBiF4OCHJ8Rhg/U1eFvBx2fMfeAtQjagcHg9E0ZEDk5k4Dl6IZ5oSbjw/KTepm8dn6FhR1y+jlcZX7v3yIyjW/qyVo91PIOHBmCpuMt2ohZhLYuKBU0KWmc3/VisqjO9g1ihawdsxv7d8c6R2lAqXxCqcUlIpJGXWOmzc2DDj2DPA+YlSIEV15LzX/FFfSwcWe7gbbCpKuJxg1meFZPw86MqE8HMAFDqh2AcH95SYmj42oHBvX/5D+TW1DQV1Su7Dy9gFKUW4spEJjlWi6Eh+W7txz2wM8mjeDXp2v3OtpB8t71/b6ghM9iA5wR+TsCXkdLwQ/qZetuHuewZZQyd9kZGvOvuqvm76ENwSoFG6oqIm3O5s4G3lPhDUbhi6wfIwBNyHTz/tifn18GDnuyJSgknZknOW4JPhXJF/IqmonF6dP/8R4XSuB9uJ/DtpKEAbna9H5hUFOzgH4szBA2uieQ0w+DoFbeTID/1apQeZybtYRoQC3H+0zhTN8qaZJqrXBed3OAjEzqbGuLhgD1+yj86QjjSxfVUpufim06FCO8rqLhgf2A+6A2OQTtsjA3wnYYo3WfJ7wm1HjpfefNvIZ7p+Zf+Rktf5cvyQwNlwXkTVygwCZ6osRxoQbHRwYPQWzPW8Tod0yR6HcrE2wfKG5Qy34RXM40Pb565hJ0hbmN4ixA2RItdGHciMLFJMj+A9U2lIu8J5RXAjlTpy7nwy3T/wZjivnICJQg3geOV4whD4UeRU+i0KtPbq9CCaDUIQT81mCilYgPgd5f98Ga6b/mqQgRCASUtJA8ffI4Tky5GjoBdmFx/ggU/xUx4ALX0cWToEo26IT2bg62yqR1muxp0OyEeCSnPvxEgYHhVT92Gf4uYnj5ccrbBRKTm5K50kuejxHw3CmJXhDFyfFBaWy3CYAMrTz9BLl/rB0+ESlm9JXFZHRICsEOJjtc8o1ys5Kpnz7V1WKXHuwkuqqD9SdsBw8BBTfRml+lrikH2M4OLkwCNUUwvko+tzg+7Z0h5NcCvr+kJN9k6UGqfxcFWSFDHpLgd/UOM0tB0n7TK7Afhz1DmTXhlYPl9KKfbXnNIJWPBoj7LQfZXKWN5EgHSBhMWovC0JRxNI27nx574CIEH+nMwHShieMGST2QXztElPBLC0dDapXu1PgYOIpGn0sEDlT1Op6bVUcNrXL15bk6vQCOt6Gqfcqn83l1FHtj+aozAy2TyZY67sBzrLQyxrq+/iji6k7efIpL5R+biRwWi0aZwmj1cKMN3PpM22sFbjAkHVyvkFbllsA8W6LbhiYXsY7eFuL4v6Dwkv0rmIWcM0DOUcPgCBpZ1mTSCjMrbts7G9zTV6UImLWJcCM0xYsWS2HO1euuQ2Cfl2ovVA6utCCW7ixmPW5oG+/9QrZdXe2wNkQqtwUpGvqSBSTG+sGYdVPAHjDESO2UzSbYs8USEgo981wjAdnB2xBVRq68+5eJZFWpIweQC3Uhap921ACjRYSA1sCwnFzsJMc0Q4+uqOou3ZlW7Hw261Kl/ZofoCpAHXIQiWe572dMHzjMpzJxlHagVP4q2kIkDbL4sU7XNqhexIGGANiztOeXteR1YphZgwsT7dkUQdRZtsYWF943g8akpbv0zVcQI+8njeqgpoRf1RhXDC59czrKBYbhVmg/XdFo2F3zykGdVnFcNvd3etJpsjcXymA5yyabLCqJfEiJYwv4aKtE0h6m+EH+BxU0IWRqRtfg1ZJwM4VF44iVxKsZZtMB+ce7pSawvPtRN+CxgxAdEA+K3LQ+XhodtC+1oS+WfSg+3g/zGnLeicZEz2Y8T7nYUjYerz04FIYAADjvlAAD7brBfexG/LueISfQFVlHuK1NeymbHWJ2qQ9TrngI3gOwDKMjyx0OcRfiiqmc/y1AdsRwrbow6iEni0pJbkqCf+SM1MEgyVBKUcLWQV3+swm4WQO+Tf51SjoRIbDjGUdoZXCY5VUnh767a06WhVJlyK27HKwqqPolYNGAAA",
        "Sauces": "data:image/jpeg;base64,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",
        # "Packaging Material": "data:image/jpeg;base64,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",
        "Packaging Material": "https://www.jiomart.com/images/product/original/rvjz09yn4t/agroha-plastic-polythene-clear-bags-small-size-pouches-transparent-self-adhesive-bopp-bags-for-jewellery-packing-pack-of-100-pieces-4-5-inch-10-12-5-cm-product-images-orvjz09yn4t-p609367969-0-202406171609.jpg?im=Resize=(360,360)",
        "Sweetener": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZVGa6EsitJTY_V6o-y1szbfFwvn12LzijQA&s"
    }

    for i in range(0, len(categories), 4):
        category_cols = st.columns(4)
        for j, cat in enumerate(categories[i:i+4]):
            with category_cols[j]:
                st.image(image_map.get(cat, "https://cdn-icons-png.flaticon.com/512/1046/1046784.png"), width=100)
                if st.button(cat):
                    st.session_state.selected_category = cat
                    st.session_state.menu = "Category"
                    st.rerun()

elif st.session_state.menu == "Category" and st.session_state.get("selected_category"):
    cat = st.session_state.selected_category
    st.subheader(f"Items in {cat}")
    cat_items = products[products['category'] == cat]
    for _, row in cat_items.iterrows():
        st.markdown(f"{row['name']}** (₹{row['price']} → ₹{row['price']*(1-row['discount']/100):.2f})")
        st.markdown(f"⭐ {row['rating']} | 📍 {row['supplier_location']} | 🚚 ₹{row['delivery_charge']}")
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Add to Cart", key=f"dept_cart_{row['product_id']}"):
                add_to_cart(row['product_id'])
        with col2:
            if st.button("💗 Wishlist", key=f"dept_wish_{row['product_id']}"):
                add_to_wishlist(row['product_id'])
        with col3:
            st.button("Order Now", key=f"dept_order_{row['product_id']}")
        st.markdown("---")

# Cart Page
# Cart Page
elif st.session_state.menu == "Cart":
    st.subheader("🛍 Your Cart")

    if not st.session_state.cart:
        st.info("Your cart is empty.")
    else:
        total_mrp = 0
        total_discount = 0
        delivery_charge_total = 0

        for pid in st.session_state.cart:
            item = products[products['product_id'] == pid].iloc[0]

            # Extract all required fields
            name = item['name']
            mrp = item['price']
            discount_percent = item['discount']
            discount_amount = mrp * (discount_percent / 100)
            final_price = mrp - discount_amount
            delivery_charge = item['delivery_charge']
            supplier = item['supplier']
            rating = item['rating']
            stock = item['stock']

            if stock <= 0:
                st.warning(f"⚠ {name} is currently out of stock.")
                continue

            # Totals
            total_mrp += mrp
            total_discount += discount_amount
            delivery_charge_total += delivery_charge

            # Product display
            st.markdown(f"""
            ### 🛒 {name}
            - 🏷 *Supplier*: {supplier}
            - ⭐ *Rating*: {rating}/5
            - 📦 *Stock Available*: {stock}
            - 💰 *MRP*: ₹{mrp:.2f}
            - 🎯 *Discount ({discount_percent}%):* ₹{discount_amount:.2f}
            - 🔖 *Price After Discount*: ₹{final_price:.2f}
            - 🚚 *Delivery Charge*: ₹{delivery_charge:.2f}
            """)

            # Remove / Wishlist options
            col1, col2 = st.columns(2)
            with col1:
                if st.button("❌ Remove", key=f"remove_{pid}"):
                    st.session_state.cart.remove(pid)
                    st.success("🗑 Removed from cart!")
                    st.rerun()
            with col2:
                if st.button("💗 Save for Later", key=f"save_{pid}"):
                    if pid not in st.session_state.wishlist:
                        st.session_state.wishlist.append(pid)
                    st.session_state.cart.remove(pid)
                    st.success("💗 Moved to Wishlist!")
                    st.rerun()

            st.markdown("---")

        # Final total payable
        final_total = total_mrp - total_discount + delivery_charge_total

        # Order Summary
        st.markdown("## 🧾 Order Summary")
        st.markdown(f"- *Total MRP:* ₹{total_mrp:.2f}")
        st.markdown(f"- *Total Discount:* ₹{total_discount:.2f}")
        st.markdown(f"- *Delivery Charges:* ₹{delivery_charge_total:.2f}")
        st.markdown(f"### ✅ Total Payable: ₹{final_total:.2f}")

        st.radio("Payment Mode", ["Cash on Delivery"], key="pay_mode")

        if st.button("✅ Place Order"):
            today = datetime.now()
            for pid in st.session_state.cart:
                item = products[products['product_id'] == pid].iloc[0]
                st.session_state.orders.append({
                "product_id": item['product_id'],
                "name": item['name'],
                "status": "Order Placed",
                "estimated_date": (today + timedelta(days=3)).strftime('%Y-%m-%d')
        })
            st.success("🎉 Order Placed Successfully with Cash on Delivery!")
            st.session_state.cart = []
# wishlist
elif st.session_state.menu == "Wishlist":
    st.subheader("💗 Wishlist")

    if not st.session_state.wishlist:
        st.info("Your wishlist is empty.")
    else:
        for pid in st.session_state.wishlist:
            item = products[products['product_id'] == pid].iloc[0]
            st.write(f"{item['name']} - ₹{item['price']}")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Add to Cart", key=f"wish_to_cart_{pid}"):
                    if pid not in st.session_state.cart:
                        st.session_state.cart.append(pid)
                    st.session_state.wishlist.remove(pid)
                    st.success("🛒 Moved to Cart!")
                    st.rerun()
            with col2:
                if st.button("Remove", key=f"wish_remove_{pid}"):
                    st.session_state.wishlist.remove(pid)
                    st.success("❌ Removed from Wishlist!")
                    st.rerun()

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
