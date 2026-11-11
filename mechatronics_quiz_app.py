# MECHATRONICS QUIZ APP
# CTE213 PYTHON MINI PROJECT
# ND2 MECHATRONICS ENGINEERING

# List containing quiz questions and answers
questions = [
    {
        "question": "What does PLC stand for?",
        "options": [
            "A. Power Line Control",
            "B. Programmable Logic Controller",
            "C. Process Level Computer",
            "D. Program Line Circuit"
        ],
        "answer": "B",
        "difficulty": "Easy"
    },
    {
        "question": "Which component detects physical changes?",
        "options": [
            "A. Sensor",
            "B. Resistor",
            "C. Switch",
            "D. Battery"
        ],
        "answer": "A",
        "difficulty": "Easy"
    },
    {
        "question": "What is the full meaning of SCADA?",
        "options": [
            "A. System Control and Data Application",
            "B. Supervisory Control and Data Acquisition",
            "C. Sensor Control and Digital Automation",
            "D. Software Control and Data Analysis"
        ],
        "answer": "B",
        "difficulty": "Medium"
    },
    {
        "question": "Which device converts electrical energy into mechanical motion?",
        "options": [
            "A. Transformer",
            "B. Capacitor",
            "C. Electric motor",
            "D. Resistor"
        ],
        "answer": "C",
        "difficulty": "Easy"
    },
    {
        "question": "Which of these is an example of an input device?",
        "options": [
            "A. Motor",
            "B. Sensor",
            "C. Lamp",
            "D. Buzzer"
        ],
        "answer": "B",
        "difficulty": "Easy"
    },
    {
        "question": "What is the main function of an actuator?",
        "options": [
            "A. To store data",
            "B. To measure temperature",
            "C. To perform physical action",
            "D. To display information"
        ],
        "answer": "C",
        "difficulty": "Medium"
    },
    {
        "question": "Which system is used to control industrial processes?",
        "options": [
            "A. DCS",
            "B. Keyboard",
            "C. Monitor",
            "D. Mouse"
        ],
        "answer": "A",
        "difficulty": "Medium"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Power Unit",
            "C. Control Program Utility",
            "D. Central Program User"
        ],
        "answer": "A",
        "difficulty": "Easy"
    },
    {
        "question": "Which component stores electrical charge?",
        "options": [
            "A. Diode",
            "B. Capacitor",
            "C. Motor",
            "D. Sensor"
        ],
        "answer": "B",
        "difficulty": "Medium"
    },
    {
        "question": "What is automation?",
        "options": [
            "A. Doing all work manually",
            "B. Using machines to perform tasks automatically",
            "C. Switching off machines",
            "D. Repairing electrical wires"
        ],
        "answer": "B",
        "difficulty": "Easy"
    }
]


# Function to display the quiz questions
def run_quiz(question_list):

    score = 0
    wrong_answers = []

    # Loop through all questions
    for number, item in enumerate(question_list, start=1):

        print("\nQuestion", number)
        print(item["question"])

        # Display answer options
        for option in item["options"]:
            print(option)

        # Collect and validate the student's answer
        while True:
            answer = input("Enter A, B, C or D: ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid choice! Enter A, B, C or D.")

        # Check the answer
        if answer == item["answer"]:
            print("Correct answer!")
            score += 1

        else:
            print("Wrong answer!")
            wrong_answers.append(item)

    return score, wrong_answers


# Function to calculate the percentage
def calculate_percentage(score, total):
    return (score / total) * 100


# Function to display the final grade
def display_result(score, total, percentage):

    print("\n" + "=" * 40)
    print("           QUIZ RESULT")
    print("=" * 40)

    print("Total questions:", total)
    print("Correct answers:", score)
    print("Wrong answers:", total - score)
    print("Percentage:", round(percentage, 2), "%")

    # Grade the student's performance
    if percentage >= 80:
        print("Grade: A - Excellent!")

    elif percentage >= 60:
        print("Grade: B - Very Good!")

    elif percentage >= 50:
        print("Grade: C - Good!")

    elif percentage >= 40:
        print("Grade: D - Fair!")

    else:
        print("Grade: F - Keep Practising!")


# Main program
def main():

    print("=" * 40)
    print("       MECHATRONICS QUIZ APP")
    print("=" * 40)

    print("Welcome to the Mechatronics Quiz!")

    # Let the student select a difficulty level
    while True:
        print("\nSelect difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. All questions")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            selected_questions = [
                q for q in questions if q["difficulty"] == "Easy"
            ]
            break

        elif choice == "2":
            selected_questions = [
                q for q in questions if q["difficulty"] == "Medium"
            ]
            break

        elif choice == "3":
            selected_questions = questions
            break

        else:
            print("Invalid choice! Select 1, 2 or 3.")

    print("\nYour quiz is starting!")

    # Run the quiz
    score, wrong_answers = run_quiz(selected_questions)

    # Calculate final percentage
    total = len(selected_questions)
    percentage = calculate_percentage(score, total)

    # Display final result
    display_result(score, total, percentage)

    # Extra feature: Review incorrect answers
    print("\n" + "=" * 40)
    print("       ANSWER REVIEW")
    print("=" * 40)

    if len(wrong_answers) == 0:
        print("Congratulations! You got every question correct.")

    else:
        for item in wrong_answers:
            print("\nQuestion:", item["question"])
            print("Correct answer:", item["answer"])

    print("\nThank you for using Mechatronics Quiz App!")


# Start the program
if __name__ == "__main__":
    main()
