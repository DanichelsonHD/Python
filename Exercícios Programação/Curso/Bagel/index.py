#Bagel = No correct numbers
#Pico = Correct numbers in the wrong position
#Fermi = Correct numbers in the correct position

import random

number_to_guess: int = 0
total_chances: int = 0

def random_number (number_size: int) -> int:
    global number_to_guess
    
    number_list: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_list: list[int] = []
    
    for _ in range(number_size):
        if len(number_list) > 0:
            new_digit = random.choice(number_list)
            number_list.remove(new_digit)
            
            new_list.append(new_digit)
    
    number_to_guess = int(''.join(map(str, new_list)))
    
    return number_to_guess

def check_digits (guess: int, number_size: int):
    correct_list: list[int] = [int(_) for _ in str(number_to_guess)]
    guess_list: list[int] = [int(_) for _ in str(guess)]
    
    bagel: bool = True
    string_to_print: str = ''
    guessed_correctly: int = 0
    
    if len(guess_list) != number_size:
        string_to_print += 'Invalid guess size'
        print(string_to_print)
        return -1
    
    for digit in guess_list:
        if digit in correct_list:
            bagel = False
            
            if guess_list.index(digit) == correct_list.index(digit):
                string_to_print += 'Fermi '
                guessed_correctly += 1
            else:
                string_to_print += 'Pico '
    
    if bagel:
        string_to_print += 'Bagel'
        
    if guessed_correctly == number_size:
        string_to_print = 'You guessed it!'
    
    print(string_to_print)
    
    return guessed_correctly
    
def main():
    global number_to_guess
    
    number_size: int = int(input('How many digits you want? '))
    chances: int = int(input('How many chances you want? '))
    number_to_guess = random_number(number_size)
    
    print('\n' + '-' * 20 + '\n')
    
    print('Welcome to Bagels!')
    print(f'Guess the {number_size}-digit number.')
    
    guessed_correctly: int = -1
    
    while guessed_correctly != number_size:
        if chances > 0:
            guess: int = int(input('Enter your guess: '))
            guessed_correctly = check_digits(guess, number_size)
            
            chances -= 1
            
            if guessed_correctly != 4:
                print(f'You have {chances} chances left.')
        else:
            print('You ran out of chances!')
            break
        
    print(f'The number was: {number_to_guess}')

main()