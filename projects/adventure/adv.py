from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = r"C:\Users\iulia\Desktop\CS_2\Graphs\projects\adventure\maps\test_line.txt"
# map_file = r"C:\Users\iulia\Desktop\CS_2\Graphs\projects\adventure\maps/test_cross.txt"
# map_file = r"C:\Users\iulia\Desktop\CS_2\Graphs\projects\adventure\maps/test_loop.txt"
# map_file = r"C:\Users\iulia\Desktop\CS_2\Graphs\projects\adventure\maps/test_loop_fork.txt"
map_file = r"C:\Users\iulia\Desktop\CS_2\Graphs\projects\adventure\maps\main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
# print(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
# print(player)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()
explored = {}
player.current_room = world.starting_room
# visited_rooms.add(player.current_room)
# print(player.current_room)

s = Stack()
s.push(player.current_room)


while s.size() > 0:
    player_room = s.pop()
    print("CURRENT ROOM:", player_room)


    if player_room not in visited_rooms:
        visited_rooms.add(player_room)

        for direction in player.current_room.get_exits():
            if player_room.get_room_in_direction(direction) != None:
                # traversal_path.append(direction)
                s.push(player_room.get_room_in_direction(direction))
  
            traversal_path.append(direction)



# print(traversal_path)
# print(len(visited_rooms))


for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)#

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# ######
# # UNCOMMENT TO WALK AROUND
# ######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
