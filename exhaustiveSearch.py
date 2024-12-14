import time  # Import the time module for tracking performance

# 2DGRID (.=passable, X=Blocked)
def soccer_exhaustive(grid):
    rows = len(grid)     # Number of rows
    # print(rows)
    cols = len(grid[0])  # Number of columns
    # print(cols)

    # Total moves needed: (r - 1:moves down, c - 1:moves right)
    total_moves = (rows - 1) + (cols - 1)

    # Keeps track of each valid path found
    valid_paths_count = 0

    # Generate all possible binary numbers: 0=movedown, 1=moveright
    # EX:   0000: down,down,down,down
    #       0001: down,down,down,right
    #       0010: down,down,right,down etc... 
    for bits in range(2 ** total_moves):  # Use multiplication for 2 ** total_moves
        row, col = 0, 0  # Start position
        is_valid = True  # Path is valid starting    

        # Process the path represented by the current binary number
        for i in range(total_moves):
            if bits & (1 << i):  # If the i-th bit is 1, move right
                col += 1
            else:  # If the i-th bit is 0, move down
                row += 1

            # Check if the move is out of bounds or hits an obstacle
            if row >= rows or col >= cols or grid[row][col] == 'X':
                is_valid = False
                break

        # If the path is valid and ends at the bottom-right corner, count it
        if is_valid and row == rows - 1 and col == cols - 1:
            valid_paths_count += 1

    return valid_paths_count


# PERFORMANCE TESTING
def performance_test(grid, description):
    print(f"Testing {description}...")

    # Measure time for exhaustive search
    start_time = time.time()
    result = soccer_exhaustive(grid)
    end_time = time.time()

    # Calculate elapsed time
    elapsed_time = end_time - start_time
    print(f"Number of valid paths: {result}")
    print(f"Exhaustive search time: {elapsed_time:.6f} seconds\n")
    return elapsed_time

# From Project2 Document
exampleGrid = [
    ['.', '.', '.', '.', '.', '.', 'X', '.', 'X'],
    ['X', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'X', '.', '.', '.', 'X', '.'],
    ['.', '.', 'X', '.', '.', '.', '.', 'X', '.'],
    ['.', 'X', '.', '.', '.', '.', 'X', '.', '.'],
    ['.', '.', '.', '.', 'X', '.', '.', '.', '.'],
    ['.', '.', 'X', '.', '.', '.', '.', '.', 'X'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.']
]

# Extra Grids for testing:
grid_2x2 = [
    ['.', '.'],
    ['.', '.']
]

grid3x3 = [
    ['.', '.', '.'],
    ['.', 'X', '.'],
    ['.', '.', '.']
]
grid4x4= [
    ['.', '.', '.', '.'],
    ['.', 'X', '.', '.'],
    ['.', '.', 'X', '.'],
    ['.', '.', '.', '.']
]

grid6x6 = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', 'X', '.', '.', '.'],
    ['.', '.', '.', 'X', '.', '.'],
    ['.', 'X', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'X', '.'],
    ['.', '.', '.', '.', '.', '.']
]

grid8x8 = [
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', 'X', '.', '.', '.', '.', '.', '.'],
    ['.', '.', 'X', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'X', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'X', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'X', '.', '.'],
    ['.', '.', '.', '.', '.', '.', 'X', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.']
]

grid10x10 = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', 'X', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', 'X', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'X', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'X', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'X', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', 'X', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', 'X', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'X', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]

grid_12x12 = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', '.'],
    ['.', '.', '.', 'X', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'X', '.', '.', '.'],
    ['X', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
]

# Run Performance Tests
time1 = performance_test(exampleGrid, "Example Grid:")
time2 = performance_test(grid_2x2, "Test2: Grid 2x2")
time3 = performance_test(grid3x3, "Test3: Grid 3x3")
time4 = performance_test(grid4x4, "Test4: Grid 4x4")
time5 = performance_test(grid6x6, "Test5: Grid 6x6")
time6 = performance_test(grid8x8, "Test6: Grid 8x8")
time6 = performance_test(grid10x10, "Test7: Grid 10x10")
time6 = performance_test(grid_12x12, "Test7: Grid 12x12")
