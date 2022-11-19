def get_grade(score):
    if score >=90: 
        grade = "A" 
    elif score >=80:
        grade = "B"
    elif score >=70:
        grade = "C"
    elif score >=60:
        grade = "D"
    else:
        grade = "F"
    return grade

score = int(input())
grade = get_grade(score)
print(grade)