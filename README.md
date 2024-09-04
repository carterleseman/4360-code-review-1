# 4360-banking

Get Started    
    - python index.py 

User Interface
- deposit [amount] [accountNumber] - deposits the amount (float number) into the accountNumber (integer)
- withdraw [amount] [accountNumber] - withdraws the amount (float number) from the accountNumber (integer)
- transfer [amount] [fromAccountNumber] [toAccountNumber] - transfers the amount (float number) from the fromAccountNumber (integer) to the toAccountNumber (integer)


Requirements
1. Functional Requirements
    - software takes user input for login name and password
    - login attempts will be limited to 3
    - software has a help menu
    - software shows list of accounts
    - software shows the balanace of a specific account
    - software deposits into an account
    - software withdraws money from an account
    - software transfers money between accounts
    - transfers between accounts will be limited to 3 per sesssion
    - transfers will be limited 10000 per transaction

2. Non Functional Requirements
    - CLI user interface
    - use a while true loop, instead of once and done.  This will facilitate logins better
    - no individual process should take longer than 1000ms to return the result
