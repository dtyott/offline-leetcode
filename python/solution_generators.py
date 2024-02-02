from typing import List

def numIslands(grid: List[List[str]]) -> int:
    visited = {}
    num_islands = 0
    water = "1"
    num_rows = len(grid)
    num_cols = len(grid[0])
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            pt = (i, j)
            if pt not in visited:
                if grid[i][j]==water:
                    num_islands+=1
                    visited[pt] = True
                    S = [pt]
                    while(S):
                        head = S.pop()
                        r,c = head
                        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
                        nbs = [(r+dr, c+dc) for dr,dc in dirs if (0<=r+dr<num_rows) and (0<=c+dc<num_cols)]
                        for nb in nbs:
                            r_nb, c_nb = nb
                            val_nb = grid[r_nb][c_nb]
                            if (val_nb == water) and (nb not in visited):
                                visited[nb] = True
                                S.append((r_nb, c_nb))
    return num_islands


def sortAList(l):
    return sorted(l)


def maxArea(height: List[int]) -> int:
    first_height = []
    for i,h in enumerate(height):
        if (not first_height) or (h>first_height[-1][0]):
            new_tup = (h,i)
            first_height.append(new_tup)
    
    max_water = 0
    end_index = len(height)-1
    while(end_index>=0 and first_height):
        end_height = height[end_index]
        first_height_val, first_height_ind = first_height[0]
        water_height = min(first_height_val, end_height)
        max_water = max(max_water, (end_index - first_height_ind)*water_height)
        if end_height>=first_height_val:
            first_height.pop(0)
        else:
            end_index+=-1
    return max_water