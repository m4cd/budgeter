# Budgeter
Budgeter is a simple python project allowing you to manage multiple budgets and bills within one account.

## What for?
Planning our home budgets having one account can be difficult. Usually we do not know how much money is left when we pay our monthly bills or spend some money on hobbies. Without such awareness it is easy to reach our account's limit.

## Components:

### Account
The assumption is we operate within one account. You can treat it as one bank account when you have all your money for different purposes. You can top-up your account whenever you want to.

It has two parameters printed in the summary:
- saldo - it is the amount of money you have on your account. It changes when you spend the money you have in your budgets or pay your bills
- money left - it is the amount of money you can spend on everyday life. It takes into account that you will spend all you have in your budgets and pay all your bills.

### Budget
Budget is essentially an amount of money you want to spend on particular purpose.

You can
1. Top-up budget - add money to your budget.
2. Spend budget - spend money from your budget
3. Delete budget - remove your budget

### Bill
Bill is a liability you are obliged to pay in certain period.
1. Create a bill
2. Delete a bill
3. Pay the bill - removes money from your account which simulates a bank transfer and changes bill status from UNPAID to PAID
4. Reset all bills - changes the status of all bills to UNPAID