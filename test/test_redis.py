import redis
import unittest

class TestRedis(unittest.TestCase):
    def setup(self):
        self.redis = redis.Redis(host='localhost', port=6379, db=0, password='dante5678')

    def test_set_get(self):
        self.redis.set('key', 'value')
        value = self.redis.get('key')
        self.assertEqual(value, 'value')

    def test_delete(self):
        self.redis.set('key', 'value')
        self.redis.delete('key')
        value = self.redis.get('key')
        self.assertIsNone(value)

if __name__ == '__main__':
    unittest.main()