import streamlit as st
import requests
import io
from PIL import Image

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/segment/"

# Set page config with background image
st.set_page_config(page_title="Lunar Image Segmentation", layout="centered")

# Custom CSS to add background image
background_image_url = "https://c4.wallpaperflare.com/wallpaper/383/768/847/moon-space-monochrome-crater-wallpaper-preview.jpg"

st.markdown(
    f"""
    <style>
    .stApp {{
        background: url({background_image_url});
        background-size: cover;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title("🌙 Lunar Surface Ground Truth Rock Segmentation")
st.write("Upload an image, and the AI model will segment the lunar terrain.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    if st.button("Upload & Segment"):
        with st.spinner("Processing..."):
            try:
                # Convert the uploaded file into bytes
                image_bytes = uploaded_file.read()

                # Send the image to FastAPI backend
                response = requests.post(API_URL, files={"file": image_bytes})

                if response.status_code == 200:
                    # Read the segmented image from response
                    segmented_image = Image.open(io.BytesIO(response.content))

                    # Display the segmented image
                    st.image(segmented_image, caption="Segmented Image", use_container_width=True)
                else:
                    st.error(f"Error: {response.json().get('error', 'Unknown error')}")

            except Exception as e:
                st.error(f"Request failed: {e}")

# Footer
st.write("---")
# Footer with Dark Pink-Violet Glow Effect (Right-Bottom Aligned)
st.markdown(
    """
    <style>
    .glow {
        position: fixed;
        bottom: 10px;
        right: 20px;
        font-size: 20px;
        font-weight: bold;
        color: #8B0A50; /* Darker Violet-Red */
        text-shadow: 0px 0px 10px #8B0A50, 0px 0px 18px #9400D3; /* Dark Magenta Glow */
        background-color: rgba(0, 0, 0, 0.7); /* Slightly Transparent Dark Background */
        padding: 8px 16px;
        border-radius: 12px;
    }
    </style>
    <div class="glow">🚀 Developed by Dev</div>
    """,
    unsafe_allow_html=True
)



