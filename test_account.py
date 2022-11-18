import pytest
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('Bob')
        self.a2 = Account('Steve')
        
    def teardown_method(self):
        del self.a1
        del self.a2
        
    def test_init(self):
        assert self.a1.get_name() == 'Bob'
        assert self.a2.get_name() == 'Steve'
        
        assert self.a1.get_balance() == 0
        assert self.a2.get_balance() == 0
        
    def test_deposit(self):
        self.a1.deposit(20)
        assert self.a1.get_balance() == 20
        self.a1.deposit(10.5)
        assert self.a1.get_balance() == 30.5
        
        assert self.a1.deposit('string') == False
        assert self.a1.deposit(-5) == False
        assert self.a1.deposit(0) == False

    def test_withdraw(self):
        assert self.a2.withdraw(20) == False
        
        self.a2.deposit(30)
        self.a2.withdraw(10)
        assert self.a2.get_balance() == 20
        
        self.a2.withdraw(5.5)
        assert self.a2.get_balance == 14.5
        
        assert self.a2.withdraw(50) == False
        assert self.a2.withdraw('string') == False
