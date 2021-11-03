import unittest

class Test(unittest.TestCase):
    dataT = [('abcd'),('s432fad'),('')]
    dataF = [('232ds2'),('hb ddasad jv')]

    def test_unique(self):
        #true check
        for test_case in self.dataT:
            actualResult = is_unique(test_case)
            self.assertTrue(actualResult)

def is_unique(str):
    char_set = {}
    for ch in str:
        if ch in char_set:
            return False
        else:
            char_set[ch] = 1
    return True

def main():
    s = input("Input a string to check unique string: ")
    print(f"Is unique: {is_unique(s)}")

if __name__ == "__main__":
    unittest.main()