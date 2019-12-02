eren = {
 "name": "Eren",
 "homework": [90.0,97.0,75.0,92.0],
 "quizzes": [88.0,40.0,94.0],
 "tests": [75.0,90.0]
}
mikasa = {
"name": "Mikasa",
"homework": [100.0, 92.0, 98.0, 100.0],
"quizzes": [82.0, 83.0, 91.0],
"tests": [89.0, 97.0]
}
armin = {
"name": "Armin",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]
}

students = [eren,mikasa,armin]

for i in students:
    for j in i:
        print(j, ":", i[j])

def average(numbers:[float]):
    result = sum(numbers) / len(numbers)
    return result

def getAverage(student: dict):
    avhw = average(student["homework"]) * 0.1
    avqz = average(student["quizzes"]) * 0.3
    avts = average(student["tests"]) * 0.6
    return hw + qz + ts 

def getLetterGrade(score: float):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

print(getLetterGrade(getAverage(eren)))
print(getLetterGrade(getAverage(mikasa)))
print(getLetterGrade(getAverage(armin)))

def getClassAverage(student: list):
    results = []
    for i in student:
        results.append(getAverage(i))
    return average(results)

classAverage = getClassAverage(students)

print(classAverage)

print(getLetterGrade(classAverage))