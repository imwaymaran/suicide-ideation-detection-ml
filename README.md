# Suicide Ideation Detection (ML Project)

This project aims to build a machine learning model that can detect suicide ideation from Reddit posts. It is intended to explore the use of text classification for mental health applications.

## Project Overview

- **Goal:** Classify Reddit posts as either indicative of suicide ideation or not.
- **Dataset:** Reddit posts from `r/SuicideWatch`, `r/depression`, and `r/teenagers` (sourced from Kaggle).
- **Approach:**
  - Build and evaluate a baseline ML pipeline locally
  - Re-implement the pipeline using Google AI tools such as Vertex AI or Gemini AI

## Folder Structure

<pre><code>.
├── data/                 # Raw and processed datasets
│
├── notebooks/            # Jupyter notebooks for development
│   ├── 01_text_preprocessing.ipynb   # EDA + preprocessing
│   └── 02_baseline_modeling.ipynb    # baseline model (TF-IDF + Logistic)
│
├── models/               # Serialized models/vectorizers
│   ├── tfidf_vectorizer.pkl
│   └── logreg_baseline.pkl
│
├── vertex_ai/            # (future) Vertex AI integration code
│   └── deploy_baseline.ipynb / .py
│
└── README.md             # Project overview & instructions
</code></pre>


## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```