# VARK Learning Style Questionnaire

**Due Date:** June 11, 2025

---

## Overview

This project is a Python-based interactive questionnaire that helps users identify their preferred learning style(s) using the VARK model: **Visual, Auditory, Read/Write, and Kinaesthetic**. Users answer a series of multiple-choice questions, and the program analyzes their responses to determine their dominant learning style(s), providing a personalized insight at the end.

---

## Features

- 16 multiple-choice questions based on the VARK model
- Option to select a primary and an optional secondary answer for each question
- Robust input validation and user-friendly error messages
- Custom insights based on the user's learning style combination
- Graceful handling of invalid input and interruptions

---

## Code Structure

### Classes

- **`InvalidAnswerException`**  
  Custom exception class for handling invalid or duplicate answers.

- **`VARK`**  
  Main class containing all questionnaire logic, scoring, and result presentation.

### Key Methods

- **`score_answer(answer, scores)`**  
  Updates the score for the selected learning style.

- **`display_results()`**  
  Shows the final scores, identifies preferred learning style(s), and prints a personalized insight.

- **`get_valid_answer(prompt, options, exclude=None)`**  
  Prompts for and validates user input, optionally excluding repeated options.

- **`start()`**  
  Runs the questionnaire from start to finish.

---

## Data Handling

- **Captured Data:**
  - User's answers to 16 multiple-choice questions (primary and optional secondary answers)
  - Scores for each learning style (V, A, R, K)

- **Data Types Used:**
  - `list`: Stores the questions
  - `dict`: Stores answer options, scores, and cumulative results
  - `str`: Stores each user answer

- **Data Source:**  
  All questions and scoring keys are hardcoded in the program.

---

## Exception Handling

- Uses a custom exception class (`InvalidAnswerException`) to handle invalid or duplicate user inputs.
- Handles `KeyboardInterrupt` to prevent accidental program termination and maintain a smooth user experience.

---

## How to Run

1. Ensure you have Python 3 installed.
2. Download or clone this repository.
3. Open a terminal in the project directory.
4. Run the program with:

   ```sh
   python vark_questionnaire.py
   ```

---

## Output

Upon successful completion, the program will:
- Display the user's total score for each learning style.
- Identify and show the most preferred learning style(s).
- Provide a descriptive insight based on the user's results.

---

## Reflection

### Challenges Encountered

- Designing clean input validation while allowing optional second choices.
- Ensuring fair scoring when users selected multiple styles per question.
- Mapping multiple combinations of learning styles to meaningful insight messages.

### What I Learned

- Structuring object-oriented Python programs for user interaction.
- Using dictionaries effectively for mapping answers and styles.
- Implementing clean, user-friendly input loops with robust error handling.

### Future Improvements

- Adding a GUI version for enhanced user experience.
- Allowing users to save their results to a file.
- Refactoring for localization support (e.g., different languages).

---

## Acknowledgements

I would like to sincerely thank my instructor, **Ms. Shirley Komogi**, for her valuable guidance and encouragement throughout the development of this project. I also extend my heartfelt appreciation to my colleagues — **Natasha Ricky**, **Margreth Kuri**, **Junior Robert**, **Rophie Nomoru**, and **Jonah Albert** — for their shared insights, feedback, and support. Your contributions were truly invaluable and greatly appreciated.
