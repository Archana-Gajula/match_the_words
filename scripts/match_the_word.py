#!/usr/bin/env python
import random
import os
from pandas import read_csv

if __name__ == '__main__':
    print('Enter the english word for given tamil word', )
    scripts_dir = os.path.dirname(__file__)
    data_path = scripts_dir + '/../data/tamil_english_words.csv'
    data = read_csv(data_path, sep='|', header=0)
    n = 0
    while True:
        i = random.randrange(0, len(data))
        print('---> ', data.at[i, 'Tamil'])
        right_ans = False
        for n in range(3):
            ans = input()
            if data.at[i, 'English'].lower() == ans.lower():
                break
            elif n < 2:
                print('Try again !!')
            else:
                print('Sorry! The correct answer is ', data.at[i, 'English'])
                n += 1
