import unittest
from Lesson_31 import  AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Тесты для класса AnonymousSurvey"""

    def setUp(self):
        """Создание опроса и набора ответов для всех метдов"""
        question = "Какой язык программировангият для вас наиболее интересен?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["Java", "Python", "Kotlin", "JavaScript", "Go"]

    def test_store_single_response(self):
        """Проверяется, что один ответ сохранен в списке"""
        self.my_survey.save_response(self.responses[2])
        self.assertIn(self.responses[2], self.my_survey.response)

    def test_five_responses(self):
        """Проверяется, что пять ответов сохранены в списке"""
        for response in self.responses:
            self.my_survey.save_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.response)

    def test_store_three_response(self):
        """Проверяется, что три ответа сохранены в списке"""
        self.my_survey.save_response(self.responses[1:4])
        self.assertIn(self.responses[1:4], self.my_survey.response)

    # def test_store_single_response(self):
    #     """Проверяется, что один ответ сохранен в списке"""
    #     question = "Какой язык программировангият для вас наиболее интересен?"
    #     my_survey = AnonymousSurvey(question)
    #     my_survey.save_response("Java")
    #     self.assertIn('Java', my_survey.response)
    #
    # def test_five_responses(self):
    #     """Проверяется, что пять ответов сохранены в списке"""
    #     question = "Какой язык программировангият для вас наиболее интересен?"
    #     my_survey = AnonymousSurvey(question)
    #     responses = ["Java", "Python", "Kotlin", "JavaScript", "Go"]
    #     for response in responses:
    #         my_survey.save_response(response)
    #
    #     for response in responses:
    #         self.assertIn(response, my_survey.response)

if __name__ == "__name__":
    unittest.main()