import unittest
from p293_classtest_survey import AnonymousSurvey

class testAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "What language?"
        my_survey = AnonymousSurvey(question)
        self.my_survey = AnonymousSurvey(question)
        responses = ['Englis', 'spanish', 'Korean']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.response[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()