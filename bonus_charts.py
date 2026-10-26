import pandas as pd
import matplotlib.pyplot as plt

# Read employee data
df = pd.read_csv("employees.csv")

# Create four plotting areas
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Chart 1: Average salary by department
avg_salary = df.groupby("department")["salary"].mean()
avg_salary.plot(kind="bar", ax=axes[0, 0])
axes[0, 0].set_title("Average Salary by Department")
axes[0, 0].set_xlabel("Department")
axes[0, 0].set_ylabel("Average Salary")

# Chart 2: Salary distribution
axes[0, 1].hist(df["salary"], bins=5)
axes[0, 1].set_title("Salary Distribution")
axes[0, 1].set_xlabel("Salary")
axes[0, 1].set_ylabel("Number of Employees")

# Chart 3: Employee ID vs Salary by department
for department in df["department"].unique():
    data = df[df["department"] == department]
    axes[1, 0].scatter(data["id"], data["salary"], label=department)

axes[1, 0].set_title("Employee ID vs Salary")
axes[1, 0].set_xlabel("Employee ID")
axes[1, 0].set_ylabel("Salary")
axes[1, 0].legend()

# Chart 4: Monthly sales
months = ["January", "February", "March", "April", "May", "June"]
sales = [12, 15, 14, 18, 22, 25]

axes[1, 1].plot(months, sales, marker="o")
axes[1, 1].set_title("Monthly Sales")
axes[1, 1].set_xlabel("Month")
axes[1, 1].set_ylabel("Sales")
axes[1, 1].tick_params(axis="x", rotation=45)

# Adjust spacing and save the combined figure
plt.tight_layout()
plt.savefig("all_charts.png")git status
plt.show()
