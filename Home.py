import streamlit as st
import streamlit_shadcn_ui as ui
from PIL import Image

# Add Google Fonts link to the HTML header
google_fonts_link = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">'

st.set_page_config(
    page_title="Zeel Thumar | Portfolio",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(google_fonts_link, unsafe_allow_html=True)
# Use custom CSS to set the font to Roboto and make it bold
html_code = """
<style>
    h1 {
        font-family: 'Poppins';
        font-weight: 600;
        letter-spacing: -2px;
        font-size: 80px;
        line-height: 0.9em;
    }
    p, h3, h2, li{
        font-family: 'Poppins';
    }
    /* Media query for larger screens, further adjust line height */
    @media screen and (max-width: 1200px) {
    h1 {
        line-height: 0.6;
    }
    @media screen and (max-width: 768px) {
    h1 {
        line-height: 0.8;
        font-size: 45px;
    }
}
</style>
"""

# Render the HTML code to apply the styling
st.markdown(html_code, unsafe_allow_html=True)

intro_image = Image.open("images/intro-bg.png")
st.image(image=intro_image)   

st.title(":gray[Hey there!] &nbsp;👋 &nbsp;")
st.title(":gray[I'm] Zeel Thumar.")

st.markdown("")

# into cards
cols = st.columns(3)
with cols[0]:
    ui.metric_card(title="Visualization", content="BI Tools", description="Power BI, Tableau, Metabase, Superset", key="card1")
with cols[1]:
    ui.metric_card(title="Machine Learning", content="Stat. Models", description="Scikit learn, Numpy, Pandas, Seaborn", key="card2")
with cols[2]:
    ui.metric_card(title="Natural language", content="LLM", description="Hugging Face, Langchain, OpenAI, Rasa", key="card3")

st.markdown("")

# get in touch url links
url_mail = 'mailto:zeelthumar04@gmail.com'
url_linkedIn = 'https://www.linkedin.com/in/zeel-thumar-522727213'
url_GitHub = 'https://github.com/zeel-04'
url_X = 'https://twitter.com/zeel_thumar'

st.write("I am a Data Science practitioner with a flair for deep learning, machine learning, and natural language processing. Specialized in fine-tuning LLMs like BERT and LLaMA for diverse use cases, I bring a track record of delivering practical solutions. Beyond technical prowess, I excel in MLOps, possess strong analytical thinking, and showcase leadership capabilities. Skillful at integrating ML models into production, I thrive on breaking down complex problems for data-driven solutions.")

st.divider()
#Social media icons
st.subheader("Get in touch &nbsp; 🤝")
st.markdown("")
col1, col2, col3, col4 = st.columns([1,1,1,1])

with col1:
    st.markdown(f'''
    <a href={url_mail}><button style='
    background-color: #262730;
    outline: None;
    border:None;
    border-radius: 50px;
    border-width: 0;
    color: #DEDEDE;
    cursor: pointer;
    display: inline-block;
    font-family: "Haas Grot Text R Web", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 14px;
    font-weight: 500;
    line-height: 20px;
    list-style: none;
    margin: 0;
    padding: 13px 37px;
    padding-top: 15px;
    text-align: center;
    transition: all 200ms;
    vertical-align: baseline;
    white-space: nowrap;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;'>Mail</button></a>
    ''',
    unsafe_allow_html=True)

with col2:
    st.markdown(f'''
    <a href={url_linkedIn}><button style='
    background-color: #262730;
    outline: None;
    border:None;
    border-radius: 50px;
    border-width: 0;
    color: #DEDEDE;
    cursor: pointer;
    display: inline-block;
    font-family: "Haas Grot Text R Web", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 14px;
    font-weight: 500;
    line-height: 20px;
    list-style: none;
    margin: 0;
    padding: 13px 25px;
    padding-top: 15px;
    text-align: center;
    transition: all 200ms;
    vertical-align: baseline;
    white-space: nowrap;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;'>LinkedIn</button></a>
    ''',
    unsafe_allow_html=True)

with col3:
    st.markdown(f'''
    <a href={url_GitHub}><button style='
    background-color: #262730;
    outline: None;
    border:None;
    border-radius: 50px;
    border-width: 0;
    color: #DEDEDE;
    cursor: pointer;
    display: inline-block;
    font-family: "Haas Grot Text R Web", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 14px;
    font-weight: 500;
    line-height: 20px;
    list-style: none;
    margin: 0;
    padding: 13px 30px;
    padding-top: 15px;
    text-align: center;
    transition: all 200ms;
    vertical-align: baseline;
    white-space: nowrap;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;'>GitHub</button></a>
    ''',
    unsafe_allow_html=True)

with col4:
    st.markdown(f'''
    <a href={url_X}><button style='
    background-color: #262730;
    outline: None;
    border:None;
    border-radius: 50px;
    border-width: 0;
    color: #DEDEDE;
    cursor: pointer;
    display: inline-block;
    font-family: "Haas Grot Text R Web", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 14px;
    font-weight: 500;
    line-height: 20px;
    list-style: none;
    margin: 0;
    padding: 13px 47px;
    padding-top: 15px;
    text-align: center;
    transition: all 200ms;
    vertical-align: baseline;
    white-space: nowrap;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;'>X</button></a>
    ''',
    unsafe_allow_html=True)
    
st.divider()
#Experience   
st.header("💼 &nbsp; Experience")

#Esmsys
st.subheader("Esmsys &nbsp; :gray[AI/ML Intern]")
st.caption("Jul 2023 - Present")
st.markdown("- Designed an API using FastAPI and Tesseract OCR engine and OpenCV to extract text of native languages from image.")
st.markdown("- Finetuned Transformer model (XLM-RoBERTa) for custom labelled Name Entity Recognition for native language.")

#Esmsys
st.subheader("Charusat University &nbsp; :gray[Research Associate]")
st.caption("May 2023 - Jun 2023")
st.markdown("- Achieved state-of-the-art results in six-way classification problem based on fake news leveraging transfer learning method of fine-tuning BERT model. ")
st.markdown("- Evaluation of model was carried out on benchmark dataset LIAR.")

#3fit
st.subheader("3fit &nbsp; :gray[Backend Developer Intern]")
st.caption("May 2022 - Jun 2022")
st.markdown("- Designed a web portal using a wagtail CMS(Content management system) and PostgreSQL database to make web pages extraordinarily dynamic.")
st.markdown("- Simplified the process of changing the content that appears on web pages with only a few clicks and the appropriate responsibilities and permissions.")

st.divider()

#Skills
st.header("🛠 &nbsp; Skills")
st.subheader(":gray[Programming]")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("Python")
    st.write("HTML")
with col2:
    st.write("SQl")
    st.write("CSS")
with col3:
    st.write("Javascript")
with col4:
    st.write("PHP")

st.subheader(":gray[General]")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("Statistical Modelling")
    st.write("Data Visualization")
with col2:
    st.write("Deep Learning")
    st.write("Web Scraping")
with col3:
    st.write("NLP")
    st.write("Docker")
with col4:
    st.write("Time Series Forecasting")
    st.write("Git")

st.subheader(":gray[Libraries and Frameworks]")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("Numpy")
    st.write("Huggingface")
    st.write("Pytorch")
with col2:
    st.write("Pandas")
    st.write("Flask")
    st.write("pySpark")
with col3:
    st.write("Matplotlib")
    st.write("FastAPI")
    st.write("Streamlit")
with col4:
    st.write("Scikit-learn")
    st.write("MLflow")

st.subheader(":gray[Visualization Tools]")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("Power BI")
with col2:
    st.write("Apache Superset")
with col3:
    st.write("Looker Studio")

st.subheader(":gray[Databases]")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("PostgreSQl")
with col2:
    st.write("BigQuery")
with col3:
    st.write("MySQl")
with col4:
    st.write("MongoDB")

st.divider()

# Project Section
st.header("🚀 &nbsp; Projects")

# Salary Prediction Engine
st.subheader(":gray[Salary Prediction Engine]")
st.markdown("- Enhanced accuracy of existing salary prediction model through comprehensive data collection from Glassdoor using web scraping.")
st.markdown("- Implemented advanced machine learning algorithms for in-depth salary trend analysis, offering valuable insights for optimized compensation strategies.")

st.markdown("")

with st.expander("Tech Stack Used"):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("**:gray[Selenium]**")
        st.write("**:gray[Numpy]**")
    with col2:
        st.write("**:gray[Scikit learn]**")
        st.write("**:gray[Seaborn]**")
    with col3:
        st.write("**:gray[Random Forest]**")
        st.write("**:gray[Matplotlib]**")
    with col4:
        st.write("**:gray[Pandas]**")

# Smart Chat Insights
st.subheader(":gray[Smart Chat Insights]")
st.markdown("- Accomplished seamless interaction with PDF documents through the implementation of a retrieval augmented generation system.")
st.markdown("- Demonstrated proficiency in Natural Language Processing by incorporating Named Entity Recognized response answers, leading to the efficient extraction and categorization of key information and displaying knowledge graph for the same.")

st.markdown("")

with st.expander("Tech Stack Used"):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("**:gray[LLM]**")
        st.write("**:gray[Streamlit]**")
    with col2:
        st.write("**:gray[Vector Database]**")
        st.write("**:gray[Knowledge Graph]**")
    with col3:
        st.write("**:gray[SpaCy]**")
    with col4:
        st.write("**:gray[Hugging Face]**")

# Admission Management System
st.subheader(":gray[Admission Management System]")
st.markdown("- Reduced human effort in manually filling forms and managing the admission process by developing a web application with various roles and permissions.")
st.markdown("- User Interface designed with bootstrap, PHP for backend logic, MySQL as a database all together provided an appropriate abstraction to the end user with multiple functionalities.")

st.markdown("")
with st.expander("Tech Stack Used"):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("**:gray[PHP]**")
        st.write("**:gray[HTML]**")
    with col2:
        st.write("**:gray[Bootstrap]**")
        st.write("**:gray[CSS]**")
    with col3:
        st.write("**:gray[MySQL]**")
    with col4:
        st.write("**:gray[Javascript]**")

# Education
st.header("📒 &nbsp; Education")

st.markdown("")

data = {
    'Institution' : ['BAPS Swaminarayan Vidhyamandir', 'BAPS Swaminarayan Vidhyamandir', 'CHARUSAT University'],
    'Level' : ['10th grade', '12th Grade', 'Undergraduate'],
    'Percentage' : ['92', '76', '94']
}

st.dataframe(data=data, use_container_width=True)