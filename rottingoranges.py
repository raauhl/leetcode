def oranges_rotting(grid):

    m = len(grid)
    n = len(grid[0])
    empty, fresh, rotten = 0, 1, 2

    def get_fresh_neighbours(i, j):
        neighbours = []
        fresh_neighbours = []
        if 0 <= i-1 < m and 0 <= j < n:
            neighbours.append((i-1, j))
        if 0 <= i < m and 0 <= j+1 < n:
            neighbours.append((i, j+1))
        if 0 <= i+1 < m and 0 <= j < n:
            neighbours.append((i+1, j))
        if 0 <= i < m and 0 <= j-1 < n:
            neighbours.append((i, j-1))
        for (i,j) in neighbours:
            if grid[i][j] == fresh:
                fresh_neighbours.append((i,j))
        return fresh_neighbours

    curr = set()
    fresh_oranges = set()
    minutes = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == rotten:
                curr.add((i,j))
            elif grid[i][j] == fresh:
                fresh_oranges.add((i,j))
    
    while True:
        next_curr = set()
        for (i, j) in curr:
            fresh_neighbours = get_fresh_neighbours(i,j)
            for (x, y) in fresh_neighbours:
                grid[x][y] = rotten
                fresh_oranges.remove((x, y))
                next_curr.add((x, y))
        if len(next_curr) == empty:
            break
        minutes += 1
        curr = next_curr
    
    return minutes if len(fresh_oranges) == 0 else -1
            
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(oranges_rotting(grid))

grid = [[2,1,1],[0,1,1],[1,0,1]]
print(oranges_rotting(grid))