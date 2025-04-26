import streamlit as st 

st.title("Unit Converter")

conversion_types = ["Length", "Weight", "Temperature"]
conversion_choice = st.selectbox("Choose Conversion Type:", conversion_types)

if conversion_choice == "Length":
    length_units = ["Meters", "Kilometers", "Feet", "Inches", "Centimeters"]
    input_value = st.number_input("Enter Length Value:", min_value=0.0, format="%.2f")  # Corrected
    from_unit = st.selectbox("From Unit:", length_units)
    to_unit = st.selectbox("To Unit:", length_units)

    length_conversions = {
        "Meters": 1,
        "Kilometers": 0.001,  # Corrected (1 meter = 0.001 km)
        "Feet": 3.28084,
        "Inches": 39.3701,
        "Centimeters": 100,
    }

    if st.button("Convert"):
        result = input_value / length_conversions[from_unit] * length_conversions[to_unit]  # Fixed conversion logic
        st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')

elif conversion_choice == "Weight":
    weight_units = ["Kilogram", "Grams", "Pounds", "Ounces"]
    input_value = st.number_input("Enter Weight Value:", min_value=0.0, format="%.2f")  # FIXED
    from_unit = st.selectbox("From Unit:", weight_units)
    to_unit = st.selectbox("To Unit:", weight_units)

    weight_conversions = {
        "Kilogram": 1,
        "Grams": 1000,  # 1 kg = 1000 grams
        "Pounds": 2.20462,  # 1 kg = 2.20462 lbs
        "Ounces": 35.274,  # 1 kg = 35.274 oz
    }

    if st.button("Convert"):
        result = input_value / weight_conversions[from_unit] * weight_conversions[to_unit]  # Fixed formula
        st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')

elif conversion_choice == "Temperature":
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]  # Fixed spelling mistake
    input_value = st.number_input("Enter Temperature Value:", format="%.2f")  # Corrected
    from_unit = st.selectbox("From Unit:", temperature_units)
    to_unit = st.selectbox("To Unit:", temperature_units)

    def convert_temperature(value, from_unit, to_unit):
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
        return value

    if st.button("Convert"):
        result = convert_temperature(input_value, from_unit, to_unit)
        st.success(f'{input_value} {from_unit} is equal to {result:.2f} {to_unit}')
