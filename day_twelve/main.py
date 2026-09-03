import random

rad_number = random.randint(1, 10)

level = input('Enter your preferred level: "easy", "medium" or "hard": ')

print(rad_number)
if level == 'easy':
    i = 0
    while i < 5:
        i += 1
        try:
            guessed_num = int(input('Guess the secret number from 1 to 10: '))
            if guessed_num != rad_number:

                print(f"You've used {i} of your trial")



            else:
                print("Goal!!! You won")
                break

        except ValueError:
            print('Input a valid number')


    else:
        print("Game Over!!! You've ran out of trails")
        




# elif level == 'medium':

# elif level == 'hard':

