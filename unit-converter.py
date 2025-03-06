
import streamlit as st

# 💡 Adding some style
st.markdown(
    """
    <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 🚀 Title with Emoji
st.title("🔢 Unit Converter ")

st.markdown("### 📏 Convert between different units easily! 🔄")

# 🎯 UI Elements
value = st.number_input("🔢 Enter the value:", min_value=1.0, step=1.0)

# 📝 Convert From (New Line)
unit_from = st.selectbox("📤 Convert from:", ["meters", "kilometers", "grams", "kilograms"])

# ⬇️ Convert To (New Line)
unit_to = st.selectbox("📥 Convert to:", ["meters", "kilometers", "grams", "kilograms"])

# Conversion Function
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
    }
    key = f"{unit_from}_{unit_to}"
    
    if key in conversions:
        return value * conversions[key]
    else:
        return "❌ Conversion not supported!"

# 💡 Convert Button with Styling
if st.button("🔄 Convert Now"):
    result = convert_units(value, unit_from, unit_to)
    st.success(f"✅ **Converted Value:** {result}")

     
