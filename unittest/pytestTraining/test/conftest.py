import pytest

@pytest.fixture(scope='function', autouse=True)
def setup_teardown():
    print('\nStarting....') #this will act as a constructor
    yield
    print('\nEnding....') # this will act as a destructor