# 📘 Math-Quiz-Generator-Python

A beginner-friendly Command Line Math Quiz Game built using Python.

This project generates random math questions and keeps track of your score in real time. It supports addition, subtraction, multiplication, and division.

---

## 🚀 Features

- Randomly generated math questions
- Supports:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (X)
  - Division (÷)
- Score tracking system
- Infinite quiz mode
- Exit option anytime
- Input validation using try/except
- Clean modular structure (separate functions file)

---

## 📂 Project Structure

```
Math-Quiz-Generator-Python/
│
├── main_file.py
└── functions_file.py
```

### 🔹 functions_file.py
Contains:
- `find_multiples()` → Ensures division questions always produce integer answers  
- `quiz_generator()` → Generates random math questions  
- `calculate_answer()` → Computes the correct answer  

### 🔹 main_file.py
- Runs the main quiz loop  
- Handles user input  
- Manages score and quiz count  
- Controls exit condition  

---

## 🛠 Requirements

- Python 3.x  
(No external libraries required)

## 🎮 How It Works

- A random math question is generated.
- You enter your answer.
- If correct → +10 points  
- If wrong → -5 points  
- Type `-99999` to exit the game anytime.

---

## 📌 Example Output

```
Welcome! To The Maths Quiz Generator...

Current Score: 0
Quiz No.1: 45 X 6
Your answer: 270
Correct answer :)
Score + 10
```

---

## 🎯 Learning Concepts Covered

- Functions
- Loops
- Conditionals
- Error Handling (try/except)
- Modular Programming
- Random Module Usage

---

## 📜 License

This project is open-source and free to use for learning purposes.
