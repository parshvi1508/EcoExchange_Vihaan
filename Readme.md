# EcoExchange

**AI-Powered Circular Marketplace for Sustainable Material Exchange**

---

## Problem & Context

Every year, billions of tons of valuable materials like coconut shells, glass, and cardboard are wasted due to the lack of an efficient link between waste generators and reusers. This leads to overflowing landfills, increased pollution, and lost income opportunities for artisans and businesses.

**Key Statistics:**
- **India:** 15 million tonnes coconut waste/year, 35% glass recycling rate, 42% cardboard landfill rate
- **Global:** 200 million tonnes coconut waste/year, 50% glass recycling rate, 35% cardboard landfill rate

---

## Solution Overview

**EcoExchange** is an AI-powered circular marketplace that:
- Lets users upload a photo of their waste material
- Instantly grades and classifies material using computer vision (CNN)
- Calculates and displays real-time CO₂ emissions saved per transaction
- Ensures blockchain-backed traceability for every exchange
- Connects waste sources directly to buyers (artisans, startups, businesses)

---

## How It Works

1. **Upload:** User uploads a photo of the material.
2. **AI Grading:** Computer vision model classifies and grades the material, calculates CO₂ saved.
3. **Marketplace:** Material is listed; buyers can view, filter, and purchase.
4. **Transaction:** Purchase is logged on blockchain for traceability.
5. **Impact Report:** Both parties receive a verified CO₂ savings report.

---

## Uniqueness & USPs

- **AI CV-based grading:** Automated, accurate, and instant material assessment
- **Live CO₂ tracking:** Emissions saved calculated per transaction, visible to all users
- **Blockchain traceability:** Immutable, auditable transaction records
- **Dynamic pricing:** AI-driven, demand and location-based
- **Hyper-specialized materials:** Focus on coconut shells, glass, cardboard, and more
- **Verified impact reports:** Auto-generated for all users
- **Sustainability certifications:** Blockchain-backed, real-time

---

## Revenue Model

- 5% transaction fee on exchanges
- Premium analytics for business users
- Certification reports for sustainability compliance

---

## Impact & Roadmap

- **120T CO₂ saved in pilot**
- Expanding to e-waste and textiles
- Municipal and corporate partnerships in progress
- Roadmap: More material categories, advanced analytics, and community features

---

## Demo

This MVP demo (built with Streamlit) showcases:
- Material upload and AI classification (mock/demo)
- Real-time CO₂ savings calculation
- Marketplace listing and simulated transaction
- Impact dashboard

---

## Getting Started

1. Clone this repository:
```
https://github.com/parshvi1508/EcoExchange_Vihaan
```
2. Change the directory
```
cd ecoexchange
```
3. Activate a virtual environment

4. Install dependencies
```
pip install -r requirements.txt
```
5. Run the application
```
streamlit run app.py
```