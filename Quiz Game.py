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

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

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
