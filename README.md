# 📄 ResumeIQ AI

ResumeIQ AI is an AI-powered Resume Analyzer built using Python and Streamlit. It helps users analyze their resumes by extracting text from PDF files, detecting technical skills, and generating an ATS-style skill score.
live link - https://resumeiq-ai-drnn8kx5j5mxfueubani7c.streamlit.app/
## 🚀 Features

* Upload Resume PDF
* Extract Resume Text
* Detect Technical Skills
* Calculate ATS Skill Score
* User-Friendly Streamlit Interface

## 🛠️ Tech Stack

* Python
* Streamlit
* PDFPlumber
* Pandas

## 📂 Project Structure

```text
ResumeIQ-AI/
│
├── app.py
├── resume_parser.py
├── skills.py
├── requirements.txt
├── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/anubhavsingh23906-code/ResumeIQ-AI.git
```

Move into the project directory:

```bash
cd ResumeIQ-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 📊 How It Works

### 1. Resume Upload

Users upload their resume in PDF format.

### 2. Text Extraction

The application extracts text from the uploaded PDF using PDFPlumber.

### 3. Skill Detection

The extracted text is scanned for predefined technical skills such as:

* Python
* C++
* Java
* SQL
* Machine Learning
* TensorFlow
* PyTorch
* Streamlit
* GitHub
* Docker

### 4. ATS Score Calculation

The application calculates an ATS-style score based on detected skills.

## 📸 Sample Output

### Detected Skills

```text
Python
Machine Learning
Pandas
NumPy
GitHub
Streamlit
```

### ATS Score

```text
ATS Score: 70/100
```

## 🎯 Future Improvements

* Skill Recommendation System
* Resume Improvement Suggestions
* Job Role Selection
* AI-Powered Resume Feedback
* Interview Question Generator
* Resume Ranking System

## 👨‍💻 Author

### Anubhav Singh

B.Tech CSE Student | Machine Learning Enthusiast

GitHub:
https://github.com/anubhavsingh23906-code

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
