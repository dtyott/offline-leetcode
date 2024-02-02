import numpy as np

class LeetcodeAllowedValue:

    ALLOWED_TYPES = [str, list, float, int, type(None), np.str_, np.int_]

    def __init__(self, input):
        self.value = input
        self.validate_inputs()

    
    def validate_inputs(self):
        input_value = self.value
        self.validate_single_value(input_value, 0)
        
    def validate_single_value(self, val, depth):
        if depth ==3:
            raise Exception("Maximum depth exceeded for LeetCode Input/Output, shouldn't be nested >2 levels deep")

        if isinstance(val, list):
            for x in val:
                self.validate_single_value(x, depth+1)

        elif type(val) in self.ALLOWED_TYPES:
            return True
        
        else:
            raise Exception(f"Unexpected type {type(val)} not an allowed type: {self.ALLOWED_TYPES}")

class LeetcodeInput(LeetcodeAllowedValue):
    pass

class LeetcodeOutput(LeetcodeAllowedValue):
    pass


def generate_list_int(nums, min, max):
    return LeetcodeInput([np.random.randint(min, max) for _ in range(nums)])
