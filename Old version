def Game():
    global P1Y1_B
    global P1Y2_B
    global P1Y3_B
    global P1Y4_B
    global P1Y5_B
    global P1Y6_B
    global P1Y7_B
    global P1Y8_B
    global P1Y9_B
    global P2Y1_B
    global P2Y2_B
    global P2Y3_B
    global P2Y4_B
    global P2Y5_B
    global P2Y6_B
    global P2Y7_B
    global P2Y8_B
    global P2Y9_B
    global P2Y1_S
    global P2Y2_S
    global P2Y3_S
    global P2Y4_S
    global P2Y5_S
    global P2Y6_S
    global P2Y7_S
    global P2Y8_S
    global P2Y9_S
    global X
    global Y
    global X_R
    global Y_R
    global ans
    global test
    global back
    global back2
    global debug
    global ship_H
    global ship_S
    global ship_H_R
    global ship_S_R
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
    time.sleep(1)
    if P == 1:
        if back == False:
            print("System: Player1 round")
            time.sleep(0.5)
            board()
        else:
            back=False
    elif P == 2:
        if back == False:
            print("System: Player2 round")
            time.sleep(0.5)
        else:
            AI()
            back=False
    time.sleep(0.5)
    if P == 1:
        print("System: Please enter the position of the box you want to hit")
        if test == True:
            X=random.randint(0,8)
            Y=random.randint(0,8)
            X=X+1
            Y=Y+1
            time.sleep(1)
            print("System: X:", X)
            print("System: Y:", Y)
        else:
            X=input("System: X:")
            Y=input("System: Y:")
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
            Y=10
            Y=int(Y)
        if Y > 9 or Y == 0 or X > 9 or X == 0:
            back=True
            print("System: Out of bounds")
            retry()
            Game()
    elif P == 2:
        print("System: Player 2 thinking...")
        AI()
    time.sleep(0.01)
    mode()
    if P == 1:
        if Y == 1:
            if P2Y1_B[X] == " ":
                P2Y1_S[X]="X"
            elif not P2Y1_S[X] == " ":
                mode()
                back=True
                retry()
                Game()
            elif P2Y1_B[X] == "1":
                P2Y1_S[X]="O"
                P2S1_HP=P2S1_HP-1
                P2S=P2S-1
                ship_H=True
                ship_S=True
            elif P2Y1_B[X] == "2":
                P2Y1_S[X]="O"
                P2S2_HP=P2S2_HP-1
                ship_H=True
                if P2S2_HP == 0:
                    P2S=P2S-1
                    ship_S=True
            elif P2Y1_B[X] == "3":
                P2Y1_S[X]="O"
                P2S3_HP=P2S3_HP-1
                ship_H=True
                if P2S3_HP == 0:
                    P2S=P2S-1
                    ship_S=True
            elif P2Y1_B[X] == "4":
                P2Y1_S[X]="O"
                P2S4_HP=P2S4_HP-1
                ship_H=True
                if P2S4_HP == 0:
                    P2S=P2S-1
                    ship_S=True
        elif Y == 2:
            if P2Y2_B[X] == " ":
                P2Y2_S[X]="X"
            elif not P2Y2_S[X] == " ":
                mode()
                back=True
                retry()
                Game()
            elif P2Y2_B[X] == "1":
                P2Y2_S[X]="O"
                P2S1_HP=P2S1_HP-1
                P2S=P2S-1
                ship_H=True
                ship_S=True
            elif P2Y2_B[X] == "2":
                P2Y2_S[X]="O"
                P2S2_HP=P2S2_HP-1
                ship_H=True
                if P2S2_HP == 0:
                    P2S=P2S-1
                    ship_S=True
            elif P2Y2_B[X] == "3":
                P2Y2_S[X]="O"
                P2S3_HP=P2S3_HP-1
                ship_H=True
                if P2S3_HP == 0:
                    P2S=P2S-1
                    ship_S=True
            elif P2Y2_B[X] == "4":
                P2Y2_S[X]="O"
                P2S4_HP=P2S4_HP-1
                ship_H=True
                if P2S4_HP == 0:
                    P2S=P2S-1
                    ship_S=True
        elif Y == 3:
            if P2Y3_B[X] == " ":
                P2Y3_S[X]="X"
            elif not P2Y3_S[X] == " ":
                mode()
                back=True
                retry()
                Game()
            elif P2Y3_B[X] == "1":
                P2Y3_S[X]="O"
                P2S1_HP=P2S1_HP-1
                P2S=P2S-1
                ship_H=True
                ship_S=True
            elif P2Y3_B[X] == "2":
                P2Y3_S[X]="O"
                P2S2_HP=P2S2_HP-1
                ship_H=True
                if P2S2_HP == 0:
                    P2S=P2S-1
                    ship_S=True
            elif P2Y3_B[X] == "3":
                P2Y3_S[X]="O"
                P2S3_HP=P2S3_HP-1
                ship_H=True
                if P2S3_HP == 0:
                    P2S=P2S-1
                    ship_S=True
            elif P2Y3_B[X] == "4":
                P2Y3_S[X]="O"
                P2S4_HP=P2S4_HP-1
                ship_H=True
                if P2S4_HP == 0:
                    P2S=P2S-1
                    ship_S=True
        elif Y == 4:
            if P2Y4_B[X] == " ":
                P2Y4_S[X]="X"
            elif not P2Y4_S[X] == " ":
                mode()
                back=True
                retry()
                Game()
            elif P2Y4_B[X] == "1":
                P2Y4_S[X]="O"
                P2S1_HP=P2S1_HP-1
                P2S=P2S-1
                ship_H=True
                ship_S=True
            elif P2Y4_B[X] == "2":
                P2Y4_S[X]="O"
                P2S2_HP=P2S2_HP-1
                ship_H=True
                if P2S2_HP == 0:
                    P2S=P2S-1
                    ship_S=True
            elif P2Y4_B[X] == "3":
                P2Y4_S[X]="O"
                P2S3_HP=P2S3_HP-1
                ship_H=True
                if P2S3_HP == 0:
                    P2S=P2S-1
                    ship_S=True
            elif P2Y4_B[X] == "4":
                P2Y4_S[X]="O"
                P2S4_HP=P2S4_HP-1
                ship_H=True
                if P2S4_HP == 0:
                    P2S=P2S-1
                    ship_S=True
        elif Y == 5:
            if P2Y5_B[X] == " ":
                P2Y5_S[X]="X"
            elif not P2Y5_S[X] == " ":
                mode()
                back=True
                retry()
                Game()
            elif P2Y5_B[X] == "1":
                P2Y5_S[X]="O"
                P2S1_HP=P2S1_HP-1
                P2S=P2S-1
                ship_H=True
                ship_S=True
            elif P2Y5_B[X] == "2":
                P2Y5_S[X]="O"
                P2S2_HP=P2S2_HP-1
                ship_H=True
                if P2S2_HP == 0:
                    P2S=P2S-1
                    ship_S=True
            elif P2Y5_B[X] == "3":
                P2Y5_S[X]="O"
                P2S3_HP=P2S3_HP-1
                ship_H=True
                if P2S3_HP == 0:
                    P2S=P2S-1
                    ship_S=True
            elif P2Y5_B[X] == "4":
                P2Y5_S[X]="O"
                P2S4_HP=P2S4_HP-1
                ship_H=True
                if P2S4_HP == 0:
                    P2S=P2S-1
                    ship_S=True
        elif Y == 6:
            if P2Y6_B[X] == " ":
                P2Y6_S[X]="X"
            elif not P2Y6_S[X] == " ":
                mode()
                back=True
                retry()
                Game()
            elif P2Y6_B[X] == "1":
                P2Y6_S[X]="O"
                P2S1_HP=P2S1_HP-1
                P2S=P2S-1
                ship_H=True
                ship_S=True
            elif P2Y6_B[X] == "2":
                P2Y6_S[X]="O"
                P2S2_HP=P2S2_HP-1
                ship_H=True
                if P2S2_HP == 0:
                    P2S=P2S-1
                    ship_S=True
            elif P2Y6_B[X] == "3":
                P2Y6_S[X]="O"
                P2S3_HP=P2S3_HP-1
                ship_H=True
                if P2S3_HP == 0:
                    P2S=P2S-1
                    ship_S=True
            elif P2Y6_B[X] == "4":
                P2Y6_S[X]="O"
                P2S4_HP=P2S4_HP-1
                ship_H=True
                if P2S4_HP == 0:
                    P2S=P2S-1
                    ship_S=True
        elif Y == 7:
            if P2Y7_B[X] == " ":
                P2Y7_S[X]="X"
            elif not P2Y7_S[X] == " ":
                mode()
                back=True
                retry()
                Game()
            elif P2Y7_B[X] == "1":
                P2Y7_S[X]="O"
                P2S1_HP=P2S1_HP-1
                P2S=P2S-1
                ship_H=True
                ship_S=True
            elif P2Y7_B[X] == "2":
                P2Y7_S[X]="O"
                P2S2_HP=P2S2_HP-1
                ship_H=True
                if P2S2_HP == 0:
                    P2S=P2S-1
                    ship_S=True
            elif P2Y7_B[X] == "3":
                P2Y7_S[X]="O"
                P2S3_HP=P2S3_HP-1
                ship_H=True
                if P2S3_HP == 0:
                    P2S=P2S-1
                    ship_S=True
            elif P2Y7_B[X] == "4":
                P2Y7_S[X]="O"
                P2S4_HP=P2S4_HP-1
                ship_H=True
                if P2S4_HP == 0:
                    P2S=P2S-1
                    ship_S=True
        elif Y == 8:
            if P2Y8_B[X] == " ":
                P2Y8_S[X]="X"
            elif not P2Y8_S[X] == " ":
                mode()
                back=True
                retry()
                Game()
            elif P2Y8_B[X] == "1":
                P2Y8_S[X]="O"
                P2S1_HP=P2S1_HP-1
                P2S=P2S-1
                ship_H=True
                ship_S=True
            elif P2Y8_B[X] == "2":
                P2Y8_S[X]="O"
                P2S2_HP=P2S2_HP-1
                ship_H=True
                if P2S2_HP == 0:
                    P2S=P2S-1
                    ship_S=True
            elif P2Y8_B[X] == "3":
                P2Y8_S[X]="O"
                P2S3_HP=P2S3_HP-1
                ship_H=True
                if P2S3_HP == 0:
                    P2S=P2S-1
                    ship_S=True
            elif P2Y8_B[X] == "4":
                P2Y8_S[X]="O"
                P2S4_HP=P2S4_HP-1
                ship_H=True
                if P2S4_HP == 0:
                    P2S=P2S-1
                    ship_S=True
        elif Y == 9:
            if P2Y9_B[X] == " ":
                P2Y9_S[X]="X"
            elif not P2Y9_S[X] == " ":
                mode()
                back=True
                retry()
                Game()
            elif P2Y9_B[X] == "1":
                P2Y9_S[X]="O"
                P2S1_HP=P2S1_HP-1
                P2S=P2S-1
                ship_H=True
                ship_S=True
            elif P2Y9_B[X] == "2":
                P2Y9_S[X]="O"
                P2S2_HP=P2S2_HP-1
                ship_H=True
                if P2S2_HP == 0:
                    P2S=P2S-1
                    ship_S=True
            elif P2Y9_B[X] == "3":
                P2Y9_S[X]="O"
                P2S3_HP=P2S3_HP-1
                ship_H=True
                if P2S3_HP == 0:
                    P2S=P2S-1
                    ship_S=True
            elif P2Y9_B[X] == "4":
                P2Y9_S[X]="O"
                P2S4_HP=P2S4_HP-1
                ship_H=True
                if P2S4_HP == 0:
                    P2S=P2S-1
                    ship_S=True
    elif P == 2:
        X_R=X
        Y_R=Y
        if Y == 1:
            if P1Y1_B[X] == " ":
                P1Y1_B[X]="X"
            elif not P1Y1_B[X] == " " and not P1Y1_B[X] == "1" and not P1Y1_B[X] == "2" and not P1Y1_B[X] == "3" and not P1Y1_B[X] == "4":
                mode()
                back=True
                Game()
            elif P1Y1_B[X] == "1":
                P1Y1_B[X]="O"
                P1S1_HP=P1S1_HP-1
                P1S=P1S-1
                ship_H=True
                ship_S=True
            elif P1Y1_B[X] == "2":
                P1Y1_B[X]="O"
                P1S2_HP=P1S2_HP-1
                ship_H=True
                if P1S2_HP == 0:
                    P1S=P1S-1
                    ship_S=True
            elif P1Y1_B[X] == "3":
                P1Y1_B[X]="O"
                P1S3_HP=P1S3_HP-1
                ship_H=True
                if P1S3_HP == 0:
                    P1S=P1S-1
                    ship_S=True
            elif P1Y1_B[X] == "4":
                P1Y1_B[X]="O"
                P1S4_HP=P1S4_HP-1
                ship_H=True
                if P1S4_HP == 0:
                    P1S=P1S-1
                    ship_S=True
        elif Y == 2:
            if P1Y2_B[X] == " ":
                P1Y2_B[X]="X"
            elif not P1Y2_B[X] == " " and not P1Y2_B[X] == "1" and not P1Y2_B[X] == "2" and not P1Y2_B[X] == "3" and not P1Y2_B[X] == "4":
                mode()
                back=True
                Game()
            elif P1Y2_B[X] == "1":
                P1Y2_B[X]="O"
                P1S1_HP=P1S1_HP-1
                P1S=P1S-1
                ship_H=True
                ship_S=True
            elif P1Y2_B[X] == "2":
                P1Y2_B[X]="O"
                P1S2_HP=P1S2_HP-1
                ship_H=True
                if P1S2_HP == 0:
                    P1S=P1S-1
                    ship_S=True
            elif P1Y2_B[X] == "3":
                P1Y2_B[X]="O"
                P1S3_HP=P1S3_HP-1
                ship_H=True
                if P1S3_HP == 0:
                    P1S=P1S-1
                    ship_S=True
            elif P1Y2_B[X] == "4":
                P1Y2_B[X]="O"
                P1S4_HP=P1S4_HP-1
                ship_H=True
                if P1S4_HP == 0:
                    P1S=P1S-1
                    ship_S=True
        elif Y == 3:
            if P1Y3_B[X] == " ":
                P1Y3_B[X]="X"
            elif not P1Y3_B[X] == " " and not P1Y3_B[X] == "1" and not P1Y3_B[X] == "2" and not P1Y3_B[X] == "3" and not P1Y3_B[X] == "4":
                mode()
                back=True
                Game()
            elif P1Y3_B[X] == "1":
                P1Y3_B[X]="O"
                P1S1_HP=P1S1_HP-1
                P1S=P1S-1
                ship_H=True
                ship_S=True
            elif P1Y3_B[X] == "2":
                P1Y3_B[X]="O"
                P1S2_HP=P1S2_HP-1
                ship_H=True
                if P1S2_HP == 0:
                    P1S=P1S-1
                    ship_S=True
            elif P1Y3_B[X] == "3":
                P1Y3_B[X]="O"
                P1S3_HP=P1S3_HP-1
                ship_H=True
                if P1S3_HP == 0:
                    P1S=P1S-1
                    ship_S=True
            elif P1Y3_B[X] == "4":
                P1Y3_B[X]="O"
                P1S4_HP=P1S4_HP-1
                ship_H=True
                if P1S4_HP == 0:
                    P1S=P1S-1
                    ship_S=True
        elif Y == 4:
            if P1Y4_B[X] == " ":
                P1Y4_B[X]="X"
            elif not P1Y4_B[X] == " " and not P1Y4_B[X] == "1" and not P1Y4_B[X] == "2" and not P1Y4_B[X] == "3" and not P1Y4_B[X] == "4":
                mode()
                back=True
                Game()
            elif P1Y4_B[X] == "1":
                P1Y4_B[X]="O"
                P1S1_HP=P1S1_HP-1
                P1S=P1S-1
                ship_H=True
                ship_S=True
            elif P1Y4_B[X] == "2":
                P1Y4_B[X]="O"
                P1S2_HP=P1S2_HP-1
                ship_H=True
                if P1S2_HP == 0:
                    P1S=P1S-1
                    ship_S=True
            elif P1Y4_B[X] == "3":
                P1Y4_B[X]="O"
                P1S3_HP=P1S3_HP-1
                ship_H=True
                if P1S3_HP == 0:
                    P1S=P1S-1
                    ship_S=True
            elif P1Y4_B[X] == "4":
                P1Y4_B[X]="O"
                P1S4_HP=P1S4_HP-1
                ship_H=True
                if P1S4_HP == 0:
                    P1S=P1S-1
                    ship_S=True
        elif Y == 5:
            if P1Y5_B[X] == " ":
                P1Y5_B[X]="X"
            elif not P1Y5_B[X] == " " and not P1Y5_B[X] == "1" and not P1Y5_B[X] == "2" and not P1Y5_B[X] == "3" and not P1Y5_B[X] == "4":
                mode()
                back=True
                Game()
            elif P1Y5_B[X] == "1":
                P1Y5_B[X]="O"
                P1S1_HP=P1S1_HP-1
                P1S=P1S-1
                ship_H=True
                ship_S=True
            elif P1Y5_B[X] == "2":
                P1Y5_B[X]="O"
                P1S2_HP=P1S2_HP-1
                ship_H=True
                if P1S2_HP == 0:
                    P1S=P1S-1
                    ship_S=True
            elif P1Y5_B[X] == "3":
                P1Y5_B[X]="O"
                P1S3_HP=P1S3_HP-1
                ship_H=True
                if P1S3_HP == 0:
                    P1S=P1S-1
                    ship_S=True
            elif P1Y5_B[X] == "4":
                P1Y5_B[X]="O"
                P1S4_HP=P1S4_HP-1
                ship_H=True
                if P1S4_HP == 0:
                    P1S=P1S-1
                    ship_S=True
        elif Y == 6:
            if P1Y6_B[X] == " ":
                P1Y6_B[X]="X"
            elif not P1Y6_B[X] == " " and not P1Y6_B[X] == "1" and not P1Y6_B[X] == "2" and not P1Y6_B[X] == "3" and not P1Y6_B[X] == "4":
                mode()
                back=True
                Game()
            elif P1Y6_B[X] == "1":
                P1Y6_B[X]="O"
                P1S1_HP=P1S1_HP-1
                P1S=P1S-1
                ship_H=True
                ship_S=True
            elif P1Y6_B[X] == "2":
                P1Y6_B[X]="O"
                P1S2_HP=P1S2_HP-1
                ship_H=True
                if P1S2_HP == 0:
                    P1S=P1S-1
                    ship_S=True
            elif P1Y6_B[X] == "3":
                P1Y6_B[X]="O"
                P1S3_HP=P1S3_HP-1
                ship_H=True
                if P1S3_HP == 0:
                    P1S=P1S-1
                    ship_S=True
            elif P1Y6_B[X] == "4":
                P1Y6_B[X]="O"
                P1S4_HP=P1S4_HP-1
                ship_H=True
                if P1S4_HP == 0:
                    P1S=P1S-1
                    ship_S=True
        elif Y == 7:
            if P1Y7_B[X] == " ":
                P1Y7_B[X]="X"
            elif not P1Y7_B[X] == " " and not P1Y7_B[X] == "1" and not P1Y7_B[X] == "2" and not P1Y7_B[X] == "3" and not P1Y7_B[X] == "4":
                mode()
                back=True
                Game()
            elif P1Y7_B[X] == "1":
                P1Y7_B[X]="O"
                P1S1_HP=P1S1_HP-1
                P1S=P1S-1
                ship_H=True
                ship_S=True
            elif P1Y7_B[X] == "2":
                P1Y7_B[X]="O"
                P1S2_HP=P1S2_HP-1
                ship_H=True
                if P1S2_HP == 0:
                    P1S=P1S-1
                    ship_S=True
            elif P1Y7_B[X] == "3":
                P1Y7_B[X]="O"
                P1S3_HP=P1S3_HP-1
                ship_H=True
                if P1S3_HP == 0:
                    P1S=P1S-1
                    ship_S=True
            elif P1Y7_B[X] == "4":
                P1Y7_B[X]="O"
                P1S4_HP=P1S4_HP-1
                ship_H=True
                if P1S4_HP == 0:
                    P1S=P1S-1
                    ship_S=True
        elif Y == 8:
            if P1Y8_B[X] == " ":
                P1Y8_B[X]="X"
            elif not P1Y8_B[X] == " " and not P1Y8_B[X] == "1" and not P1Y8_B[X] == "2" and not P1Y8_B[X] == "3" and not P1Y8_B[X] == "4":
                mode()
                back=True
                Game()
            elif P1Y8_B[X] == "1":
                P1Y8_B[X]="O"
                P1S1_HP=P1S1_HP-1
                P1S=P1S-1
                ship_H=True
                ship_S=True
            elif P1Y8_B[X] == "2":
                P1Y8_B[X]="O"
                P1S2_HP=P1S2_HP-1
                ship_H=True
                if P1S2_HP == 0:
                    P1S=P1S-1
                    ship_S=True
            elif P1Y8_B[X] == "3":
                P1Y8_B[X]="O"
                P1S3_HP=P1S3_HP-1
                ship_H=True
                if P1S3_HP == 0:
                    P1S=P1S-1
                    ship_S=True
            elif P1Y8_B[X] == "4":
                P1Y8_B[X]="O"
                P1S4_HP=P1S4_HP-1
                ship_H=True
                if P1S4_HP == 0:
                    P1S=P1S-1
                    ship_S=True
        elif Y == 9:
            if P1Y9_B[X] == " ":
                P1Y9_B[X]="X"
            elif not P1Y9_B[X] == " " and not P1Y9_B[X] == "1" and not P1Y9_B[X] == "2" and not P1Y9_B[X] == "3" and not P1Y9_B[X] == "4":
                mode()
                back=True
                Game()
            elif P1Y9_B[X] == "1":
                P1Y9_B[X]="O"
                P1S1_HP=P1S1_HP-1
                P1S=P1S-1
                ship_H=True
                ship_S=True
            elif P1Y9_B[X] == "2":
                P1Y9_B[X]="O"
                P1S2_HP=P1S2_HP-1
                ship_H=True
                if P1S2_HP == 0:
                    P1S=P1S-1
                    ship_S=True
            elif P1Y9_B[X] == "3":
                P1Y9_B[X]="O"
                P1S3_HP=P1S3_HP-1
                ship_H=True
                if P1S3_HP == 0:
                    P1S=P1S-1
                    ship_S=True
            elif P1Y9_B[X] == "4":
                P1Y9_B[X]="O"
                P1S4_HP=P1S4_HP-1
                ship_H=True
                if P1S4_HP == 0:
                    P1S=P1S-1
                    ship_S=True
    time.sleep(0.01)
    mode()
    if ship_H == True:
        ship_H=False
        if P == 1:
            print("System: Player2 ship got hit")
        elif P == 2:
            ship_H_R=True
            print("System: Player1 ship got hit")
    time.sleep(0.01)
    if ship_S == True:
        ship_S=False
        if P == 1:
            print("System: Player2 ship got sink")
        elif P == 2:
            ship_S_R=True
            print("System: Player1 ship got sink")
    change()
def AI():
    global RAM
    global P1Y1_B
    global P1Y2_B
    global P1Y3_B
    global P1Y4_B
    global P1Y5_B
    global P1Y6_B
    global P1Y7_B
    global P1Y8_B
    global P1Y9_B
    global target
    global X
    global Y
    global X_R #last fired X
    global Y_R #last fired Y
    global ans
    global ship_H_R #ship hit register
    global ship_S_R #ship sink register
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
    X=int(X)
    Y=int(Y)
def change():
    global P1S
    global P2S
    global P
    if P == 1:
        P=2
    elif P == 2:
        P=1
    time.sleep(0.01)
    if P1S == 0:
        print("System: Player2 Win!")
        end()
    elif P2S == 0:
        print("System: Player1 Win!")
        end()
    else:
        print(" ")
        print("System: Player1 have", P1S, "ships remaining")
        print("System: Player2 have", P2S, "ships remaining")
        time.sleep(1)
        Game()
def end():
    global ans
    time.sleep(0.5)
    ans=input("System: press enter to end the progrem")
    sys.exit()
def ready():
    global P1Y1_B
    global P1Y2_B
    global P1Y3_B
    global P1Y4_B
    global P1Y5_B
    global P1Y6_B
    global P1Y7_B
    global P1Y8_B
    global P1Y9_B
    global P2Y1_S
    global P2Y2_S
    global P2Y3_S
    global P2Y4_S
    global P2Y5_S
    global P2Y6_S
    global P2Y7_S
    global P2Y8_S
    global P2Y9_S
    global X
    global Y
    global ans
    global test
    global back
    global back2
    global P
    global i
    global total
    while i < total:
        i=i+1
        if P == 1:
            if back == False:
                board()
            else:
                back=False
            print("System: Please enter your", i, "ship's top left position")
            if test == True:
                X=random.randint(0,8)
                Y=random.randint(0,8)
                X=X+1
                Y=Y+1
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
            if Y > 9 or Y == 0 or X > 9 or X == 0:
                back=True
                i=i-1
                print("System: Out of bounds")
                retry()
                ready()
        elif P == 2:
            X=random.randint(0,8)
            Y=random.randint(0,8)
            X=X+1
            Y=Y+1
        time.sleep(0.01)
        if P == 1:
            if i == 2:
                if X == 9:
                    i=i-1
                    back=True
                    print("System: Out of bounds")
                    retry()
                    ready()
            elif i == 3:
                if Y == 8 or Y == 9:
                    i=i-1
                    back=True
                    print("System: Out of bounds")
                    retry()
                    ready()
            elif i == 4:
                if X==7 or X == 8 or X == 9:
                    i=i-1
                    back=True
                    print("System: Out of bounds")
                    retry()
                    ready()
        elif P == 2:
            if i == 2:
                if X == 9:
                    X=random.randint(0,7)
                    X=X+1
            elif i == 3:
                if Y == 8 or Y == 9:
                    Y=random.randint(0,6)
                    Y=Y+1
            elif i == 4:
                if X==7 or X == 8 or X == 9:
                    X=random.randint(0,5)
                    X=X+1
        time.sleep(0.01)
        if P == 1:
            if Y == 1:
               if not P1Y1_B[X] == " ":
                    i=(i-1)
                    back=True
                    retry()
               else:
                    if i == 1:
                        P1Y1_B[X]="1"
                    elif i == 2:
                        P1Y1_B[X]="2"
                        X=X+1
                        if not P1Y1_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y1_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y1_B[X]="2"
                    elif i == 3:
                        P1Y1_B[X]="3"
                        if not P1Y2_B[X] == " ":
                            back=True
                            P1Y1_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y2_B[X]="3"
                        time.sleep(0.01)
                        if not P1Y3_B[X] == " ":
                            back=True
                            P1Y1_B[X]=" "
                            P1Y2_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y3_B[X]="3"
                    elif i == 4:
                        P1Y1_B[X]="4"
                        X=X+1
                        if not P1Y1_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y1_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y1_B[X]="4"
                        X=X+1
                        if not P1Y1_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y1_B[X]=" "
                            X=X-1
                            P1Y1_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y1_B[X]="4"
                        X=X+1
                        if not P1Y1_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y1_B[X]=" "
                            X=X-1
                            P1Y1_B[X]=" "
                            X=X-1
                            P1Y1_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y1_B[X]="4"
                            P=2
                            i=0
            elif Y == 2:
               if not P1Y2_B[X] == " ":
                    i=(i-1)
                    back=True
                    retry()
               else:
                    if i == 1:
                        P1Y2_B[X]="1"
                    elif i == 2:
                        P1Y2_B[X]="2"
                        X=X+1
                        if not P1Y2_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y2_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y2_B[X]="2"
                    elif i == 3:
                        P1Y2_B[X]="3"
                        if not P1Y3_B[X] == " ":
                            back=True
                            P1Y2_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y3_B[X]="3"
                        time.sleep(0.01)
                        if not P1Y4_B[X] == " ":
                            back=True
                            P1Y2_B[X]=" "
                            P1Y3_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y4_B[X]="3"
                    elif i == 4:
                        P1Y2_B[X]="4"
                        X=X+1
                        if not P1Y2_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y2_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y1_B[X]="4"
                        X=X+1
                        if not P1Y2_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y2_B[X]=" "
                            X=X-1
                            P1Y2_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y2_B[X]="4"
                        X=X+1
                        if not P1Y2_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y2_B[X]=" "
                            X=X-1
                            P1Y2_B[X]=" "
                            X=X-1
                            P1Y2_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y2_B[X]="4"
                            P=2
                            i=0
            elif Y == 3:
               if not P1Y3_B[X] == " ":
                    i=(i-1)
                    back=True
                    retry()
               else:
                    if i == 1:
                        P1Y3_B[X]="1"
                    elif i == 2:
                        P1Y3_B[X]="2"
                        X=X+1
                        if not P1Y3_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y3_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y3_B[X]="2"
                    elif i == 3:
                        P1Y3_B[X]="3"
                        if not P1Y4_B[X] == " ":
                            back=True
                            P1Y3_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y4_B[X]="3"
                        time.sleep(0.01)
                        if not P1Y5_B[X] == " ":
                            back=True
                            P1Y3_B[X]=" "
                            P1Y4_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y5_B[X]="3"
                    elif i == 4:
                        P1Y3_B[X]="4"
                        X=X+1
                        if not P1Y3_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y3_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y3_B[X]="4"
                        X=X+1
                        if not P1Y3_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y3_B[X]=" "
                            X=X-1
                            P1Y3_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y3_B[X]="4"
                        X=X+1
                        if not P1Y3_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y3_B[X]=" "
                            X=X-1
                            P1Y3_B[X]=" "
                            X=X-1
                            P1Y3_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y3_B[X]="4"
                            P=2
                            i=0
            elif Y == 4:
               if not P1Y4_B[X] == " ":
                    i=(i-1)
                    back=True
                    retry()
               else:
                    if i == 1:
                        P1Y4_B[X]="1"
                    elif i == 2:
                        P1Y4_B[X]="2"
                        X=X+1
                        if not P1Y4_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y4_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y4_B[X]="2"
                    elif i == 3:
                        P1Y4_B[X]="3"
                        if not P1Y5_B[X] == " ":
                            back=True
                            P1Y4_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y5_B[X]="3"
                        time.sleep(0.01)
                        if not P1Y6_B[X] == " ":
                            back=True
                            P1Y4_B[X]=" "
                            P1Y5_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y6_B[X]="3"
                    elif i == 4:
                        P1Y4_B[X]="4"
                        X=X+1
                        if not P1Y4_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y4_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y4_B[X]="4"
                        X=X+1
                        if not P1Y4_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y4_B[X]=" "
                            X=X-1
                            P1Y4_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y4_B[X]="4"
                        X=X+1
                        if not P1Y4_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y4_B[X]=" "
                            X=X-1
                            P1Y4_B[X]=" "
                            X=X-1
                            P1Y4_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y4_B[X]="4"
                            P=2
                            i=0
            elif Y == 5:
               if not P1Y5_B[X] == " ":
                    i=(i-1)
                    back=True
                    retry()
               else:
                    if i == 1:
                        P1Y5_B[X]="1"
                    elif i == 2:
                        P1Y5_B[X]="2"
                        X=X+1
                        if not P1Y5_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y5_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y5_B[X]="2"
                    elif i == 3:
                        P1Y5_B[X]="3"
                        if not P1Y6_B[X] == " ":
                            back=True
                            P1Y5_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y6_B[X]="3"
                        time.sleep(0.01)
                        if not P1Y7_B[X] == " ":
                            back=True
                            P1Y5_B[X]=" "
                            P1Y6_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y7_B[X]="3"
                    elif i == 4:
                        P1Y5_B[X]="4"
                        X=X+1
                        if not P1Y5_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y5_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y5_B[X]="4"
                        X=X+1
                        if not P1Y5_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y5_B[X]=" "
                            X=X-1
                            P1Y5_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y5_B[X]="4"
                        X=X+1
                        if not P1Y5_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y5_B[X]=" "
                            X=X-1
                            P1Y5_B[X]=" "
                            X=X-1
                            P1Y5_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y5_B[X]="4"
                            P=2
                            i=0
            elif Y == 6:
               if not P1Y6_B[X] == " ":
                    i=(i-1)
                    back=True
                    retry()
               else:
                    if i == 1:
                        P1Y6_B[X]="1"
                    elif i == 2:
                        P1Y6_B[X]="2"
                        X=X+1
                        if not P1Y6_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y6_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y6_B[X]="2"
                    elif i == 3:
                        P1Y6_B[X]="3"
                        if not P1Y7_B[X] == " ":
                            back=True
                            P1Y6_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y7_B[X]="3"
                        time.sleep(0.01)
                        if not P1Y8_B[X] == " ":
                            back=True
                            P1Y6_B[X]=" "
                            P1Y7_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y8_B[X]="3"
                    elif i == 4:
                        P1Y6_B[X]="4"
                        X=X+1
                        if not P1Y6_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y6_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y6_B[X]="4"
                        X=X+1
                        if not P1Y6_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y6_B[X]=" "
                            X=X-1
                            P1Y6_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y6_B[X]="4"
                        X=X+1
                        if not P1Y6_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y6_B[X]=" "
                            X=X-1
                            P1Y6_B[X]=" "
                            X=X-1
                            P1Y6_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y6_B[X]="4"
                            P=2
                            i=0
            elif Y == 7:
               if not P1Y7_B[X] == " ":
                    i=(i-1)
                    back=True
                    retry()
               else:
                    if i == 1:
                        P1Y7_B[X]="1"
                    elif i == 2:
                        P1Y7_B[X]="2"
                        X=X+1
                        if not P1Y7_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y8_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y7_B[X]="2"
                    elif i == 3:
                        P1Y7_B[X]="3"
                        if not P1Y8_B[X] == " ":
                            back=True
                            P1Y7_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y8_B[X]="3"
                        time.sleep(0.01)
                        if not P1Y9_B[X] == " ":
                            back=True
                            P1Y7_B[X]=" "
                            P1Y8_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y9_B[X]="3"
                    elif i == 4:
                        P1Y7_B[X]="4"
                        X=X+1
                        if not P1Y7_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y7_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y7_B[X]="4"
                        X=X+1
                        if not P1Y7_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y7_B[X]=" "
                            X=X-1
                            P1Y7_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y7_B[X]="4"
                        X=X+1
                        if not P1Y7_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y7_B[X]=" "
                            X=X-1
                            P1Y7_B[X]=" "
                            X=X-1
                            P1Y7_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y7_B[X]="4"
                            P=2
                            i=0
            elif Y == 8:
               if not P1Y8_B[X] == " ":
                    i=(i-1)
                    back=True
                    retry()
               else:
                    if i == 1:
                        P1Y8_B[X]="1"
                    elif i == 2:
                        P1Y8_B[X]="2"
                        X=X+1
                        if not P1Y8_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y8_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y8_B[X]="2"
                    elif i == 4:
                        P1Y8_B[X]="4"
                        X=X+1
                        if not P1Y8_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y8_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y8_B[X]="4"
                        X=X+1
                        if not P1Y8_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y8_B[X]=" "
                            X=X-1
                            P1Y8_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y8_B[X]="4"
                        X=X+1
                        if not P1Y8_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y8_B[X]=" "
                            X=X-1
                            P1Y8_B[X]=" "
                            X=X-1
                            P1Y8_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y8_B[X]="4"
                            P=2
                            i=0
            elif Y == 9:
               if not P1Y9_B[X] == " ":
                    i=(i-1)
                    back=True
                    retry()
               else:
                    if i == 1:
                        P1Y9_B[X]="1"
                    elif i == 2:
                        P1Y9_B[X]="2"
                        X=X+1
                        if not P1Y9_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y9_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y9_B[X]="2"
                    elif i == 4:
                        P1Y9_B[X]="4"
                        X=X+1
                        if not P1Y9_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y9_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y9_B[X]="4"
                        X=X+1
                        if not P1Y9_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y9_B[X]=" "
                            X=X-1
                            P1Y9_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y9_B[X]="4"
                        X=X+1
                        if not P1Y9_B[X] == " ":
                            back=True
                            X=X-1
                            P1Y9_B[X]=" "
                            X=X-1
                            P1Y9_B[X]=" "
                            X=X-1
                            P1Y9_B[X]=" "
                            i=(i-1)
                            retry()
                            ready()
                        else:
                            P1Y9_B[X]="4"
                            P=2
                            i=0
        elif P == 2:
            if Y == 1:
               if not P2Y1_B[X] == " ":
                    i=(i-1)
                    ready()
               else:
                    if i == 1:
                        P2Y1_B[X]="1"
                    elif i == 2:
                        P2Y1_B[X]="2"
                        X=X+1
                        if not P2Y1_B[X] == " ":
                            X=X-1
                            P2Y1_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y1_B[X]="2"
                    elif i == 3:
                        P2Y1_B[X]="3"
                        if not P2Y2_B[X] == " ":
                            P2Y1_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y2_B[X]="3"
                        time.sleep(0.01)
                        if not P2Y3_B[X] == " ":
                            P2Y1_B[X]=" "
                            P2Y2_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y3_B[X]="3"
                    elif i == 4:
                        P2Y1_B[X]="4"
                        X=X+1
                        if not P2Y1_B[X] == " ":
                            X=X-1
                            P2Y1_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y1_B[X]="4"
                        X=X+1
                        if not P2Y1_B[X] == " ":
                            X=X-1
                            P2Y1_B[X]=" "
                            X=X-1
                            P2Y1_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y1_B[X]="4"
                        X=X+1
                        if not P2Y1_B[X] == " ":
                            back=True
                            X=X-1
                            P2Y1_B[X]=" "
                            X=X-1
                            P2Y1_B[X]=" "
                            X=X-1
                            P2Y1_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y1_B[X]="4"
            elif Y == 2:
               if not P2Y2_B[X] == " ":
                    i=(i-1)
                    retry()
               else:
                    if i == 1:
                        P2Y2_B[X]="1"
                    elif i == 2:
                        P2Y2_B[X]="2"
                        X=X+1
                        if not P2Y2_B[X] == " ":
                            X=X-1
                            P2Y2_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y2_B[X]="2"
                    elif i == 3:
                        P2Y2_B[X]="3"
                        if not P2Y3_B[X] == " ":
                            P2Y2_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y3_B[X]="3"
                        time.sleep(0.01)
                        if not P2Y4_B[X] == " ":
                            P2Y2_B[X]=" "
                            P2Y3_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y4_B[X]="3"
                    elif i == 4:
                        P2Y2_B[X]="4"
                        X=X+1
                        if not P2Y2_B[X] == " ":
                            X=X-1
                            P2Y2_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y1_B[X]="4"
                        X=X+1
                        if not P2Y2_B[X] == " ":
                            X=X-1
                            P2Y2_B[X]=" "
                            X=X-1
                            P2Y2_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y2_B[X]="4"
                        X=X+1
                        if not P2Y2_B[X] == " ":
                            X=X-1
                            P2Y2_B[X]=" "
                            X=X-1
                            P2Y2_B[X]=" "
                            X=X-1
                            P2Y2_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y2_B[X]="4"
            elif Y == 3:
               if not P2Y3_B[X] == " ":
                    i=(i-1)
                    retry()
               else:
                    if i == 1:
                        P2Y3_B[X]="1"
                    elif i == 2:
                        P2Y3_B[X]="2"
                        X=X+1
                        if not P2Y3_B[X] == " ":
                            X=X-1
                            P2Y3_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y3_B[X]="2"
                    elif i == 3:
                        P2Y3_B[X]="3"
                        if not P2Y4_B[X] == " ":
                            P2Y3_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y4_B[X]="3"
                        time.sleep(0.01)
                        if not P2Y5_B[X] == " ":
                            P2Y3_B[X]=" "
                            P2Y4_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y5_B[X]="3"
                    elif i == 4:
                        P2Y3_B[X]="4"
                        X=X+1
                        if not P2Y3_B[X] == " ":
                            X=X-1
                            P2Y3_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y3_B[X]="4"
                        X=X+1
                        if not P2Y3_B[X] == " ":
                            X=X-1
                            P2Y3_B[X]=" "
                            X=X-1
                            P2Y3_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y3_B[X]="4"
                        X=X+1
                        if not P2Y3_B[X] == " ":
                            X=X-1
                            P2Y3_B[X]=" "
                            X=X-1
                            P2Y3_B[X]=" "
                            X=X-1
                            P2Y3_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y3_B[X]="4"
            elif Y == 4:
               if not P2Y4_B[X] == " ":
                    i=(i-1)
                    retry()
               else:
                    if i == 1:
                        P2Y4_B[X]="1"
                    elif i == 2:
                        P2Y4_B[X]="2"
                        X=X+1
                        if not P2Y4_B[X] == " ":
                            X=X-1
                            P2Y4_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y4_B[X]="2"
                    elif i == 3:
                        P2Y4_B[X]="3"
                        if not P2Y5_B[X] == " ":
                            P2Y4_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y5_B[X]="3"
                        time.sleep(0.01)
                        if not P2Y6_B[X] == " ":
                            P2Y4_B[X]=" "
                            P2Y5_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y6_B[X]="3"
                    elif i == 4:
                        P2Y4_B[X]="4"
                        X=X+1
                        if not P2Y4_B[X] == " ":
                            X=X-1
                            P2Y4_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y4_B[X]="4"
                        X=X+1
                        if not P2Y4_B[X] == " ":
                            X=X-1
                            P2Y4_B[X]=" "
                            X=X-1
                            P2Y4_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y4_B[X]="4"
                        X=X+1
                        if not P2Y4_B[X] == " ":
                            X=X-1
                            P2Y4_B[X]=" "
                            X=X-1
                            P2Y4_B[X]=" "
                            X=X-1
                            P2Y4_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y4_B[X]="4"
            elif Y == 5:
               if not P2Y5_B[X] == " ":
                    i=(i-1)
                    retry()
               else:
                    if i == 1:
                        P2Y5_B[X]="1"
                    elif i == 2:
                        P2Y5_B[X]="2"
                        X=X+1
                        if not P2Y5_B[X] == " ":
                            X=X-1
                            P2Y5_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y5_B[X]="2"
                    elif i == 3:
                        P2Y5_B[X]="3"
                        if not P2Y6_B[X] == " ":
                            P2Y5_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y6_B[X]="3"
                        time.sleep(0.01)
                        if not P2Y7_B[X] == " ":
                            P2Y5_B[X]=" "
                            P2Y6_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y7_B[X]="3"
                    elif i == 4:
                        P2Y5_B[X]="4"
                        X=X+1
                        if not P2Y5_B[X] == " ":
                            X=X-1
                            P2Y5_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y5_B[X]="4"
                        X=X+1
                        if not P2Y5_B[X] == " ":
                            X=X-1
                            P2Y5_B[X]=" "
                            X=X-1
                            P2Y5_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y5_B[X]="4"
                        X=X+1
                        if not P2Y5_B[X] == " ":
                            X=X-1
                            P2Y5_B[X]=" "
                            X=X-1
                            P2Y5_B[X]=" "
                            X=X-1
                            P2Y5_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y5_B[X]="4"
            elif Y == 6:
               if not P2Y6_B[X] == " ":
                    i=(i-1)
                    retry()
               else:
                    if i == 1:
                        P2Y6_B[X]="1"
                    elif i == 2:
                        P2Y6_B[X]="2"
                        X=X+1
                        if not P2Y6_B[X] == " ":
                            X=X-1
                            P2Y6_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y6_B[X]="2"
                    elif i == 3:
                        P2Y6_B[X]="3"
                        if not P2Y7_B[X] == " ":
                            P2Y6_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y7_B[X]="3"
                        time.sleep(0.01)
                        if not P2Y8_B[X] == " ":
                            P2Y6_B[X]=" "
                            P2Y7_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y8_B[X]="3"
                    elif i == 4:
                        P2Y6_B[X]="4"
                        X=X+1
                        if not P2Y6_B[X] == " ":
                            X=X-1
                            P2Y6_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y6_B[X]="4"
                        X=X+1
                        if not P2Y6_B[X] == " ":
                            X=X-1
                            P2Y6_B[X]=" "
                            X=X-1
                            P2Y6_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y6_B[X]="4"
                        X=X+1
                        if not P2Y6_B[X] == " ":
                            X=X-1
                            P2Y6_B[X]=" "
                            X=X-1
                            P2Y6_B[X]=" "
                            X=X-1
                            P2Y6_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y6_B[X]="4"
            elif Y == 7:
               if not P2Y7_B[X] == " ":
                    i=(i-1)
                    retry()
               else:
                    if i == 1:
                        P2Y7_B[X]="1"
                    elif i == 2:
                        P2Y7_B[X]="2"
                        X=X+1
                        if not P2Y8_B[X] == " ":
                            X=X-1
                            P2Y8_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y7_B[X]="2"
                    elif i == 3:
                        P2Y7_B[X]="3"
                        if not P2Y8_B[X] == " ":
                            P2Y7_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y8_B[X]="3"
                        time.sleep(0.01)
                        if not P2Y9_B[X] == " ":
                            P2Y7_B[X]=" "
                            P2Y8_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y9_B[X]="3"
                    elif i == 4:
                        P2Y7_B[X]="4"
                        X=X+1
                        if not P2Y7_B[X] == " ":
                            X=X-1
                            P2Y7_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y7_B[X]="4"
                        X=X+1
                        if not P2Y7_B[X] == " ":
                            X=X-1
                            P2Y7_B[X]=" "
                            X=X-1
                            P2Y7_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y7_B[X]="4"
                        X=X+1
                        if not P2Y7_B[X] == " ":
                            X=X-1
                            P2Y7_B[X]=" "
                            X=X-1
                            P2Y7_B[X]=" "
                            X=X-1
                            P2Y7_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y7_B[X]="4"
            elif Y == 8:
               if not P2Y8_B[X] == " ":
                    i=(i-1)
                    retry()
               else:
                    if i == 1:
                        P2Y8_B[X]="1"
                    elif i == 2:
                        P2Y8_B[X]="2"
                        X=X+1
                        if not P2Y8_B[X] == " ":
                            X=X-1
                            P2Y8_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y8_B[X]="2"
                    elif i == 4:
                        P2Y8_B[X]="4"
                        X=X+1
                        if not P2Y8_B[X] == " ":
                            X=X-1
                            P2Y8_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y8_B[X]="4"
                        X=X+1
                        if not P2Y8_B[X] == " ":
                            X=X-1
                            P2Y8_B[X]=" "
                            X=X-1
                            P2Y8_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y8_B[X]="4"
                        X=X+1
                        if not P2Y8_B[X] == " ":
                            X=X-1
                            P2Y8_B[X]=" "
                            X=X-1
                            P2Y8_B[X]=" "
                            X=X-1
                            P2Y8_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y8_B[X]="4"
            elif Y == 9:
               if not P2Y9_B[X] == " ":
                    i=(i-1)
                    retry()
               else:
                    if i == 1:
                        P2Y9_B[X]="1"
                    elif i == 2:
                        P2Y9_B[X]="2"
                        X=X+1
                        if not P2Y9_B[X] == " ":
                            X=X-1
                            P2Y9_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            if i == 1:
                                P2Y9_B[X]="1"
                    elif i == 2:
                        P2Y9_B[X]="2"
                        X=X+1
                        if not P2Y9_B[X] == " ":
                            X=X-1
                            P1Y9_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y8_B[X]="2"
                    elif i == 4:
                        P2Y9_B[X]="4"
                        X=X+1
                        if not P2Y9_B[X] == " ":
                            X=X-1
                            P2Y9_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y9_B[X]="4"
                        X=X+1
                        if not P2Y9_B[X] == " ":
                            X=X-1
                            P2Y9_B[X]=" "
                            X=X-1
                            P2Y9_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y9_B[X]="4"
                        X=X+1
                        if not P2Y9_B[X] == " ":
                            X=X-1
                            P2Y9_B[X]=" "
                            X=X-1
                            P2Y9_B[X]=" "
                            X=X-1
                            P2Y9_B[X]=" "
                            i=(i-1)
                            ready()
                        else:
                            P2Y9_B[X]="4"
    P=random.randint(0,1)
    P=P+1
    change()
def board():
    global P1Y1_B
    global P1Y2_B
    global P1Y3_B
    global P1Y4_B
    global P1Y5_B
    global P1Y6_B
    global P1Y7_B
    global P1Y8_B
    global P1Y9_B
    global P2Y1_S
    global P2Y2_S
    global P2Y3_S
    global P2Y4_S
    global P2Y5_S
    global P2Y6_S
    global P2Y7_S
    global P2Y8_S
    global P2Y9_S
    print("Y/X 1     2     3     4     5     6     7     8     9")
    print("1", "[", P2Y1_S[1], "]", "[", P2Y1_S[2], "]", "[", P2Y1_S[3], "]", "[", P2Y1_S[4], "]", "[", P2Y1_S[5], "]", "[", P2Y1_S[6], "]", "[", P2Y1_S[7], "]", "[", P2Y1_S[8], "]", "[", P2Y1_S[9], "]")
    print("2", "[", P2Y2_S[1], "]", "[", P2Y2_S[2], "]", "[", P2Y2_S[3], "]", "[", P2Y2_S[4], "]", "[", P2Y2_S[5], "]", "[", P2Y2_S[6], "]", "[", P2Y2_S[7], "]", "[", P2Y2_S[8], "]", "[", P2Y2_S[9], "]")
    print("3", "[", P2Y3_S[1], "]", "[", P2Y3_S[2], "]", "[", P2Y3_S[3], "]", "[", P2Y3_S[4], "]", "[", P2Y3_S[5], "]", "[", P2Y3_S[6], "]", "[", P2Y3_S[7], "]", "[", P2Y3_S[8], "]", "[", P2Y3_S[9], "]")
    print("4", "[", P2Y4_S[1], "]", "[", P2Y4_S[2], "]", "[", P2Y4_S[3], "]", "[", P2Y4_S[4], "]", "[", P2Y4_S[5], "]", "[", P2Y4_S[6], "]", "[", P2Y4_S[7], "]", "[", P2Y4_S[8], "]", "[", P2Y4_S[9], "]")
    print("5", "[", P2Y5_S[1], "]", "[", P2Y5_S[2], "]", "[", P2Y5_S[3], "]", "[", P2Y5_S[4], "]", "[", P2Y5_S[5], "]", "[", P2Y5_S[6], "]", "[", P2Y5_S[7], "]", "[", P2Y5_S[8], "]", "[", P2Y5_S[9], "]")
    print("6", "[", P2Y6_S[1], "]", "[", P2Y6_S[2], "]", "[", P2Y6_S[3], "]", "[", P2Y6_S[4], "]", "[", P2Y6_S[5], "]", "[", P2Y6_S[6], "]", "[", P2Y6_S[7], "]", "[", P2Y6_S[8], "]", "[", P2Y6_S[9], "]")
    print("7", "[", P2Y7_S[1], "]", "[", P2Y7_S[2], "]", "[", P2Y7_S[3], "]", "[", P2Y7_S[4], "]", "[", P2Y7_S[5], "]", "[", P2Y7_S[6], "]", "[", P2Y7_S[7], "]", "[", P2Y7_S[8], "]", "[", P2Y7_S[9], "]")
    print("8", "[", P2Y8_S[1], "]", "[", P2Y8_S[2], "]", "[", P2Y8_S[3], "]", "[", P2Y8_S[4], "]", "[", P2Y8_S[5], "]", "[", P2Y8_S[6], "]", "[", P2Y8_S[7], "]", "[", P2Y8_S[8], "]", "[", P2Y8_S[9], "]")
    print("9", "[", P2Y9_S[1], "]", "[", P2Y9_S[2], "]", "[", P2Y9_S[3], "]", "[", P2Y9_S[4], "]", "[", P2Y9_S[5], "]", "[", P2Y9_S[6], "]", "[", P2Y9_S[7], "]", "[", P2Y9_S[8], "]", "[", P2Y9_S[9], "]")
    print("Player: Computer Board")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~SEA~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Player: P1 Board")
    print("Y/X 1     2     3     4     5     6     7     8     9")
    print("1", "[", P1Y1_B[1], "]", "[", P1Y1_B[2], "]", "[", P1Y1_B[3], "]", "[", P1Y1_B[4], "]", "[", P1Y1_B[5], "]", "[", P1Y1_B[6], "]", "[", P1Y1_B[7], "]", "[", P1Y1_B[8], "]", "[", P1Y1_B[9], "]")
    print("2", "[", P1Y2_B[1], "]", "[", P1Y2_B[2], "]", "[", P1Y2_B[3], "]", "[", P1Y2_B[4], "]", "[", P1Y2_B[5], "]", "[", P1Y2_B[6], "]", "[", P1Y2_B[7], "]", "[", P1Y2_B[8], "]", "[", P1Y2_B[9], "]")
    print("3", "[", P1Y3_B[1], "]", "[", P1Y3_B[2], "]", "[", P1Y3_B[3], "]", "[", P1Y3_B[4], "]", "[", P1Y3_B[5], "]", "[", P1Y3_B[6], "]", "[", P1Y3_B[7], "]", "[", P1Y3_B[8], "]", "[", P1Y3_B[9], "]")
    print("4", "[", P1Y4_B[1], "]", "[", P1Y4_B[2], "]", "[", P1Y4_B[3], "]", "[", P1Y4_B[4], "]", "[", P1Y4_B[5], "]", "[", P1Y4_B[6], "]", "[", P1Y4_B[7], "]", "[", P1Y4_B[8], "]", "[", P1Y4_B[9], "]")
    print("5", "[", P1Y5_B[1], "]", "[", P1Y5_B[2], "]", "[", P1Y5_B[3], "]", "[", P1Y5_B[4], "]", "[", P1Y5_B[5], "]", "[", P1Y5_B[6], "]", "[", P1Y5_B[7], "]", "[", P1Y5_B[8], "]", "[", P1Y5_B[9], "]")
    print("6", "[", P1Y6_B[1], "]", "[", P1Y6_B[2], "]", "[", P1Y6_B[3], "]", "[", P1Y6_B[4], "]", "[", P1Y6_B[5], "]", "[", P1Y6_B[6], "]", "[", P1Y6_B[7], "]", "[", P1Y6_B[8], "]", "[", P1Y6_B[9], "]")
    print("7", "[", P1Y7_B[1], "]", "[", P1Y7_B[2], "]", "[", P1Y7_B[3], "]", "[", P1Y7_B[4], "]", "[", P1Y7_B[5], "]", "[", P1Y7_B[6], "]", "[", P1Y7_B[7], "]", "[", P1Y7_B[8], "]", "[", P1Y7_B[9], "]")
    print("8", "[", P1Y8_B[1], "]", "[", P1Y8_B[2], "]", "[", P1Y8_B[3], "]", "[", P1Y8_B[4], "]", "[", P1Y8_B[5], "]", "[", P1Y8_B[6], "]", "[", P1Y8_B[7], "]", "[", P1Y8_B[8], "]", "[", P1Y8_B[9], "]")
    print("9", "[", P1Y9_B[1], "]", "[", P1Y9_B[2], "]", "[", P1Y9_B[3], "]", "[", P1Y9_B[4], "]", "[", P1Y9_B[5], "]", "[", P1Y9_B[6], "]", "[", P1Y9_B[7], "]", "[", P1Y9_B[8], "]", "[", P1Y9_B[9], "]")
    print(" ")
def retry():
    print("System: Please try again")
def mode():
    global debug
    global show_state
    if debug == True:
        response()
    elif keep_showing_state == True:
        state()
def response():
    print("DEBUG")
    time.sleep(1)
def state():
    global RAM
    global X
    global Y
    global X_R
    global Y_R
    global ans
    global test
    global back
    global back2
    global debug
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
    print("RAM:",RAM)
    print("X:", X)
    print("Y:", Y)
    print("X_R:", X_R)
    print("Y_R:", Y_R)
    print("ans:", ans)
    print("test:", test)
    print("back:", back)
    print("back2:", back2)
    print("debug:",debug)
    print("ship_H:",ship_H)
    print("ship_S:",ship_S)
    print("ship_H_R:",ship_H_R)
    print("ship_S_R:",ship_S_R)
    print("target:",target)
    print("keep_showing_state:",keep_showing_state)
    print("total:",total)
    print("P:",P)
    print("i:",i)
    print("P1S:",P1S)
    print("P2S:",P2S)
    print("P1S1_HP:",P1S1_HP)
    print("P2S1_HP:",P2S1_HP)
    print("P1S2_HP:",P1S2_HP)
    print("P2S2_HP:",P2S2_HP)
    print("P1S3_HP:",P1S3_HP)
    print("P2S3_HP:",P2S3_HP)
    print("P1S4_HP:",P1S4_HP)
    print("P2S4_HP:",P2S4_HP)
    print("//////////STATE//////////STATE//////////STATE////////////////////STATE//////////STATE//////////")
    time.sleep(3)

import sys
import time
import random
P1Y1_B=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P1Y2_B=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P1Y3_B=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P1Y4_B=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P1Y5_B=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P1Y6_B=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P1Y7_B=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P1Y8_B=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P1Y9_B=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P2Y1_B=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P2Y2_B=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P2Y3_B=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P2Y4_B=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P2Y5_B=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P2Y6_B=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P2Y7_B=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P2Y8_B=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P2Y9_B=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P2Y1_S=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P2Y2_S=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P2Y3_S=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P2Y4_S=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P2Y5_S=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P2Y6_S=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P2Y7_S=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P2Y8_S=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
P2Y9_S=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
RAM=[" "]*2
X=None
Y=None
X_R=None
Y_R=None
ans=None
test=False
back=False
back2=False
debug=False
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
try:
    ans=input("System: Press enter to start.")
    if ans == "/debug":
        debug=True
        total=2
    elif ans == "/test":
        test=True
        total=3
    elif ans == "/quit":
        sys.exit()
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
