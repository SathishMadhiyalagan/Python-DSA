

## **Project Overview**
This project is a **Text Processing Web Application** built using **Flask** for the backend. It allows users to input text and processes it using **NLP techniques** such as **summarization, keyword extraction, and sentiment analysis**. The application also stores processed text data in an **SQLite database** and provides API endpoints for retrieving and managing text history.

---

## **Key Concepts Used**

### **1. Web Framework - Flask**
- Used **Flask** to create a RESTful API and serve an HTML frontend.
- Defined routes (`/process`, `/history`, `/delete`) for handling requests.
- Integrated **Flask-SQLAlchemy** for database management.

### **2. Natural Language Processing (NLP)**
- **Summarization:** Used Hugging Face’s **BART model** to generate text summaries.
- **Keyword Extraction:** Used **spaCy** to extract meaningful keywords from input text.
- **Sentiment Analysis:** Used **TextBlob** to classify text as **Positive, Negative, or Neutral** based on sentiment polarity.

### **3. Database - SQLite**
- Created a **database model** (`ProcessedTextDB`) using **SQLAlchemy** to store text, summary, keywords, and sentiment.
- Implemented **CRUD operations** for storing and retrieving processed text history.

### **4. API Integration - Google Generative AI**
- Configured **Google Gemini API** for text processing.
- Used an API key from **Google AI Studio** to authenticate and fetch responses.

### **5. Frontend - HTML, Tailwind CSS, and jQuery**
- Designed a simple UI using **Tailwind CSS**.
- Integrated **jQuery** to handle API calls and update the UI dynamically.
- Implemented a **tab-based UI** for API documentation and live text processing.

---

## **Code Breakdown**
### **1. Backend (Flask API)**
- **Route `/process`**: Accepts user text, processes it (summarization, keywords, sentiment), stores it in the database, and returns the response.
- **Route `/history`**: Retrieves previously processed text records.
- **Route `/delete`**: Deletes a specific history record.

### **2. NLP Processing Functions**
- `generate_summary(text)`: Uses **BART** model to generate a summary.
- `extract_keywords(text)`: Uses **spaCy** to extract important words.
- `analyze_sentiment(text)`: Uses **TextBlob** to determine sentiment polarity.

### **3. Frontend (index.html)**
- Contains a **textarea** for user input and a **submit button**.
- Displays results dynamically using **jQuery**.
- Includes **API documentation** for easy reference.

---

## **How to Explain in the Interview**
1. **Start with the goal of the project**: 
   - "This project is a text processing web application that takes user input, analyzes it using NLP techniques, and provides insights like summarization, keyword extraction, and sentiment analysis."

2. **Explain the technology stack**:
   - Backend: Flask, SQLAlchemy (SQLite)
   - NLP: Hugging Face Transformers, spaCy, TextBlob
   - API: Google Gemini AI
   - Frontend: HTML, Tailwind CSS, jQuery

3. **Describe the workflow**:
   - "When a user submits text, the backend processes it using NLP models and stores the results in the database. The frontend dynamically updates to display the results."

4. **Highlight your contributions**:
   - "I integrated the Flask API, implemented the database model, connected NLP models, and designed the UI using Tailwind CSS and jQuery."

5. **Show your understanding of NLP concepts**:
   - Explain how **BART** is used for summarization, how **spaCy** extracts keywords, and how **TextBlob** determines sentiment.

---
