from ddt import ddt, data, unpack
import unittest


@ddt
class Test1(unittest.TestCase):
    @data(['aaa', 'bbb'], ['ccc', 'ddd'])
    @unpack
    def test_1(self, aaa, bbb):
        print(aaa)
        print(bbb)


if __name__ == '__main__':
    unittest.main()
