import time

def describe(scenario):
    print('\033[94m=\033[0m'*125)
    print('\033[94m'+GAME_MAP[scenario][1]+'\033[0m')
    print('\033[94m=\033[0m'*125)

def choice():
    return int(input(f"\nPress \n{GAME_MAP[scenario][2]} \n\n==> "))

def displayInventory(inventory):
    global scenario
    print('\033[33m*\033[0m'*50)
    print('\033[33mINVENTORY :\033[0m\n')
    if not inventory:
        print('\033[33m["You have not picked up any items yet"]\033[0m\n')
    else: 
        print('\033[33m'+str([objects.get(item) for item in inventory])+'\033[0m\n')
    print('\033[33m*\033[0m'*50)
    selection = scenario
    return selection

def checkpoint(scenario):
    displayInventory(inventory)
    print('\033[94m=\033[0m'*125)
    verification = input('\033[94m'+GAME_MAP[scenario][2]+'\033]0m]')
    print('\033[94m=\033[0m'*125)
    if verification == GAME_MAP[scenario][6]:
        print('\033[32mSUCCESS!!\033[0m')
        return 1
    else:
        print('\033[31mThat was INCORRECT. Returning ...\033[0m')
        return 2 


objects = {1: 'SOFA CARD', 2: 'ROOM KEY-CARD', 3:'IRON KEY w SYMBOLS : %&@', 4: '🌸☘🍁🌺'}
inventory = []


GAME_MAP = [
    ["0 - Introduction", """The door slams behind you, just as you open your eyes groggily. A key turning in the lock jolts you back to reality. 
Where am I?  you think, as you gaze around the room. You see a door, marked I, then another -- II, then one more, III. 
You try door II, but it is locked, so you fiddle with the handle of door I, and it is unlocked. You push it open, enter, 
and see yet another set of doors. Part one, two, three, they are marked. Doors two and three are obviously locked,
so you try one.It opens, and you step into another world....""", "\n1: to continue ... ", {1:1}, [], False],
    ["1 - Introduction II", """You step into the room, which is a....TOILET?????!!!!!
In confusion, you bang the wall angrily, but the tiled wall slides away to reveal a gorgeously decorated living room.
Not so bad, you think. You look around and see the following. Where do you want to investigate?""", "\n0: Check inventory\n1: Go to Toilet \n2: Go to Living Room", {1:3, 2:2}, [], False],
    ["2 - Living Room", """You step into the living room, which is richly furnished. Drapes of various colours and materials hung over the windows, sofas
and there is even a four-poster bed. A discreet chest was placed in one shadowy corner, hidden in the darkness. 
At the side of the room, there is another door.""", "\n0: Check inventory\n1: Window \n2: Sofa \n3: Bed \n4: Chest \n5: Door \n6: Back to the toilet", {1:4, 2:5, 3:26, 4:27, 5:13, 6:3}, [], False],
    ["3 - Toilet", """Turning away from the living room, you survey the toilet.
Looks like what you would call a normal toilet....In the far corner, there is a bathtub that seems to be made out of marble. 
At the sink, hot and cold water taps are present, and so are various brands of soap. There is also a cupboard wedged between the sink and the bathtub.""", "\n0: Check inventory\n1: Bathtub \n2: Sink \n3: Cupboard \n4: Back to Living Room", {1:6, 2:7, 3:8, 4:2}, [], False],
    ["4 - Window", """You go over to the window and push away the curtains. A piece of paper is neatly tucked in the window-sill. 
You pick it up and unfold it. You see this:  
EHT YEK OT EHT ROOD SI NO EHT YEK, TUB EREHW SI EHT YEK?
It looks simple enough to decode, you think.""", "\n0: Check inventory\n1: Sofa \n2: Bed \n3: Chest \n4: Door \n5: Back to the toilet", {1:5, 2:26, 3:27, 4:13, 5:3}, [], False],
    ["5 - Sofa", """Fluffing up the cushions on the sofa, you find a card. 
You pick it up and pocket it.""", "\n0: Check inventory\n1: Window \n2: Bed \n3: Chest \n4: Door \n5: Back to the toilet", {1:4, 2:26, 3:27, 4:13, 5:3}, [1], False],
    ["6 - Bathtub", """You look into the bathtub and find a number pasted inside: 7""", "\n0: Check inventory\n1: Sink \n2: Cupboard \n3: Back to Living Room", {1:7, 2:8, 3:2}, [], False],
    ["7 - Sink", """You find the numbers: 349 pasted at the back of the soap bottles. """, " \n1: Bathtub \n2: Cupboard \n3: Back to Living Room", {1:6, 2:8, 3:2}, [], False],
    ["8 - Locked cupboard", """The cupboard is locked with a padlock. Do you have the code?""", "\n0: Check inventory\n1: Yes \n2: No", {1:9, 2:10}, [], False],
    ["9 - Correct Code", "", "Type in the code for verification : ", {1:11, 2:10}, [], True, "3189"],
    ["10 - Wrong Code", """You must find the code...""", "\n0: Check inventory\n1: Bathtub \n2: Sink \n3: Back to Living Room", {1:6, 2:7, 3:2}, [], False],
    ["11 - Unlocked Cupboard", """The cupboard opens and you see a room-key-card. You pick it up. Where do you go now?""", "\n0: Check inventory\n1: Bathtub \n2: Sink \n3: To Living Room", {1:6, 2:7, 3:2}, [2], False],
    ["12 - Unlocked Chest", """The chest opens and you see an iron key placed inside. You pick it up, weighing it in your hand. It is extremely heavy. You notice three symbols stamped on it: '%&@ '
Pocketing it, you turn back to investigate the other things.""", "\n0: Check inventory\n1: Window \n2: Sofa \n3: Bed \n4: Door \n5: Back to the toilet", {1:4, 2:5, 3:26, 4:13, 5:3}, [3], False],
    ["13 - Living Room Locked Door", """You try the door but it is locked. Do you have a key?""", "\n0: Check inventory\n1: Yes \n2: No", {1:14, 2:16}, [], False],
    ["14 - Unlocked Door From Living Room", """You place the key into the keyhole and turn it. It doesn't unlock the door. Maybe you need to do something else? 
Suddenly, you find a digital lock. It seems you need to enter the symbols on the key into the lock. """, "\n1: Use keyboard to enter the code or \n2: return to Living Room", {1:32, 2:2}, [], False],
    ["15 - Unlocked door from living room from chest", """You place the iron key in the lock and it fits exactly. But....the door doesn't open. 
You see a digital lock and make your way over to it. Hey, that's the code on the key!, you realise. 
You enter the code and turn the key too...Hooray! The lock clicks and the door swings open on silent hinges. 
You look around and see another door with a panel next to it and a safe. Where do you go?""", "\n0: Check inventory\n1: Door and Panel \n2: Safe \n3: Back to Living Room", {1:18, 2:24, 3:28}, [], False],
    ["16 - Living Room locked door without key", """Go find a key. Where do you go now?""", "\n0: Check inventory\n1: Window \n2: Sofa \n3: Bed \n4: Chest \n5: Back to the toilet", {1:4, 2:5, 3:26, 4:27, 5:3}, [], False],
    ["17 - Correct Symbols", """The panel flashed green and you turn the key by instinct. The door swings open. You look around and see another door with a panel next to it and a safe. """, "\n0: Check inventory\n1: Door + panel \n2: Safe \n3. Back to living room""", {1:18, 2:24, 3:28}, [], False],    
    ["18 - Door & Panel", """You see a slit in the panel for the room-key-card to slide in. Do you have one?""", "\n0: Check inventory\n1: Yes \n2: No", {1:19, 2:23}, [], False],
    ["19 - Verification", """So you've got the key. Just one more step of verification. Where did you get the key from? (all lowercase, please)""", "Type your answer here : ", {1:20, 2:17}, [], True, 'cupboard'],
    ["20 - Cupboard verification", """What is the cupboard's code?""", "Enter code : ", {1:21 , 2:17}, [], True, '3189'],
    ["21 - Hallway", """The door unlocks as you slide the card (from the cupboard) on the panel. You push open the door and head into the hallway. You try the lift, but it doesn't work! The door to the stairs also does not open. 
The is a sticker pasted on the door: OBTAIN KEY FROM LAST ROOM. 
You have to go into the next room, you realise, then the next, then the next to get the key as the door to the last room is -- of course -- locked. 
You try the handle of the room adjacent to the one you walked out of. With a sinking heart, you see ANOTHER panel. Do you have the card? """, "\n1: Yes I have the card.\n2: No card. Back to small room.", {1:33, 2:29}, [], {}, False],
    ["22 - Success!", """You tap the card on the panel and the door unlocks!!! :D YOU HAVE COMPLETED CHAPTER 1!!!""", {}, [], False],
    ["23 - No room key card", """Hmmm...go find one.""", "Where do you want to go?\n1: Safe \n2: To Living Room", {1:24, 2:28}, [], False],
    ["24 - Safe", """There is a 5 digit number code. What do you enter? (you have to guess the last digit) HINT: 7 is the first digit""" , "Input the answer (Hint** - You might have to guess the last digit) : ", {1:25, 2:30}, [], True, '73491'],
    ["25 - Unlocked Safe", """The safe unlocked and you see an iPhone. You switch it on and see: 3189. """, "\n0: Check inventory\n1: Door + Panel \n2: Back to Living Room", {1:18, 2:28}, [], False],
    ["26 - Bed", """You go over to the bed and lift up all the pillows. Finding nothing, you then proceed to the blankets. After a few minutes of searching, you come out empty-handed. 
Suddenly, the bed-knob catches your eye. On it, four plants are engraved. 🌸☘🍁🌺 """, "\n0: Check inventory\n1: Go to Window \n2: Go to Sofa \n3: Go to Chest \n4: Investigate Door \n5: To the Toilet", {1:4, 2:5, 3:27, 4:13, 5:3}, [4], False],
    ["27 - Chest", """Making your way to the chest, you try and lift the lid. Locked. 
There are four digital locks. You tap one of them curiously. 
It lights up and displays this: 🌲You keep tapping and the plant displayed changes. Do you want to try inputting the code?""", "\n1: Input Code\n2: No Code yet. Back to living room", {1:31 , 2:2}, [], False],
    [28, """You go back to the living room. Where do you investigate now?""", "\n0: Check inventory\n1: Window \n2: Sofa \n3: Bed \n4: Chest \n5: Back to small room \n6: Back to the toilet", {1:4, 2:5, 3:26, 4:27, 5:29, 6:3}, [], False],
    [29, """You go back to the small room. Where do you go now? """,  "\n0: Check inventory\n1: Door + panel \n2: Safe \n3. Back to living room", {1:18, 2:24, 3:28}, [], False],
    [30, """Wrong code. Where do you go now?""", "\n0: Check inventory\n1: Door + panel \n2: Safe \n3. Back to living room", {1:18, 2:24, 3:28}, [], False],
    [31, "", "Enter code (Check inventory. Use 'Ctrl+C' and 'Ctrl+V') : ", {1:12, 2:2}, [], True, '🌸☘🍁🌺'],
    [32, "", "Enter code (Using keyboard) : ", {1:17, 2:2}, [], True, '%&@'],
    [33, "", "Where did you locate this key-card? ", {1:22, 2:17}, [], True, 'sofa']

]

scenario = 0
startTime = time.perf_counter()
while True:
    describe(scenario)
    if GAME_MAP[scenario][4]:
        a = GAME_MAP[scenario][4].pop(0)
        inventory.append(a)
    try:
        if GAME_MAP[scenario][5]:
            selection = checkpoint(scenario)
        else:
            selection = choice()
            while (selection > len(GAME_MAP[scenario][3])):
                print('\033[31m*\033[0m'*125)
                print('\033[31m>>> That choice is not available. Try again.\033[0m')
                print('\033[31m*\033[0m'*125)
                selection = choice()
    except ValueError:
        print('\033[31m*\033[0m'*125)
        print('\033[31m>>> Please key in a valid NUMBER corresponding to the choices given.\033[0m')
        print('\033[31m*\033[0m'*125)
        selection = choice()
    if selection == 0:
        selection = displayInventory(inventory)
    else:  
        scenario = GAME_MAP[scenario][3].get(selection)
    if scenario == 22:
        timeTaken = time.perf_counter()-startTime
        print(f"CONGRATULATIONS! You've escaped Level 1 in {timeTaken/60:.1f} minutes")
        break
    
