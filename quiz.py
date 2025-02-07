import random

# enter quiz questions here
# format should be:
# "question": "example question",
# "options": ["list", "four", "possible", "answers"],
# "correct_answer": "correct answer"
questions = [
    {
        "question": "What is the capital of Scotland?",
        "options": ["London", "Edinburgh", "Glasgow", "Aberdeen"],
        "correct_answer": "Edinburgh"
    },
    {
        "question": "What is the southernmost county in the UK?",
        "options": ["Devon", "Dorset", "Kent", "Cornwall"],
        "correct_answer": "Cornwall"
    },
    {
        "question": "What is the second-largest city in Northern Ireland?",
        "options": ["Belfast", "Derry", "Coleraine", "Bangor"],
        "correct_answer": "Derry"
    },
    {
        "question": "What is the most visited paid attraction in the UK?",
        "options": ["Tower of London", "Stonehenge", "Edinburgh Castle", "British Museum"],
        "correct_answer": "Tower of London"
    }
]

# display questions on screen
def display_question(question):
    print(question['question'])
    for i, option in enumerate(question['options'], 1):
        print(f'{i}. {option}')

# get user input
def get_answer():
    while True:
        try:
            choice = int(input('Enter your answer (1-4): '))
            if 1 <= choice <= 4:
                return choice - 1
            else: 
                print('Please enter a number between 1 and 4.')
        except ValueError:
            print('Invalid input. Please enter a number.')

# run quiz
def run_quiz():
    score = 0
    total_questions = len(questions)

    random.shuffle(questions)

    for question in questions:
        display_question(question)
        choice = get_answer()

        if question['options'][choice] == question['correct_answer']:
            print('Correct!')
            score += 1
        else:
            print(f"Incorrect, the answer is: {question['correct_answer']}")
        
        print() # blank line between questions
    
    print(f'Complete! You scored {score} out of {total_questions}')
    percentage = (score/total_questions)*100
    print(f'Score: {percentage:.2f}%')

# build loop
def main():
    while True:
        print('Welcome to the quiz!')
        run_quiz()

        play_again = input('Play again? (yes/no):')
        if play_again != 'yes':
            print('Thanks for playing!')
            break

if __name__ == "__main__":
    main()