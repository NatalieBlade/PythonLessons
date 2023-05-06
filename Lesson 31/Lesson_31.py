class AnonymousSurvey():
    """"Для анонимных ответов"""

    def __init__(self, question):
        """Сохраняем вопрос"""
        self.question = question
        self.response = []

    def show_question(self):
        """Вывод вопроса"""
        print(self.question)

    def save_response(self, new_response):
        """Сохранение ответа"""
        self.response.append(new_response)

    def show_response(self):
        """Вывод всех ответов"""
        print("Ответы опроса: ")
        for response in self.response:
            print("- " + response)

