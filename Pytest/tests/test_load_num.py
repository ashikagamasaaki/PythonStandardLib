import pytest
import os
from app.load_num import load_numbers_sorted

@pytest.fixture
def txt():
    with open('num.txt', 'w') as f:
        for n in [2,5,4,3,1]:
            f.write('{}\n'.format(n))
    
    yield 'num.txt'
    os.remove('num.txt')


@pytest.fixture
def txt_and_list(txt):
    yield txt, [1,2,3,4,5]


def test_load_numbers_sorted(txt_and_list):
    # assert load_numbers_sorted(txt) == [1,2,3,4,5]
    assert load_numbers_sorted(txt_and_list[0]) == txt_and_list[1]