from robot import Robot
from course import map_matrix
from course import goal

def main():

    robo = Robot(start_position = (0, 0))

    print("ROBO NAV SIM")
    print("CONTROLS: w = up, s = down, a = left, d = right, , m = show map, q = quit")
    print(robo)
    print("**********************")

    while True:
        command = input("traverse: ").lower()

        if command == "q":
            print("simulation terminated.")
            break

        if command == "m":
            # list comprehension to copy map
            temp_map = [row[:] for row in map_matrix]

            # robo curr pos = 2
            x, y = robo.get_position()
            temp_map[x][y] = 2

            # print map
            print(temp_map[0])
            print(temp_map[1])
            print(temp_map[2])
            print(temp_map[3])
            print(temp_map[4])
            command = "to show map"
            
        moved = robo.move(command)
        
        # overwrite command for lazy displaying. prob bad for perfomance
        if command == "w":
            command = "up"
        if command == "s":
            command = "down"
        if command == "a":
            command = "left"
        if command == "d":
            command = "right" 
        
        if moved:
            print(f"Moved {command}. {robo}")
        else:
            print("Blocked. Obstacle or boundary.")
        
        # goal check
        if robo.get_position() == goal:
            print("*#*#*#*#*#*#| GOAL |#*#*#*#*#*#*")
            break

if __name__ == "__main__":
    main()