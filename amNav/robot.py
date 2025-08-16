from course import map_matrix

class Robot:

    def __init__(self, start_position = (0, 0)):
        self.position = list(start_position)  # [row, col]

    def move(self, direction):
        new_row, new_col = self.position

        if direction == "w":  # up
            new_row -= 1
        elif direction == "s":  # down
            new_row += 1
        elif direction == "a":  # left
            new_col -= 1
        elif direction == "d":  # right
            new_col += 1

        # Check boundaries
        if 0 <= new_row < len(map_matrix) and 0 <= new_col < len(map_matrix[0]):
            if map_matrix[new_row][new_col] == 0:  # not an obstacle
                self.position = [new_row, new_col]
                return True  # Move successful
        return False  # Move blocked

    def get_position(self):
        return tuple(self.position)

    def __str__(self):
        return f"Currently at coords: {self.position}"