# personal finances calcultator

monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monhly expenses: "))
monthly_savings = monthly_income-total_monthly_expenses
projected_avings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_avi6ngs}")
