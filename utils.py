import json
import hashlib
from datetime import datetime

def load_demo_data():
    with open('demo_data.json', 'r') as f:
        return json.load(f)

def ai_classify_material(image):
    # Mock AI function (replace with real model)
    material_types = {
        "coconut": ("Coconut Shell", 95),
        "glass": ("Glass Bottle", 92),
        "cardboard": ("Cardboard", 89)
    }
    for key in material_types:
        if key in image.name.lower():
            return material_types[key]
    return ("Other", 75)

def calculate_co2_savings(material_type, quantity):
    co2_factors = {
        "Coconut Shell": 0.82,
        "Glass Bottle": 0.62,
        "Cardboard": 1.12
    }
    return quantity * co2_factors.get(material_type, 0.5)

def generate_blockchain_entry(data):
    timestamp = datetime.now().isoformat()
    block_string = json.dumps(data) + timestamp
    return hashlib.sha256(block_string.encode()).hexdigest()

def save_transaction(data):
    demo_data = load_demo_data()
    demo_data['transactions'].append({
        **data,
        "timestamp": datetime.now().isoformat(),
        "blockchain_hash": generate_blockchain_entry(data)
    })
    with open('demo_data.json', 'w') as f:
        json.dump(demo_data, f, indent=4)
