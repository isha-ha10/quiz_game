# 🧠 Quizzler App

A simple **Python Quiz Application** built with **Tkinter** that fetches True/False trivia questions from the **Open Trivia Database (OpenTDB) API**. The application presents random trivia questions in a graphical interface, provides instant feedback on answers, and keeps track of the user's score.

---

## 🚀 Features

- Fetches **10 random True/False** trivia questions from the Open Trivia Database API.
- Interactive graphical user interface built with **Tkinter**.
- Instant feedback:
  - 🟢 Green background for correct answers.
  - 🔴 Red background for incorrect answers.
- Displays the current score throughout the quiz.
- Automatically disables the answer buttons when the quiz is complete.
- Handles HTML entities in questions for better readability.

---

## 📸 Screenshots

### Quiz Interface

<img width="424" height="674" alt="image" src="https://github.com/user-attachments/assets/52037236-6ff1-4d8f-8242-359be150fd9d" />




### Correct Answer Feedback

<img width="426" height="678" alt="image" src="https://github.com/user-attachments/assets/fae12dcf-4f78-4c37-b664-bb80b981492a" />




### Incorrect Answer Feedback

<img width="415" height="675" alt="image" src="https://github.com/user-attachments/assets/ebc16bd9-8019-4bb1-bcb4-250570d1a163" />




### Final Score Screen

<img width="414" height="676" alt="image" src="https://github.com/user-attachments/assets/8e3aeb31-a1de-4ca6-a062-1e4211e1da1b" />



---

## 📁 Project Structure

```
quizzler-app/
│
├── main.py               # Entry point of the application
├── data.py               # Fetches quiz data from the API
├── question_model.py     # Defines the Question class
├── quiz_brain.py         # Contains quiz logic
├── ui.py                 # Tkinter user interface
│
├── images/
│   ├── true.png
│   └── false.png
│
└── README.md
```

---

## 🛠️ Technologies Used

- Python 3
- Tkinter
- Requests
- Open Trivia Database (OpenTDB) API

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/quizzler-app.git
```

2. Navigate to the project folder:

```bash
cd quizzler-app
```

3. Install the required dependency:

```bash
pip install requests
```

---

## ▶️ Running the Application

Run the following command:

```bash
python main.py
```

A quiz window will open where you can answer True/False trivia questions.

---

## ⚙️ How It Works

1. The application requests **10 random True/False** questions from the Open Trivia Database API.
2. The JSON response is converted into `Question` objects.
3. `QuizBrain` manages:
   - Current question
   - Score
   - Answer validation
4. `QuizInterface` displays each question in a Tkinter window.
5. When the user selects an answer:
   - The background turns **green** if the answer is correct.
   - The background turns **red** if the answer is incorrect.
6. After a short delay, the next question is displayed.
7. Once all questions have been answered, the quiz ends and the answer buttons are disabled.

---

## 🌐 API Used

**Open Trivia Database (OpenTDB)**

https://opentdb.com/

Example API Request:

```
https://opentdb.com/api.php?amount=10&type=boolean
```

---

## 📚 Learning Outcomes

This project demonstrates:

- Object-Oriented Programming (OOP)
- Working with REST APIs
- Parsing JSON data
- Building desktop applications with Tkinter
- Event-driven programming
- Managing application state across multiple modules

---

## 🚀 Future Improvements

- Add multiple-choice questions
- Select quiz category
- Choose difficulty level
- Add a countdown timer
- Save high scores
- Add a restart button
- Improve UI with themes and animations
