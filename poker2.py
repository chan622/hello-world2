from itertools import combinations, permutations
import time
import pandas as pd
import numpy as np

### Generate all poker cards
all_suits = ['club','diamond','heart','spade']
all_ranks = [str(i) for i in range(2,11)] + ['J','Q','K','A']
pokers = [i+'-'+j for i in all_suits for j in all_ranks]

#### Solution 2: Statistical solution
tStart = time.time()
N = 100000
k = 5
count = 0 ## To count if consecutive suits occur
found = False

for i in range(N):
    hand = np.random.choice(pokers, k, replace=False)
    suits = []
    for card in hand:
        s, _ = card.split('-')
        suits.append(s)

    for i in range(k-1):
        if suits[i]==suits[i+1]:
            count += 1
            break

print(str((N-count)/N*100)+ '%')

tEnd = time.time()
print("The program costs", (tEnd-tStart), "sec")


#### Question 2
# #### Solution 1 : Memory Error
# tStart = time.time()
#
# all_permutations = list(permutations(pokers,5))
# print(all_permutations)
#
# def no_consecutive_suits(cards):
#     suits = []
#     for card in cards:
#         s, _ = card.split('-')
#         suits.append(s)
#     for i in range(len(suits)-1):
#         if suits[i] == suits[i+1]:
#             return False
#     return True
#
# num_of_no_consecutive = 0
# for cards in all_permutations:
#     if no_consecutive_suits(cards):
#         num_of_no_consecutive += 1
#
# print(num_of_no_consecutive)
#
# tEnd = time.time()
# print("The program costs", (tEnd-tStart), "sec")
# ####
