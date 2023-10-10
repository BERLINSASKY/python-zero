if __name__ == '__main__':
    print('hello')
else:
    print('fuck u')
    
# -------------------------------------------------------------

# نعمل امبورت لمكتبة ال
# unittest
# ندخل unittest.TestCase
# كبرامترايز للكلاس
# من اجل ان يرث الفانكشن الي بتلزمني مشان التيست

import unittest

class testcase(unittest.TestCase) :
    def test1(self):
        self.assertEqual(1+1,2,'should be 2')
    def test2(self):
        self.assertFalse(50<30,'should be false')

if __name__ == '__main__' :
    unittest.main()