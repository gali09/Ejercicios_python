"""
palabra == intento -> win
letra in palabra -> ayuda
letra not in palabra -> no existe
"""
colors = {
    'green': '\033[92m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'ENDC': '\033[m',
}

def color_letter(letter, color):
    return colors[color] + letter + colors['ENDC']


#init game
print('Intruduce la palabra')
win = False
word = 'trineo'
board = []
for i in range(6):
    board.append(['_' for l in range(6)])

game_counter = 0
while (not win) and (game_counter<6):
    text = input("")
    while len(text) != len(word):
        print(f"La palabra debe de tener {len(word)} caracteres")
        text = input("")

    #Win logic
    if word == text:
        board [game_counter] = [l for l in text]
        win = True
        print('HAS GANADO!!')
    else:
        test_list=[]
        for j in range(len(word)):
            if text[j] == word[j]:
                test_list.append(color_letter(text[j],'green'))
            elif text[j] in word:
                test_list.append(color_letter(text[j],'yellow'))
            else:
                test_list.append(color_letter(text[j], 'red'))
        board[game_counter] = test_list

    #Draw
    for i in range(6):
        print(" ".join(board[i]))
    game_counter +=1

if win:
    print('YEAAAH!!!')
else:
    print('OUCHH!!')
