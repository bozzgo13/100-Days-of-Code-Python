# raising errors

def withdraw_funds(balance, amount):
    """
    Simulates a bank withdrawal.
    Checks for logical errors before performing the calculation.
    """

    # Check if the user is trying to withdraw a negative amount or zero
    if amount <= 0:
        # We raise a ValueError because the 'value' of the input is logically wrong
        raise ValueError("Withdrawal amount must be greater than zero.")

    # Check if the user actually has enough money
    if amount > balance:
        # We raise a RuntimeError because the operation cannot be completed
        # given the current state of the account
        raise RuntimeError(f"Insufficient funds. Available balance: ${balance}")

    # If all checks pass, proceed with the transaction
    new_balance = balance - amount
    return new_balance



current_account_balance = 100.0

try:
    # Scenario 1: Trying to withdraw more than we have
    print(f"Attempting to withdraw $150.00...")
    current_account_balance = withdraw_funds(current_account_balance, 150.0)

    # Scenario 2: Trying to withdraw negative amount
    print(f"Attempting to withdraw $-150.00...")
    current_account_balance = withdraw_funds(current_account_balance, -150.0)

except ValueError as e:
    print(f"INPUT ERROR: {e}")
except RuntimeError as e:
    print(f"TRANSACTION ERROR: {e}")
except Exception as e:
    print(f"AN UNEXPECTED ERROR OCCURRED: {e}")
finally:
    print(f"Final session balance: ${current_account_balance}")