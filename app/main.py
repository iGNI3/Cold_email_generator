import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

def create_streamlit_app(llm, portfolio, clean_text):
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    st.title("📧 Cold Mail Generator")

    url_input = st.text_input("Enter a job posting URL:", value="https://careers.nike.com/data-engineer-itc/job/R-63119")
    submit_button = st.button("Analyze Job Post")

    # Store jobs and URL in session state
    if 'jobs' not in st.session_state:
        st.session_state.jobs = []
    if 'url' not in st.session_state:
        st.session_state.url = ""

    # When Analyze is clicked, load and extract jobs
    if submit_button or (url_input != st.session_state.url):
        try:
            loader = WebBaseLoader([url_input])
            raw_content = loader.load().pop().page_content
            data = clean_text(raw_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            st.session_state.jobs = jobs
            st.session_state.url = url_input
        except Exception as e:
            st.error(f"An Error Occurred during scraping or extraction: {e}")
            st.session_state.jobs = []

    if not st.session_state.jobs:
        st.info("Submit a URL to extract jobs.")
        return

    st.success(f"Found {len(st.session_state.jobs)} job(s)! Select a job below to generate a cold email.")

    job_titles = [job.get("role", f"Job {i+1}") for i, job in enumerate(st.session_state.jobs)]
    selected_job_idx = st.selectbox("Select a job", range(len(job_titles)), format_func=lambda i: job_titles[i])
    job = st.session_state.jobs[selected_job_idx]
    skills = job.get('skills', [])

    st.subheader(f"Job: {job.get('role', 'N/A')}")
    st.markdown(f"**Experience:** {job.get('experience', 'Unknown')}")
    st.markdown("**Skills:**")
    st.write(", ".join(skills) if skills else "_No skills listed._")
    st.markdown("**Job Description:**")
    with st.expander("Show full description"):
        st.write(job.get("description", "No description."))

    if st.button("Generate Cold Email"):
        try:
            links = portfolio.query_links(skills)
            email = llm.write_mail(job, links)
            st.success("Cold email generated!")
            with st.expander("Preview Cold Email (Markdown)", expanded=True):
                st.markdown(email)
        except Exception as e:
            st.error(f"An Error Occurred while generating email: {e}")

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio, clean_text)