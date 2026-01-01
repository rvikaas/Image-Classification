# Vegetable Recognition & Nutrition Insights

## 🚀 Overview

This is a **full-stack AI-powered web application** that allows users to:

- Upload an image of a vegetable.
- Predict the 15 types of vegetables using a **Convolutional Neural Network (CNN)**.
- Display **model confidence** for the prediction.
- Fetch **nutrition information per 100g** using an external API.
- Provide users with **health insights** based on nutritional data.
  
---

## 💻 Tech Stack

- **Frontend**: React.js, HTML, CSS
- **Backend**: FastAPI, Python
- **CNN Model**: Convolutional Neural Network (Keras/TensorFlow), EfficientNetV2M
- **External API**: [API-Ninjas Nutrition API](https://api.api-ninjas.com/)
- **Environment Variables**: `.env` for API keys

---

## ⚡ How It Works

1. User uploads an image of a vegetable.
2. The **frontend** sends the image to the **FastAPI backend**.
3. Backend uses the **CNN model** to predict the vegetable.
4. Backend calls **Nutrition API** to fetch nutrient information.
5. Backend returns the Prediction and the nutrient information to the frontend.

---

## ⚙️ Installation & Setup

### 1️⃣Clone Repository
git clone https://github.com/rvikaas/Image-Classification.git
cd vegetable-nutrition-ai

### 2️⃣ Backend Setup
- venv\Scripts\activate
- pip install -r requirements.txt
- Download the cnn model from [https://drive.google.com/file/d/159e9mAiSqZLVbujpnxDTcR4sPYnliZMK/view?usp=drive_link]
- cd Backend
- save the downloaded model file in a folder named model
- cd ..
- uvicorn Backend.main:app --reload
  
### 3️⃣ Frontend Setup
- cd frontend
- npm install
- npm run dev

---

