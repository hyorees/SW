balance = 1000  # 초기 잔액

def deposit(amount):
    global balance
    balance += amount
    return f"Deposited {amount}. Current balance: {balance}"

def withdraw(amount):
    global balance
    if amount > balance:
        return "Insufficient balance."
    balance -= amount
    return f"Withdrew {amount}. Current balance: {balance}"

def check_balance():
    return f"Current balance: {balance}"

# 실행
while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = int(input("Choose an option: "))
    if choice == 1:
        amount = int(input("Enter amount to deposit: "))
        print(deposit(amount))
    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        print(withdraw(amount))
    elif choice == 3:
        print(check_balance())
    elif choice == 4:
        break
