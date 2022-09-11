from random import randint
lis = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
table = f' {lis[0]} {lis[1]} {lis[2]}\n {lis[3]} {lis[4]} {lis[5]}\n {lis[6]} {lis[7]} {lis[8]}'
print('-'*29)
print(' '*8, 'Tic-Tac-Toe')
print('-'*29)
while True:
    play = str(input('Input "x" or "o" to start.\n').lower())
    if play == 'x':
        cpu = 'o'
        print("You've chosen x!\n")
        break
    if play == 'o':
        cpu = 'x'
        print("You've chosen o!\n")
        break
    print('Invalid input!')
while True:
    table = f' {lis[0]} {lis[1]} {lis[2]}\n {lis[3]} {lis[4]} {lis[5]}\n {lis[6]} {lis[7]} {lis[8]}'
    print(f'{table}\n')
    while True:
        jog = int(input('Where do you want to play? '))
        if play == 'x':
            if 'o' != lis[jog] != 'x':
                lis[jog] = 'x'
        if play == 'o':
            if 'o' != lis[jog] != 'x':
                lis[jog] = 'o'
        break
#    break
