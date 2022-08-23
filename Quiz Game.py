# def check_guess(guess, answer):
#     global score
#     still_guessing = True
#     attempt = 0
#     while still_guessing and attempt < 3:
#         if guess.lower() == answer.lower():
#             print("Correct Answer")
#             score = score + 1
#             still_guessing = False
#         else:
#             if attempt < 2:
#                 guess = input("Sorry Wrong Answer, try again")
#             attempt = attempt + 1
#     if attempt == 3:
#         print("The Correct answer is ", answer)
#
#
# score = 0
# print("Guess the Animal")
# guess1 = input("Which bear lives at the North Pole? ")
# check_guess(guess1, "polar bear")
# guess2 = input("Which is the fastest land animal? ")
# check_guess(guess2, "Cheetah")
# guess3 = input("Which is the larget animal? ")
# check_guess(guess3, "Blue Whale")
# print("Your Score is " + str(score))

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    # print("Answers: ", end="")
    # for i in questions:
    #     print(questions.get(i), end=" ")
    # print()
    #
    # print("Guesses: ", end="")
    # for i in guesses:
    #     print(i, end=" ")
    # print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
# def play_again():
#
#     response = input("Do you want to play again? (yes or no): ")
#     response = response.upper()
#
#     if response == "YES":
#         return True
#     else:
#         return False
# -------------------------


questions = {
 "How old is Keanu Reeves?: ": "A",
 "Which is the tallest mountain in the world?: ": "D",
 "When was the year when Romanian football team won the Champions League?: ": "C",
 "When the World War II started, and how long it lasted?: ": "A",
 "How many letters are in the alphabet?": "B"
}

options = [["A. 57 Years Old", "B. 65 Years Old", "C. 60 Years Old", "D. 72 Years Old"],
          ["A. Little Mountain", "B. Mount LHOTSE", "C. Mount K2", "D. Mount Everest"],
          ["A. Year 1995", "B. Year 1990", "C. Year 1986", "D. Year 1988"],
          ["A. Year 1939, 6 years", "B. Year 1945, 4 years", "C. Year 1938, 5 years", "D. Year 1939, 4 years"],
          ["A. 31 letters", "B. 29 letters", "C. 35 letters", "D. 33 letters"]]

new_game()
#
# while play_again():
#     new_game()
#     if ('yes'):
#         print("Byeeeeee!")