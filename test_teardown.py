import pytest
from bank import BankAccount

@pytest.fixture
def account():
    print("[setup]")
    account = BankAccount(100)
    yield account
    print("[teardown]")

def test_account_starts_with_balance(account):
    assert account.balance == 100

def test_deposit_after_setup(account):
    account.deposit(50)
    assert account.balance == 150