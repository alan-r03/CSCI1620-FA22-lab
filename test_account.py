import pytest
from account import *

def test__init__():
    test_personI1 = Account('TesterI1')
    assert test_personI1.account_name == 'TesterI1'
    assert test_personI1.account_balance == 0.0
    assert test_personI1.get_name() == 'TesterI1'
    assert test_personI1.get_balance() == 0.0
    test_personI2 = Account(20)
    assert test_personI2.account_name == '20'
    assert test_personI2.account_balance == 0.0
    assert test_personI2.get_name() == '20'
    assert test_personI2.get_balance() == 0.0

def test_deposit():
    test_personI = Account('TesterD')
    assert test_personI.deposit(10) == True
    assert test_personI.deposit(' 5 ') == True
    assert test_personI.deposit(2.5) == True
    assert test_personI.deposit(' 2.02 ')
    assert test_personI.deposit(-1) == False
    assert test_personI.deposit(0) == False
    assert test_personI.get_balance() == 19.52

def test_withdraw():
    test_personW = Account('TesterW')
    assert test_personW.deposit(1000) == True
    assert test_personW.withdraw(10) == True
    assert test_personW.withdraw(' 100 ') == True
    assert test_personW.withdraw(900) == False
    assert test_personW.withdraw(' 900 ') == False
    assert test_personW.withdraw(10.66) == True
    assert test_personW.withdraw(' 100.25 ') == True
    assert test_personW.withdraw(913.75) == False
    assert test_personW.withdraw(' 947.75 ') == False
    assert test_personW.get_balance() == 779.09