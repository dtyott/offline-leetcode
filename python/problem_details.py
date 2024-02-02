from typing import List
import input_generators
import problem
import data_utils
import solution_generators

###number of islands 
number_of_islands_name = 'Number of Islands'
number_of_islands_description = '''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''

### sort a list

sort_a_list_name = 'Sorting a List'
sort_a_list_description = 'Sort the input list and return it'


##container water

container_water_name = 'Container With Most Water'
container_water_description = '''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 
Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

'''



PROBLEMS = {
    number_of_islands_name: {
        'name': number_of_islands_name,
        'description': number_of_islands_description,
        'inputs': input_generators.islands_input_generator(test_cases = 100),
        'solution': solution_generators.numIslands,
        'difficulty': 'MEDIUM'
    },
    sort_a_list_name: {
        'name': sort_a_list_name,
        'description': sort_a_list_description,
        'inputs': input_generators.generic_int_list_generator(test_cases=100),
        'solution': solution_generators.sortAList,
        'difficulty': 'EASY'
    },
    container_water_name: {
        'name': container_water_name,
        'description': container_water_description,
        'inputs': input_generators.generic_int_list_generator(test_cases=100, max_size = 50),
        'solution': solution_generators.maxArea,
        'difficulty': 'MEDIUM'
    }
}

if __name__ == '__main__':
    for name, details in PROBLEMS.items():
        lc_problem = problem.get_leetcode_problem_from_details(details)
        data_utils.pickle_leetcode_problem(lc_problem)