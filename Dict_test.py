import unittest
from myDict import Dict

class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
    
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
    
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
    
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
    
    def setUp(self):
        print('set up')

    def tearDown(self):
        print('tear down')

def main():
    pass

if __name__ == '__main__':
    unittest.main()  

'''
    单元测试中两个特殊的方法， setUp， tearDown,这两个方法分别在每调用一个测试方法前后分别执行
'''

# 文档测试 doctest



