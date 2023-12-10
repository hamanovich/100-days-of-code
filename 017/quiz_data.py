import requests


class QuizData:
    def __init__(self, difficulty="easy", amount="10"):
        self.params = {
            amount: amount,
            difficulty: difficulty,
            type: "boolean"
        }

    def select_difficulty(self):
        self.params["difficulty"] = input(
            "Select Difficulty (easy/medium/hard): ").lower()

    def select_amount(self):
        self.params["amount"] = int(
            input("Select Number of Questions (from 2 to 30): "))

    def get_questions(self):
        self.select_difficulty()
        self.select_amount()

        response = requests.get(
            "https://opentdb.com/api.php", params=self.params)
        _, results = response.json().values()

        return results
