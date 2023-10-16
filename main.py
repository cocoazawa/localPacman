# Made by Pete Kou
# (C) 2023 
#
# MIT LICENSED


# Imports
import pygame 

pygame.init()
canvas = pygame.display.set_mode((400, 400))
pygame.display.set_caption("PACMAN") 



junctionsX = [40, 64, 102, 139, 176, 179, 220, 222, 259, 297, 334, 361]
junctionsY = [16, 66, 103, 141, 179, 216, 253, 291, 333, 366]

portedNUp = ['000', '003', '004', '005', '006', '008', '010', '011', '012', '013', '014', '015', '016', '017', '019', '020', '029', '030', '031', '033', '037', '039', '040', '042', '044', '045', '046', '048', '050', '052', '054', '055', '056', '058', '060', '062', '064', '065', '066', '068', '070', '071', '072', '074', '075', '076', '078', '080', '081', '083', '087', '089', '090', '100', '101', '102', '103', '104', '105', '106', '107', '109', '110', '113', '114', '115', '116', '118', '000', '003', '004', '005', '006', '008', '010', '011', '012', '013', '014', '015', '016', '017', '019', '020', '029', '030', '031', '033', '037', '039', '040', '042', '044', '045', '046', '048', '050', '052', '054', '055', '056', '058', '060', '062', '064', '065', '066', '068', '070', '071', '072', '074', '075', '076', '078', '080', '081', '083', '087', '089', '090', '100', '101', '102', '103', '104', '105', '106', '107', '109', '110', '113', '114', '115', '116', '118']
portedNDown = ['002', '003', '004', '005', '007', '009', '011', '012', '013', '014', '015', '016', '018', '019', '028', '029', '030', '032', '036', '038', '039', '041', '043', '044', '045', '047', '049', '051', '053', '054', '055', '057', '059', '060', '061', '063', '064', '065', '067', '073', '074', '075', '077', '078', '079', '080', '086', '088', '089', '098', '099', '100', '101', '102', '103', '104', '105', '106', '108', '109', '112', '113', '114', '115', '117', '119', '002', '003', '004', '005', '007', '009', '011', '012', '013', '014', '015', '016', '018', '019', '028', '029', '030', '032', '036', '038', '039', '041', '043', '044', '045', '047', '049', '051', '053', '054', '055', '057', '059', '060', '061', '063', '064', '065', '067', '073', '074', '075', '077', '078', '079', '080', '086', '088', '089', '098', '099', '100', '101', '102', '103', '104', '105', '106', '108', '109', '112', '113', '114', '115', '117', '119']
portedNLeft = ['000', '001', '002', '003', '005', '006', '007', '008', '009', '010', '014', '015', '023', '025', '027', '032', '033', '035', '038', '044', '054', '060', '062', '064', '066', '068', '070', '072', '074', '076', '084', '092', '093', '095', '098', '103', '105', '107', '113', '115', '000', '001', '002', '003', '005', '006', '007', '008', '009', '010', '014', '015', '023', '025', '027', '032', '033', '035', '038', '044', '054', '060', '062', '064', '066', '068', '070', '072', '074', '076', '084', '092', '093', '095', '098', '103', '105', '107', '113', '115']
portedNRight = ['054']

pacmanMouthState = False
pacmanMouthCounter = 0

pacmanFacingQ = "right"

while not exit: 
    # First Row & Section Borders
    pygame.Rect(25, 0, 350, 168.5, border="blue", borderWidth = 3),
    Line(-10, 168, 410, 168, lineWidth = 10),
    pygame.Rect(25, 190, 350, 188, border="blue", borderWidth = 3),
    Line(-10, 188, 410, 188, lineWidth = 10),

    pygame.Rect(52, 28, 37.5, 25, border="blue", borderWidth = 3),
    pygame.Rect(114.5, 28, 50, 25, border="blue", borderWidth = 3),
    pygame.Rect(234.5, 28, 50, 25, border="blue", borderWidth = 3),
    pygame.Rect(309.5, 28, 37.5, 25, border="blue", borderWidth = 3),

    pygame.Rect(189, -10, 20, 63, border="blue", borderWidth = 3),


    # Second & Third Rows
    pygame.Rect(52, 78, 37.5, 12.5, border="blue", borderWidth = 3),
    Polygon(114.5, 78, 127, 78, 127, 115.5, 164, 115.5, 164, 128, 127, 128, 127, 168.5, 114, 168.5, border="blue", borderWidth = 3), # Left
    Polygon(284, 78, 272, 78, 272, 115.5, 234.5, 115.5, 234.5, 128, 272, 128, 272, 168.5, 284, 168.5, border="blue", borderWidth = 3), # Right
    Polygon(152, 78, 247, 78, 247, 90.5, 206.5, 90.5, 206.5, 128, 193.75, 128, 193.75, 90.5, 152, 90.5, border="blue", borderWidth = 3), # Middle
    pygame.Rect(309.5, 78, 37.5, 12.5, border="blue", borderWidth = 3),

    pygame.Rect(-10, 115.5, 100, 50, border="blue", borderWidth = 3),
    pygame.Rect(310, 115.5, 100, 50, border="blue", borderWidth = 3),


    # Fourth and SlightFifth Rows
    pygame.Rect(114, 190, 12.5, 50, border="blue", borderWidth = 3),
    pygame.Rect(272, 190, 12.5, 50, border="blue", borderWidth = 3),

    Polygon(152, 228, 247, 228, 247, 240.5, 206.5, 240.5, 206.5, 278, 193.75, 278, 193.75, 240.5, 152, 240.5, border="blue", borderWidth = 3), # Middle

    pygame.Rect(-10, 190.5, 100, 50, border="blue", borderWidth = 3),
    pygame.Rect(310, 190.5, 100, 50, border="blue", borderWidth = 3),


    # Fifth and SlightSixth Rows
    pygame.Rect(114, 265, 50, 12.5, border="blue", borderWidth = 3),
    pygame.Rect(234, 265, 50, 12.5, border="blue", borderWidth = 3),

    Polygon(51.5, 265, 90, 265, 90, 315, 77.5, 315, 77.5, 277.5, 51.5, 277.5, border="blue", borderWidth = 3), # Left
    Polygon(347.5, 265, 310, 265, 310, 315, 322.5, 315, 322.5, 277.5, 347.5, 277.5, border="blue", borderWidth = 3), # Right


    # Sixth Row
    Polygon(52, 340.5, 114, 340.5, 114, 303, 126.5, 303, 126.5, 340.5, 163.5, 340.5, 163.5, 353, 52, 353, border="blue", borderWidth = 3), # Left
    Polygon(152, 303, 247, 303, 247, 315.5, 206.5, 315.5, 206.5, 353, 193.75, 353, 193.75, 315.5, 152, 315.5, border="blue", borderWidth = 3), # Middle
    Polygon(348, 340.5, 284, 340.5, 284, 303, 271.5, 303, 271.5, 340.5, 234, 340.5, 234, 353, 348, 353, border="blue", borderWidth = 3), # Left


    # Ghost Box
    pygame.Rect(151.5, 153, 95, 50, border="blue", borderWidth = 2),
    pygame.Rect(156.5, 158, 85, 40, border="blue", borderWidth = 2),
    pygame.Rect(187.75, 153, 25, 10),
    Line(187.75, 153, 187.75, 160, fill="blue", lineWidth = 2),
    Line(212.75, 153, 212.75, 160, fill="blue", lineWidth = 2),


    # Ending Border & Finishing Touches
    Line(-10, 115, 25, 115, lineWidth = 10),
    Line(-10, 239, 25, 239, lineWidth = 10),
    Line(375, 115, 410, 115, lineWidth = 10),
    Line(375, 239, 410, 239, lineWidth = 10),

    pygame.Rect(25, 302.5, 25, 12.5, border="blue", borderWidth = 3),
    pygame.Rect(347, 302.5, 28, 12.5, border="blue", borderWidth = 3),

    pacmanSprite = Group()

    pacmanMainBody = Circle(200,200,10,fill="lime")
    pacmanMainML = RegularPolygon(193,200,10,3,fill='black', rotateAngle=90,opacity=0)
    pacmanMainMR = RegularPolygon(207,200,10,3,fill='black', rotateAngle=270,opacity=0)
    pacmanMainMT = RegularPolygon(200,193,10,3,fill='black', rotateAngle=180,opacity=0)
    pacmanMainMB = RegularPolygon(200,207,10,3,fill='black', rotateAngle=0,opacity=0)

    pacmanSprite.add(pacmanMainBody, pacmanMainML, pacmanMainMR, pacmanMainMT, pacmanMainMB)
    pacmanSprite.centerX = 40
    pacmanSprite.centerY = 16

    proceedToMoveIndicator = Circle(140, 390, 7, fill = "yellowGreen")
    Label("Move indicator!", 200, 390, size=14, fill="white")


    def collisionOKUpdate(direction, cX, cY):
        global portedNUp
        global portedNDown
        global portedNLeft
        global portedNRight  
        global junctionsX
        global junctionsY

        validTurn = ((cX in junctionsX) or (cX+1 in junctionsX) or (cX+2 in junctionsX) or (cX-1 in junctionsX) or (cX-2 in junctionsX) or (cX-3 in junctionsX) or (cX+3 in junctionsX) or (cX+4 in junctionsX) or (cX+5 in junctionsX) or (cX+6 in junctionsX) or (cX-4 in junctionsX) or (cX-5 in junctionsX) or (cX-6 in junctionsX)) and ((cY in junctionsY) or (cY+1 in junctionsY) or (cY+2 in junctionsY) or (cY-1 in junctionsY) or (cY-2 in junctionsY) or (cY-3 in junctionsY) or (cY+3 in junctionsY) or (cY+4 in junctionsY) or (cY+5 in junctionsY) or (cY+6 in junctionsY) or (cY-4 in junctionsY) or (cY-5 in junctionsY) or (cY-6 in junctionsY))

        print(validTurn)

        if validTurn == True:
            proceedToMoveIndicator.fill = "yellowGreen"
        else:
            proceedToMoveIndicator.fill = "orangeRed"


    def turnDetectHandler(direction, cX, cY):
        # Check if it is a valid turn in the first place
        validTurn = ((cX in junctionsX) or (cX+1 in junctionsX) or (cX+2 in junctionsX) or (cX-1 in junctionsX) or (cX-2 in junctionsX) or (cX-3 in junctionsX) or (cX+3 in junctionsX) or (cX+4 in junctionsX) or (cX+5 in junctionsX) or (cX+6 in junctionsX) or (cX-4 in junctionsX) or (cX-5 in junctionsX) or (cX-6 in junctionsX)) and ((cY in junctionsY) or (cY+1 in junctionsY) or (cY+2 in junctionsY) or (cY-1 in junctionsY) or (cY-2 in junctionsY) or (cY-3 in junctionsY) or (cY+3 in junctionsY) or (cY+4 in junctionsY) or (cY+5 in junctionsY) or (cY+6 in junctionsY) or (cY-4 in junctionsY) or (cY-5 in junctionsY) or (cY-6 in junctionsY))
        
        if validTurn == False:
            return False  # IT AIN'T A TURN


        # Actual Turn Detection
        cXApproach = []
        cYApproach = []

        # cXCheck        
        for cXCheckIndex in range(len(junctionsX)):
            currentSelectedX = junctionsX[cXCheckIndex]  # Get the current index junctionCoordinate
            diffCSXwcX = abs((currentSelectedX - cX))  # Get the difference between the current index junctionCoordinate and currentActual coordinate

            cXApproach.append([diffCSXwcX, cXCheckIndex])  # Append the difference to the "approach" array and rerun the for loop
        
        cXApproach = sorted(cXApproach[0], None, True)  # Sort the array of the cXApproach to be in descending order, and the first item is the 


        turnPointUNIDX = junctionsX.index()
        if len(str(turnPointUNIDX)) <= 1:
            turnPointUNIDX = f"0{turnPointUNIDX}"
        
        turnPointUNIDY = junctionsY.index()
        turnPoint = f"{turnPointUNIDX}{turnPointUNIDY}"
        portedNUp.append(turnPoint)


    def collisionPreventHandler(direction, cX, cY):

        proceedQ = turnDetectHandler(direction, cX, cY)

        if proceedQ == True:
            return False
        else:
            return True


    def pacmanMovementHandler(direction, state):
        global pacmanFacingQ

        if (direction != "null" and collisionPreventHandler(direction, pacmanSprite.centerX, pacmanSprite.centerY) == False):
            if(direction == "left"):
                pacmanFacingQ = "left"
                pacmanMainML.opacity=100
                pacmanMainMR.opacity=0
                pacmanMainMT.opacity=0
                pacmanMainMB.opacity=0
            elif(direction == "right"):
                pacmanFacingQ = "right"
                pacmanMainML.opacity=0
                pacmanMainMR.opacity=100
                pacmanMainMT.opacity=0
                pacmanMainMB.opacity=0
            elif(direction == "up"):
                pacmanFacingQ = "up"
                pacmanMainML.opacity=0
                pacmanMainMR.opacity=0
                pacmanMainMT.opacity=100
                pacmanMainMB.opacity=0
            elif(direction == "down"):
                pacmanFacingQ = "down"
                pacmanMainML.opacity=0
                pacmanMainMR.opacity=0
                pacmanMainMT.opacity=0
                pacmanMainMB.opacity=100
        
        if(state == True):
            if(pacmanFacingQ == "left"):
                pacmanMainML.opacity=100
                pacmanMainMR.opacity=0
                pacmanMainMT.opacity=0
                pacmanMainMB.opacity=0
            elif(pacmanFacingQ == "right"):
                pacmanMainML.opacity=0
                pacmanMainMR.opacity=100
                pacmanMainMT.opacity=0
                pacmanMainMB.opacity=0
            elif(pacmanFacingQ == "up"):
                pacmanMainML.opacity=0
                pacmanMainMR.opacity=0
                pacmanMainMT.opacity=100
                pacmanMainMB.opacity=0
            elif(pacmanFacingQ == "down"):
                pacmanMainML.opacity=0
                pacmanMainMR.opacity=0
                pacmanMainMT.opacity=0
                pacmanMainMB.opacity=100
        else:
            pacmanMainML.opacity=0
            pacmanMainMR.opacity-0
            pacmanMainMT.opacity=0
            pacmanMainMB.opacity=0
            
        
    def onKeyPress(key):
        pacmanMovementHandler(key, pacmanMouthState)


    def onStep():
        global pacmanMouthState
        global pacmanMouthCounter
        global pacmanFacingQ
        
        if(pacmanMouthCounter <= 10):
            pacmanMouthState = True
            pacmanMovementHandler("null", pacmanMouthState)
        elif(pacmanMouthCounter > 10 and pacmanMouthCounter < 20):
            pacmanMouthState = False
            pacmanMovementHandler("null", pacmanMouthState)
        elif(pacmanMouthCounter == 20):
            pacmanMouthState = False
            pacmanMovementHandler("null", pacmanMouthState)
            pacmanMouthCounter=0
            
        if(pacmanFacingQ == "left"):
            pacmanSprite.centerX -= 1
        elif(pacmanFacingQ == "right"):
            pacmanSprite.centerX += 1
        elif(pacmanFacingQ == "up"):
            pacmanSprite.centerY -= 1
        elif(pacmanFacingQ == "down"):
            pacmanSprite.centerY += 1
        
        pacmanMouthCounter +=1

        collisionOKUpdate(pacmanFacingQ, pacmanSprite.centerX, pacmanSprite.centerY)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
    pygame.display.update() 