import { useState } from "react"
import predictImage from "../api/predict";

const NUTRITION_LABELS = {
  serving_size_g: "Serving Size (g)",
  fat_total_g: "Total Fat (g)",
  fat_saturated_g: "Saturated Fat (g)",
  sodium_mg: "Sodium (mg)",
  potassium_mg: "Potassium (mg)",
  cholesterol_mg: "Cholesterol (mg)",
  carbohydrates_total_g: "Carbohydrates (g)",
  fiber_g: "Fiber (g)",
  sugar_g: "Sugar (g)"
};

const ImageUploader = () => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [file, setFile] = useState(null);

    async function handleSubmit(file){
    setData(null); 
    setLoading(true);
    const data = await predictImage(file);
    setData(data);
    setLoading(false);
    }
    
    return (
            <div className="app-container">
            <div className="card">
            <h2 className="title">Vegetable Predictor</h2>
            <h3 className="sub-title">Smart Vegetable Recognition & Nutrition Insights</h3>

            <label className="file-input-wrapper">
            <input
                type="file"
                accept="image/*"
                onChange={(e) => setFile(e.target.files[0])}
                className="file-input"
            />
            <span>Select an Image</span>
            </label>

            <button
            type="button"
            className="predict-btn"
            onClick={() => handleSubmit(file)} disabled={loading}>{loading ? "Predicting..." : "Predict"}</button>

            {data && (
            <div className="result">
                <h2 className="result-title">{data.class_name}</h2>
                <p className="confidence"><strong>The AI is {data.confidence.toFixed(2)}% sure it's a {data.class_name}</strong>
                </p>

                {data?.nutrition && (
                <div className="nutrition">
                    <h3>Nutrition (per 100g)</h3>
                    <ul>
                    {Object.keys(NUTRITION_LABELS).map(
                        (key) =>
                        data.nutrition[key] !== undefined && (
                            <li key={key}>
                            <span>{NUTRITION_LABELS[key]}</span>
                            <span>{data.nutrition[key]}</span>
                            </li>
                        )
                    )}
                    </ul>
                </div>
                )}
            </div>
            )}
        </div>
        </div>
    )
}

export default ImageUploader