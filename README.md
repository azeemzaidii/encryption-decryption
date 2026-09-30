# Password Strength Checker 🔐

A Python-based password strength checker developed as **Project 1** during my Cyber Security Internship at **DecodeLabs**.

## Project Objective

The goal of this project is to create a program that evaluates a password and classifies its strength as:

- Weak
- Medium
- Strong

The checker validates the password using length and character-type requirements.

## Requirements

The program checks:

- Password length
- Presence of numbers
- Presence of uppercase letters
- Presence of symbols

According to the project guidelines, a password with fewer than 8 characters fails the minimum length requirement.

## Password Strength Logic

The program follows these rules:

### Weak

A password is classified as **Weak** if it contains fewer than 8 characters.

### Medium

A password is classified as **Medium** if it contains at least 8 characters but is missing one or more of the required character types:

- Uppercase letter
- Number
- Symbol

### Strong

A password is classified as **Strong** when it contains:

- At least 8 characters
- At least one uppercase letter
- At least one number
- At least one symbol

## Technologies Used

- Python
- String handling
- Conditional statements
- Character validation

## How It Works

The program:

1. Takes a password as input.
2. Calculates its length.
3. Checks whether it contains a number.
4. Checks whether it contains an uppercase letter.
5. Checks whether it contains a symbol.
6. Classifies the password as Weak, Medium, or Strong.
7. Displays the password analysis and final strength.

## How to Run

Make sure Python is installed on your system.

Clone the repository:

```bash
git clone https://github.com/azeemzaidii/password-strength-checker.git