import unittest
from binary_search import binary_search

class TestBubleSort(unittest.TestCase):
    def test_binary_search(self):
        array = [3, 4, 5, 6, 7, 8, 9]
        find = 4

        result = binary_search(array, find, 0, len(array)-1)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored']) # Passando o argumento argv para ignorar os argumentos da linha de comando em ambientes interativos
