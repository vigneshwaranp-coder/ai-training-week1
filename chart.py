import pandas as pd
import matplotlib.pyplot as plt

# Read employee data
df = pd.read_csv("employees.csv")

# Chart 1: Average salary by department
avg_salary = df.groupby("department")["salary"].mean()

avg_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.savefig("department_salary.png")
plt.show()

# Chart 2: Salary distribution using 5 bins
plt.hist(df["salary"], bins=5)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("salary_distribution.png")
plt.show()

# Chart 3: Employee ID versus salary, coloured by department
for department in df["department"].unique():
    data = df[df["department"] == department]
    plt.scatter(data["id"], data["salary"], label=department)

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("employee_salary_scatter.png")
plt.show()

# Chart 4: Monthly sales from January to June
months = ["January", "February", "March", "April", "May", "June"]
sales = [12, 15, 14, 18, 22, 25]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()
