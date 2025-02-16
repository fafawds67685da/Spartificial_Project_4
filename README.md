# Lunar Terrain Segmentation App

Hey, this repository will help you set up your webapp for lunar image segmentation.
* I have used FastAPI for building the API
* I have used Streamlit for the Frontend

## Setup 
1. Clone or Download the Repository and open the project directory in your editor (vs code)
2. Install the requirements
3. You can train your model using the pyhton notebook via [Kaggle](https://www.kaggle.com/datasets/romainpessia/artificial-lunar-rocky-landscape-dataset)
4. Add your trained model in 'models' and remove if there are other models present there
5. In command prompt first run your FastAPI app:- 'uvicorn backend:app --reload'
6. Then again open command prompt and run the streamlit app:- 'streamlit run frontend.py'

## About Trained model used in this app
* This model is trained using the UNET with VGG16 Backbone
* The data used for the training can be found on [Kaggle](https://www.kaggle.com/datasets/romainpessia/artificial-lunar-rocky-landscape-dataset)
* We used first 8000 images from 'render' (artificially generated Moon terrain) & 'clean' (respective masks) directories for training.
* We used all the other remaining images for validation except the last 4 which we used as test set.
* This model on Validation set gave 83% IOU on average.
* The model we trained as a part of training program at [Spartificial](https://spartificial.com/) where student's task was to improve this IOU score.
