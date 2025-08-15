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
├── data/           # Raw and processed data
├── notebooks/      # Jupyter notebooks for EDA and modeling
├── scripts/        # Python scripts for preprocessing and training
├── models/         # Saved models
├── vertex_ai/      # Vertex AI integration (scripts/notebooks)
</code></pre>


## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```