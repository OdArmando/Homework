# #
# #
# def new_game():
#
#     guesses = []
#     correct_guesses = 0
#     question_num = 1
#
#     for key in questions:
#         print("-------------------------")
#         print(key)
#         for i in options[question_num-1]:
#             print(i)
#         guess = input("Enter (A, B, C, or D): ")
#         guess = guess.upper()
#         guesses.append(guess)
#
#         correct_guesses += check_answer(questions.get(key), guess)
#         question_num += 1
#
#     display_score(correct_guesses, guesses)
#
# # -------------------------
# def check_answer(answer, guess):
#
#     if answer == guess:
#         print("CORRECT!")
#         return 1
#     else:
#         print("WRONG!")
#         return 0
#
# # -------------------------
# def display_score(correct_guesses, guesses):
#     print("-------------------------")
#     print("RESULTS")
#     print("-------------------------")
#
#     score = int((correct_guesses / len(questions)) * 100)
#     print("Your score is: " + str(score) + "%")
#
# def play_again():
#
#     response = input("Do you want to play again? (yes or no): ")
#     response = response.upper()
#
#     if response == "YES":
#         return True
#     else:
#         return False
#
# questions = {
#  "How old is Keanu Reeves?: ": "A",
#  "Which is the tallest mountain in the world?: ": "D",
#  "When was the year when Romanian football team won the Champions League?: ": "C",
#  "When the World War II started, and how long it lasted?: ": "A",
#  "How many letters are in the alphabet?": "B"
# }
#
# options = [["A. 57 Years Old", "B. 65 Years Old", "C. 60 Years Old", "D. 72 Years Old"],
#           ["A. Little Mountain", "B. Mount LHOTSE", "C. Mount K2", "D. Mount Everest"],
#           ["A. Year 1995", "B. Year 1990", "C. Year 1986", "D. Year 1988"],
#           ["A. Year 1939, 6 years", "B. Year 1945, 4 years", "C. Year 1938, 5 years", "D. Year 1939, 4 years"],
#           ["A. 31 letters", "B. 29 letters", "C. 35 letters", "D. 33 letters"]]
#
# new_game()
#
# while play_again():
#     new_game()
#     if ('yes'):
#         print("Byeeeeee!")
#
# # Sunt numarul 4



#Hangman Game ver.1

# import random
#
# words = ['casa', 'python', 'masina', 'autobuz']
#
#
# # #Version 1
# # chosen_word = words [random.randint(0, len(words) -1)]
# # print(chosen_word)
#
# #Version 2
# chosen_word = random.choice(words)
# lives = 5
# print(chosen_word)
# guess_word = "_" * len(chosen_word)
# print(guess_word)
# guess_word = ""
# user_guessed_letters_correctly = set()
#
# while True:
#     # Userul a bagat o litera
#     user_input = input("Specify a letter: ")
#     if len(user_input) > 1:
#         print("Please add only one character!")
#         continue
#
#     # Daca litera exista in cuvant
#     if user_input in chosen_word:
#         user_guessed_letters_correctly.add(user_input)
#     else:
#         lives = lives - 1
#     guess_word = ""
#
#     # Verificam daca litera este in cuvant
#     for letter in chosen_word:
#         if letter in user_guessed_letters_correctly:
#             guess_word = guess_word + letter
#         else:
#             guess_word = guess_word + "_"
#     print(guess_word)
#     print(f'Lives {lives}')
#     if guess_word == chosen_word:
#         print("Congrats!")
#         break
#     if lives == 0:
#         print("Sorry, try again!")
#         break


#Hangman game ver.2
import random
words = ['casa', 'python', 'masina', 'autobuz']
chosen_word = words[random.randint(0, len(words) - 1)]
print(chosen_word)


chosen_word = random.choice(words)

hangman_word = chosen_word[0] + "_" * (len(chosen_word) - 2) + chosen_word[-1]

hangman_word = list(hangman_word)

for i in range(0, len(chosen_word)):
    if chosen_word[i] == chosen_word[0] or chosen_word[i] == chosen_word[-1]:
        hangman_word[i] = chosen_word[i]

backup_word = hangman_word
hangman_word = str()
for i in range(0, len(backup_word)):
    hangman_word = hangman_word +backup_word[i]