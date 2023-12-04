import requests


class QuizData:
    def __init__(self, difficulty='easy', amount='10'):
        self.difficulty = difficulty
        self.amount = amount

    def select_difficulty(self):
        self.difficulty = input(
            "Select Difficulty (easy/medium/hard): ").lower()

    def select_amount(self):
        self.amount = int(input("Select Number of Questions (from 2 to 30): "))

    def get_questions(self):
        self.select_difficulty()
        self.select_amount()

        response = requests.get(
            f"https://opentdb.com/api.php?amount={self.amount}&difficulty={self.difficulty}&type=boolean")
        _, results = response.json().values()

        return results
