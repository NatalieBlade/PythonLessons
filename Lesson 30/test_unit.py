import unittest
from Lesson_30_Тестирование import full_name

class NameTestCase(unittest.TestCase):
    """Тесты для функции"""

    def test_first_last_name(self):
        """Имена вида 'Ким Наталья' работает нормально?"""
        format_name = full_name("Ким", "Наталья")
        self.assertEqual(format_name, 'Ким Наталья') #assertEqual сравнивает левую часть в скобках с правой

    def test_first_last_middle_name(self):
        """Имена вида 'Ким Наталья Валентиновна' работает нормально"""
        format_name = full_name("Ким", "Наталья", "Валентиновна")
        self.assertEqual(format_name, "Ким Наталья Валентиновна")

if __name__ == "__name__":
    unittest.main()