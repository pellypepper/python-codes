"""
a simple program that take in a grid and return a grid where each dash
is replaced by the number of mines in the surrounding cells
"""

def mine_sweeper(grid):

    new_grid = []
    col = len(grid[0]) # get the length of the first row
    row = len(grid) # get the length of the grid
 
    directions = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1] ,[0, 1],
        [1, -1], [1, 0], [1, 1]
    ]


    for rows in range(row): # loop through the rows

        temp_grid = []
        for cols in range(col): # loop through the columns
        
            if grid[rows][cols] == "#":     # check if the cell is a mine 
                temp_grid.append("#")
           
            else :  # check if the cell is a dash
                count = 0
                for dr , dc in directions:
                    # check if the cell is within the grid
                    new_row, new_col = rows + dr, cols + dc
                    if 0 <= new_row < row and 0 <= new_col < col:
                      if grid[new_row][new_col] == "#":
                         count += 1
                # append the count to the temp_grid
                temp_grid.append(count)
        # append the temp_grid to the
        new_grid.append(temp_grid)
    return   new_grid

grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

# call the function and print the result
result = mine_sweeper(grid)

for row in result:
    print(row)