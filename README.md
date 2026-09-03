# BMI Calculator

A simple command-line Body Mass Index (BMI) calculator written in Python.

## What it does

- Takes your name, weight (kg), and height (m) as input
- Calculates BMI using the standard formula: `BMI = weight / height²`
- Tells you which category you fall into:
  - Underweight: BMI ≤ 18.5
  - Healthy weight: 18.5 < BMI ≤ 24.9
  - Overweight: 24.9 < BMI ≤ 29.9
  - Obese: BMI > 29.9
- Lets you run the check again without restarting the script

## Requirements

- Python 3.6+

## Usage

```bash
python bmi_calculator.py
```

Follow the prompts:

```
Enter your Full Name: John Doe
Enter your Weight in Kg: 70
Enter your Height in metres: 1.75
22.86
John Doe, you are healthy weight
Do you want to check again?(y/n): n
okeyy, bye bye!!
```

## Known issues / to-do

- The `input("Enter your Full Name: ".strip().lower())` line calls `.strip().lower()` on the prompt text, not the entered name — should be `input("Enter your Full Name: ").strip().lower()`.
- No error handling for non-numeric weight/height input (will crash with `ValueError`).
- Recursive `health()` calls on repeat will eventually hit Python's recursion limit if checked many times in one session — a `while True` loop wrapping the whole flow would be safer.
- No validation for zero/negative weight or height (will raise `ZeroDivisionError` or produce a nonsensical BMI).

## License

MIT (or specify your own)
