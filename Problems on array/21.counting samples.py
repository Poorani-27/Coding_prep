'''Problem Statement: Given an array samples[] denoting sizes of rock samples and a 2D array ranges[], the task is to count the rock samples that are in the range ranges[i][0] to ranges[i][1], for every possible 1 <= i <= N.

Examples:

Input: samples[] = {345, 604, 321, 433, 704, 470, 808, 718, 517, 811}, ranges[] = {{300, 380}, {400, 700}}
Output: 2 4
Explanation: 
Range [300, 380]: Samples {345, 321} lie in the range. Therefore, the count is 2. 
Range [400, 700]: Samples {433, 604, 517, 470} lie in the range. Therefore, the count is 4.'''

def counting(samples, ranges):
    counts = []
    for r in ranges:
        count = 0
        for sample in samples:
            if r[0] <= sample <= r[1]:
                count += 1
        counts.append(count)
    return counts

samples = [345, 604, 321, 433, 704, 470, 808, 718, 517, 811]
ranges = [[300, 380], [400, 700]]
output = counting(samples, ranges)
print(output)
