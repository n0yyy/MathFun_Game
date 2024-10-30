import random
import operator

# Define operations
operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(list(operations.keys()))
    answer = operations[operation](num1, num2)
    return num1, operation, num2, answer

def math_game():
    score = 0
    print("Welcome to the Math Game!")
    print("Solve the problems or type 'q' to quit.")
    
    while True:
        num1, operation, num2, correct_answer = generate_question()
        question = f"{num1} {operation} {num2} = ? "
        
        user_input = input(question)

        if user_input.lower() == 'q':
            print(f"Game Over! Your final score is: {score}")
            break

        try:
            user_answer = int(user_input)
            if user_answer == correct_answer:
                score += 1
                print("Correct! Your score:", score)
            else:
                print(f"Wrong! The correct answer was {correct_answer}.")
                print(f"Game Over! Your final score is: {score}")
                break
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")

# Run the game
math_game()
