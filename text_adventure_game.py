import random
class TextAdventureGame:
    def __init__(self):
        self.up_down = 1
        self.left_right = 1
        self.start()

    def start(self):
        print("[p] play")
        print("[q] quit")
        command = input()
        print("")
        if command == 'p':
            self.play()
        elif command == 'q':
            pass
        else:
            print("Invalid command \n")
            self.start()

    def play(self):
        print("You are in position [1,1] of a 3 by 3 room.")
        print("Find the key then the door to get out. \n")
        print("[w] forward")
        print("[s] backward")
        print("[a] left")
        print("[d] right \n")
        all_the_movements = ["w", "a", "s", "d"]
        self.up_down = 1
        self.left_right = 1
        key_found = False
        door_found = False
        key_up_down, key_left_right = self.key_placement()
        door_up_down, door_left_right = self.door_placement(key_up_down, key_left_right)
        while key_found == False or door_found == False:
            choice = input()
            if choice not in all_the_movements:
                print("Invalid input \n")
            self.movement(choice)
            print("Your position is: [" + str(self.left_right) + ", " + str(self.up_down) + "] \n")
            
            if key_up_down == self.up_down and key_left_right == self.left_right:
                print("You found the key! \n")
                key_found = True
            if door_up_down == self.up_down and door_left_right == self.left_right and key_found == True:
                print("You found the door!")
                door_found = True
            elif door_up_down == self.up_down and door_left_right == self.left_right and key_found == False:
                print("You found the door but need to find the key \n")
                

    def movement(self, choice):
        if choice == "w":
            self.up_down += 1
            if self.up_down > 3:
                print("Unable to go any further forward. \n")
                self.up_down -= 1
            else:
                pass
        elif choice == "s":
            self.up_down -= 1
            if self.up_down < 1:
                print("Unable to go any further backward. \n")
                self.up_down += 1
            else:
                pass
        elif choice == "a":
            self.left_right -= 1
            if self.left_right < 1:
                print("Unable to go any further to the left. \n")
                self.left_right += 1
            else:
                pass
        elif choice == "d":
            self.left_right += 1
            if self.left_right > 3:
                print("Unable to go any further to the right. \n")
                self.left_right -= 1
            else:
                pass
            
    def key_placement(self):
        key_up_down = random.randrange(1, 4)
        key_left_right = random.randrange(1, 4)
        if key_up_down == 1 and key_left_right == 1:
            self.key_placement()
        else:
            return key_up_down, key_left_right

    def door_placement(self, key_up_down, key_left_right):
        door_up_down = random.randrange(1, 4)
        door_left_right = random.randrange(1, 4)
        if door_up_down == 1 and door_left_right == 1 or door_up_down == key_up_down and door_left_right == key_left_right:
            self.door_placement(key_up_down, key_left_right)
        else:
            return door_up_down, door_left_right 
        

text_adventure_game = TextAdventureGame()
