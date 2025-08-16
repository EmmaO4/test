# list of lists 5 x 5 2d map matrix
# 0: free, 1: obstacle
map_matrix = [
    [0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

# map_matrix[4][4] didn't work because is just a look up
goal = (4, 4)

# more advanced
# class Course:
#     def __init__(self, matrix):
#         self.matrix = matrix
#         self.rows = len(matrix)
#         self.cols = len(matrix[0])

#     def is_valid_position(self, row, col):
#         """Check if a position is within bounds and not an obstacle."""
#         if 0 <= row < self.rows and 0 <= col < self.cols:
#             return self.matrix[row][col] == 0
#         return False

#     def display(self, robot_position=None):
#         """Prints the course with robot (R), obstacles (X), and free space (.)."""
#         for r in range(self.rows):
#             row_display = ""
#             for c in range(self.cols):
#                 if robot_position and (r, c) == tuple(robot_position):
#                     row_display += " R "
#                 elif self.matrix[r][c] == 1:
#                     row_display += " X "
#                 else:
#                     row_display += " . "
#             print(row_display)
#         print()