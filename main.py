import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import blood_test_analyst, article_researcher, health_advisor
from tasks import initialize_tasks  # Update to import a function to initialize tasks
from pypdf import PdfReader
import streamlit as st

# Load environment variables
load_dotenv()

def main():
    st.title("Medical Report Analysis ➕")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Extract text from PDF
        text = ""
        try:
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                text += page.extract_text()
        except Exception as e:
            st.error(f"Error reading the PDF file: {e}")
            return

        if st.button("Analyze Report"):
            st.write("Analyzing the report... This may take a few minutes.")

            # Initialize tasks with the extracted text
            tasks = initialize_tasks(text)

            # Initialize and run the Crew
            crew = Crew(
                agents=[blood_test_analyst, article_researcher, health_advisor],
                tasks=tasks,
                verbose=True,
                process=Process.sequential
            )

            with st.spinner("Processing..."):
                try:
                    result = crew.kickoff()
                except Exception as e:
                    st.error(f"An error occurred during analysis: {e}")
                    return

            # Display results using Markdown for word wrapping and clickable links
            st.subheader("Analysis Results")
            st.markdown(result)
    else:
        st.write("Please upload a PDF file to begin analysis.")

if __name__ == "__main__":
    main()
