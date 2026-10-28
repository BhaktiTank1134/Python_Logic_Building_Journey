# Test Cases — Bank Account Management System

## 1. Purpose

This document records the test scenarios used to verify the behavior of the `BankAccount` class, including balance inquiry, deposits, withdrawals, and independent account objects.

## 2. Test Environment

- **Language:** Python
- **Execution:** Python terminal / VS Code
- **Main file:** `main.py`
- **Testing approach:** Manual testing

## 3. Test Scenarios

| Test ID | Test Scenario | Test Input / Action | Expected Result | Status |
|---|---|---|---|---|
| TC01 | Create an account | Create an account with a name, PIN, and opening balance of ₹5,000 | Account initializes with the supplied details | PASS |
| TC02 | Check balance with correct PIN | Enter the correct PIN | Current balance is displayed | PASS |
| TC03 | Check balance with incorrect PIN | Enter an incorrect PIN | Invalid PIN message is displayed; balance is not revealed | PASS |
| TC04 | Deposit a positive amount | Deposit ₹500 into an account with ₹5,000 | Balance increases to ₹5,500 | PASS |
| TC05 | Deposit zero | Deposit ₹0 | Transaction is rejected; balance remains unchanged | PASS |
| TC06 | Deposit a negative amount | Deposit -₹500 | Transaction is rejected; balance remains unchanged | PASS |
| TC07 | Withdraw a valid amount | Withdraw ₹1,000 from an account with ₹5,500 | Balance decreases to ₹4,500 | PASS |
| TC08 | Withdraw the exact available balance | Withdraw the full available balance | Balance becomes ₹0 | NOT RUN |
| TC09 | Withdraw more than the available balance | Attempt to withdraw ₹10,000 from an account with ₹4,500 | Transaction is rejected; balance remains ₹4,500 | PASS |
| TC10 | Withdraw zero | Withdraw ₹0 | Transaction is rejected; balance remains unchanged | PASS |
| TC11 | Withdraw a negative amount | Withdraw -₹500 | Transaction is rejected; balance remains unchanged | PASS |
| TC12 | Maintain independent account balances | Create two accounts and perform transactions on one | The other account's balance remains unchanged | PASS |

## 4. Test Execution Notes

- Valid deposits and withdrawals update the balance correctly.
- Invalid transaction amounts are rejected.
- Withdrawals exceeding the available balance are rejected.
- Balance inquiries respond differently to valid and invalid PINs.
- Multiple account objects maintain independent balances.

## 5. Known Limitations

The current implementation does not yet include:

- PIN verification for deposits and withdrawals.
- Opening-balance validation.
- Comprehensive input-type validation.
- Automated unit tests using Python's `unittest` or `pytest`.

These areas can be addressed in future iterations.

## 6. Conclusion

The manually executed test cases confirm the implemented core banking operations and basic transaction validation behavior. Additional validation, authentication, and automated testing can improve the reliability of the application as it evolves.
