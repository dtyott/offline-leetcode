import typing
from enum import Enum
from test_case import TestCase
from inputs import LeetcodeInput, LeetcodeOutput
import timeit
import datetime
import data_utils
import getpass
from inspect import signature


class LeetcodeDifficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


class LeetcodeStatus(Enum):
    PASS = 1
    FAIL = 2

class LeetcodeResult:

    def __init__(self, name, status, num_test_cases, passing_test_cases, time, breaking_input, user_wrong_output, correct_output):
        self.name = name
        self.status = status
        self.num_test_cases = num_test_cases
        self.passing_test_cases = passing_test_cases
        self.time = time
        self.passing_percent = self.passing_test_cases/self.num_test_cases
        self.username = getpass.getuser()
        self.timestamp =  datetime.datetime.now()
        self.breaking_input = breaking_input
        self.user_wrong_output = user_wrong_output
        self.correct_output = correct_output
        
    def summary(self):
        initial_status = f'{self.status}: {self.passing_test_cases}/{self.num_test_cases} test cases passed.\n'
        wrong_answer = f'Input: {self.breaking_input}\nExpected Answer: {self.correct_output}\nYour Answer: {self.user_wrong_output}.\n'
        submissions = data_utils.load_submissions_for_problem(self.name)
        successful_submissions = [ s for s in submissions if s.status == LeetcodeStatus.PASS ]
        fastest_submission = min([s.time for s in successful_submissions if s is not None ], default = None)
        fast_message = f'Fastest Solution: {round(fastest_submission,2)}s\n' if fastest_submission else None
        attempts = f'Attempts: {len(submissions)}'
        return f'{initial_status}{wrong_answer if self.breaking_input else ""}{fast_message if fastest_submission else ""}{attempts}'

class LeetcodeProblem:

    def __init__(self, name: str, 
                 description: str, 
                 difficulty: LeetcodeDifficulty, 
                 test_cases: typing.List[TestCase],
                 solution: typing.Callable[[LeetcodeInput], LeetcodeOutput]
                 ):
        self.name = name
        self.description = description
        self.difficulty = difficulty
        self.test_cases = test_cases
        self.solution = solution


    def __repr__(self):
        single_quote = "'"
        first_line = f"{self.name}: ({self.difficulty.name})"
        return f"{3*single_quote}\n{first_line}\n{self.description}\n{3*single_quote}"
    
    def getting_started(self):
        code_samples = f"\n\n\n#leetcode.test({self.solution.__name__}, test_case) #submit a test case\n#leetcode.submit({self.solution.__name__}) #submit your answer"
        return str(self) + f"\n\ndef {self.solution.__name__}{signature(self.solution)}:\n    ##Insert Solution Here :)\n    pass\n{code_samples}"
    
    def test_user_input(self, user_input: typing.Callable[[LeetcodeInput], typing.Any], pickle_result = True):
        correct = 0
        test_cases = self.test_cases
        num_test_cases = len(test_cases)
        breaking_input = None
        user_wrong_output = None
        correct_output = None

        a = timeit.default_timer()
        for test_case in test_cases:
            test_input = test_case.input
            expected_output = test_case.output
            user_output = LeetcodeOutput(user_input(test_input.value))
            if user_output.value == expected_output.value:
                correct+=1
            else:
                breaking_input = test_input.value
                correct_output = expected_output.value
                user_wrong_output = user_output.value
                break
        
        b = timeit.default_timer()
        
        if correct == num_test_cases:
            status = LeetcodeStatus.PASS
        else:
            status = LeetcodeStatus.FAIL

        result =  LeetcodeResult(self.name, status, num_test_cases, correct, b-a, breaking_input, user_wrong_output, correct_output)
    
        if pickle_result:
            data_utils.pickle_problem_submission(self.name, result)
        print(result.summary())
    

    def get_submissions_for_problem(self):
        data_utils.load_submissions_for_problem(self.name)

    
    def test_custom_user_input(self, user_test_case: LeetcodeInput):
        user_value = user_test_case.value
        solution = self.solution
        correct_answer = LeetcodeOutput(solution(user_value))
        return correct_answer


def get_leetcode_problem_from_details(details):
    name = details['name']
    description = details['description']
    inputs = details['inputs']
    solution = details['solution']
    difficulty = getattr(LeetcodeDifficulty,details['difficulty'])

    test_cases = []

    for input in inputs:
        output = LeetcodeOutput(solution(input.value))
        test_case = TestCase(input, output)
        test_cases.append(test_case)

    return LeetcodeProblem(name, description, difficulty, test_cases, solution)