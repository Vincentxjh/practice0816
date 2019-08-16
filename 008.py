#第八个练习 - 计算个人所得税
from settings import tax
salary = int(input("请输入月收入："))
tax = tax.tax_calculate(salary)
print("应纳个人所得税为：", tax)