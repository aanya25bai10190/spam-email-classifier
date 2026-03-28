# 📧 Spam Email Classifier

## 📌 Project Overview
This project is a Machine Learning-based Spam Email Classifier that detects whether a message is spam or not.

## 🚀 Features
- Classifies messages as Spam or Not Spam
- Built using Naive Bayes algorithm
- Simple user interface using Streamlit
- High accuracy (~98%)

## 🧠 Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

## 📊 Dataset
- SMS Spam Collection Dataset
- Contains labeled messages (spam/ham)

## ⚙️ How It Works
1. Data is cleaned and preprocessed
2. Text is converted into numbers using CountVectorizer
3. Model is trained using Naive Bayes
4. User inputs message → model predicts result

## ▶️ How to Run

1. Install dependencies:
```bash
pip install pandas numpy scikit-learn streamlit

```

### Step 2: Train the model
```bash
python model.py

```

### Step 3: Run the app
```bash
streamlit run app.py

```

---

## 📈 Results
- Achieved accuracy of **~98%**
- Successfully detects spam and non-spam messages  

---


## 🔮 Future Improvements
- Use advanced NLP models (like TF-IDF, Deep Learning)  
- Deploy the app online  
- Improve UI/UX design  
- Add real-time email filtering  

---

## 👩‍💻 Author
**Aanya Yadav**

---

## 📌 Conclusion
This project demonstrates how machine learning can be applied to solve real-world problems like spam detection. It highlights the importance of data preprocessing, feature extraction, and model selection in building effective AI systems.
