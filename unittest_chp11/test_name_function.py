import unittest

from name_function import get_formatted_name


class NameTestClass(unittest.TestCase):

    def test_formated_name(self):
        full_name = get_formatted_name('sheriffo', 'ceesay')
        self.assertEqual(full_name, 'Sheriffo Ceesay')

if __name__ == '__main__':
    unittest.main()