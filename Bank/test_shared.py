def test_shared_deposit(funded_account):
    funded_account.deposit(100)
    assert funded_account.balance == 1100

def test_shared_withdraw(funded_account):
    funded_account.withdraw(200)
    assert funded_account.balance == 800