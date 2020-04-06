import random
import os
class TextAdventureGame:
    def __init__(self):
        self.y = 1
        self.x = 1
        self.start()

    def start(self):
        print("[p] play")
        print("[q] quit")
        command = input()
        print("")
        if command == 'p':
            room_size = 3
            self.play(room_size)
        elif command == 'q':
            pass
        else:
            print("Invalid command \n")
            self.start()

    def continue_playing(self, room_size):
        print("[c] continue")
        print("[q] quit")
        command = input()
        print("")
        if command == 'c':
            room_size += 1
            self.play(room_size)
        elif command == 'q':
            pass
        else:
            print("Invalid command \n")
            self.continue_playing(room_size)

    def play(self, room_size):
        self.y = random.randrange(1, room_size + 1)
        self.x = random.randrange(1, room_size + 1)
        key_y, key_x = self.key_placement(room_size)
        door_y, door_x = self.door_placement(key_y, key_x, room_size)
        turns = room_size * 2
        way_to_key = str(self.steps_to_key(key_x, key_y))
        print("You are in position [" + str(self.x) + ", " + str(self.y) + "] of a " + str(room_size) + " by " + str(room_size) + " room.")
        print("Find the key then the door to get out.")
        print("You have " + str(turns) + " turns to find both of them.")
        print("You are " + way_to_key + " steps away from the key. \n")
        print("[w] forward")
        print("[s] backward")
        print("[a] left")
        print("[d] right \n")
        all_the_movements = ["w", "a", "s", "d"]
        key_found = False
        door_found = False
        while (not key_found or not door_found) and turns > 0:
            choice = input()
            self.clear()
            if choice not in all_the_movements:
                print("Invalid input \n")
                turns += 1
            else:    
                movement_ret = self.movement(choice, room_size)
                if movement_ret == -1:
                    turns += 1
            print("Your position is: [" + str(self.x) + ", " + str(self.y) + "] \n")
            if key_y == self.y and key_x == self.x and not key_found:
                print("You found the key! \n")
                key_found = True
            if door_y == self.y and door_x == self.x and key_found == True:
                print("You got out of the room! \n")
                door_found = True
                break
            elif door_y == self.y and door_x == self.x and key_found == False:
                print("You found the door but need to find the key \n")
            turns -= 1
            if turns == 1:
                print("You have 1 turn left. \n")
            elif turns > 1:
                print("You have " + str(turns) + " turns left. \n")
            elif turns == 0:
                print("You suck and you LOSE and you smell like POO!!! \n")
                self.start()
            if not key_found:
                way_to_key = str(self.steps_to_key(key_x, key_y))
                print("You are " + way_to_key + " steps to the key")
        if door_found:
            self.continue_playing(room_size)
                

    def movement(self, choice, room_size):
        if choice == "w":
            self.y += 1
            if self.y > room_size:
                print("Unable to go any further forward. \n")
                self.y -= 1
                return -1
        elif choice == "s":
            self.y -= 1
            if self.y < 1:
                print("Unable to go any further backward. \n")
                self.y += 1
                return -1
        elif choice == "a":
            self.x -= 1
            if self.x < 1:
                print("Unable to go any further to the left. \n")
                self.x += 1
                return -1
        elif choice == "d":
            self.x += 1
            if self.x > room_size:
                print("Unable to go any further to the right. \n")
                self.x -= 1
                return -1
            
    def key_placement(self, room_size):
        key_y = random.randrange(1, room_size + 1)
        key_x = random.randrange(1, room_size + 1)
        if key_y == self.y and key_x == self.x:
            return self.key_placement(room_size)
        else:
            return key_y, key_x

    def door_placement(self, key_y, key_x, room_size):
        edge_size = ((room_size - 1) * 4) + 1
        edge_position = random.randrange(1, edge_size + 1)
        if edge_position <= room_size:
            door_x = 1
            door_y = edge_position
        elif edge_position > room_size and edge_position <= (room_size * 2) - 1:
            door_x = edge_position - (room_size - 1)
            door_y = room_size
        elif edge_position > (room_size * 2) - 1 and edge_position <= (room_size * 3) - 2:
            door_x = room_size
            door_y = ((room_size * 2) + (room_size - 1) - edge_position)
        else:
            door_x = (-1 * edge_position) + (3 * room_size) + (room_size - 2)
            door_y = 1
        if door_y == self.y and door_x == self.x or door_y == key_y and door_x == key_x:
            return self.door_placement(key_y, key_x, room_size)
        else:
            return door_y, door_x

    def clear(self):
        command = "clear"
        os.system(command)

    def steps_to_key(self, key_x, key_y):
        if self.x > key_x:
            if self.y > key_y:
                return (int(self.x) - int(key_x)) + (int(self.y) - int(key_y))
            else:
                return (int(self.x) - int(key_x)) + (int(key_y) - int(self.y))
        else:
            if self.y > key_y:
                return (int(key_x) - int(self.x)) + (int(self.y) - int(key_y))
            else:
                return (int(key_x) - int(self.x)) + (int(key_y) - int(self.y))

text_adventure_game = TextAdventureGame()
