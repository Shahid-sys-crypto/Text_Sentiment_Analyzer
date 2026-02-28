# 📝 Text Sentiment Analyzer

A simple Python-based sentiment analysis program that analyzes text using two popular NLP libraries:

- TextBlob  
- VADER Sentiment Analyzer  

The program takes user input and classifies the sentiment as:

- Positive  
- Negative  
- Neutral  

---

## 🚀 Features

- Uses TextBlob polarity score for sentiment detection  
- Uses VADER compound score for sentiment detection  
- Compares results from both analyzers  
- Simple command-line interface  
- Easy to understand and modify  

---

## 📂 Project Structure


Text_Sentiment_Analyzer.py
README.md


---

## 📦 Requirements

Make sure Python 3.7+ is installed.

Install required libraries:

```bash
pip install textblob vaderSentiment

For first-time TextBlob users:

python -m textblob.download_corpora
🧠 How It Works
1. TextBlob Analysis

Calculates polarity score between -1 and 1

0 → Positive

< 0 → Negative

= 0 → Neutral

2. VADER Analysis

Uses compound score between -1 and 1

0.5 → Positive

< -0.5 → Negative

Otherwise → Neutral
