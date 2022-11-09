import copy

def read_file(path : str) -> dict:
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
        dictionary = {}
        for i in data:
            buf= i.split()
            dictionary[buf[0]]=[]
            for i in range(1, len(buf)):
                dictionary[buf[0]].append((buf[i][0], buf[i][1]))
        return dictionary
# print(read_file('chess_board.txt'))   
            

def write_chessboard(dictionary : dict, filename : str):
    rooks =   ['  ** ** **  ', '  ********  ', '    ****    ','    ****    ','   ******   ', '  ********  ']
    bishops = ['     **     ', '    ****    ', '    ****    ','     **     ','     **     ', '   ******   ']
    paws =    ['            ', '            ', '   ******   ','    ****    ','    ****    ', '  ********  ']
    knights = ['  * *       ', ' ******     ', ' * *****    ','*********   ','***  ****   ', '  ********  ']
    king =   ['     **     ', '  *  **  *  ', ' *** ** *** ',' ********** ','  ********  ', ' ********** ']
    queen =  ['**   **   **', ' **  **  ** ', '  ** ** **  ','   ******   ','   ******   ', '  ********  ']
    square_w = ['████████████', '████████████', '████████████', '████████████', '████████████', '████████████']
    square_b = ['░░░░░░░░░░░░', '░░░░░░░░░░░░', '░░░░░░░░░░░░', '░░░░░░░░░░░░', '░░░░░░░░░░░░', '░░░░░░░░░░░░']
    
    field = []
    k=0
    white=['0','1','0','1','0','1','0','1']
    black=['1','0','1','0','1','0','1','0']
    for i in range(8):
        if k%2==0:
            field.append(copy.deepcopy(white))
        else:
            field.append(copy.deepcopy(black))
        k=k+1

    for i in dictionary:
        for j in dictionary[i]:
            field[ord(j[0])-97][int(j[1])-1]+=" "+ i

    for i in range(8):
        for j in range(8):
            element=(field[i][j]).split(" ")
            if len(element) == 1:
                if element[0]=="1":
                    field[i][j]=square_w
                else:
                    field[i][j]=square_b
            else:
                buf=copy.deepcopy(eval(element[1]))
                for iter in range(6):
                    if int(element[0])==1:
                        buf[iter]=buf[iter].replace(' ', '█')
                    if int(element[0])==0:
                        buf[iter]=buf[iter].replace(' ', '░')
                field[i][j] = buf
    line=""
    for i in range(8):
        for k in range(6):
            for j in range(8):
                line+=field[i][j][k]
            line+="\n"
    with open('board.txt', 'w') as fil:
        fil.write(line)
    # return line
# print(write_chessboard(read_file('chess_board.txt'), 'random.txt'))