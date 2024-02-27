import pickle
from pathlib import Path

#import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth



# User Authentication


names = ["Saniya Kapur", "Shruti Mundargi"]
usernames = ["skapur", "smundargi"]

#load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    # Sample list of clients
    clients = ["Client 1", "Client 2", "Client 3"]

    # Function to simulate fetching previous session history for a client
    def get_session_history(client_name):
        # Sample session history for demonstration
        session_history = {
            "Client 1": [
                "Session 1 notes for Client 1",
                "Session 2 notes for Client 1",
                "Session 3 notes for Client 1"
            ],
            "Client 2": [
                "Session 1 notes for Client 2",
                "Session 2 notes for Client 2"
            ],
            "Client 3": [
                "Session 1 notes for Client 3",
                "Session 2 notes for Client 3",
                "Session 3 notes for Client 3",
                "Session 4 notes for Client 3"
            ]
        }
        return session_history.get(client_name, [])

    def logout():
        authenticator.logout('Logout', 'main')

    def main():
        
        
        st.title("Therapist Chatbot")

        st.sidebar.title('Welcome *%s*' % (name))
        selected_client = st.sidebar.selectbox("Select a client", clients)
        
        st.sidebar.button("Logout", on_click= logout)

        session_history = get_session_history(selected_client)
        st.subheader(f"Session History for {selected_client}")
        for session_notes in session_history:
            st.write(session_notes)

        st.subheader("Chat with Chatbot")

        therapist_input = st.text_input("Type your message here")

        if st.button("Send"):
            st.write(f"You: {therapist_input}")

    if __name__ == "__main__":
        main()
    # authenticator.logout('Logout', 'main')
    # st.write('Welcome *%s*' % (name))
    # st.title('Some content')

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
