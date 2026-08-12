# # 1.5
# def check_session(month):
#     report = ''
#     if month == 'Match' or month == 'April' or month == 'May':
#         report = 'It the Spring season'
#         return report
    
#     if month == 'June' or month == 'July' or month == 'August':
#         report = 'It the Summer season'
#         return report
#     if month == 'September' or month == 'October' or month == 'November':
#         report = 'It the Autum season'
#         return report
#     if month == 'December' or month == 'January' or month == 'February':
#         report =  'It the Winter season'
#         return report

# print(check_session('January'))

# # 1.6
# def calculate_slope(equation):

#     equation = str(equation)
#     equation = equation.split(' ')
#     equation = ''.join(equation)
#     m = int(equation[2])
#     return (f'The slope of the equation is {m}')

# print(calculate_slope('y = 3x + 5'))

# 1.7
def solve_quadratic_eqn(quadratic_eqn):
    quadratic_eqn = str(quadratic_eqn)
    quadratic_eqn = quadratic_eqn.strip('= 0')
    

    parameter = []

    for i, char in enumerate(quadratic_eqn):
        if i == 0 :
            if char.isnumeric():
                a = int(char)
                parameter.append(a)
            elif char.isalpha:
                a = 1
                parameter.append(a)


        if char == ' ' and i < len(quadratic_eqn)-2 :
    
            if quadratic_eqn[i + 1].isnumeric() and quadratic_eqn[i + 2].isalpha():
                b = int(quadratic_eqn[i + 1])
                parameter.append(b)
            elif quadratic_eqn[i + 1].isalpha():
                b = 1
                parameter.append(b)

        if i == len(quadratic_eqn)-1:
            if char.isnumeric() :
                c = int(char)
                parameter.append(c)
            elif char.isnumeric() :
                c = -int(char)
                parameter.append(c)

    a = parameter[0]
    b = parameter[1]
    c = parameter[2]

    root_sol = (b**2 - (4*a*c))**(1/2)
    denom = 2*a 
    total_sol1 = (-b + root_sol)/ denom
    total_sol2 = (-b - root_sol)/ denom
    return int(total_sol1), int(total_sol2)
          
        
            

print(solve_quadratic_eqn('x² + 5x + 6 = 0'))