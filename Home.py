import streamlit as st

st.set_page_config(
    page_title="WasteApp",
    page_icon= "♻️",
    layout = "wide", 
    initial_sidebar_state = "auto"
)

st.image("img.png", width = 100)
st.title(" Welcome to Garbage Detection WebApp")
st.write("## Lets make our enviornment more clean")

st.write(
    "### Our web app is here to help you understand waste in our surroundings. By uploading images, our advanced algorithms detect and categorize various types of waste, from your neighborhood streets to vast landscapes. Whether it's plastic bottles or food waste, we unveil the presence of waste in our midst. \n "
    )

github = "https://github.com/aman977381/Waste-Detection-using-YOLO.git"
st.write("You can access this project through this link 👉 [GitHub](%s)"%github)

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://images.unsplash.com/photo-1597655601841-214a4cfe8b2c?q=80&w=1889&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
    background-color: rgba(255, 255, 255, 0.1);
}
[data-testid=stSidebar] {
        background-color: #5888c6;
    }
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)