# Junction Checker
# Made by Peter Go 
# (C) 2023 Woojin Kou

junctionsX = [40, 64, 102, 139, 176, 179, 220, 222, 259, 297, 334, 361]
junctionsY = [16, 66, 103, 141, 179, 216, 253, 291, 333, 366]

junctionsNXUp = [40, 40, 40, 40, 40, 40, 64, 64, 64, 64, 64, 64, 64, 64, 64, 102, 102, 139, 139, 139, 139, 139, 176, 176, 176, 176, 176, 176, 179, 179, 179, 179, 179, 179, 220, 220, 220, 220, 220, 220, 222, 222, 222, 222, 222, 222, 222, 259, 259, 259, 259, 259, 297, 334, 334, 334, 334, 334, 334, 334, 334, 334, 361, 361, 361, 361, 361, 361]
junctionsNXDown = [40, 40, 40, 40, 40, 40, 64, 64, 64, 64, 64, 64, 64, 64, 102, 102, 139, 139, 139, 139, 139, 176, 176, 176, 176, 176, 176, 179, 179, 179, 179, 179, 179, 220, 220, 220, 220, 220, 220, 222, 222, 222, 222, 222, 222, 259, 259, 259, 259, 297, 297, 334, 334, 334, 334, 334, 334, 334, 334, 334, 361, 361, 361, 361, 361, 361]
junctionsNXLeft = [40, 40, 40, 40, 40, 40, 40, 40, 40, 64, 64, 64, 102, 102, 102, 139, 139, 139, 139, 176, 179, 220, 220, 220, 220, 220, 222, 222, 222, 222, 259, 297, 297, 297, 297, 334, 334, 334, 361, 361]
junctionsNXRight = [141, 216, 179, 216, 291, 103, 141, 216, 333, 179, 16, 103, 179, 253, 333, 16, 103, 179, 253, 333, 179, 179, 103, 141, 216, 333, 141, 216, 291, 141, 216, 16, 66, 103, 141, 216, 253, 291, 333, 366]
junctionsNYUp = [16, 141, 179, 216, 253, 333, 16, 66, 103, 141, 179, 216, 253, 291, 366, 16, 366, 16, 66, 141, 291, 366, 16, 103, 179, 216, 253, 333, 16, 103, 179, 216, 253, 333, 16, 103, 179, 216, 253, 333, 16, 66, 103, 179, 216, 253, 333, 16, 66, 141, 291, 366, 16, 16, 66, 103, 141, 179, 216, 253, 291, 366, 16, 141, 179, 216, 253, 333]
junctionsNYDown = [103, 141, 179, 216, 291, 366, 66, 103, 141, 179, 216, 253, 333, 366, 333, 366, 16, 103, 253, 333, 366, 66, 141, 179, 216, 291, 366, 66, 141, 179, 216, 291, 366, 16, 66, 141, 179, 216, 291, 141, 179, 216, 291, 333, 366, 16, 253, 333, 366, 333, 366, 16, 66, 103, 141, 179, 216, 253, 333, 366, 103, 141, 179, 216, 291, 366]
junctionsNYLeft = [16, 66, 103, 141, 216, 253, 291, 333, 366, 16, 179, 216, 141, 216, 291, 103, 141, 216, 333, 179, 179, 16, 103, 179, 253, 333, 16, 103, 179, 253, 179, 103, 141, 216, 333, 141, 216, 291, 141, 216]
junctionsNYRight = [141, 216, 179, 216, 291, 103, 141, 216, 333, 179, 16, 103, 179, 253, 333, 16, 103, 179, 253, 333, 179, 179, 103, 141, 216, 333, 141, 216, 291, 141, 216, 16, 66, 103, 141, 216, 253, 291, 333, 366]


portedNUp = []
portedNDown = []
portedNLeft = []
portedNRight = []

print("available commands:")
print(" - junctionCord")
print(" - portCordUNID")

commandEnter = input("Enter your command: junctionChecker/")

if commandEnter == "junctionCord":
    for x in range(len(junctionsX)):
        for y in range(len(junctionsY)):
            print("\033[2J")
            print(f"({junctionsX[x]}, {junctionsY[y]}) or Column {x}, Row {y}!")

            checkIN = input("Can you move UP? (Enter key for Yes, \"n\" for No)  ")
            if checkIN == "":
                pass
            else:
                junctionsNXUp.append(junctionsX[x])
                junctionsNYUp.append(junctionsY[y])
            
            checkIN = input("Can you move DOWN? (Enter key for Yes, \"n\" for No)  ")
            if checkIN == "":
                pass
            else:
                junctionsNXDown.append(junctionsX[x])
                junctionsNYDown.append(junctionsY[y])
            
            checkIN = input("Can you move LEFT? (Enter key for Yes, \"n\" for No)  ")
            if checkIN == "":
                pass
            else:
                junctionsNXLeft.append(junctionsX[x])
                junctionsNYLeft.append(junctionsY[y])
            

            checkIN = input("Can you move RIGHT? (Enter key for Yes, \"n\" for No)  ")
            if checkIN == "":
                pass
            else:
                junctionsNXRight.append(junctionsX[x])
                junctionsNYRight.append(junctionsY[y])


    print("\033[2J")
    print("Here are the junction invalidations:")
    print("INVALID JUNCTIONS. ERROR 500.")
elif commandEnter == "portCordUNID":
    print("Porting... STANDBY.")

    for nUP in range(len(junctionsNXUp)):
        if junctionsNXUp[nUP] in junctionsX and junctionsNYUp[nUP] in junctionsY:
            turnPointUNIDX = junctionsX.index(junctionsNXUp[nUP])
            if len(str(turnPointUNIDX)) <= 1:
                turnPointUNIDX = f"0{turnPointUNIDX}"
            
            turnPointUNIDY = junctionsY.index(junctionsNYUp[nUP])
            turnPoint = f"{turnPointUNIDX}{turnPointUNIDY}"
            portedNUp.append(turnPoint)
    
    for nDOWN in range(len(junctionsNXDown)):
        if junctionsNXDown[nDOWN] in junctionsX and junctionsNYDown[nDOWN] in junctionsY:
            turnPointUNIDX = junctionsX.index(junctionsNXDown[nDOWN])
            if len(str(turnPointUNIDX)) <= 1:
                turnPointUNIDX = f"0{turnPointUNIDX}"
            
            turnPointUNIDY = junctionsY.index(junctionsNYDown[nDOWN])
            turnPoint = f"{turnPointUNIDX}{turnPointUNIDY}"
            portedNDown.append(turnPoint)
    
    for nLEFT in range(len(junctionsNXLeft)):
        if junctionsNXLeft[nLEFT] in junctionsX and junctionsNYLeft[nLEFT] in junctionsY:
            turnPointUNIDX = junctionsX.index(junctionsNXLeft[nLEFT])
            if len(str(turnPointUNIDX)) <= 1:
                turnPointUNIDX = f"0{turnPointUNIDX}"
            
            turnPointUNIDY = junctionsY.index(junctionsNYLeft[nLEFT])
            turnPoint = f"{turnPointUNIDX}{turnPointUNIDY}"
            portedNLeft.append(turnPoint)

    for nRight in range(len(junctionsNXRight)):
        if junctionsNXRight[nRight] in junctionsX and junctionsNYRight[nRight] in junctionsY:
            turnPointUNIDX = junctionsX.index(junctionsNXRight[nRight])
            if len(str(turnPointUNIDX)) <= 1:
                turnPointUNIDX = f"0{turnPointUNIDX}"
            
            turnPointUNIDY = junctionsY.index(junctionsNYRight[nRight])
            turnPoint = f"{turnPointUNIDX}{turnPointUNIDY}"
            portedNRight.append(turnPoint)
    
    for nYUP in range(len(junctionsNXUp)):
        if junctionsNXUp[nYUP] in junctionsX and junctionsNYUp[nYUP] in junctionsY:
            turnPointUNIDX = junctionsX.index(junctionsNXUp[nYUP])
            if len(str(turnPointUNIDX)) <= 1:
                turnPointUNIDX = f"0{turnPointUNIDX}"
            
            turnPointUNIDY = junctionsY.index(junctionsNYUp[nYUP])
            turnPoint = f"{turnPointUNIDX}{turnPointUNIDY}"
            portedNUp.append(turnPoint)
    
    for nYDOWN in range(len(junctionsNXDown)):
        if junctionsNXDown[nYDOWN] in junctionsX and junctionsNYDown[nYDOWN] in junctionsY:
            turnPointUNIDX = junctionsX.index(junctionsNXDown[nYDOWN])
            if len(str(turnPointUNIDX)) <= 1:
                turnPointUNIDX = f"0{turnPointUNIDX}"
            
            turnPointUNIDY = junctionsY.index(junctionsNYDown[nYDOWN])
            turnPoint = f"{turnPointUNIDX}{turnPointUNIDY}"
            portedNDown.append(turnPoint)
    
    for nYLEFT in range(len(junctionsNXLeft)):
        if junctionsNXLeft[nYLEFT] in junctionsX and junctionsNYLeft[nYLEFT] in junctionsY:
            turnPointUNIDX = junctionsX.index(junctionsNXLeft[nYLEFT])
            if len(str(turnPointUNIDX)) <= 1:
                turnPointUNIDX = f"0{turnPointUNIDX}"
            
            turnPointUNIDY = junctionsY.index(junctionsNYLeft[nYLEFT])
            turnPoint = f"{turnPointUNIDX}{turnPointUNIDY}"
            portedNLeft.append(turnPoint)

    for nYRight in range(len(junctionsNXRight)):
        if junctionsNXRight[nYRight] in junctionsX and junctionsNYRight[nYRight] in junctionsY:
            turnPointUNIDX = junctionsX.index(junctionsNXRight[nYRight])
            if len(str(turnPointUNIDX)) <= 1:
                turnPointUNIDX = f"0{turnPointUNIDX}"
            
            turnPointUNIDY = junctionsY.index(junctionsNYRight[nYRight])
            turnPoint = f"{turnPointUNIDX}{turnPointUNIDY}"
            portedNRight.append(turnPoint)

    print("\033[2J")
    print("Here are the ported turnPoints:")
    print(f"portedNUp = {portedNUp}")
    print(f"portedNDown = {portedNDown}")
    print(f"portedNLeft = {portedNLeft}")
    print(f"portedNRight = {portedNRight}")