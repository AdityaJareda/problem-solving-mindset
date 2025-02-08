# Problem Solving Mindset

## Project Objective:
The goal of "Problem Solving Mindset" is to provide students with a structured learning path, where they will not only learn the fundamentals of programming (variables, data types, control flow, functions, etc.) but also engage with practical applications and interactive exercises.

## Functionalities:

1. **Topic Selection:** Display content for different learning topics (Variables, Data Types, Control Flow, Functions, OOP, etc.).

2. **Progress Tracking:** Keep a record of the student's progress (completed topics, quiz scores).

3. **Feedback Mechanism:** Provide feedback after each topic through small quizzes/exercises.

## Design Patterns:

1. **DRY (Don’t Repeat Yourself):** Convert repetitive code into functions and modules.

2. **Modularity:** Divide code logically (e.g., separate modules for learning content, feedback, and progress tracking).

## Project Structure:

```bash
problem-solving-mindset/Project/
├── main.py                # It will display the menu and control the workflow.
├── config.py              # Contains global settings.
├── modules/               # Feature-specific modules
│   ├── __init__.py        # Makes it a package.
│   ├── learning.py        # Handles learning content.
│   ├── feedback.py        # Manages quizzes and collects user feedback.
│   ├── progress.py        # Stores and retrieves user progress.
├── utils/                 # Utility functions
│   ├── __init__.py
│   ├── file_handler.py    # Handles file reading/writing for saving progress.
│   ├── validators.py      # Input validation and error handling functions.
└── tests/                 # Unit testing
    ├── __init__.py
    └── test_modules.py
```