from Lesson_31 import AnonymousSurvey

question = "Какой язык программировангият для вас наиболее интересен?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Нажмите 'Q' для выхода с опроса. \n")
while True:
    response = input("Language: ")
    if response == 'Q':
        break
    my_survey.save_response(response)

print("\nСпасибо за ответ!")
my_survey.show_response()