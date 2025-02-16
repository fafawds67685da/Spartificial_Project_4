from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
from PIL import Image
import numpy as np
import io
import tensorflow as tf
import os
from utils import preprocess_image, get_color_map

app = FastAPI()

# Fix Windows path issue (Use raw string)
model_path = r"D:\Image segmentation project\Spartificial_Project_4\models\LunarModel_2.h5"

# Ensure model exists before loading
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

# Load the trained model
model = tf.keras.models.load_model(model_path, compile=False)

@app.get("/")
async def read_root():
    """Root endpoint to check if the server is running."""
    return {"Dev's Lunar image segmentation project": "is working"}

@app.post("/segment/")
async def segment_image(file: UploadFile = File(...)):
    """Process and segment an uploaded image."""
    
    # Read image bytes
    image_bytes = await file.read()
    
    # DEBUG: Print file details
    print(f"File name: {file.filename}")
    print(f"File size: {len(image_bytes)} bytes")
    print(f"File type: {file.content_type}")

    if not image_bytes:
        return JSONResponse(content={"error": "Uploaded file is empty"}, status_code=400)

    try:
        # Convert bytes to a file-like object
        image_file = io.BytesIO(image_bytes)

        # Open and verify the image
        image = Image.open(image_file)
        image.verify()  # Check if it's a valid image
        image_file.seek(0)  # Reset buffer
        image = Image.open(image_file)

        # Convert PNG to RGB if needed
        if image.mode != "RGB":
            image = image.convert("RGB")

        # Convert image to NumPy array and preprocess
        image_array = preprocess_image(image_file)

        # DEBUG: Print processed image shape
        print(f"Processed image shape: {image_array.shape}")

        # Perform segmentation with the model
        pred_mask = model.predict(np.expand_dims(image_array, axis=0))
        pred_mask = np.argmax(pred_mask, axis=-1)  # Get class with highest probability
        pred_mask = pred_mask[0]  # Remove batch dimension

        # Map the predicted mask to colors
        color_map = get_color_map()
        segmentation_img = color_map[pred_mask]  # Convert class indices to colors

        # Convert NumPy array back to PIL image
        segmentation_img_pil = Image.fromarray(segmentation_img.astype(np.uint8))

        # Save the segmentation result to a BytesIO object
        img_byte_arr = io.BytesIO()
        segmentation_img_pil.save(img_byte_arr, format="PNG")
        img_byte_arr.seek(0)  # Reset buffer position

        # Return segmented image as a streaming response
        return StreamingResponse(img_byte_arr, media_type="image/png")

    except Exception as e:
        return JSONResponse(content={"error": f"Image processing failed: {str(e)}"}, status_code=500)
