from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
default_profile_pic_path = current_dir / "assets" / "profile-pic.png"
current_profile_pic_path = current_dir / "assets" / "current_profile.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Sweet Pinky T. Martinez // Biography"
PAGE_ICON = ":wave:"
NAME = "Martinez, Sweet Pinky T."
DESCRIPTION = """
Bachelor of Science in Computer Engineering - BSCpE 1A
"""
EMAIL = "smartinez1.ssct.edu.ph"
SOCIAL_MEDIA = {
    "Facebook": "https://www.facebook.com/pinky.092005",
    "Instagram": "https://www.instagram.com/spm9_20/",
    "Tiktok": "https://www.tiktok.com/@_imnotpinky"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- SESSION STATE FOR PROFILE PICTURE ---
if "profile_pic_path" not in st.session_state:
    # Initialize session state with the current profile picture
    if current_profile_pic_path.exists():
        st.session_state.profile_pic_path = current_profile_pic_path
    else:
        st.session_state.profile_pic_path = default_profile_pic_path

# --- PROFILE ---
col1, col2 = st.columns(2, gap="small")
with col1:
    # Load and display the current profile picture
    profile_pic = Image.open(st.session_state.profile_pic_path)
    st.image(profile_pic, width=250, caption="Profile Picture")
    
# Upload a new profile picture
uploaded_file = st.file_uploader("Change Profile Pic", type=["png", "jpg", "jpeg"])
    
if uploaded_file is not None:
    # Save the uploaded file as the new profile picture
    with open(current_profile_pic_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
    # Update session state to point to the new profile picture
    st.session_state.profile_pic_path = current_profile_pic_path
        

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
st.write ("---")


# --- BACKGROUND ---
st.markdown ("""Hi! I am Sweet Pinky T. Martinez. I graduated from Kitcharao National High School, where I got to join lots of math competitions to represent my school. I’ve always loved numbers and solving problems, so it was really exciting to compete and challenge myself.

When I am not studying or competing, I love playing volleyball and playing musical instruments. Both of these hobbies let me stay active and creative, and I enjoy every minute of it.

I also really love dogs, and I have a lot of them at home! They bring so much joy to my life, and I am always there for them.

Right now, I am focused on becoming a successful programmer. I want to build my own company someday and make a real impact with the things I create. I’m working hard to learn as much as I can to make this dream a reality.""",
unsafe_allow_html=True,
)

# --- EDUCATIONAL ATTAINMENT ---
st.write('\n')
st.write ("---")
tab1, tab2 = st.tabs(["📚 Educational Attainments", "🎯 Accomplishments"])
tab1.markdown(
    """
    ELEMENTARY:
    <ul style="margin-left: 20px; font-size: 16px;">
        <ul style="margin-left: 20px;">
            <li>Kitcharao National High School</li>
            <li>Poblacion, Kitcharao Agusan del Norte</li>
            <li>2017-2018</li>
        </ul>
    </ul>
    
    SECONDARY:
    <ul style="margin-left: 20px; font-size: 16px;">
        <ul style="margin-left: 20px;">
            <li>Kitcharao National High School</li>
            <li>P-1 Crossing, Kitcharao Agusan del Norte</li>
            <li>2023-2024</li>
        </ul>
    </ul>
    
    TERTIARY:
    <ul style="margin-left: 20px; font-size: 16px;">
        <ul style="margin-left: 20px;">
            <li>Surigao Del Norte State University</li>
            <li>Narciso Street, Surigao City, 8400 Surigao del Norte</li>
        </ul>
    </ul>
    
    """,
    unsafe_allow_html=True,
)

# Initialize session state for accomplishments if not present
if 'accomplishments' not in st.session_state:
    st.session_state.accomplishments = {
        'elementary': [
            "🏅Grade 1: Second Place",
            "🏅Grade 2: Eight Place",
            "🏅Grade 3: Second Place",
            "🏅Grade 4: First Place",
            "🏅Grade 5: With Honors",
            "🏅Grade 6: With Honors",
        ],
        'secondary': [
            "🏅Grade 7-10: With Honors",
            "🏅Grade 11: With Honors",
            "🏅Grade 12: With Honors"
        ],
        'extracurricular activities': [
            
        ]
    }

# Function to display accomplishments
def display_accomplishments(data):
    for key, values in data.items():
        st.markdown(f"**{key.upper()}**:")
        st.markdown("<ul style='margin-left: 20px;'>", unsafe_allow_html=True)
        for value in values:
            st.markdown(f"<li>{value}</li>", unsafe_allow_html=True)
        st.markdown("</ul>", unsafe_allow_html=True)

# --- Tab 2: Accomplishments ---
with tab2:
    st.write("### Current Accomplishments:")
    display_accomplishments(st.session_state.accomplishments)

    # --- Add/Update Accomplishment ---
    st.write("### Add/Update Accomplishment")
    level = st.selectbox("Choose accomplishment level:", ["Elementary", "Secondary", "Extracurricular Activities"])
    accomplishment = st.text_input(f"Enter accomplishment for {level}:")

    # Button to add or update
    if st.button(f"Add/Update {level}"):
        level_key = level.lower()
        if accomplishment:
            st.session_state.accomplishments[level_key].append(accomplishment)
            st.success(f"Accomplishment added/updated for {level}!")
        else:
            st.warning("Please enter an accomplishment.")

    # --- Remove Accomplishment ---
    st.write("### Remove Accomplishment")
    remove_level = st.selectbox("Select level to remove an accomplishment from:", ["Elementary", "Secondary", "Extracurricular Activities"])
    accomplishments_to_remove = st.session_state.accomplishments[remove_level.lower()]
    accomplishment_to_remove = st.selectbox("Select accomplishment to remove:", accomplishments_to_remove)

    # Button to remove an accomplishment
    if st.button(f"Remove Accomplishment from {remove_level}"):
        if accomplishment_to_remove in accomplishments_to_remove:
            st.session_state.accomplishments[remove_level.lower()].remove(accomplishment_to_remove)
            st.success(f"Accomplishment removed from {remove_level}!")
        else:
            st.warning("Accomplishment not found.")