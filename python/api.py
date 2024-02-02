import data_utils
from problem import LeetcodeProblem

SOLUTION_NAME_TO_PROBLEM_NAME = {}

def get_random_problem():
    problem_name = data_utils.get_random_problem()
    lc_problem= data_utils.get_leetcode_problem_from_name(problem_name)
    SOLUTION_NAME_TO_PROBLEM_NAME[lc_problem.solution.__name__] = lc_problem.name
    return lc_problem

def get_problem_from_solution(solution:str) -> LeetcodeProblem:
    name = SOLUTION_NAME_TO_PROBLEM_NAME[solution.__name__]
    return data_utils.get_leetcode_problem_from_name(name)


def submit(solution):
    problem = get_problem_from_solution(solution)
    return problem.test_user_input(solution)