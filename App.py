import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from pathlib import Path




# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Navi Resume in Python", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("styles/styles.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_tljjahng.json")
img_Navi = Image.open("images/Navi.png")
img_linkedin_logo = Image.open("images/linkedin-logo.png")
img_tableau_logo = Image.open("images/tableau-logo.png")
img_resume_icon = Image.open("images/resume-icon.png")
img_GA_Advanced = Image.open("images/GA-Advanced-Certificate.JPG")
img_GA_GAIQ = Image.open("images/GAIQ-Certificate.JPG")
img_GTM = Image.open("images/GTM-Certificate.JPG")
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "images" / "Navi-CV.pdf"
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# ---- HEADER SECTION ----
with st.container():
    st.write("---")
    st.header("--- Hi, I am Navi :wave: ---")
    st.write("created using Python - Streamlit library")
    ## st.markdown("<h1 style='text-align: center; color: black;'>Hi, I am Navi :wave:</h1>", unsafe_allow_html=True)
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
       st.image(img_Navi)
    with text_column:
        st.title("A Marketing Data Analyst & Strategist From planet earth ")
        st.write(
            "I am passionate about finding ways to use Technology stacks and all Data collected and minned throuhout the whole user lifecycle in our digital system to be more efficient and effective in achieveing business goals."
            " Analyzing data since 1988, professionally since 2015 :smile:"
     )
        
        image_column, text_column = st.columns((1, 10))
        with image_column:
            st.image(img_resume_icon, width = 50)
            st.image(img_linkedin_logo, width = 50)
            st.image(img_tableau_logo, width = 50)
            st.write("📫")
        with text_column:
            st.write(" ")
            st.download_button(
                label=" 📄 Download Resume",
                data=PDFbyte,
                file_name=resume_file.name,
                mime="application/octet-stream",
            )
            st.write(" ")
            st.write("[Linkedin Profile >](https://www.linkedin.com/in/navaneeth-murali-mba-64692263/)")
            st.write(" ")
            st.write("[Tableau Viz samples >](https://public.tableau.com/app/profile/navaneeth.murali7129)")
            st.write("navaneethmurali.mba@gmail.com")


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            - Own and maintain the Blue Cross Blue Shield of Nebraska’s Google Analytics Account
            - Establish link between cross domain and vendor web domain to capture all the user web traffic data
            - Linked GA with Google Ads, Google Search console, Bing ads and facebook ads to create remarketing and audience lists and segments
            - Migrating from Google Analytics Universal Analytics to GA4 Properties across all domains and platforms
            - Use Google Tag Manager to tag various events, goals and conversions and drive data to the correct platforms
            - Nebraskablue.com website redesign (Working with web designers and vendors to provide analysis on user behavior online and user flow with web analytics data)
            - Practicing the best SEO strategies to improve the user experience by using the available SEO tools like site improve, MOZ and SEMrush.
            - Use A/B testing tools like Optimizely and ABtasty to run experiments on landing pages.
            - Perform cost analysis by campaign to determine the ROI of marketing campaigns like direct mail, email, social, search engine and other traceable non-digital campaigns (TV, Radio, Billboards).
            - Generate reports weekly and monthly basis via GA and other data sources to provide meaningful strategic insights for the Individual Business Unit owners (Med Sup – over 65, Individual - under 65 and Group insurance)
            - Analyze the historic user behavior data, Vendor data (Experian) and create user profiles via demographic and psychographics and recommend actionable strategies for future campaigns
            - Performing sentiment analysis on Customer service call center Surveys and feedbacks from SQM Group.
            - Statistical modelling on the direct sales prediction.
            - Create custom reports from Exact Target (Marketing cloud). Testing various subject lines and creatives and analyzing the best way to make the customers open and click the desired actions in our Emails sent.
            - Use Tableau to connect GA data with Salesforce, SQL and other databases and create executive dashboards and customized reports
            - Running SEM Campaigns - Analyzing branded and non-branded keywords to invest on Adwords and Bing ads using historic data, google trends and keyword planner.
            - Salesforce Admin - to create and maintain different Salesforce campaigns and fields and manage reporting.
            - Use Basecamp 2.0 to keep track of all the projects.
            """
        )
        st.write("[Linkedin Profile >](https://www.linkedin.com/in/navaneeth-murali-mba-64692263/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="Analytics")
        st.markdown("<h1 style='text-align: center; color: grey;'>Certifications</h1>", unsafe_allow_html=True)
        st.image(img_GA_GAIQ, width = 300)
        st.image(img_GA_Advanced, width = 300)
        st.image(img_GTM, width = 300)

        # ---- Skills ----
with st.container():
    st.write("---")
    st.header("My Skills")
    st.write("##")
    column1, column2, column3 = st.columns((1, 1, 1))
    with column1:
       st.subheader("Web Analytics")
       st.write(
            """
            - GA UA / GA4 / GA 360
            - Google Data Studio
            - GTM
            - Google webmasters
            - Debibel Insights
            - Google Search console
            - SEO : Siteimprove, MOZ
            """
        )
    with column2:
        st.subheader("Digital Marketing")
        st.write(
            """
            - SEM : Paid ads (Google Ads, Bing Ads)
            - Display ads (Google)
            - Paid Social Media Marketing (Facebook, Instagram, Linkedin)
            - SproutSocial for organic social media posts
            - Google trends
            """
        )
    with column3:
        st.subheader("Analytics and Reporting")
        st.write(
                """
                    - SQL
                    - Tableau
                    - PowerBI
                    - Excel
                    - Vendor data platforms
                    """
                )    
    column4, column5, column6 = st.columns((1, 1, 1))
    
    with column4:
            st.subheader("CRM")
            st.write(
                """
                - Salesforce
                - Marketing Cloud (Email marketing : User Journey and automation)
                """
            )
    with column5:
                st.subheader("Programming Languages")
                st.write(
                    """
                    - Javascript
                    - HTML / CSS
                    - Python
                    """
                )
    with column6:
                st.subheader("Design")
                st.write(
                    """
                    - Wordpress
                    - Canva
                    """
                )          
    

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/navaneethmurali.mba@gmail.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
