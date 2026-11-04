import random

MIN_NUM = 1
MAX_NUM = 100
NUM = 3

def is_unique(list):
    return len(list) == len(set(list))

def generate_num(min = MIN_NUM, max = MAX_NUM): #generate 3 distinct random numbers according to the given range,and return them as a list
    result = []
    while True:
        for _ in range(NUM):
            result.append(random.randint(min, max))
        if sum(result) == 100 and is_unique(result):
            break
        else:
            result = []
    
    result.sort()
    return result

def greeting():
    print('\nHello kid, welcome to my mental arithmatic practice game!\n')
    print(f'I will generate THREE dinstinct random integers between {MIN_NUM} and {MAX_NUM}', "\033[32m INCLUSIVE!\033[0m")
    print('It is your job to guess my generation, smaller guess times will get higher scores')
    print('You will be prompted whether your guess is larger or smaller than one of my generation')

def do_game():
    nums = generate_num()
    small = nums[0] 
    mid = nums[1] 
    big = nums[2]

    n = 0
    small_hit = False
    mid_hit = False
    big_hit = False
    
    while True:
        guess = input("\nPlease input your guess or type 'q': ")
        if guess.lower() == 'q':
            break
        
        n += 1
        guess = int(guess)

        if(guess == small):
            small_hit = True
            print("Bingo!")
        elif(guess == mid):
            mid_hit = True
            print("Bingo!")
        elif(guess == big):
            big_hit = True
            print("Bingo!")
        elif guess < small:
            print('Too small!')
        elif guess > small and guess < mid:
            print('Between the smaller two')
        elif guess > mid and guess < big:
            print('Between the bigger two')
        else:
            print('Too big!')
        
        if small_hit and mid_hit and big_hit:
            caculate_score(n, nums)
            break

def caculate_score(n, nums):
    print('\nCongratulations! You have guessed correctly for all three!')
    print(f'Total Guesses: {n}')
    print('Numbers of this game:', nums)

def ending():
    print('\nBye bye!')

def main():
    greeting()
    while True:
        do_game()
        response = input('\nWanna another one? (y/n):')
        if response.lower() == 'n':
            break

    ending()

if __name__ == '__main__':
    main()