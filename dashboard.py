import streamlit as st

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

def main():
    st.title("Therapist Chatbot")

    selected_client = st.sidebar.selectbox("Select a client", clients)

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
