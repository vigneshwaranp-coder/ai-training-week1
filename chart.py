import matplotlib.pyplot as plt

subjects = ["python", "sql", "git"]
marks = [80, 60, 90]

plt.bar(subjects, marks)
plt.title("my learning progress")
plt.xlabel("subjects")
plt.ylabel("marks")
plt.show()
