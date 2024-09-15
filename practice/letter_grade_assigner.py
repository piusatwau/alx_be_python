#simple letter grade assigning systeme to help first year students master their grades

score = int(input("Enter your score: "))

if score >= 90:
  grade = "A"
elif score >= 80:
  grade = "B"
elif score >= 70:
  grade = "C"
else:
  grade = "F"

print("Your grade is:", grade)