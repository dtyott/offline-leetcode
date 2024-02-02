import os
import pickle
import numpy as np

DATA_PATH = os.path.abspath(os.path.join(__file__,  "..",'..', 'data'))

def pickle_leetcode_problem(leetcode_problem):
    name = leetcode_problem.name
    path = os.path.join(DATA_PATH, name)
    results_path = os.path.join(path, 'submissions')
    pickle_filename = os.path.join(path, 'problem.p')
    try:
        os.mkdir(path)
        os.mkdir(results_path)
    except:
        print(f'{name} already exists in {DATA_PATH}')

    with open(pickle_filename, "wb") as f:
        pickle.dump(leetcode_problem, f)
    
    return


def get_problem_names():
     return os.listdir(DATA_PATH)


def get_random_problem():
     return np.random.choice(get_problem_names())


def get_submissions_for_problem(problem_name):
     submissions_path = os.path.join(DATA_PATH, problem_name, 'submissions')
     return [os.path.join(submissions_path,x) for x in os.listdir(submissions_path)]


def load_submissions_for_problem(problem_name):
     abs_paths = get_submissions_for_problem(problem_name)
     return [load_problem_submission(p) for p in abs_paths]


def pickle_problem_submission(problem_name, result):
     prev_submissions = get_submissions_for_problem(problem_name)
     submission_filename = os.path.join(DATA_PATH, problem_name, 'submissions', f'{len(prev_submissions)+1}.p')
     with open(submission_filename, "wb") as f:
          pickle.dump(result, f)


def load_problem_submission(submission_abs_path):
    with open(submission_abs_path, "rb") as f:
        result = pickle.load(f)
    return result
     

def get_leetcode_problem_from_name(name: str):
    path = os.path.join(DATA_PATH, name)
    pickle_filename = os.path.join(path, 'problem.p')
    with open(pickle_filename, "rb") as f:
        result = pickle.load(f)
    return result