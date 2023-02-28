#Mark Hendri
#Professor Eckert
#Average and Grade Assigemnt

def calculate_average(scores):
    total = sum(scores)
    return total / len(scores)

def find_grade(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score <= 89:
        return "B"
    elif score >= 70 and score <= 79:
        return "C"
    elif score >= 60 and score <= 69:
        return "D"
    else:
        return "F"

def repeat():
    response = input("Do you want another calculation? (yes/no) ")
    return response.lower() == "yes"

while True:
    scores = []
    for i in range(5):
        score = int(input(f"Enter score {i+1}: "))
        grade = find_grade(score)
        print(f"Score {score} is a(n) {grade}")
        scores.append(score)

    average = calculate_average(scores)
    print(f"The average score is {average:.2f}")

    if not repeat():
        break
