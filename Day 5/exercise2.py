
# You are given a list of exam scores, and you have to print out the highest score from the List.
# You will need to use what you have learnt about Lists, For Loops and Conditionals to print out the highest score in the list of student_scores.
# For example, if the scores were:
# ```
# 8 65 89 86 55 91 64 89
# ```
# Your code should print
# ```
# 91
# ```

student_scores = [8, 65, 89, 86, 55, 91, 64, 89]
max=0
for score in student_scores:
    if score > max:
        max = score

print(max)