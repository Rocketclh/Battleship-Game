def Game():
    global X
    global Y
    global X_R
    global Y_R
    global ans
    global test
    global type_error
    global mode
    global ship_H
    global ship_S
    global ship_H_R
    global ship_S_R
    global keep_showing_state
    global total
    global P
    global i
    global P1_B
    global P2_B
    global P2_S
    global P1S
    global P2S
    global P1S1_HP
    global P2S1_HP
    global P1S2_HP
    global P2S2_HP
    global P1S3_HP
    global P2S3_HP
    global P1S4_HP
    global P2S4_HP
    time.sleep(1)
    if P == 1:
        if type_error == False:
            print("System: Player1 round")
            if mode == 1:
                if test == True:
                    print("System: press enter to continue")
                else:
                    ans=input("System: press enter to continue")
            time.sleep(0.5)
            board()
        else:
            type_error=False
        time.sleep(0.5)
        print("System: Please enter the position of the box you want to hit")
        if test == True:
            X=random.randint(0,8)
            Y=random.randint(0,8)
            time.sleep(1)
            print("System: X:", X)
            print("System: Y:", Y)
        else:
            X=input("System: X:")
            Y=input("System: Y:")
    elif P == 2:
        if type_error == False:
            if mode == 1:
                print("System: Player2 round")
                if test == True:
                    print("System: press enter to continue")
                else:
                    ans=input("System: press enter to continue")
            elif mode == 2:
                print("System: Computer round")
            time.sleep(0.5)
            board()
        else:
            type_error=False
        time.sleep(0.5)
        if mode == 1:
            print("System: Please enter the position of the box you want to hit")
            if test == True:
                X=random.randint(0,8)
                Y=random.randint(0,8)
                time.sleep(1)
                print("System: X:", X)
                print("System: Y:", Y)
            else:
                X=input("System: X:")
                Y=input("System: Y:")
        elif mode == 2:
            print("System: Computer thinking...")
            AI()
    time.sleep(0.01)
    time.sleep(0.01)
    if X == "/show state" or Y == "/show state":
        state()
    elif X == "/state on" or Y == "/state on":
        keep_showing_state=True
    elif X == "/state off" or Y == "/state off":
        keep_showing_state=False
    elif X == "/end" or Y == "/end":
        sys.exit()
    time.sleep(0.01)
    try:
        Y=int(Y)
        X=int(X)
    except:
        Y=9
    if Y > 8 or Y < 0 or X > 8 or X < 0:
        type_error=True
        print("System: Out of bounds")
        retry()
        Game()
    debug()
    if P == 1:
        if P2_B[X][Y] == "O" or P2_B[X][Y] == "X":
            print("System: You already hit this box")
            type_error=True
            retry()
            Game()
        elif P2_B[X][Y] == " ":
            P2_B[X][Y]="X"
            P2_S[X][Y]="X"
        elif P2_B[X][Y] == "1":
            P2_B[X][Y]="O"
            P2_S[X][Y]="O"
            P2S1_HP=P2S1_HP-1
            P2S=P2S-1
            ship_H=True
            ship_S=True
        elif P2_B[X][Y] == "2":
            P2_B[X][Y]="O"
            P2_S[X][Y]="O"
            P2S2_HP=P2S2_HP-1
            ship_H=True
            if P2S2_HP == 0:
                P2S=P2S-1
                ship_S=True
        elif P2_B[X][Y] == "3":
            P2_B[X][Y]="O"
            P2_S[X][Y]="O"
            P2S3_HP=P2S3_HP-1
            ship_H=True
            if P2S3_HP == 0:
                P2S=P2S-1
                ship_S=True
        elif P2_B[X][Y] == "4":
            P2_B[X][Y]="O"
            P2_S[X][Y]="O"
            P2S4_HP=P2S4_HP-1
            ship_H=True
            if P2S4_HP == 0:
                P2S=P2S-1
                ship_S=True
    elif P == 2:
        X_R=X
        Y_R=Y
        if P1_B[X][Y] == "O" or P1_B[X][Y] == "X":
            type_error=True
            Game()
        elif P1_B[X][Y] == " ":
            P1_B[X][Y]="X"
            P1_S[X][Y]="X"
        elif P1_B[X][Y] == "1":
            P1_B[X][Y]="O"
            P1_S[X][Y]="O"
            P1S1_HP=P1S1_HP-1
            P1S=P1S-1
            ship_H=True
            ship_S=True
        elif P1_B[X][Y] == "2":
            P1_B[X][Y]="O"
            P1_S[X][Y]="O"
            P1S2_HP=P1S2_HP-1
            ship_H=True
            if P1S2_HP == 0:
                P1S=P1S-1
                ship_S=True
        elif P1_B[X][Y] == "3":
            P1_B[X][Y]="O"
            P1_S[X][Y]="O"
            P1S3_HP=P1S3_HP-1
            ship_H=True
            if P1S3_HP == 0:
                P1S=P1S-1
                ship_S=True
        elif P1_B[X][Y] == "4":
            P1_B[X][Y]="O"
            P1_S[X][Y]="O"
            P1S4_HP=P1S4_HP-1
            ship_H=True
            if P1S4_HP == 0:
                P1S=P1S-1
                ship_S=True
    time.sleep(0.01)
    debug()
    if ship_H == True:
        ship_H=False
        if P == 1:
            if mode == 1:
                print("System: Player2 ship got hit")
            elif mode == 2:
                print("System: Computer ship got hit")
            if ship_S == True:
                ship_S=False
                if mode == 1:
                    print("System: Player2 ship got sink")
                elif mode == 2:
                    print("System: Computer ship got sink")
        elif P == 2:
            ship_H_R=True
            print("System: Player1 ship got hit")
            if ship_S == True:
                ship_S=False
                ship_S_R=True
                print("System: Player1 ship got sink")
    change()
def AI():
    global RAM #register array
    global X #X coordinate
    global X_R #last fired X
    global Y #Y coordinate
    global Y_R #last fired Y
    global ship_H_R #ship hit register
    global ship_S_R #ship sink register
    global target #target register
    if ship_S_R == False:
        if ship_H_R == True:
            if target == False:
                i=0
                target=True
                RAM[0]=X_R
                RAM[1]=Y_R
            i=i+1
            if Y_R == 9:
                Y=Y_R
                X=X_R+1
            else:
                if i == 1:
                    X=X_R
                    Y=Y_R+1
                elif i == 2:
                    X=X_R
                    Y=Y_R+1
                else:
                    X_R=RAM[0]
                    Y_R=RAM[1]
                    RAM=None
                    RAM=[" "]*2
                    ship_H_R=False
                    ship_S_R=False
                    target=False
                    i=0
                    if Y_R == 9:
                        X=X_R+1
                        Y=1
                    else:
                        X=X_R
                        Y=Y_R+1
        elif ship_H_R == False:
            if target == True:
                i=i+1
                if Y_R == 9:
                    Y=Y_R
                    X=X_R+1
                else:
                    if i == 2:
                        X=X_R+1
                        Y=RAM[1]
                    if i == 3:
                        X=X_R+1
                        Y=Y_R
                    if i == 4:
                        X=X_R+1
                        Y=Y_R
                    else:
                        X_R=RAM[0]
                        Y_R=RAM[1]
                        RAM=None
                        RAM=[" "]*2
                        ship_H_R=False
                        ship_S_R=False
                        target=False
                        i=0
                        if Y_R == 9:
                            X=X_R+1
                            Y=1
                        else:
                            X=X_R
                            Y=Y_R+1
            elif target == False:
                if X_R == None and Y_R == None:
                    X=1
                    Y=1
                elif Y_R == 9:
                    X=X_R+1
                    Y=1
                else:
                    X=X_R
                    Y=Y_R+1
        time.sleep(0.01)   
        ship_H_R=False
    else:
        X_R=RAM[0]
        Y_R=RAM[1]
        RAM=None
        RAM=[" "]*2
        ship_H_R=False
        ship_S_R=False
        target=False
        i=0
        if Y_R == 9:
            X=X_R+1
            Y=1
        else:
            X=X_R
            Y=Y_R+1
    X=int(X)-1
    Y=int(Y)-1
def change():
    global P
    global P1S
    global P2S
    if P == 1:
        P=2
    elif P == 2:
        P=1
    time.sleep(0.01)
    if P1S == 0:
        if mode == 1:
            print("System: Player2 Win!")
        elif mode == 2:
            print("System: Computer Win!")
        end()
    elif P2S == 0:
        print("System: Player1 Win!")
        end()
    else:
        print(" ")
        print("System: Player1 have", P1S, "ships remaining")
        if mode == 1:
            print("System: Player2 have", P2S, "ships remaining")
        elif mode == 2:
            print("System: Computer have", P2S, "ships remaining")
        time.sleep(1)
        Game()
def end():
    global ans
    time.sleep(0.5)
    ans=input("System: press enter to end the progrem")
    sys.exit()
def ready():
    global X
    global Y
    global ans
    global test
    global type_error
    global mode
    global total
    global P
    global i
    global P1_B
    global P2_B
    while i < total:
        i=i+1
        if P == 1:
            if type_error == False:
                board()
            else:
                type_error=False
            print("System: Please enter your", i, "ship's top left position")
            if test == True:
                X=random.randint(0,8)
                Y=random.randint(0,8)
                time.sleep(1)
                print("System: X:", X)
                print("System: Y:", Y)
            else:
                try:
                    X=int(input("System: X:"))
                    Y=int(input("System: Y:"))
                except:
                    Y=10
            time.sleep(0.01)
            if Y > 8 or Y < 0 or X > 8 or X < 0:
                ready_retry(True)
            debug()
        elif P == 2:
            if mode == 1:
                if type_error == False:
                    board()
                else:
                    type_error=False
                print("System: Please enter your", i, "ship's top left position")
                if test == True:
                    X=random.randint(0,8)
                    Y=random.randint(0,8)
                    time.sleep(1)
                    print("System: X:", X)
                    print("System: Y:", Y)
                else:
                    try:
                        X=int(input("System: X:"))
                        Y=int(input("System: Y:"))
                    except:
                        Y=10
                time.sleep(0.01)
                if Y > 8 or Y < 0 or X > 8 or X < 0:
                    ready_retry(True)
                debug()
            elif mode == 2:
                X=random.randint(0,8)
                Y=random.randint(0,8)
        time.sleep(0.01)
        if P == 1:
            if i == 2:
                if X == 8:
                    ready_retry(True)
            elif i == 3:
                if Y > 6 :
                    ready_retry(True)
            elif i == 4:
                if X > 5 :
                    ready_retry(True)
        elif P == 2:
            if i == 2:
                if X == 8:
                    if mode == 1:
                        ready_retry(True)
                    elif mode == 2:
                        X=random.randint(0,7)
            elif i == 3:
                if Y > 6 :
                    if mode == 1:
                        ready_retry(True)
                    elif mode == 2:
                        Y=random.randint(0,6)
            elif i == 4:
                if X > 5 :
                    if mode == 1:
                        ready_retry(True)
                    elif mode == 2:
                        X=random.randint(0,5)
        time.sleep(0.01)
        if P == 1:
            if i == 1:
                P1_B[X][Y]="1"
            elif i == 2:
                if  P1_B[X][Y] != " " and P1_B[X+1][Y] != " ":
                    ready_retry(True)
                else:
                    P1_B[X][Y] = "2"
                    X=X+1
                    P1_B[X][Y] = "2"
            elif i == 3:
                if  P1_B[X][Y] != " " and P1_B[X][Y+1] != " " and P1_B[X][Y+2] != " ":
                    ready_retry(True)
                else:
                    P1_B[X][Y] = "3"
                    Y=Y+1
                    P1_B[X][Y] = "3"
                    Y=Y+1
                    P1_B[X][Y] = "3"
            elif i == 4:
                if  P1_B[X][Y] != " " and P1_B[X+1][Y] != " " and P1_B[X+2][Y] != " " and P1_B[X+3][Y] != " ":
                    ready_retry(True)
                else:
                    P1_B[X][Y] = "4"
                    X=X+1
                    P1_B[X][Y] = "4"
                    X=X+1
                    P1_B[X][Y] = "4"
                    X=X+1
                    P1_B[X][Y] = "4"
        elif P == 2:
            if i == 1:
                P2_B[X][Y]="1"
            elif i == 2:
                if  P2_B[X][Y] != " " and P2_B[X+1][Y] != " ":
                    if mode == 1:
                        ready_retry(True)
                    elif mode == 2:
                        ready_retry(False)
                else:
                    P2_B[X][Y] = "2"
                    X=X+1
                    P2_B[X][Y] = "2"
            elif i == 3:
                if  P2_B[X][Y] != " " and P2_B[X][Y+1] != " " and P2_B[X][Y+2] != " ":
                    if mode == 1:
                        ready_retry(True)
                    elif mode == 2:
                        ready_retry(False)
                else:
                    P2_B[X][Y] = "3"
                    Y=Y+1
                    P2_B[X][Y] = "3"
                    Y=Y+1
                    P2_B[X][Y] = "3"
            elif i == 4:
                if  P2_B[X][Y] != " " and P2_B[X+1][Y] != " " and P2_B[X+2][Y] != " " and P2_B[X+3][Y] != " ":
                    if mode == 1:
                        ready_retry(True)
                    elif mode == 2:
                        ready_retry(False)
                else:
                    P2_B[X][Y] = "4"
                    X=X+1
                    P2_B[X][Y] = "4"
                    X=X+1
                    P2_B[X][Y] = "4"
                    X=X+1
                    P2_B[X][Y] = "4"
        debug()
    if P == 1:
        if i == total:
            i=0
            P=2
            ready()
        else:
            print("System: Unknown error")
            print("System: Please contact the developer")
            ans=input("System: press enter to end the progrem")
            sys.exit()
    elif P == 2:
        if i == total:
            P=random.randint(1,2)
            change()
        else:
            print("System: Unknown error")
            print("System: Please contact the developer")
            ans=input("System: press enter to end the progrem")
            sys.exit()
def board():
    global P1_B
    global P1_S
    global P2_B
    global P2_S
    global mode
    if mode == 1:
        if P == 1:
            print("Y/X   0     1     2     3     4     5     6     7     8")
            print("0  ", "[", P1_B[0][0], "]", "[", P1_B[1][0], "]", "[", P1_B[2][0], "]", "[", P1_B[3][0], "]", "[", P1_B[4][0], "]", "[", P1_B[5][0], "]", "[", P1_B[6][0], "]", "[", P1_B[7][0], "]", "[", P1_B[8][0], "]")
            print("1  ", "[", P1_B[0][1], "]", "[", P1_B[1][1], "]", "[", P1_B[2][1], "]", "[", P1_B[3][1], "]", "[", P1_B[4][1], "]", "[", P1_B[5][1], "]", "[", P1_B[6][1], "]", "[", P1_B[7][1], "]", "[", P1_B[8][1], "]")
            print("2  ", "[", P1_B[0][2], "]", "[", P1_B[1][2], "]", "[", P1_B[2][2], "]", "[", P1_B[3][2], "]", "[", P1_B[4][2], "]", "[", P1_B[5][2], "]", "[", P1_B[6][2], "]", "[", P1_B[7][2], "]", "[", P1_B[8][2], "]")
            print("3  ", "[", P1_B[0][3], "]", "[", P1_B[1][3], "]", "[", P1_B[2][3], "]", "[", P1_B[3][3], "]", "[", P1_B[4][3], "]", "[", P1_B[5][3], "]", "[", P1_B[6][3], "]", "[", P1_B[7][3], "]", "[", P1_B[8][3], "]")
            print("4  ", "[", P1_B[0][4], "]", "[", P1_B[1][4], "]", "[", P1_B[2][4], "]", "[", P1_B[3][4], "]", "[", P1_B[4][4], "]", "[", P1_B[5][4], "]", "[", P1_B[6][4], "]", "[", P1_B[7][4], "]", "[", P1_B[8][4], "]")
            print("5  ", "[", P1_B[0][5], "]", "[", P1_B[1][5], "]", "[", P1_B[2][5], "]", "[", P1_B[3][5], "]", "[", P1_B[4][5], "]", "[", P1_B[5][5], "]", "[", P1_B[6][5], "]", "[", P1_B[7][5], "]", "[", P1_B[8][5], "]")
            print("6  ", "[", P1_B[0][6], "]", "[", P1_B[1][6], "]", "[", P1_B[2][6], "]", "[", P1_B[3][6], "]", "[", P1_B[4][6], "]", "[", P1_B[5][6], "]", "[", P1_B[6][6], "]", "[", P1_B[7][6], "]", "[", P1_B[8][6], "]")
            print("7  ", "[", P1_B[0][7], "]", "[", P1_B[1][7], "]", "[", P1_B[2][7], "]", "[", P1_B[3][7], "]", "[", P1_B[4][7], "]", "[", P1_B[5][7], "]", "[", P1_B[6][7], "]", "[", P1_B[7][7], "]", "[", P1_B[8][7], "]")
            print("8  ", "[", P1_B[0][8], "]", "[", P1_B[1][8], "]", "[", P1_B[2][8], "]", "[", P1_B[3][8], "]", "[", P1_B[4][8], "]", "[", P1_B[5][8], "]", "[", P1_B[6][8], "]", "[", P1_B[7][8], "]", "[", P1_B[8][8], "]")
            print("Player: P1 Board")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~SEA~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Player: P2 Board")
            print("Y/X   0     1     2     3     4     5     6     7     8")
            print("0  ", "[", P2_S[0][0], "]", "[", P2_S[1][0], "]", "[", P2_S[2][0], "]", "[", P2_S[3][0], "]", "[", P2_S[4][0], "]", "[", P2_S[5][0], "]", "[", P2_S[6][0], "]", "[", P2_S[7][0], "]", "[", P2_S[8][0], "]")
            print("1  ", "[", P2_S[0][1], "]", "[", P2_S[1][1], "]", "[", P2_S[2][1], "]", "[", P2_S[3][1], "]", "[", P2_S[4][1], "]", "[", P2_S[5][1], "]", "[", P2_S[6][1], "]", "[", P2_S[7][1], "]", "[", P2_S[8][1], "]")
            print("2  ", "[", P2_S[0][2], "]", "[", P2_S[1][2], "]", "[", P2_S[2][2], "]", "[", P2_S[3][2], "]", "[", P2_S[4][2], "]", "[", P2_S[5][2], "]", "[", P2_S[6][2], "]", "[", P2_S[7][2], "]", "[", P2_S[8][2], "]")
            print("3  ", "[", P2_S[0][3], "]", "[", P2_S[1][3], "]", "[", P2_S[2][3], "]", "[", P2_S[3][3], "]", "[", P2_S[4][3], "]", "[", P2_S[5][3], "]", "[", P2_S[6][3], "]", "[", P2_S[7][3], "]", "[", P2_S[8][3], "]")
            print("4  ", "[", P2_S[0][4], "]", "[", P2_S[1][4], "]", "[", P2_S[2][4], "]", "[", P2_S[3][4], "]", "[", P2_S[4][4], "]", "[", P2_S[5][4], "]", "[", P2_S[6][4], "]", "[", P2_S[7][4], "]", "[", P2_S[8][4], "]")
            print("5  ", "[", P2_S[0][5], "]", "[", P2_S[1][5], "]", "[", P2_S[2][5], "]", "[", P2_S[3][5], "]", "[", P2_S[4][5], "]", "[", P2_S[5][5], "]", "[", P2_S[6][5], "]", "[", P2_S[7][5], "]", "[", P2_S[8][5], "]")
            print("6  ", "[", P2_S[0][6], "]", "[", P2_S[1][6], "]", "[", P2_S[2][6], "]", "[", P2_S[3][6], "]", "[", P2_S[4][6], "]", "[", P2_S[5][6], "]", "[", P2_S[6][6], "]", "[", P2_S[7][6], "]", "[", P2_S[8][6], "]")
            print("7  ", "[", P2_S[0][7], "]", "[", P2_S[1][7], "]", "[", P2_S[2][7], "]", "[", P2_S[3][7], "]", "[", P2_S[4][7], "]", "[", P2_S[5][7], "]", "[", P2_S[6][7], "]", "[", P2_S[7][7], "]", "[", P2_S[8][7], "]")
            print("8  ", "[", P2_S[0][8], "]", "[", P2_S[1][8], "]", "[", P2_S[2][8], "]", "[", P2_S[3][8], "]", "[", P2_S[4][8], "]", "[", P2_S[5][8], "]", "[", P2_S[6][8], "]", "[", P2_S[7][8], "]", "[", P2_S[8][8], "]")
            print(" ")
        elif P == 2:
            print("Y/X   0     1     2     3     4     5     6     7     8")
            print("0  ", "[", P1_S[0][0], "]", "[", P1_S[1][0], "]", "[", P1_S[2][0], "]", "[", P1_S[3][0], "]", "[", P1_S[4][0], "]", "[", P1_S[5][0], "]", "[", P1_S[6][0], "]", "[", P1_S[7][0], "]", "[", P1_S[8][0], "]")
            print("1  ", "[", P1_S[0][1], "]", "[", P1_S[1][1], "]", "[", P1_S[2][1], "]", "[", P1_S[3][1], "]", "[", P1_S[4][1], "]", "[", P1_S[5][1], "]", "[", P1_S[6][1], "]", "[", P1_S[7][1], "]", "[", P1_S[8][1], "]")
            print("2  ", "[", P1_S[0][2], "]", "[", P1_S[1][2], "]", "[", P1_S[2][2], "]", "[", P1_S[3][2], "]", "[", P1_S[4][2], "]", "[", P1_S[5][2], "]", "[", P1_S[6][2], "]", "[", P1_S[7][2], "]", "[", P1_S[8][2], "]")
            print("3  ", "[", P1_S[0][3], "]", "[", P1_S[1][3], "]", "[", P1_S[2][3], "]", "[", P1_S[3][3], "]", "[", P1_S[4][3], "]", "[", P1_S[5][3], "]", "[", P1_S[6][3], "]", "[", P1_S[7][3], "]", "[", P1_S[8][3], "]")
            print("4  ", "[", P1_S[0][4], "]", "[", P1_S[1][4], "]", "[", P1_S[2][4], "]", "[", P1_S[3][4], "]", "[", P1_S[4][4], "]", "[", P1_S[5][4], "]", "[", P1_S[6][4], "]", "[", P1_S[7][4], "]", "[", P1_S[8][4], "]")
            print("5  ", "[", P1_S[0][5], "]", "[", P1_S[1][5], "]", "[", P1_S[2][5], "]", "[", P1_S[3][5], "]", "[", P1_S[4][5], "]", "[", P1_S[5][5], "]", "[", P1_S[6][5], "]", "[", P1_S[7][5], "]", "[", P1_S[8][5], "]")
            print("6  ", "[", P1_S[0][6], "]", "[", P1_S[1][6], "]", "[", P1_S[2][6], "]", "[", P1_S[3][6], "]", "[", P1_S[4][6], "]", "[", P1_S[5][6], "]", "[", P1_S[6][6], "]", "[", P1_S[7][6], "]", "[", P1_S[8][6], "]")
            print("7  ", "[", P1_S[0][7], "]", "[", P1_S[1][7], "]", "[", P1_S[2][7], "]", "[", P1_S[3][7], "]", "[", P1_S[4][7], "]", "[", P1_S[5][7], "]", "[", P1_S[6][7], "]", "[", P1_S[7][7], "]", "[", P1_S[8][7], "]")
            print("8  ", "[", P1_S[0][8], "]", "[", P1_S[1][8], "]", "[", P1_S[2][8], "]", "[", P1_S[3][8], "]", "[", P1_S[4][8], "]", "[", P1_S[5][8], "]", "[", P1_S[6][8], "]", "[", P1_S[7][8], "]", "[", P1_S[8][8], "]")
            print("Player: P1 Board")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~SEA~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Player: P2 Board")
            print("Y/X   0     1     2     3     4     5     6     7     8")
            print("0  ", "[", P2_B[0][0], "]", "[", P2_B[1][0], "]", "[", P2_B[2][0], "]", "[", P2_B[3][0], "]", "[", P2_B[4][0], "]", "[", P2_B[5][0], "]", "[", P2_B[6][0], "]", "[", P2_B[7][0], "]", "[", P2_B[8][0], "]")
            print("1  ", "[", P2_B[0][1], "]", "[", P2_B[1][1], "]", "[", P2_B[2][1], "]", "[", P2_B[3][1], "]", "[", P2_B[4][1], "]", "[", P2_B[5][1], "]", "[", P2_B[6][1], "]", "[", P2_B[7][1], "]", "[", P2_B[8][1], "]")
            print("2  ", "[", P2_B[0][2], "]", "[", P2_B[1][2], "]", "[", P2_B[2][2], "]", "[", P2_B[3][2], "]", "[", P2_B[4][2], "]", "[", P2_B[5][2], "]", "[", P2_B[6][2], "]", "[", P2_B[7][2], "]", "[", P2_B[8][2], "]")
            print("3  ", "[", P2_B[0][3], "]", "[", P2_B[1][3], "]", "[", P2_B[2][3], "]", "[", P2_B[3][3], "]", "[", P2_B[4][3], "]", "[", P2_B[5][3], "]", "[", P2_B[6][3], "]", "[", P2_B[7][3], "]", "[", P2_B[8][3], "]")
            print("4  ", "[", P2_B[0][4], "]", "[", P2_B[1][4], "]", "[", P2_B[2][4], "]", "[", P2_B[3][4], "]", "[", P2_B[4][4], "]", "[", P2_B[5][4], "]", "[", P2_B[6][4], "]", "[", P2_B[7][4], "]", "[", P2_B[8][4], "]")
            print("5  ", "[", P2_B[0][5], "]", "[", P2_B[1][5], "]", "[", P2_B[2][5], "]", "[", P2_B[3][5], "]", "[", P2_B[4][5], "]", "[", P2_B[5][5], "]", "[", P2_B[6][5], "]", "[", P2_B[7][5], "]", "[", P2_B[8][5], "]")
            print("6  ", "[", P2_B[0][6], "]", "[", P2_B[1][6], "]", "[", P2_B[2][6], "]", "[", P2_B[3][6], "]", "[", P2_B[4][6], "]", "[", P2_B[5][6], "]", "[", P2_B[6][6], "]", "[", P2_B[7][6], "]", "[", P2_B[8][6], "]")
            print("7  ", "[", P2_B[0][7], "]", "[", P2_B[1][7], "]", "[", P2_B[2][7], "]", "[", P2_B[3][7], "]", "[", P2_B[4][7], "]", "[", P2_B[5][7], "]", "[", P2_B[6][7], "]", "[", P2_B[7][7], "]", "[", P2_B[8][7], "]")
            print("8  ", "[", P2_B[0][8], "]", "[", P2_B[1][8], "]", "[", P2_B[2][8], "]", "[", P2_B[3][8], "]", "[", P2_B[4][8], "]", "[", P2_B[5][8], "]", "[", P2_B[6][8], "]", "[", P2_B[7][8], "]", "[", P2_B[8][8], "]")
            print(" ")
    elif mode == 2:
        print("Y/X   0     1     2     3     4     5     6     7     8")
        print("0  ", "[", P1_B[0][0], "]", "[", P1_B[1][0], "]", "[", P1_B[2][0], "]", "[", P1_B[3][0], "]", "[", P1_B[4][0], "]", "[", P1_B[5][0], "]", "[", P1_B[6][0], "]", "[", P1_B[7][0], "]", "[", P1_B[8][0], "]")
        print("1  ", "[", P1_B[0][1], "]", "[", P1_B[1][1], "]", "[", P1_B[2][1], "]", "[", P1_B[3][1], "]", "[", P1_B[4][1], "]", "[", P1_B[5][1], "]", "[", P1_B[6][1], "]", "[", P1_B[7][1], "]", "[", P1_B[8][1], "]")
        print("2  ", "[", P1_B[0][2], "]", "[", P1_B[1][2], "]", "[", P1_B[2][2], "]", "[", P1_B[3][2], "]", "[", P1_B[4][2], "]", "[", P1_B[5][2], "]", "[", P1_B[6][2], "]", "[", P1_B[7][2], "]", "[", P1_B[8][2], "]")
        print("3  ", "[", P1_B[0][3], "]", "[", P1_B[1][3], "]", "[", P1_B[2][3], "]", "[", P1_B[3][3], "]", "[", P1_B[4][3], "]", "[", P1_B[5][3], "]", "[", P1_B[6][3], "]", "[", P1_B[7][3], "]", "[", P1_B[8][3], "]")
        print("4  ", "[", P1_B[0][4], "]", "[", P1_B[1][4], "]", "[", P1_B[2][4], "]", "[", P1_B[3][4], "]", "[", P1_B[4][4], "]", "[", P1_B[5][4], "]", "[", P1_B[6][4], "]", "[", P1_B[7][4], "]", "[", P1_B[8][4], "]")
        print("5  ", "[", P1_B[0][5], "]", "[", P1_B[1][5], "]", "[", P1_B[2][5], "]", "[", P1_B[3][5], "]", "[", P1_B[4][5], "]", "[", P1_B[5][5], "]", "[", P1_B[6][5], "]", "[", P1_B[7][5], "]", "[", P1_B[8][5], "]")
        print("6  ", "[", P1_B[0][6], "]", "[", P1_B[1][6], "]", "[", P1_B[2][6], "]", "[", P1_B[3][6], "]", "[", P1_B[4][6], "]", "[", P1_B[5][6], "]", "[", P1_B[6][6], "]", "[", P1_B[7][6], "]", "[", P1_B[8][6], "]")
        print("7  ", "[", P1_B[0][7], "]", "[", P1_B[1][7], "]", "[", P1_B[2][7], "]", "[", P1_B[3][7], "]", "[", P1_B[4][7], "]", "[", P1_B[5][7], "]", "[", P1_B[6][7], "]", "[", P1_B[7][7], "]", "[", P1_B[8][7], "]")
        print("8  ", "[", P1_B[0][8], "]", "[", P1_B[1][8], "]", "[", P1_B[2][8], "]", "[", P1_B[3][8], "]", "[", P1_B[4][8], "]", "[", P1_B[5][8], "]", "[", P1_B[6][8], "]", "[", P1_B[7][8], "]", "[", P1_B[8][8], "]")
        print("Player: P1 Board")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~SEA~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Player: Computer Board")
        print("Y/X   0     1     2     3     4     5     6     7     8")
        print("0  ", "[", P2_S[0][0], "]", "[", P2_S[1][0], "]", "[", P2_S[2][0], "]", "[", P2_S[3][0], "]", "[", P2_S[4][0], "]", "[", P2_S[5][0], "]", "[", P2_S[6][0], "]", "[", P2_S[7][0], "]", "[", P2_S[8][0], "]")
        print("1  ", "[", P2_S[0][1], "]", "[", P2_S[1][1], "]", "[", P2_S[2][1], "]", "[", P2_S[3][1], "]", "[", P2_S[4][1], "]", "[", P2_S[5][1], "]", "[", P2_S[6][1], "]", "[", P2_S[7][1], "]", "[", P2_S[8][1], "]")
        print("2  ", "[", P2_S[0][2], "]", "[", P2_S[1][2], "]", "[", P2_S[2][2], "]", "[", P2_S[3][2], "]", "[", P2_S[4][2], "]", "[", P2_S[5][2], "]", "[", P2_S[6][2], "]", "[", P2_S[7][2], "]", "[", P2_S[8][2], "]")
        print("3  ", "[", P2_S[0][3], "]", "[", P2_S[1][3], "]", "[", P2_S[2][3], "]", "[", P2_S[3][3], "]", "[", P2_S[4][3], "]", "[", P2_S[5][3], "]", "[", P2_S[6][3], "]", "[", P2_S[7][3], "]", "[", P2_S[8][3], "]")
        print("4  ", "[", P2_S[0][4], "]", "[", P2_S[1][4], "]", "[", P2_S[2][4], "]", "[", P2_S[3][4], "]", "[", P2_S[4][4], "]", "[", P2_S[5][4], "]", "[", P2_S[6][4], "]", "[", P2_S[7][4], "]", "[", P2_S[8][4], "]")
        print("5  ", "[", P2_S[0][5], "]", "[", P2_S[1][5], "]", "[", P2_S[2][5], "]", "[", P2_S[3][5], "]", "[", P2_S[4][5], "]", "[", P2_S[5][5], "]", "[", P2_S[6][5], "]", "[", P2_S[7][5], "]", "[", P2_S[8][5], "]")
        print("6  ", "[", P2_S[0][6], "]", "[", P2_S[1][6], "]", "[", P2_S[2][6], "]", "[", P2_S[3][6], "]", "[", P2_S[4][6], "]", "[", P2_S[5][6], "]", "[", P2_S[6][6], "]", "[", P2_S[7][6], "]", "[", P2_S[8][6], "]")
        print("7  ", "[", P2_S[0][7], "]", "[", P2_S[1][7], "]", "[", P2_S[2][7], "]", "[", P2_S[3][7], "]", "[", P2_S[4][7], "]", "[", P2_S[5][7], "]", "[", P2_S[6][7], "]", "[", P2_S[7][7], "]", "[", P2_S[8][7], "]")
        print("8  ", "[", P2_S[0][8], "]", "[", P2_S[1][8], "]", "[", P2_S[2][8], "]", "[", P2_S[3][8], "]", "[", P2_S[4][8], "]", "[", P2_S[5][8], "]", "[", P2_S[6][8], "]", "[", P2_S[7][8], "]", "[", P2_S[8][8], "]")
        print(" ")
def retry():
    print("System: Please try again")
def debug():
    global show_state
    if keep_showing_state == True:
        state()
def state():
    global RAM
    global X
    global Y
    global X_R
    global Y_R
    global ans
    global test
    global type_error
    global mode
    global ship_H
    global ship_S
    global ship_H_R
    global ship_S_R
    global target
    global keep_showing_state
    global total
    global P
    global i
    global P1S
    global P2S
    global P1S1_HP
    global P2S1_HP
    global P1S2_HP
    global P2S2_HP
    global P1S3_HP
    global P2S3_HP
    global P1S4_HP
    global P2S4_HP
    print("")
    print("//////////STATE//////////STATE//////////STATE////////////////////STATE//////////STATE//////////")
    print("RAM:",RAM,type(RAM))
    print("X:",X ,type(X))
    print("Y:",Y,type(Y))
    print("X_R:",X_R,type(X_R))
    print("Y_R:",Y_R,type(Y_R))
    print("ans:",ans,type(ans))
    print("test:",test,type(test))
    print("type_error:",type_error,type(type_error))
    print("mode:",mode,type(mode))
    print("ship_H:",ship_H,type(ship_H))
    print("ship_S:",ship_S,type(ship_S))
    print("ship_H_R:",ship_H_R,type(ship_H_R))
    print("ship_S_R:",ship_S_R,type(ship_S_R))
    print("target:",target,type(target))
    print("keep_showing_state:",keep_showing_state,type(keep_showing_state))
    print("total:",total,type(total))
    print("P:",P,type(P))
    print("i:",i,type(i))
    print("P1S:",P1S,type(P1S))
    print("P2S:",P2S,type(P2S))
    print("P1S1_HP:",P1S1_HP,type(P1S1_HP))
    print("P2S1_HP:",P2S1_HP,type(P2S1_HP))
    print("P1S2_HP:",P1S2_HP,type(P2S2_HP))
    print("P2S2_HP:",P2S2_HP,type(P2S2_HP))
    print("P1S3_HP:",P1S3_HP,type(P1S3_HP))
    print("P2S3_HP:",P2S3_HP,type(P2S3_HP))
    print("P1S4_HP:",P1S4_HP,type(P1S4_HP))
    print("P2S4_HP:",P2S4_HP,type(P2S4_HP))
    print("//////////STATE//////////STATE//////////STATE////////////////////STATE//////////STATE//////////")
    time.sleep(3)
def ready_retry(Print):
    global i
    global type_error
    type_error=True
    i=i-1
    if Print == True:
        print("System: Out of bounds")
        Print=False
    retry()
    ready()

import sys
import time
import random
global RAM
global X
global Y
global X_R
global Y_R
global ans
global test
global type_error
global mode
global ship_H
global ship_S
global ship_H_R
global ship_S_R
global target
global keep_showing_state
global total
global P
global i
global P1_B
global P1_S
global P2_B
global P2_S
global P1S
global P2S
global P1S1_HP
global P2S1_HP
global P1S2_HP
global P2S2_HP
global P1S3_HP
global P2S3_HP
global P1S4_HP
global P2S4_HP
P1_B=[[" "] * 9 for _ in range(9)]
P1_S=[[" "] * 9 for _ in range(9)]
P2_B=[[" "] * 9 for _ in range(9)]
P2_S=[[" "] * 9 for _ in range(9)]
RAM=[" "]*2
X=None
Y=None
X_R=None
Y_R=None
ans=None
test=False
type_error=False
mode=None
ship_H=False
ship_S=False
ship_H_R=False
ship_S_R=False
target=False
keep_showing_state=False
total=4
P=1
i=0
P1S=4
P2S=4
P1S1_HP=1
P2S1_HP=1
P1S2_HP=2
P2S2_HP=2
P1S3_HP=3
P2S3_HP=3
P1S4_HP=4
P2S4_HP=4
print("System: Battleships is a game for two players.")
time.sleep(1)
print("System: Each player places four ships on a board but does not reveal their location to their opponent.")
time.sleep(1)
print("System: Each ship occupies one or more adjacent squares either horizontally or vertically.")
time.sleep(1)
print("System: Each player takes it in turn to pick a grid reference.")
time.sleep(1)
print("System: The player scores a hit if the number matches a space occupied by a ship, or a miss if it does not.")
time.sleep(1)
print("System: If the player scores a hit, it will show 'O' on the oposite player board.")
time.sleep(1)
print("System: If the player miss a hit, it will show 'X' on the oposite player board.")
time.sleep(1)
print("System: The player to sink all their opponents ships first wins.")
time.sleep(1)
while ans != "1" and ans != "2":
    ans=input("System: Please select the game mode, 1 for player vs player, 2 for player vs AI:")
    if ans == "1":
        print("System: Player vs Player mode selected")
        mode=1
    elif ans == "2":
        print("System: Player vs Computer mode selected")
        mode=2
    else:
        print("System: Invalid input, please try again")
time.sleep(0.5)
try:
    ans=input("System: Press enter to start.")
    if ans == "/test":
        test=True
        total=3
    elif ans == "/quit":
        sys.exit()
    elif ans == "/state on":
        keep_showing_state=True
    elif ans == "/state off":
        keep_showing_state=False
except:
    print("Error, please restart the game")
    time.sleep(1)
    sys.exit()
P1S=total
P2S=total
time.sleep(0.5)
print("System: Player1 round")
time.sleep(0.5)
ready()
