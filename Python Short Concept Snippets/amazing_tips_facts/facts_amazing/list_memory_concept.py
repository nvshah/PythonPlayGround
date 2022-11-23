import sys

# ! -> List Size doesnt determine how much memory it will Consume

l1 = [0, 0, 0]  # seperate object
l2 = [0] * 8
l3 = [0] * 3   # repeat

print(sys.getsizeof(l1))  # 120
print(sys.getsizeof(l2))  # 120
print(sys.getsizeof(l3))  # 80    // much lesser than l1
