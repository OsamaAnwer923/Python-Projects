
import pandas
data = pandas.read_csv(r'G:\osama\TO DO OSAMA\Python Projects(100 Days of Python Boot Camp)\nato_alphabet_project\nato_phonetic_alphabet.csv')

alphabatic_dic = {row.letter:row.code for (index,row) in data.iterrows()}

user_input = input("type a word").upper()


list_word = [alphabatic_dic[letter] for letter in user_input]
print(list_word)