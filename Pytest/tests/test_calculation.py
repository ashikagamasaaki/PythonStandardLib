import pytest
from app.calculation import Cal

# def test_add_num_and_double():
#     cal = Cal()
#     assert cal.add_num_and_double(1, 1) == 4
    
    
class TestCal(object):
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = Cal()
    
    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal
    
    def setup_method(self, method):
        print(f'setup method={method.__name__}')
        # self.cal = Cal()
    
    def teardown_method(self, method):
        print(f'teardown method={method.__name__}')
        # del self.cal
        
    # @pytest.mark.skip(reason='skip!')
    def test_add_num_and_double(self):
        # cal = Cal()
        assert self.cal.add_num_and_double(1, 1) == 4
    
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            # cal = Cal()
            self.cal.add_num_and_double('1', '1')

