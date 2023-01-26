#modules
import streamlit as st
import re

st.title("Weighbridge System")
 
# inputs
charge = 0 #initializing charge
truckno = st.text_input(label="Truk No:") #truck number input
weight = st.number_input(label="Weight:") #vehicle weight input
# payment_type = st.radio("Payment Type:", ("RTGS", "USD", "RAND")) #Payment type radio input
payment_used = st.selectbox("Payment Type", ("RTGS", "USD", "RAND")) #Payment type dropdown input
 
def weight_range(x): #weight range function
    if weight >= 1 and weight <= 500:
        charge = 50
    elif weight >= 501 and weight <= 1000:
        charge = 100
    elif weight >= 1001 and weight <= 2000:
        charge = 130
    elif weight >= 2001:
        charge = 200
    return charge

def Calculate(): #Rate conversions function
    if weight >= 1:
        fx_charge = weight_range(charge)
        rtgs_val = fx_charge * 1 #RTGS rate conversion
        usd_val = fx_charge * 2.5 #USD rate conversion
        rand_val = fx_charge * 3.30 #RAND rate conversion
        st.success(f"Total RTGS = {rtgs_val}") #print RTGS value
        st.success(f"Total USD = {usd_val}") #print USD value
        st.success(f"Total RAND = {rand_val}") #print RAND value
    else:
        st.warning("The weight can only be at least be 1kg")

#Error Handling Implementation
try:
    if st.button("Calculate result"): 
        if not re.match("^[A-Za-z]{3}[0-9]{4}$", truckno): #Truck Number Validation using regex
            st.warning("Please enter the required Truck Number format (e.g acd1117)")
            if weight < 1: #Weight verification
                st.warning("The weight can only be at least be 1kg")
        else:
            Calculate() #calling the calculate function
except:
    st.error("Something went wrong, Please Contact your Support +263784030630")