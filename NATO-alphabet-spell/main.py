"""NATO Alphabet auto-spell.
Project for Angela Wu's 100 days of code challenges.
"""
import pandas

alphabet_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")  # df from csv
# dict comprehension through a pandas DataFrame
nato_codes = {row.letter: row.code for (index, row) in alphabet_dataframe.iterrows()}

word_to_code = input("Enter a word to get the NATO's code:\n").upper()
nato_code = [nato_codes[letter] for letter in word_to_code]

print(nato_code)
