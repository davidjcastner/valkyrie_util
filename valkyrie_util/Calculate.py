class Calculate:
    '''formulas for fast calculations'''

    @staticmethod
    def range_sum_int(start: int, end: int, divisor: int = 1) -> int:
        '''returns the sum of all integers in the range [start, end] that are divisible by the divisor'''
        calc_start = (min(start, end) + divisor - 1) // divisor
        calc_end = max(start, end) // divisor
        return ((calc_start + calc_end) * (calc_end - calc_start + 1) // 2) * divisor
