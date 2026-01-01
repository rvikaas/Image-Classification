# Vegetable Recognition & Nutrition Insights

## 🚀 Overview

This is a **full-stack AI-powered web application** that allows users to:

- Upload an image of a vegetable.
- Predict the type of vegetable using a **Convolutional Neural Network (CNN)**.
- Display **model confidence** for the prediction.
- Fetch **nutrition information per 100g** using an external API.
- Provide users with **health insights** based on nutritional data.
- 
---

## 💻 Tech Stack

- **Frontend**: React.js, HTML, CSS
- **Backend**: FastAPI, Python
- **AI Model**: Convolutional Neural Network (Keras/TensorFlow)
- **External API**: [API-Ninjas Nutrition API](https://api.api-ninjas.com/)
- **Environment Variables**: `.env` for API keys

---

## ⚡ How It Works

1. User uploads an image of a vegetable.
2. The **frontend** sends the image to the **FastAPI backend**.
3. Backend uses the **CNN model** to predict the vegetable.
4. Backend calls **Nutrition API** to fetch nutrient info.
5. Backend returns the Prediction and the nutrient info to the frontend.
