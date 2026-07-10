#file name: test.py
#Author: Marko Gvero
#created: 2024-06-10
#Module 5 Programming Assignment - Testing

from fractions import Fraction

import unittest
from my_sum import sum



#target = __import__("my_sum.py") ##unsure if this needs to be here
#sum = target.sum

class TestSum(unittest.TestCase):
    def test_list_int(self): #Test that it can sum a list of integers
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self): #Test that it can sum a list of fractions
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()

'''
terminal results 
PS C:\Users\marko\OneDrive\Desktop\School\SDEV220\Module5\project> python
Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL
>>> import my_sum
>>> print(my_sum)
<module 'my_sum' from 'C:\\Users\\marko\\OneDrive\\Desktop\\School\\SDEV220\\Module5\\project\\my_sum\\__init__.py'>
>>> dir(my_sum)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'sum']
>>> my_sum.sum
<function sum at 0x000001FBB2FC9640>
>>> exit()
PS C:\Users\marko\OneDrive\Desktop\School\SDEV220\Module5\project> python test.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
PS C:\Users\marko\OneDrive\Desktop\School\SDEV220\Module5\project> python -m unittest test
F.
======================================================================
FAIL: test_list_fraction (test.TestSum.test_list_fraction)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\marko\OneDrive\Desktop\School\SDEV220\Module5\project\test.py", line 25, in test_list_fraction
    self.assertEqual(result, 1)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^
AssertionError: Fraction(9, 10) != 1

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
PS C:\Users\marko\OneDrive\Desktop\School\SDEV220\Module5\project> 
'''