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
        while(chances)



if isAlpha:
    print("good")
else:
    print("bad")
