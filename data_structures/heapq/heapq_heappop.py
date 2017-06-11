import heapq
from headpq_showtree import show_tree
from heapq_heapdata import data

print('random:', data)
heapq.heapify(data)

print('heapified:')
show_tree(data)

print

for i in range(2):
    smallest = heapq.heappop(data)
    print('pop   {:>3}'.format(smallest))
    show_tree(data)
