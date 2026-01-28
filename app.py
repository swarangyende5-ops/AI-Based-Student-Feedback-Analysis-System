import streamlit as st
import pandas as pd
from textblob import TextBlob
from collections import Counter

# Page configuration
st.set_page_config(page_title="smart Feedback Analysis System", layout="wide")

st.title("🎓 Smart Student Feedback Analysis System(NLP)")
st.write("AI-powered analysis of student feedback for faculty & NAAC")

# File upload
uploaded_file = st.file_uploader("Upload student Feedback CSV", type="csv")

if uploaded_file:
  df = pd.read_csv(uploaded_file)

  st.subheader("📄Raw Student Feedback")
  st.dataframe(df)

  sentiments = []
  keywords = []

# Sentiment Analysis
  for feedback in df['feedback']:
    analysis = TextBlob(feedback)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
      sentiments.append ("Positive")
    elif polarity < 0:
      sentiments.append ("Negative")
    else:
      sentiments.append("Neutral")

    # Extract keywords safely
    keywords.extend(analysis.words.lower())

  # Add sentiment column
  df['Sentiment'] = sentiments

  st.subheader("📊 Sentiment Analysis Result")
  st.dataframe(df[['feedback','Sentiment']])

  # Sentiment chart
  sentiment_count = df['Sentiment'].value_counts()
  st.bar_chart(sentiment_count)

  # Common issues / topics
  st.subheader("🔍 Common Issues / Topics Identified")
  common_words = Counter(keywords).most_common(10)
  issues_df = pd.DataFrame(common_words, columns=["keyword", "Frequency"])
  st.dataframe(issues_df)

  st.subheader("📝 Auto Summary")
  st.write(
    f"""
    - Total Feedback Analyzed: {len(df)}
    - positive Responses: {sentiment_count.get('Positive',0)}
    - Negative Responses: {sentiment_count.get('Negative',0)}
    - Neutral Responses: {sentiment_count.get('Neutral',0)}
    """
  )    

  st.subheader("✅ Suggested Action Points (Faculty Support)")
  if sentiment_count.get('Negative',0) > 0:
    st.write("- Slow down teaching pace where required")
    st.write("- Add more practical examples")
    st.write("- Improve note distribution")
  else:
    st.write("- Continue current teaching approach")  
    st.write("- Maintain student engagement") 

else:
  st.info("Please upload a CSV file with a column named **feedback**.")   