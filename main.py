import random

someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon'''

someWords = someWords.split(' ')

#randomly choose workds from the above list
word = random.choice(someWords)

print(someWords)


if __name__ == 'main':
    print("Guess the word")

    for i in word:
        print('_', end=' ')
    print()

    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0 
    try:
        while(chances != 0) and flag == 0:
            print()
            chances -=1

            try:
                guess = str(input('Enter a letter to guess: '))
            
            except:
                print('Enter only letter')
                continue
            if not guess.isalpha():
                print('Enter  only a letter')
                continue
            elif len(guess) > 1:
                print ('Enter only single letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed this letter, try something else')
                continue

            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess
                print('Good going, few more to go')
                continue
            
    except:
        print()