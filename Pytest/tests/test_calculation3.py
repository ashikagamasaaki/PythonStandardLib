import pytest
import os
from app.calculation3 import Cal
    
class TestCal(object):
    @classmethod
    def setup_class(cls):
        cls.cal = Cal()
        cls.test_dir = 'tmp'
        cls.test_file_name = 'test.txt'
    
    def teardown_class(cls):
        import shutil
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)
    
    def test_save_no_dir(self):
        self.cal.save(self.test_dir, self.test_file_name)
        test_file_path = os.path.join(
            self.test_dir, self.test_file_name)
        assert os.path.exists(test_file_path) is True
    
    # fixture tmpdir
    def test_add_num_and_double(self, csv_file):
        print(csv_file)
        assert self.cal.add_num_and_double(1, 1) == 4
        
    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(
            tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True
        