import requests
import streamlit as st

# Define the URL of your locally hosted webservice endpoint
API_URL = "http://127.0.0.1:8000/run_crew"
st.title("Medical Insurance Policy RAG Example")
st.markdown("""
Enter text below and click the button to send it to a
locally hosted Flask API which will call the Agent.
""")
# Text input widget
user_input = st.text_input("Enter the medical insurance topic to be researched:")
# Button to trigger the API call
if st.button("Send to Local API"):
    if user_input:
        try:
            # Prepare the data payload as a JSON dictionary
            payload = {"topic": user_input}
            # Make a POST request to the local API
            response = requests.post(API_URL, json=payload)
            # Check if the request was successful (HTTP Status Code 200-299)
            if response.status_code == 200:
                res = response.json()
                st.success("API Call Successful!")
                st.write(f"Result: **{res['result']}**")
                # st.write(f"Processed Text (Reversed): **{result['processed']}**")
                # st.write(f"Processed Text (Reversed): **{result['processed']}**")
            # The rest of this doesn't work due to the limited info that gets passed back from
            # the agent now.  You could return the entire raw result and then do some better (working)
            # error handling...
            else:
                st.error(f"API Call Failed with status code: {response.status_code}")
                st.json(response.json())
        except requests.exceptions.ConnectionError:
            st.error(
                "Could not connect to the local API service. Please ensure `api_service.py` is running in another terminal."
            )
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning("Please enter text before sending.")
