# import statistics
# class StatisticOperator:
#     def __init__(self,listed_items):
#         self.listed_items = listed_items

#     def count(self):
#         couunts = len(self.listed_items)
#         return couunts
#     def sum(self):
#         total = 0
#         for age in self.listed_items:
#             total += age
#         return total

#     def min(self):
#         return min(self.listed_items)
#     def max(self):
#         maxi = max(self.listed_items)
#         return maxi
#     def range(self):
#         range_ = max(self.listed_items) - min(self.listed_items)
#         return range_

#     def mean(self):
#         datas = self.listed_items
#         mean_val = statistics.mean(datas)
#         return mean_val
#     def median(self):
#         datas = self.listed_items
#         median_val = statistics.median(datas)
#         return median_val
#     def mode(self):
#         datas = self.listed_items
#         mode_counts = 0
#         mode_val =  statistics.mode(datas)
#         for element in datas:
#             if element == mode_val:
#                 mode_counts += 1
#         return {'mode': mode_val, 'counts': mode_counts}
#     def std(self):
#         datas = self.listed_items
#         std_dev = statistics.stdev(datas)
#         return round(std_dev, 2)
#     def var(self):
#         datas = self.listed_items
#         variance = statistics.variance(datas)
    
#         return round(variance, 2)

    
# ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

# data = StatisticOperator(ages)

# print(data.count())
# print(data.sum())
# print(data.min())
# print(data.range())
# print(data.mean())
# print(data.median())
# print(data.mode())
# print(data.std())
# print(data.var())


# Excercise Level 2

# 2.0

class PersonAccount:
    def __init__(self, firstname, lastname):

        self.firstname = firstname
        self.lastname = lastname
        self.expenses = []
        self.incomes = []     

    def total_income(self):
        tol_incom = 0
        for expense in self.expenses:
            tol_exp += expense['Amount']

        return f"Total Income is {tol_exp}."
        

    def total_expense(self):
        tol_exp = 0
        for expense in self.expenses:
            tol_exp += expense['Amount'] 
        return f"Total Expense is {tol_exp}."
        

    def add_income(self, description, amount ):
        dict_income = {"Description": description,
        "Amount": amount}
        self.incomes.append(dict_income)

    def add_expense(self, description, amount):
        dict_expense = {"Description": description,
        "Amount": amount}
        self.expenses.append(dict_expense)
    
    def account_balance(self):
        total_exp = 0
        total_inc = 0

        for expense in self.incomes:
            total_inc += expense['Amount']
        for each_exp in self.expenses:
            total_exp += each_exp['Amount'] 
                  
    
        balance = total_inc - total_exp
        if balance < 0:
            return f"You've spent more than your income. Your debt is {balance}"
        elif balance == 0:
            return f"You've Spent all your momey"
        else:
            return f"You've spent your  money wisely. Your balance is {balance} "
    def account_info(self):

        total_exps = 0
        total_incs = 0

        for expense in self.incomes:
            total_incs += expense['Amount']
        for each_exp in self.expenses:
            total_exps += each_exp['Amount'] 
        bal = total_incs - total_exps

        
        return f"Account Name: {self.firstname} {self.lastname}\nTotal Incomes: {total_incs}\nTotal Expense: {total_exps}\nAccount Balance: {bal}"
    def all_expense(self):
        return self.expenses
    def all_incomes(self):
        return self.incomes
acc = PersonAccount('Abubakr', 'Akeeb')
incom1 = acc.add_income('Salary', 4000000)
income2 = acc.add_income('Stipend', 150000)
expenses = acc.all_expense()
incomes = acc.all_incomes()
exp1 = acc.add_expense('Internet', 13194)
info = acc.account_info()
to_exp = acc.total_expense()
print(to_exp)
# print(info)

