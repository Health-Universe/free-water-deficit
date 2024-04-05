import streamlit as st

def calculate_fwd(na_serum, na_ideal, weight, gender):
    # Calculate Total Body Water (TBW) based on gender
    if gender == 'Male':
        tbw = weight * 0.6
    else:  # Female
        tbw = weight * 0.5
    # Calculate Free Water Deficit (FWD)
    fwd = ((na_serum - na_ideal) * tbw) / na_ideal
    return fwd

# Streamlit app UI
st.title('Free Water Deficit in Hypernatremia Calculator')

# User inputs
na_serum = st.number_input('Enter Serum Sodium (Na) level (mmol/L):', min_value=100, max_value=200, value=145)
na_ideal = st.number_input('Enter Ideal Sodium (Na) level (mmol/L):', min_value=100, max_value=150, value=140)
weight = st.number_input('Enter Patient Weight (kg):', min_value=1, max_value=200, value=70)
gender = st.radio('Select Gender:', ('Male', 'Female'))

# Calculate button
if st.button('Calculate Free Water Deficit'):
    # Perform calculation
    fwd = calculate_fwd(na_serum, na_ideal, weight, gender)
    # Display result
    st.write(f'The Free Water Deficit is: {fwd:.2f} L')
