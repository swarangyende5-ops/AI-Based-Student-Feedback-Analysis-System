# 🎓 Smart Student Feedback Analysis System (NLP)

An AI-powered web application built using **Streamlit** and **Natural Language Processing (NLP)** to analyze student feedback.  
This system helps **faculty, institutions, and NAAC teams** understand student sentiment and identify common issues automatically.

---

## 🚀 Features

- 📂 Upload student feedback CSV file
- 😊 Sentiment Analysis (Positive / Negative / Neutral)
- 📊 Visual sentiment distribution using bar charts
- 🔍 Common issues & topic extraction using keywords
- 📝 Auto-generated summary for NAAC documentation
- ✅ Suggested action points for faculty improvement

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit** – Web application framework
- **Pandas** – Data processing
- **TextBlob** – NLP & sentiment analysis
- **Collections (Counter)** – Keyword frequency analysis

---

## 📁 CSV File Format

The uploaded CSV file **must contain a column named `feedback`**.

### Example:
```csv
feedback
"The teacher explains concepts very clearly"
"Classes are too fast"
"Good interaction with students"
▶️ How to Run the Project
1️⃣ Install required libraries
pip install streamlit pandas textblob
2️⃣ Download TextBlob corpora (first time only)
python -m textblob.download_corpora
3️⃣ Run the application
streamlit run app.py
📊 Output Screens
Raw student feedback table

Sentiment-labeled feedback

Sentiment bar chart

Common keywords/issues table

Auto summary report

Suggested faculty action points

🎯 Use Cases
Academic institutions

Faculty performance review

NAAC & accreditation reports

Student satisfaction analysis

Educational data analytics

🔮 Future Enhancements
☁️ Word Cloud visualization

📄 Downloadable NAAC-ready PDF report

🤖 Advanced sentiment models (VADER / BERT)

👨‍🏫 Faculty-wise feedback analysis

📈 Feedback scoring system (out of 5)

👨‍💻 Author
Swarang Yende
AI & Machine Learning Enthusiast