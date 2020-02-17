from itertools import combinations, permutations
import time
import pandas as pd

### Generate all poker cards
all_suits = ['club','diamond','heart','spade']
all_ranks = [str(i) for i in range(2,11)] + ['J','Q','K','A']
pokers = [i+'-'+j for i in all_suits for j in all_ranks]

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

#### Solution 2
tStart = time.time()

num_of_all_permutation = 52*51*50*49*48

suits = []
for card in pokers:
    s, _ = card.split('-')
    suits.append(s)


tEnd = time.time()
print("The program costs", (tEnd-tStart), "sec")
