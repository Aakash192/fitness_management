import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Aakash Suryavanshi - Resume",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Add custom CSS
st.markdown("""
    <style>
        body {
            font-family: sans-serif;
            margin: 0;
        }

        .container {
            max-width: 850px;
            margin: 30px auto;
            padding: 30px;
            background-color: #fff; /* White background */
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        h1 {
            font-size: 2rem;
            margin-bottom: 10px;
        }

        .contact-info {
            margin-bottom: 15px;
        }

        h2 {
            margin-top: 20px;
        }

        ul {
            list-style: disc;
            margin-left: 20px;
            padding-left: 0;
        }

        li {
            margin-bottom: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Resume Content
with st.container():
    st.title("Aakash Suryavanshi")
    st.write(
        "Calgary, AB | aakash.suryavanshi2001@gmail.com | +1 4374214775 | LinkedIn: [Aakash Suryavanshi](http://www.linkedin.com/in/aakash-suryavanshi)",
        class_="contact-info",
    )

    st.header("Summary")
    st.write(
        "Cloud enthusiast with a strong foundation in AWS and Azure cloud services and IaC tools like Terraform and Ansible. "
        "Eager to leverage these skills to design, build, and maintain scalable, secure, and cost-efficient cloud infrastructure."
    )

    st.header("Skills")
    st.write("- **Cloud Platforms:** Azure, AWS")
    st.write("- **IaC:** Terraform, Ansible")
    st.write("- **Containerization Tools:** Docker, Kubernetes")
    st.write("- **Data Visualization:** Power BI, Tableau")
    st.write("- **Programming Languages:** JavaScript, Python, SQL, R, Java")
    st.write("- **Soft Skills:** Analytical Skills, Communication, and Presentation Skills")

    st.header("Education")
    st.write(
        "- **Post Graduate Diploma in Integrated Artificial Intelligence** - Southern Alberta Institute of Technology (Sept 2024 - April 2025)"
    )
    st.write(
        "- **Post Graduate Certificate in Cloud Computing** - Humber Institute of Advanced Technology (Sept 2023 - April 2024)"
    )
    st.write(
        "- **Bachelor of Science in Information Technology** - Lala Lajpat Rai College of Commerce and Economics, University of Mumbai (June 2019 - April 2022)"
    )

    st.header("Project Experience")

    st.subheader("Predictive Analysis of Student Dropouts (Sep 2024 - Dec 2024)")
    st.write("- Built a machine learning model to predict student dropouts in Canadian institutions using supervised learning algorithms such as Linear Regression, KNN, and Decision Trees.")
    st.write("- Integrated and prepared datasets from sources like Kaggle and Statistics Canada to analyze key dropout factors.")
    st.write("- Visualized insights using Power BI to identify at-risk students and support data-driven interventions.")
    st.write("- Delivered actionable recommendations for resource allocation and retention strategies to educational authorities.")

    st.subheader("Wayfinders (Dec 2023 - April 2024)")
    st.write("- Deployed Single Sign-On (SSO) across the company using KeyCloak, streamlining authentication processes and improving security.")
    st.write("- Managed user provisioning and access controls for the Wayfinders group, ensuring seamless integration with existing IT infrastructure.")
    st.write("- Established SSO integration for Wayfinders users across their website and Nextcloud application, reducing login redundancies by 70%.")

    st.subheader("Bookstore Management App (Oct 2023 - Dec 2023)")
    st.write("- Containerized the bookstore application using Docker to streamline deployment processes.")
    st.write("- Implemented CI/CD pipelines using GitHub Actions, reducing deployment time by 40%.")
    st.write("- Enhanced scalability and ensured high availability using Azure infrastructure, including load balancers and auto-scaling groups.")
    st.write("- Developed automated monitoring solutions to ensure system reliability.")

    st.subheader("Fitness Management Application (Sep 2023 - Nov 2023)")
    st.write("- Developed a full-stack fitness management application to help users track fitness and nutritional goals.")
    st.write("- Built the backend using Python and Django with robust RESTful APIs for seamless integration.")
    st.write("- Designed and implemented a responsive frontend using HTML, CSS, Bootstrap, and JavaScript for enhanced user experience.")
    st.write("- Optimized the MySQL database schema to ensure efficient data handling, reducing query time by 30%.")

