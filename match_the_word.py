#!/usr/bin/env python
import random

if __name__ == '__main__':
    print('Enter the english word for given tamil word', )
    tamil = ['Amma', 'Appa', 'Maphalam', 'Elumichai', 'Vangayam', 'Thakkali']
    english = ['Mom', 'Dad', 'Mango', 'Lemon', 'Onion', 'Tomato']
    n = 0
    while True:
        i = random.randrange(0, 6)
        print('---> ', tamil[i])
        right_ans = False
        for n in range(3):
            ans = input()
            if english[i].lower() == ans.lower():
                break
            elif n < 2:
                print('Try again !!')
            else:
                print('Sorry! The correct answer is ', english[i])
                n += 1
