from pandas import read_csv

data = read_csv("nato_phonetic.csv")
phonetic_dict = {row.letter: row.code for (_, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter your name: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Only letters from the alphabet available")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
