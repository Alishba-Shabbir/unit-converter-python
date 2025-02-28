import streamlit as st

def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "Metre": 1,
        "Centimetre": 100,
        "Millimetre": 1000,
        "Kilometre": 0.001,
        "Inch": 39.3701,
        "Foot": 3.28084,
        "Yard": 1.09361,
        "Mile": 0.000621371
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def weight_converter(value, from_unit, to_unit):
    conversion_factors = {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1000000,
        "Pound": 2.20462,
        "Ounce": 35.274
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32

def time_converter(value, from_unit, to_unit):
    conversion_factors = {
        "Seconds": 1,
        "Minutes": 60,
        "Hours": 3600,
        "Days": 86400,
        "Weeks": 604800
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def data_converter(value, from_unit, to_unit):
    conversion_factors = {
        "Bytes": 1,
        "Kilobytes": 1/1024,
        "Megabytes": 1/(1024**2),
        "Gigabytes": 1/(1024**3),
        "Terabytes": 1/(1024**4)
    }
    return value / conversion_factors[from_unit] * conversion_factors[to_unit]

def currency_converter(value, from_currency, to_currency):
    exchange_rates = {
        "USD": {"PKR": 278.50, "EUR": 0.92, "GBP": 0.78, "INR": 83.00},
        "PKR": {"USD": 0.0036, "EUR": 0.0033, "GBP": 0.0028, "INR": 0.30},
        "EUR": {"USD": 1.09, "PKR": 300.00, "GBP": 0.85, "INR": 90.00},
        "GBP": {"USD": 1.28, "PKR": 350.00, "EUR": 1.17, "INR": 105.00},
        "INR": {"USD": 0.012, "PKR": 3.35, "EUR": 0.011, "GBP": 0.0095}
    }
    
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        return value * exchange_rates[from_currency][to_currency]
    else:
        return None

st.title("Professional Converter")
category = st.selectbox("Select Category", ["Unit Converter", "Currency Converter"])

if category == "Unit Converter":
    unit_category = st.selectbox("Select Unit Category", ["Length", "Weight", "Temperature", "Time", "Data"])
    col1, col2 = st.columns(2)
    
    if unit_category == "Length":
        units = ["Metre", "Centimetre", "Millimetre", "Kilometre", "Inch", "Foot", "Yard", "Mile"]
        with col1:
            from_unit = st.selectbox("From", units)
            value = st.number_input("Enter value", min_value=0.0, format="%.6f")
        with col2:
            to_unit = st.selectbox("To", units)
            result = length_converter(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")
    
    elif unit_category == "Weight":
        units = ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"]
        with col1:
            from_unit = st.selectbox("From", units)
            value = st.number_input("Enter value", min_value=0.0, format="%.6f")
        with col2:
            to_unit = st.selectbox("To", units)
            result = weight_converter(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")
    
elif category == "Currency Converter":
    col1, col2 = st.columns(2)
    with col1:
        from_currency = st.text_input("From Currency (e.g., USD, EUR, GBP, PKR)", "USD")
        value = st.number_input("Enter amount", min_value=0.0, format="%.2f")
    with col2:
        to_currency = st.text_input("To Currency (e.g., USD, EUR, GBP, PKR)", "PKR")
        result = currency_converter(value, from_currency.upper(), to_currency.upper())
        if result is not None:
            st.success(f"{value} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")
        else:
            st.error("Invalid currency code or conversion not available.")
