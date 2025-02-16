import io
from PIL import Image
import numpy as np

def preprocess_image(image_file):
    """
    Preprocess the input image for the segmentation model.
    Ensures the image is correctly read, resized, and normalized.
    """

    try:
        # Open image using PIL
        if isinstance(image_file, io.BytesIO):
            image_file.seek(0)  # Reset buffer position
            img = Image.open(image_file)  # Open image from memory
        elif isinstance(image_file, (bytes, bytearray)):
            img = Image.open(io.BytesIO(image_file))  # Convert bytes to PIL Image
        else:
            raise TypeError("Invalid input type. Expected BytesIO or bytes, got:", type(image_file))

        # Convert PNG to RGB if it has an alpha channel
        if img.mode != "RGB":
            img = img.convert("RGB")

        # Convert PIL image to NumPy array
        img = np.array(img)

        # Target height and width for cropping
        H, W = 480, 480

        # Debugging: Print the original image shape
        print(f"Original Image Shape: {img.shape}")

        # Validate image dimensions
        if img.shape[0] < H or img.shape[1] < W:
            raise ValueError(f"Image must be at least {H}x{W} pixels. Provided: {img.shape}")

        if img.shape[-1] != 3:
            raise ValueError(f"Expected 3-channel RGB image, got {img.shape[-1]} channels!")

        # Crop the image to 480x480 pixels
        img_resized = img[:H, :W, :]

        # Normalize the image (scale pixel values to 0-1)
        normalized_img = img_resized / 255.0
        float32_img = normalized_img.astype(np.float32)

        # Debugging: Print final image shape
        print(f"Processed Image Shape: {float32_img.shape}")

        return float32_img

    except Exception as e:
        print(f"Error in preprocess_image: {str(e)}")
        raise

def get_color_map():
    """
    Define color mappings for different segmented classes.
    """
    return np.array([
        [0, 0, 0],    # Class 0: Black (Lunar soil/ Background)
        [255, 0, 0],  # Class 1: Red (Large Rocks)
        [0, 255, 0],  # Class 2: Green (Sky)
        [0, 0, 255]   # Class 3: Blue  (small rocks)
    ], dtype=np.uint8)
