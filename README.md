# Suicide Ideation Detection (ML Project)

This project builds a text classifier to detect suicide ideation from Reddit posts. It includes a local baseline (TF-IDF + Logistic Regression) and deployment on Google Vertex AI.

## Overview
- **Goal:** Classify Reddit posts as suicidal vs. non-suicidal  
- **Dataset:** Kaggle (r/SuicideWatch, r/depression, r/teenagers)  
- **Approach:**  
  1. Local baseline (TF-IDF + Logistic Regression)  
  2. Cloud deployment on Vertex AI  

## Structure

<pre><code>.
├── data/                 # Raw and processed datasets
│
├── notebooks/            # Jupyter notebooks for development
│   ├── 01_text_preprocessing.ipynb   # EDA + preprocessing
│   └── 02_baseline_modeling.ipynb    # baseline model (TF-IDF + Logistic)
│
├── models/               # Saved pipeline
│   ├── model.joblib
│
├── vertex_ai/            # Vertex AI integration code
│   └── deploy_sklearn.py / .py
│   └── predict.py / .py
│
└── README.md             # Project overview & instructions
</code></pre>


## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```