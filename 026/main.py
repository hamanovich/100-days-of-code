from pandas import read_csv

data = read_csv("nato_phonetic.csv")
phonetic_dict = {row.letter: row.code for (_, row) in data.iterrows()}

word = input("Enter your name: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
