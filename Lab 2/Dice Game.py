# Dice Game
import random
user_number = -1
generated_number = random.randint(1, 6)
while int(user_number) >6 or int(user_number) <1:
    user_number = int(input('Please select a number between 1 and 6: '))
rolls = ['one', 'two', 'three', 'four', 'five', 'six']
Correct_Incorrect = ['Incorrect', 'Correct']
user_number = rolls[user_number-1]
generated_number = rolls[generated_number-1]
print('Your guess:', user_number)
print('Actual number:', generated_number)
print('Your guess was', Correct_Incorrect[int(user_number == generated_number)])
# Challenge

bracket_list = ['+-----+', '+------+', '+-------+']

print('\n ', bracket_list[len(generated_number)-3])
print('  |', generated_number, '|' )
print(' ', bracket_list[len(generated_number)-3])

input('\nPress Enter to exit...')