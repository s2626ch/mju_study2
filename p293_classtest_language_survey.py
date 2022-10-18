from p293_classtest_survey import AnonymousSurvey

question = "Whar language?"
my_survey = AnonymousSurvey(question)
my_survey.show_question()
print("Enter q to quit")
while True:
    response = input("> ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\n Thanks")
my_survey.show_result()