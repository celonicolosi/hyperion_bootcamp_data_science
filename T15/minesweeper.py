# using the same input as the example of input in exercise description
minefield = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"],
]

def mine_sweeper(grid):
    # getting the length of the rows and columns
    rows = len(grid)
    cols = len(grid[0])

    # variable to store the new 2D list
    new_grid = []

    # iterating through the rows and columns
    for r in range(rows):
        new_row = []
        for c in range(cols):
            if grid[r][c] == '-':
                # variable to store the count of surrounding mines
                count = 0
                # iterating through the surrounding cells using max and min to avoid go out of bounds
                for r2 in range(max(0, r-1), min(rows, r+2)):
                    for c2 in range(max(0, c-1), min(cols, c+2)):
                        if grid[r2][c2] == '#':
                            count += 1
                # appending the count to the new grid
                new_row.append(str(count))
            else:
                # if the cell is a mine, just append it to the new grid
                new_row.append('#')        
        # after iterating through the columns, append the row to the new grid
        new_grid.append(new_row)
    return new_grid

# in order to not print the list as a list of lists, we can iterate through the list and print each row
for row in mine_sweeper(minefield):
    print(row)

# but if you want to print it as a list of lists, just uncomment the line below
# print(mine_sweeper(minefield))