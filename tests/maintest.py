import pytest

@pytest.fixture
def input_value():
	input = 2
	return input

@pytest.mark.inoff
def testLogin():
    print("Login Successful")

@pytest.mark.inoff
def testLogoff():
    print("Logoff Sucessful")

@pytest.mark.others
def testCalculation(input_value):
    assert input_value + 2 == 4
