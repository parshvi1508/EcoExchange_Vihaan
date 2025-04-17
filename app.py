# app.py
import streamlit as st
from streamlit_option_menu import option_menu
import json
import os
from datetime import datetime
import uuid

# Initialize materials.json if not exists
if not os.path.exists('materials.json'):
    with open('materials.json', 'w') as f:
        json.dump({"vendors": [], "materials": []}, f)

# Load materials data
def load_materials():
    with open('materials.json', 'r') as f:
        return json.load(f)

# Save materials data
def save_materials(data):
    with open('materials.json', 'w') as f:
        json.dump(data, f, indent=4)

# Generate unique IDs
def generate_id(existing_ids):
    new_id = 0
    while new_id in existing_ids:
        new_id += 1
    return new_id

# Main app configuration
st.set_page_config(
    page_title="EcoExchange | Circular Marketplace",
    page_icon="♻️",
    layout="wide"
)

# Custom CSS Styles
st.markdown("""
<style>
:root {
    --eco-green: #2ecc71;
    --forest-green: #27ae60;
    --ocean-blue: #3498db;
    --deep-teal: #16a085;
    --soft-gray: #ecf0f1;
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, rgba(46, 204, 113, 0.1) 0%, rgba(39, 174, 96, 0.1) 100%);
}

.material-card {
    background: white;
    border-radius: 15px;
    box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    transition: all 0.4s ease;
    overflow: hidden;
    position: relative;
    margin-bottom: 20px;
    padding: 20px;
}

.material-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 5px;
    background: linear-gradient(90deg, var(--eco-green), var(--ocean-blue));
}

.stButton>button {
    background: linear-gradient(45deg, var(--eco-green), var(--deep-teal));
    border: none;
    color: white;
    padding: 12px 25px;
    border-radius: 50px;
    transition: all 0.3s ease;
}

.stButton>button:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# Navigation Bar
selected = option_menu(
    menu_title=None,
    options=["Home", "Browse", "Sell", "How It Works", "Impact"],
    icons=["house", "search", "shop", "info-circle", "graph-up"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
)

# Home Page
if selected == "Home":
    st.markdown("""
    <div style="text-align: center; margin-bottom: 40px;">
        <h1 style='color: var(--forest-green); font-size: 3em;'>🌱 EcoExchange</h1>
        <p style='color: var(--deep-teal); font-size: 1.2em;'>
            Connecting Waste Generators with Sustainable Buyers
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("### Featured Materials")
        data = load_materials()
        for material in data['materials'][:3]:
            with st.container():
                st.markdown(f"""
                <div class="material-card">
                    <h3>{material['title']}</h3>
                    <p>Category: {material['category']}</p>
                    <p>Price: ₹{material['price_per_unit']}/kg</p>
                    <p>Available: {material['quantity_available']} kg</p>
                </div>
                """, unsafe_allow_html=True)

    with col2:
        st.markdown("### Why Choose EcoExchange?")
        benefits = [
            "♻️ Reduce waste sent to landfills",
            "💰 Monetize unused materials",
            "🌍 Contribute to circular economy",
            "📈 Connect with verified buyers"
        ]
        for benefit in benefits:
            st.markdown(f"<div class='material-card'>{benefit}</div>", unsafe_allow_html=True)

# Browse Page
elif selected == "Browse":
    st.title("🌍 Material Marketplace")
    
    data = load_materials()
    materials = data.get('materials', [])
    vendors = data.get('vendors', [])

    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        category = st.selectbox("Category", ["All", "Organic Waste", "Plastics", "Glass", "Paper & Cardboard"])
    with col2:
        price_range = st.slider("Price Range (₹)", 0, 100, (0, 100))
    with col3:
        sort_by = st.selectbox("Sort By", ["Newest", "Price: Low to High", "Price: High to Low"])

    # Filtering logic
    filtered = []
    for mat in materials:
        if (category == "All" or mat['category'] == category) and \
           (price_range[0] <= mat['price_per_unit'] <= price_range[1]):
            filtered.append(mat)

    # Display results
    st.write(f"Showing {len(filtered)} materials")
    for mat in filtered:
        vendor = next((v for v in vendors if v['id'] == mat['vendor_id']), {})
        st.markdown(f"""
        <div class="material-card">
            <h4>{mat['title']}</h4>
            <p>Price: ₹{mat['price_per_unit']}/kg | Available: {mat['quantity_available']} kg</p>
            <p>Vendor: {vendor.get('name', 'Unknown')} ({vendor.get('location', '')})</p>
        </div>
        """, unsafe_allow_html=True)

# Sell Page
elif selected == "Sell":
    st.title("📤 List Your Materials")
    
    with st.form("new_listing"):
        st.write("### Material Details")
        title = st.text_input("Material Name")
        category = st.selectbox("Category", ["Organic Waste", "Plastics", "Glass", "Paper & Cardboard"])
        price = st.number_input("Price per kg (₹)", min_value=0.0)
        quantity = st.number_input("Available Quantity (kg)", min_value=1)
        description = st.text_area("Description")
        
        if st.form_submit_button("List Material"):
            data = load_materials()
            material_id = generate_id([m['id'] for m in data['materials']])
            vendor_id = generate_id([v['id'] for v in data['vendors']])
            
            new_material = {
                "id": material_id,
                "title": title,
                "category": category,
                "price_per_unit": price,
                "quantity_available": quantity,
                "description": description,
                "vendor_id": vendor_id
            }
            
            new_vendor = {
                "id": vendor_id,
                "name": "Demo Vendor",
                "location": "Mumbai"
            }
            
            data['materials'].append(new_material)
            data['vendors'].append(new_vendor)
            save_materials(data)
            st.success("Material listed successfully!")

# How It Works Page
elif selected == "How It Works":
    st.title("🛠️ How It Works")
    steps = [
        ("1. Upload", "Submit details about your materials"),
        ("2. Verify", "Our AI verifies material quality"),
        ("3. List", "Get matched with potential buyers"),
        ("4. Transact", "Complete secure transactions"),
        ("5. Impact", "Track your environmental contribution")
    ]
    
    cols = st.columns(5)
    for i, (title, desc) in enumerate(steps):
        with cols[i]:
            st.markdown(f"""
            <div class="material-card" style="text-align: center;">
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

# Impact Page
elif selected == "Impact":
    st.title("📊 Environmental Impact")
    data = load_materials()
    
    total_materials = len(data['materials'])
    total_quantity = sum(m['quantity_available'] for m in data['materials'])
    co2_saved = total_quantity * 2.5  # Example calculation
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Listings", total_materials)
    col2.metric("Total Quantity (kg)", total_quantity)
    col3.metric("Estimated CO₂ Saved (kg)", f"{co2_saved:,.0f}")
    
    st.write("### Transaction History")
    for mat in data['materials']:
        st.write(f"{mat['title']} - {mat['quantity_available']} kg available")

# Run the app
if __name__ == "__main__":
    st.session_state.setdefault('materials', load_materials())
