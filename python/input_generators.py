from inputs import LeetcodeInput
import numpy as np


def islands_input_generator(test_cases = 100, min_rows=1, max_rows = 100, min_cols = 1, max_cols = 100, values = ["0","1"]):
    results = []
    for _ in range(test_cases):
        rows = np.random.randint(min_rows, max_rows)
        cols = np.random.randint(min_cols, max_cols)
        results.append(LeetcodeInput([[np.random.choice(values) for _ in range(cols)] for _ in range(rows)]))

    return results


def generic_int_list_generator(test_cases = 100, min_len=2, max_len=100,  min_size = 1, max_size = 10_000):
    return [LeetcodeInput([np.random.randint(min_size, max_size) for _ in range(np.random.randint(min_len, max_len))]) for _ in range(test_cases)]