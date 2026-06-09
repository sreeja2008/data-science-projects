students = []
n = int(input("How many students? "))
for i in range(n):
    name  = input(f"Student {i+1} name: ")
    marks = list(map(float, input("Enter marks (space-separated): ").split()))
    students.append({"name": name, "marks": marks})
print(students)
def calc_total_avg(marks):
    total   = sum(marks)
    average = total / len(marks)
    return total, average

marks = [85, 90, 78, 92, 88]
total, avg = calc_total_avg(marks)
print(f"Total: {total}, Average: {avg:.2f}")
def get_grade(avg):
    if avg >= 90:   return "A"
    elif avg >= 80: return "B"
    elif avg >= 70: return "C"
    elif avg >= 60: return "D"
    elif avg >= 50: return "E"
    else:           return "F"

def get_result(avg):
    return "Pass" if avg >= 50 else "Fail"

avg = 75
print(f"Grade: {get_grade(avg)}, Result: {get_result(avg)}")
students = [("Alice", [85,90,78]), ("Bob", [55,60,50])]
def get_grade(avg):
    if avg>=90: return "A"
    elif avg>=80: return "B"
    elif avg>=70: return "C"
    elif avg>=60: return "D"
    elif avg>=50: return "E"
    else: return "F"
with open("grades.txt", "w") as f:
    for name, marks in students:
        avg   = sum(marks)/len(marks)
        grade = get_grade(avg)
        t     = (name, grade)
        f.write(f"{t}\n")
        print(f"Saved: {t}")
print("Grades saved to grades.txt")