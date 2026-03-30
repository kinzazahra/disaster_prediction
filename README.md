# 🌍 AI-Based Disaster Prediction & Alert System

## 🚀 Overview

This project is an AI-powered web application that predicts disaster risk (such as floods or landslides) based on environmental factors like rainfall, slope, and elevation. It visualizes risk zones on an interactive map and helps simulate early warning alerts.

---

## 💡 Features

* 📊 Machine Learning-based risk prediction
* 🗺️ Interactive map visualization using Folium
* 🔴 Risk zones marked as **High Risk** (red) and **Safe** (green)
* 🌐 Flask-based web application
* 📍 Real-world coordinates support (latitude & longitude)
* 🚨 Alert simulation for high-risk areas

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn (Random Forest)
* **Data Processing:** Pandas, NumPy
* **Visualization:** Folium (Leaflet.js)
* **Frontend:** HTML, CSS

---

## 📁 Project Structure

```
disaster_prediction/
│
├── app.py                 # Main Flask application
├── data/
│   └── dataset.csv        # Dataset used for training
├── model/
│   ├── train.py           # ML model training script
│   └── model.pkl          # Trained model
├── utils/
│   └── map_utils.py       # Map generation logic
├── templates/
│   └── index.html         # Frontend UI
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/kinzazahra/disaster_prediction.git
cd disaster_prediction
```

### 2️⃣ Install dependencies

```bash
pip install flask pandas scikit-learn folium
```

### 3️⃣ Train the model

```bash
cd model
python train.py
cd ..
```

### 4️⃣ Run the application

```bash
python app.py
```

### 5️⃣ Open in browser

```
http://127.0.0.1:5000
```

---

## 📊 Dataset

The dataset contains:

* Rainfall
* Slope
* Elevation
* Latitude & Longitude
* Risk label (0 = Safe, 1 = High Risk)

---

## 🧠 How It Works

1. The ML model is trained using environmental data.
2. The Flask app loads the trained model.
3. Data points are visualized on a map using Folium.
4. Each location is marked based on predicted risk.

---

## 📈 Future Enhancements

* 🌦️ Real-time weather API integration
* 📡 Satellite data (NASA / Sentinel)
* 🔥 Heatmap visualization
* 📱 Mobile-friendly UI
* 📩 SMS/Email alert system
* 🤖 Deep learning for terrain analysis

---

## 🎯 Use Case

This project can help in:

* Disaster management systems
* Government planning
* Emergency response systems
* Environmental monitoring

---

## 👩‍💻 Author

**Kinza Zahra**

<<<<<<< HEAD
=======

>>>>>>> 787c38b (update)
