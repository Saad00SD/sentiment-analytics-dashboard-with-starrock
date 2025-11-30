# Sentiment Analytic Dashboard with StarRocks

A complete end-to-end sentiment analytics system built using **StarRocks**, **FastAPI**, and a **React-based dashboard UI**.  
This project allows users to upload social media text data, run sentiment classification, store large-scale datasets (100GB+), and visualize insights in real time.

---

## 🚀 Features

### 🔍 **1. Sentiment Analysis**
- Processes social media posts (text, hashtags, metadata).
- Classifies sentiment (Positive / Negative / Neutral).
- Supports custom ML models via FastAPI.

### 🗄️ **2. StarRocks Data Warehouse Integration**
- Optimized for large datasets (100GB+).
- Fast OLAP queries for dashboards.
- Uses Stream Load for high-speed ingestion.

### 📊 **3. Interactive Analytics Dashboard**
- Built using React (V2 version of your UI).
- Real-time filtering: user, sentiment, platform.
- Charts:
  - Pie charts (Sentiment distribution)
  - Complaint vs Satisfaction analysis
  - Trends over time
- Search by username.

### 🔌 **4. REST API (FastAPI)**
- Endpoints for:
  - data ingestion  
  - sentiment classification  
  - analytics queries  
  - dashboard backend  

---

## 🗂️ Project Folder Structure

```

sentiment-analytic-dashboard-with-starrocks/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── ml/
│   │   │   ├── model.pkl
│   │   │   ├── sentiment.py
│   │   ├── routes/
│   │   │   ├── sentiment.py
│   │   │   ├── analytics.py
│   │   │   ├── load_csv.py
│   │   ├── db/
│   │   │   ├── connector.py
│   │   │   ├── queries.py
│   │   ├── utils/
│   │   │   ├── preprocess.py
│   ├── requirements.txt
│   ├── Dockerfile
│
├── starrocks/
│   ├── docker-compose.yml
│   ├── load_scripts/
│   │   ├── stream_load.sh
│   │   ├── create_tables.sql
│   ├── data/
│       ├── sentimentdataset.csv
│
├── frontend/
│   ├── sentiment-ui/
│   │   ├── src/
│   │   │   ├── components/
│   │   │   ├── pages/
│   │   │   ├── charts/
│   │   └── package.json
│
└── README.md

````

---

## ⚙️ Installation Guide

### 1️⃣ **Start StarRocks**
```bash
cd starrocks
docker-compose up -d
````

### 2️⃣ **Start FastAPI backend**

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 3️⃣ **Start React frontend**

```bash
cd frontend/sentiment-ui
npm install
npm start
```

---

## 🧵 Data Ingestion (Stream Load)

Example command used to load CSV into StarRocks:

```bash
curl -u root: \
  -H "Expect: 100-continue" \
  -H "column_separator:," \
  -H "skip_header:1" \
  -T sentimentdataset.csv \
  http://127.0.0.1:8030/api/sentiment_app/social_posts/_stream_load
```

---

## 📈 Dashboard Insights

* Sentiment summary
* Complaint vs Satisfaction
* User-level insights
* Platform-level breakdown
* Real-time reporting from StarRocks OLAP engine

---
## Snapshots
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/9063afb1-a5e8-4b9c-88f1-02b9ad75149c" />

### Docker Desktop 
<img width="1609" height="916" alt="image" src="https://github.com/user-attachments/assets/83c64705-4c43-4589-8472-08c3c6b27f5b" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/e2f4713e-f612-43a5-939d-07a9937c7d75" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/ff12c54c-3fcf-4491-bec3-90e4db3c5e39" />

### MySQL
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/27e5d045-9ff7-4cac-9ecc-00798e104283" />



