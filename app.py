import streamlit as st
from prompt_builder import build_prompt
from image_generator import generate_image
from io import BytesIO
import random

st.set_page_config(
    page_title="AI Interior Designer",
    page_icon="🏠",
    layout="wide"
)
st.markdown("""
<style>

.stApp{
    background-color:#0F1117;
}

.main-title{
    font-size:55px;
    font-weight:800;
    text-align:center;
    color:#C9A227;
    margin-bottom:0px;
}

.subtitle{
    text-align:center;
    color:white;
    font-size:18px;
    margin-bottom:30px;
}

.card{
    background:#1A1D24;
    padding:25px;
    border-radius:20px;
    border:1px solid #2D2D2D;
    margin-bottom:20px;
}

.feature-card{
    background:#151922;
    padding:15px;
    border-radius:15px;
    text-align:center;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:15px;
    border:none;
    background:#C9A227;
    color:black;
    font-weight:bold;
    font-size:16px;
}

.stButton>button:hover{
    background:#E4C441;
}

.history-card{
    background:#1A1D24;
    border-left:4px solid #C9A227;
    padding:15px;
    border-radius:10px;
    margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state.history = []

ROOM_IDEAS = [
    "Tiny Apartment in Tokyo",
    "Luxury Penthouse",
    "Gamer's Bedroom",
    "Futuristic Mars Habitat",
    "Cozy Mountain Cabin",
    "Beachside Villa",
    "Cyberpunk Studio Apartment"
]

st.markdown("""
<div class="main-title">
🏠 AI Interior Designer
</div>

<div class="subtitle">
Transform simple room descriptions into stunning AI-generated interiors
</div>
""", unsafe_allow_html=True)
col1,col2,col3,col4=st.columns(4)

with col1:
    st.metric("Styles","8+")

with col2:
    st.metric("AI Model","FLUX")

with col3:
    st.metric("Quality","HD")

with col4:
    st.metric("Designs",len(st.session_state.history))

with st.sidebar:
    st.markdown("""
# 🏠 AI Designer

Create premium AI-powered room designs.

Powered By:
- FLUX.1 Schnell
- Hugging Face
- Streamlit
""")

    st.header("Settings")

    style = st.radio(
        "Choose Style",
        [
            "Minimalist",
            "Japanese Zen",
            "Luxury",
            "Cyberpunk",
            "Gaming Setup",
            "Scandinavian",
            "Industrial",
            "Modern Apartment"
        ]
    )

    image_size = st.selectbox(
        "Image Size",
        ["Square", "Portrait", "Landscape"]
    )

    if st.button("🎲 Random Room Idea"):
        st.session_state.random_idea = random.choice(ROOM_IDEAS)

default_text = st.session_state.get(
    "random_idea",
    ""
)

prompt = st.text_area(
    "Describe Your Room",
    value=default_text,
    height=150
)

if st.button("Generate Design"):

    if not prompt.strip():
        st.error("Please enter a room description.")
        st.stop()

    try:

        final_prompt = build_prompt(
            prompt,
            style
        )

        with st.spinner(
            "Designing your dream room..."
        ):
            image_bytes = generate_image(
                final_prompt
            )

        st.success("Image Generated!")

        st.image(
            image_bytes,
            use_container_width=True
        )

        st.download_button(
            "⬇ Download Image",
            image_bytes,
            file_name="interior_design.png",
            mime="image/png"
        )

        st.session_state.history.insert(
            0,
            final_prompt
        )

    except Exception as e:
        st.error(str(e))

st.divider()

st.subheader("Prompt History")

for item in st.session_state.history:

    st.markdown(
        f"""
        <div style="
        padding:10px;
        border:1px solid #ddd;
        border-radius:10px;
        margin-bottom:10px;">
        {item}
        </div>
        """,
        unsafe_allow_html=True
    )