import streamlit as st
import phonenumbers
from phonenumbers import geocoder, carrier

def main():
	st.title("Phone Number Location Tracker & Also Service Operator")
	st.subheader("Coded by: TheInsidious!")
	mobile_number = st.text_input("Enter a Phone Number: ",type="password")
	if st.button("Track"):
		ch_number=phonenumbers.parse(mobile_number,'CH')
		st.success("Location: {}".format(geocoder.description_for_number(ch_number,"en")))
		service_operator=phonenumbers.parse(mobile_number,'RO')
		st.success("Service Operator/Carrier: {}".format(carrier.name_for_number(service_operator,'en')))

if __name__=='__main__':
	main()
