#------------Libraries------------#
import streamlit as st
from PIL import Image
from pathlib import Path

#----------Configuration----------#
# --- CSS Styles -----#
st.markdown(
    """
<style>
/* Main content area */
    .stAppViewBlockContainer, .block-container, .stApp {
        padding: 0px 0px 0px 0px !important;
        margin: 0px 0 0 0 !important;
    }
    
    /* Header removal (if needed) */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    
    /* Footer removal */
    .stApp footer {
        display: none !important;
    }
/* General Styles 
body {
    font-family: sans-serif;
}
a {
    text-decoration: none;
    color: inherit;
}
/* Sections */
.section p {
    font-size: 12px;
    margin: 0 0 0 0 ;
}
.section h5 {
    font-weight: bold;
    margin: 0 0 0 0 ;
}
.section h6 {
    font-weight: bold;
    margin: 5px 0 0 0 ;
}
.section h7 {
    font-weight: bold;
    margin: 0px 0 0 0 ;
}
.section ul {
    padding-left: 15px;
    margin: 0px 0 0px 0 ;
}
.section li {
    padding-left: 0px;
    margin: 0 0 4px 0 ;
    font-size:12px;
}

/* Contact Info */
.contact-info p {
    text-align: left;
    font-size: 12px;
    margin: 0px 0 4px 0;
}
.contact-info h3 {
    font-weight: bold;
    margin: 0 0 0px 0;
}
/* Professional Summary */
.summary h6{
    text-align: center;
    font-weight: bold;
    margin: 0 0 0px 0px;
}
.summary p{
    text-align: justify;
    font-size: 12px;
    margin: 0px 20px 0px 0px;
}
/* Skill Section */
.skill-section h7 {
    font-weight: bold;
    margin: 20px 0px 0px 0px ;
}
.skill-section ul {
    font-size: 12px;
    text-align: left;
    padding-left: 0;
    margin-bottom: 10px; /* Space between skill sections */
}
.skill-section li {
    margin-bottom: 0px;
}

# .experience-section ul {
#     font-size: 14px;
#     text-align: left;
#     padding-left: 20px;
#     margin-bottom: 10px; /* Space between skill sections */
# }
# .experience-section li {
#     margin-bottom: 0.25rem;
# }

/* References Section */
.references-section ul {
    font-size: 12px;
    text-align: left;
    padding-left: 0;
    margin-bottom: 1rem; /* Space between references */
}
.references-section li {
    margin-bottom: 0.5rem; /* Space between reference items */
}
 .bordered-column {
        border: 1px solid #ddd;
        padding: 15px;
        border-radius: 5px;

</style>
""",
    unsafe_allow_html=True,
)
# Add this right after the CSS
st.container()  # Creates a tight container

#--------------Layout-------------#
col1, col2, col3 =st.columns([0.3, 0.5, 0.2])
with col1:
    st.markdown(
        """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <div class="contact-info">
        <h3>Sami Kazemi</h3>
        <p>📞 <a href="tel:+358445195357">+358 (44) 519-5357</a></p>
        <p><i class="fa fa-envelope" style="color: #D44638; margin-right: 5px;"></i>
            <a href="mailto:s.sami.kazemi@gmail.com" style="color: #D44638;">s.sami.kazemi@gmail.com</a></p>
        <p><i class="fa fa-linkedin" style="color: #0A66C2; margin-right: 5px;"></i>
            <a href="https://linkedin.com/in/samikazemi" style="color: #0A66C2;">linkedin.com/in/samikazemi</a></p>
        <p><i class="fa fa-github" style="color: #333; margin-right: 5px;"></i>
            <a href="https://github.com/Sir-Analyst" style="color: #0A66C2;">github.com/Sir-Analyst</a></p>
        <p><i class="fa fa-map-marker" style="color: #555; margin-right: 5px;"></i>
            Helsinki, Finland</p>
        <p>🌐 <a href="https://sami_resume.streamlit.app" style="color: #0A66C2;" target="_blank">sami_resume.streamlit.app</a></p>
        """,
        unsafe_allow_html=True,

    )
with col2:
    st.markdown(
        """
        <p style='font-size:14px; margin: 0 0 10px 0;'></p>
        <p style='font-size:14px; margin: 0 0 10px 0;'></p>
        <div class="summary";>
            <h6>PROFESSIONAL SUMMARY</h6>
            <p>
                Results-driven finance professional (MSc, Economics & Business Administration) with a strong focus on strategic analysis and data-driven revenue optimization. Experienced in leveraging Python, SQL, Tableau, and Power BI to interpret complex data, enhance demand forecasting accuracy, and support pricing decisions. Motivated by the challenge of maximizing network revenue through analytical insight, commercial awareness, and continuous process improvement.        """,
            unsafe_allow_html=True,
    )
with col3:
    st.markdown(
    """
    <p style='font-size:14px; margin: 0px 0 10px 0;'></p>
    """,
    unsafe_allow_html=True)    
    profile_path = Path(__file__).parent / "assets/pic.jpg"
    profile = Image.open(profile_path)
    st.image(profile_path, width=300)

# education, expereince, course, skill, refrence
col4, col5 = st.columns([0.7, 0.3], border=True)  # Removed border=True; handled with CSS if needed
with col4:
    st.markdown(
        """
    <div class="section">
        <h6>EDUCATION</h6>
        <p>
            <b>MSc in Economics and Business Administration</b> (08/2019 - 10/2022, Hanken School of Economics, Finland): Accounting & Finance
        </p>
        <ul>
            <li>Specialized in Accounting & Finance</li>
            <li>
                <a href="https://www.researchgate.net/publication/375182722_Impact_of_COVID-19_Pandemic_on_Earnings_Management">Thesis: Impact of COVID-19 on Earnings Management</a>
            </li>
        </ul>
        <p>
            <b>BSc in International Business</b> (08/2011 - 12/2015, Haaga-Helia University of Applied Sciences, Finland): International Business
        </p>
        <ul>
            <li>Focused on Financial Management, Corporate Taxation, and International Marketing</li>
            <li>
                <a href="https://www.theseus.fi/bitstream/handle/10024/99029/Creating%20Activity-%20Based%20Costing%20system%20tool.pdf">Thesis: Creating Activity-Based Costing System Tool</a>
            </li>
        </ul>
        <p></p>
        <p></p>
        <h6 style="margin-top:20px;">WORK EXPERIENCE</h6>
        <p>
            <b>Financial Management Assistant</b> (10/2017 - 04/2018, Accado Oy, Finland)
        </p>
        <ul>
            <li>Created comprehensive financial reports to support executive decision-making.</li>
            <li>Optimized accounts payable workflows.</li>
            <li>Analyzed financial data to identify trends and cost-saving opportunities.</li>
        </ul>
        <p>
            <b>Balance Sheet and Income Statement Analyst</b> (05/2015 - 11/2015, SanSox Oy, Finland)
        </p>
        <ul>
            <li>Developed an Excel-based budgeting tool, improving financial planning efficiency.</li>
            <li>Refined pricing strategies, boosting profitability.</li>
            <li>Presented actionable insights to stakeholders through data visualization.</li>
        </ul>
        <p>
            <b>Instructor</b> (09/2014 - 05/2015, Viikarit Oy, Finland)
        </p>
        <ul>
            <li>Delivered tailored academic support and mentoring to children.</li>
            <li>Planned and managed activities to enhance engagement and learning outcomes.</li>
            <li>Provided tutoring in academic tasks, fostering a supportive learning environment.</li>
            <li>Promoted holistic development by encouraging critical thinking and problem-solving skills.</li>
        </ul>
        <p>
            <b>Office Manager & Teacher</b> (01/2002 - 02/2004, Tebyan-Institute, Iran)
        </p>
        <ul>
            <li>Designed and managed training schedules and staff operations to ensure seamless course delivery.</li>
            <li>Delivered beginner to intermediate English language training with measurable progress.</li>
            <li>Conducted hands-on lessons in computer applications, including MS Office, Adobe Photoshop, and system operations.</li>
            <li>Built client relationships through exceptional service and clear communication.</li>
            <li>Created an environment conducive to active learning and professional growth.</li>
        </ul>
    </div>
    """,
        unsafe_allow_html=True,
 
    )
with col5:
    st.markdown(
        """
    <div class="skill-section">
        <h7 class="section-title">STRENGTHS</h7>
        <ul class="skill-section">
            <li>Strategic Thinking</li>
            <li>Analytical Thinking</li>
            <li>Adaptability</li>
            <li>Technical Proficiency</li>
        </ul>
    </div>
    <div class="skill-section">
        <h7 class="section-title">INTERPERSONAL SKILLS</h7>
        <ul class="skill-section">
            <li>Collaboration</li>
            <li>Communication</li>
            <li>Problem-Solving</li>
            <li>Attention to Detail</li>
        </ul>
    </div>
    <div class="skill-section">
        <h7 class="section-title">TECHNICAL SKILLS</h7>
        <ul class="skill-section">
            <li>Python (Pandas, NumPy, Matplotlib, scikit-learn)</li>
            <li>SQL (Data queries and optimization)</li>
            <li>Data visualization tools: Tableau, Power BI</li>
            <li>Advanced Excel (PowerQuery, VBA), HTML, CSS</li>
        </ul>
    </div>
    <div class="skill-section">
        <h7 class="section-title">LANGUAGE SKILLS</h7>
        <ul class="skill-section">
            <li>English (Fluent)</li>
            <li>Finnish (Intermediate)</li>
            <li>Persian (Native)</li>
        </ul>
    </div>
    <div class="skill-section">
        <h7 class="section-title">REFERENCES</h7>
        <ul>
            <li>Benjamin Mohseni: CEO | Entrepreneur <a href="mailto:Benjamin.mohseni@zarillo.fi">(Benjamin.mohseni@zarillo.fi)</a></li>
            <li>Francisco Jousi: Solution Analyst (OP Osuuskunta) <a href="mailto:francisco.jousi@gmail.com">(francisco.jousi@gmail.com)</a></li>
            <li>Dong Pham: Quality Engineering | Entrepreneur in Testing <a href="mailto:dong@qaraton.com">dong@qaraton.com)</a></li>
        </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )
# Course section one column
col6, = st.columns(1, gap="medium")  # Remove border=True (handle via CSS)

with col6:
    st.markdown(
        """
    <div class="bordered-column section">
        <h5>COURSES</h5>
        <p>
            <b>Advanced Data Analytics</b> (09/2024 - 4/2025, Taitotalo (Adult Educational Center), Finland): Data Analytics
        </p>
        <p>
            <b>Financial Management</b> (01/2024 - 03/2024, Rastor Institute, Finland): Accounting
        </p>
        <p>
            <b>Payroll Management</b> (04/2019 - 06/2019, Taitotalo (Adult Educational Center), Finland): Accounting
        </p>
        <p>
            <b>e-TalousPro - Financial and Payroll Management Expert</b> (10/2017 - 04/2018, Saranen Consulting Institute, Finland): Accounting
        </p>
        
    </div>
    """,
        unsafe_allow_html=True,
    )
# Footer
st.markdown("""
<style>
.footer {
    position: fixed;
    left: 10px;
    bottom: 0;
    width: 100%;
    color: #333;
    text-align: left;
    padding: 10px;
    font-size: 10px !important;
    background: #fff;
    z-index: 9999;
}
</style>
<div class="footer">
    © 2025 Sami Kazemi - Resume generated programmatically using Python and Streamlit.
</div>
""", unsafe_allow_html=True)
