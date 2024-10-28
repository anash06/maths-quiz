import random

print("             Let's Start Maths Quizzz...")
def generate_question():
    operations = ['+', '-', '*']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(operations)
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return f"{num1} {operation} {num2}", answer

def quiz():
    score = 0
    num_questions = 10  # You can change the number of questions

    for _ in range(num_questions):
        question, answer = generate_question()
        user_answer = input(f"What is {question}? ")
        
        try:
            if int(user_answer) == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {answer}.")
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"Your score: {score}/{num_questions}")

if __name__ == "__main__":
    quiz()
