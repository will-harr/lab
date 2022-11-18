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
        assert self.a1.deposit(20) is True
        assert self.a1.get_balance() == 20
        self.a1.deposit(10.5)
        assert self.a1.get_balance() == pytest.approx(30.5, abs=0.001)
        
        assert self.a1.deposit('string') is False
        assert self.a1.deposit(-5) is False
        assert self.a1.deposit(0) is False

    def test_withdraw(self):
        assert self.a2.withdraw(20) is False
        
        self.a2.deposit(30)
        assert self.a2.withdraw(10) is True
        assert self.a2.get_balance() == 20
        
        self.a2.withdraw(5.5)
        assert self.a2.get_balance() == pytest.approx(14.5, abs=0.001)
        
        assert self.a2.withdraw(50) is False
        assert self.a2.withdraw('string') is False
        
        assert self.a2.withdraw(0) is False
