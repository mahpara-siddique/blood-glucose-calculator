import streamlit as st

# Function to calculate estimated HbA1c
def calculate_hba1c(avg_glucose):
    # HbA1c formula: (Average glucose (mg/dL) + 46.7) / 28.7
    return round((avg_glucose + 46.7) / 28.7, 2)

# Function to provide health advice based on glucose level
def provide_health_advice(glucose_level, time):
    if time == "Fasting":
        if glucose_level < 70:
            return "Your glucose level is too low (hypoglycemia). Consider eating something and consult a doctor if this persists."
        elif 70 <= glucose_level <= 100:
            return "Your fasting glucose level is normal. Keep maintaining a healthy lifestyle!"
        elif 101 <= glucose_level <= 125:
            return "You are in the prediabetes range. Consider consulting a healthcare professional for advice on diet and exercise."
        else:
            return "Your fasting glucose level indicates diabetes. Consult a doctor for proper management."
    elif time == "Post-meal":
        if glucose_level < 140:
            return "Your post-meal glucose level is normal. Great job!"
        elif 140 <= glucose_level <= 199:
            return "You are in the prediabetes range. Consider monitoring your diet and exercise."
        else:
            return "Your post-meal glucose level indicates diabetes. Consult a healthcare professional."

# Streamlit app interface
st.title("Blood Glucose and HbA1c Assessment App")
st.write("This app helps assess your blood glucose levels, provides health advice, and estimates your HbA1c value.")

# User inputs
glucose_level = st.number_input("Enter your blood glucose level (mg/dL):", min_value=0, max_value=500, step=1)
time = st.selectbox("When was this glucose level measured?", ["Fasting", "Post-meal"])
average_glucose = st.number_input("Enter your average blood glucose level (mg/dL) (optional for HbA1c calculation):", min_value=0, max_value=500, step=1)

# Button to assess glucose level
if st.button("Assess and Calculate HbA1c"):
    if glucose_level > 0:
        # Provide health advice
        advice = provide_health_advice(glucose_level, time)
        st.subheader("Health Advice")
        st.write(advice)

    if average_glucose > 0:
        # Calculate HbA1c
        hba1c = calculate_hba1c(average_glucose)
        st.subheader("Estimated HbA1c")
        st.write(f"Your estimated HbA1c is: {hba1c}%")
    else:
        st.write("Please enter your average glucose level to calculate HbA1c.")
