import streamlit as st
from backend.orchestrator import run_agents

# Page config
st.set_page_config(
    page_title="AI Sales Co-Pilot",
    layout= "centered"
)

# Header
st.title("AI Sales Co-Pilot")
st.caption("Multi-Agent AI System for Lead Qualification & Smart Response")

# Input
lead_input = st.text_area(
    "Enter a lead message",
    placeholder= "Example: Hi, I need pricing for your service urgently..."
)

# Button
if st.button("Analyze Lead"):
    
    # Input Validation
    if not lead_input.strip():
        st.warning("Please enter a lead message")
    
    elif len(lead_input) < 5:
        st.warning("Input is too Short")
    
    else:
        try:
            # Loading spinner
            with st.spinner("Processing...."):
                result = run_agents(lead_input)

            st.divider()

            # Layout: 2 columns
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Analysis Output")
                st.code(result["analysis"], language= "json")

            with col2:
                st.subheader("Lead Score")
                    
                if result["score"] == "HOT":
                    st.success(result["score"])
                elif result["score"] == "WARM":
                    st.warning(result["score"])
                else:
                    st.error(result["score"])

            st.divider()

            # RAG Response
            st.subheader("AI Response")
            st.write(result["response"])

            st.divider()

            # Action Recommendation
            st.subheader("Recommended Action")
            st.info(result["action"])

        except Exception as e:
            st.error("Something went wrong")
            st.text(str(e))