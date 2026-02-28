from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment_textblob(text):
    sentiment=TextBlob(text).sentiment.polarity
    if sentiment>0:
        return "positive"
    elif sentiment<0:
        return "negative"
    else:
        return "neutral"

def analyze_sentiment_vader(text):
    sentiment=analyzer.polarity_scores(text)["compound"]
    if sentiment>0.5:
        return "positive"
    elif sentiment<-0.5:
        return "negative"
    else:
        return"neutral"

def main():
    text=input("enter the text to be analyzed")
    first=analyze_sentiment_textblob(text)
    second=analyze_sentiment_vader(text)
    print("textblob",first)
    print("vader",second)

if __name__=="__main__":
    main()