# **Lunar Terrain Segmentation App**  

🚀 **Project Type:** Web App  
🛰️ **Tech Stack:** FastAPI (Backend), Streamlit (Frontend)  
🧠 **Model:** UNET with VGG16 Backbone  
📊 **Performance:** 83% IOU on Validation Set  
📂 **Dataset:** [Artificial Lunar Rocky Landscape Dataset (Kaggle)](https://www.kaggle.com/datasets/romainpessia/artificial-lunar-rocky-landscape-dataset)  
🎓 **Developed At:** [Spartificial](https://spartificial.com/)  

## **Demo Video**  
📹 [Watch the Demo](#) *(Replace "#" with your video link once uploaded)*  

---

## **Setup**  
1. Clone or download the repository and open the project directory in your editor (VS Code).  
2. Install the required dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Train your model using the Python notebook via [Kaggle](https://www.kaggle.com/datasets/romainpessia/artificial-lunar-rocky-landscape-dataset).  
4. Add your trained model to the `models` folder and remove any other models present.  
5. Open a command prompt and start the FastAPI backend:  
   ```bash
   uvicorn backend:app --reload
   ```  
6. Open another command prompt and run the Streamlit frontend:  
   ```bash
   streamlit run frontend.py
   ```  

---

## **About the Trained Model**  
- The model is trained using **UNET with a VGG16 Backbone**.  
- **Training Data:** First 8000 images from the `render` (artificial Moon terrain) and `clean` (respective masks) directories.  
- **Validation Data:** Remaining images, except the last 4, which were used as the test set.  
- **Performance:** Achieved **83% IOU** on the validation set.  
- **Developed as part of a training program at [Spartificial](https://spartificial.com/),** where students aimed to improve this IOU score.  

---
