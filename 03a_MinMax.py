student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(f"Highest score of the class is {max_score}")
min_score = student_scores[0]
for score in student_scores:
    if score < student_scores:
        min_score = score
print(f"Minimum Score of the class is {min_score}")