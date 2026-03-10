# UNIT-PROJECT-1


## Based on what you’ve learned until now , create a project of your choosing (impress us with your imagination) . This project must at least satisfy the following minimum requirements :

- Must be interactive on CLI.
- Use your coding skills in Python accurately.
- Organize Your Code into modules & (or packages)
- Use git & Github to track changes in your code.

# Bank System CLI

Overview

A command-line banking system written in Python.

The system allows users to register, login, deposit money, withdraw money, transfer to other customers, and view their balance.

Customer data and transactions are stored in JSON files.

## Features & User Stories

As a customer I can:

- Register a new account.
- Login to my account.
- View my balance.
- Deposit money.
- Withdraw money.
- Transfer money to another customer.

System Features

- Input validation for amounts and IDs.
- Transactions are stored in "transactions.json".
- Customer data is stored in "customers.json".
- Colored CLI output using Colorama.

Usage:

Run the program: python main.py

Example operations in the CLI:

- sign in
- sign up
- Exit

after sign in successfully:
- deposit
- withdraw
- Show balance
- Transfer
- Logout 

Author

Ali Alshehri


### For your project. Edit this README.md file to include your own project name,  overview, user stories, and usage. 

### NOTE: before submitting the final project, please do the following command:
`pip freeze > requirements.txt` to enable use to know & use the packages used in your project.
