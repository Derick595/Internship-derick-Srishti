import random

def licreate(lw):
    global li
    li = ['_'] * lw

def rightguess(wgr, rw):
    for i in range(len(rw)):
        if rw[i] == wgr:
            li[i] = wgr

    print("\nRight Guess")
    print(" ".join(li))

def wrongguess(co):
    stages = [
        r"""
------
|    |
     |
     |
     |
     |
=========
""",
        r"""
------
|    |
O    |
     |
     |
     |
=========
""",
        r"""
------
|    |
O    |
|    |
     |
     |
=========
""",
        r"""
------
|    |
O    |
/|   |
     |
     |
=========
""",
        r"""
------
|    |
O    |
/|\  |
     |
     |
=========
""",
        r"""
------
|    |
O    |
/|\  |
/    |
     |
=========
""",
        r"""
------
|    |
O    |
/|\  |
/ \  |
     |
=========
"""
    ]
    
    print(stages[co])

coun=0
words=[
    ('abacus', 'A counting tool used in math'),
    ('train', 'A mode of transport on tracks'),
    ('beach', 'Sandy place near the sea'),
    ('wheel', 'Round object used in vehicles'),
    ('cream', 'Dairy product, often used in desserts'),
    ('doctor', 'A person who treats patients'),
    ('stomach', 'Part of the digestive system')
]

ranword, hint = random.choice(words)
licreate(len(ranword))
print("Welcome to Hangman Game!")

while coun < 6:
    print("\nWord:", " ".join(li))
    wg=input("Enter a letter: ").lower()

    if wg in ranword:
        rightguess(wg, ranword)

        if "_" not in li:
            print("\nYou Won! The word was:", ranword)
            break
    else:
        coun=coun+1
        wrongguess(coun)
        print("Wrong guess! Attempts left:", 6 - coun)
        if coun==1:
            print("Hint: The word has", len(ranword), "letters")
        elif coun==2:
            print("Hint: First letter is", ranword[0])
        elif coun>=3:
            print("Hint:", hint)

if coun == 6:
    print("\nGame Over! The word was:", ranword)