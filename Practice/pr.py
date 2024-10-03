# def calculate_coins(amount, denominations):
#     # Create a DP table to store the minimum number of coins needed
#     dp_table = [float('inf')] * (amount + 1)
#     # Track the coins chosen for each amount
#     coins_chosen = [-1] * (amount + 1)
    
#     # Base case: No coins needed to make 0
#     dp_table[0] = 0
    
#     # Iterate over each denomination
#     for coin in denominations:
#         # For each coin, update the table for all amounts from coin to the target amount
#         for current_amount in range(coin, amount + 1):
#             if dp_table[current_amount - coin] + 1 < dp_table[current_amount]:
#                 dp_table[current_amount] = dp_table[current_amount - coin] + 1
#                 coins_chosen[current_amount] = coin

#     # If the amount can't be formed, return -1 and an empty list
#     if dp_table[amount] == float('inf'):
#         return -1, []
    
#     # Backtrack to find the coins used
#     result_set = []
#     while amount > 0:
#         result_set.append(coins_chosen[amount])
#         amount -= coins_chosen[amount]
    
#     # Return the minimum number of coins and the set of coins used
#     return dp_table[-1], result_set

# # Example usage:
# if _name_ == "_main_":
#     amount = int(input("Enter the amount: "))
#     denominations = [1, 4, 6]
    
#     coin_count, selected_coins = calculate_coins(amount, denominations)
    
#     if coin_count == -1:
#         print("It's not possible to form the amount with the given denominations.")
#     else:
#         print(f"Minimum number of coins: {coin_count}")
#         print(f"Coins used: {selected_coins}")



#### matrix chain multiplication
# def mcm(d):
#     n = len(d) - 1
    
#     # Initialize the table m to store minimum costs and s to store split points
#     m = {(i, j): float('inf') for i in range(1, n + 1) for j in range(i, n + 1)}
#     s = {}  # Stores the optimal split points
    
#     # Set the diagonal to 0, since multiplying one matrix requires no cost
#     for i in range(1, n + 1):
#         m[(i, i)] = 0

#     # Fill the table using a bottom-up approach
#     for l in range(2, n + 1):  # l is the chain length
#         for i in range(1, n - l + 2):  # i is the starting index
#             j = i + l - 1  # j is the ending index
#             for k in range(i, j):
#                 q = m[(i, k)] + m[(k + 1, j)] + d[i - 1] * d[k] * d[j]
#                 if q < m[(i, j)]:
#                     m[(i, j)] = q
#                     s[(i, j)] = k  # Store the split point

#     # Function to build the optimal parenthesization
#     def build_optimal_parens(s, i, j):
#         if i == j:
#             return f"M{i}"  # Single matrix
#         else:
#             k = s[(i, j)]
#             left_part = build_optimal_parens(s, i, k)
#             right_part = build_optimal_parens(s, k + 1, j)
#             return f"({left_part} x {right_part})"

#     # Function to display the cost matrix
#     def display_matrix(m, n):
#         print("\nCost Matrix (Minimum Multiplications):")
#         for i in range(1, n + 1):
#             for j in range(1, n + 1):
#                 if i > j:
#                     print("   -  ", end=" ")  # For invalid entries (i > j)
#                 else:
#                     print(f"{m[(i, j)]:6}", end=" ")
#             print()

#     # Call the function to return the optimal parenthesization
#     optimal_parens = build_optimal_parens(s, 1, n)

#     # Display the matrix
#     display_matrix(m, n)

#     return m[(1, n)], optimal_parens

# # Function to take input for matrix dimensions
# def take_input():
#     n = int(input("Enter the number of matrices: "))
#     dimensions = []
#     print("Enter the dimensions of matrices (for n matrices, provide n+1 dimensions):")
#     for i in range(n + 1):
#         dim = int(input(f"Dimension {i + 1}: "))
#         dimensions.append(dim)
#     return dimensions

# # Take input from the user
# dimensions = take_input()

# # Call the matrix chain multiplication function and print the result
# min_cost, optimal_parenthesization = mcm(dimensions)
# print(f"\nThe minimum number of multiplications is: {min_cost}")
# print(f"The optimal parenthesization is: {optimal_parenthesization}")


#knapsack x

# def knapsack(W,n,weights,profits):
#     table = [[0 for x in range(W+1)] for x in range(n+1)]
    
#     for i in range(1,n+1):
#         for j in range(w+1):
#             if weights[i-1] <= j:
#                 table[i][j]= max(table[i-1][j] , profits[i-1] + table[i-1][j-weights[i-1]])
#             else:
#                 table[i][j] = table[i-1][j]
            
#     max_profit = table[n][W]
#     return table, max_profit



# n = int(input("Enter Number of items: "))
# w = int(input("Enter weight of knapsack"))
# weights = list(map(int,input("Enter Weights: ").split()))
# profits = list(map(int,input("Enter ProfiysL ").split()))
# table , maxprofit = knapsack(w,n,weights,profits)
# for i in range(n+1):
#     print("\n")
#     for j in range(w+1):
#          print(f"{table[i][j]:6}", end=" ")
         
# print(f"\nmax profit {maxprofit}")



#p2_1 / 1 to N 
# import time
# import matplotlib.pyplot as plt
# import sys

# Increase the recursion limit
# sys.setrecursionlimit(1500)

# def sum_using_loop(N):
#     total = 0
#     for i in range(1, N + 1):
#         total += i
#     return total

# def sum_using_equation(N):
#     return N * (N + 1) // 2

# def sum_using_recursion(N):
#     if N == 0:
#         return 0
#     else:
#         return N + sum_using_recursion(N - 1)

# def measure_time(func, N):
#     start_time = time.time()
#     try:
#         func(N)
#     except RecursionError:
#         return None
#     end_time = time.time()
#     return end_time - start_time

# N_values = [10, 100, 1000, 5000, 10000, 50000, 100000]
# loop_times = []
# equation_times = []
# recursion_times = []

# for N in N_values:
#     loop_times.append(measure_time(sum_using_loop, N))
#     equation_times.append(measure_time(sum_using_equation, N))
#     recursion_time = measure_time(sum_using_recursion, N)
#     recursion_times.append(recursion_time if recursion_time is not None else float('inf'))

# plt.figure(figsize=(10, 6))
# plt.plot(N_values, loop_times, label='Loop', marker='o')
# plt.plot(N_values, equation_times, label='Equation', marker='o')
# plt.plot(N_values, recursion_times, label='Recursion', marker='o')
# plt.xlabel('N')
# plt.ylabel('Execution Time (seconds)')
# plt.title('Comparison of Execution Time for Sum Calculation')
# plt.legend()
# plt.grid(True)
# plt.yscale('log')
# plt.show()

#bunny

# import matplotlib.pyplot as plt

# n = int(input("Enter number of months: "))

# # Recursive function to calculate the number of rabbit pairs
# def no_of_Rabbit_using_recur(n):
#     global l1
#     l1 += 1
#     if n <= 2:
#         l1 += 1
#         return 1
#     else:
#         l1 += 1
#         return no_of_Rabbit_using_recur(n - 1) + no_of_Rabbit_using_recur(n - 2)

# # Iterative function to calculate the number of rabbit pairs
# def no_of_Rabbit_using_iter(n):
#     l2 = 1
#     n1 = 1
#     n2 = 1
#     if n > 2:
#         for i in range(n - 2):
#             l2 += 1
#             n3 = n1 + n2
#             n1 = n2
#             n2 = n3
#     return n2, l2

# # Lists to store loop counts
# loopcount1 = []
# loopcount2 = []

# # Loop through the number of months
# for i in range(1, n + 1):
#     l1 = 0
#     no_of_Rabbit_using_recur(i)
#     loopcount1.append(l1)
#     loopcount2.append(no_of_Rabbit_using_iter(i)[1])

# # Print results
# print("Total pairs (using recursive method): ", no_of_Rabbit_using_recur(n))
# print("Total steps (using recursive method): ", l1)
# print("Total pairs (using iteration method): ", no_of_Rabbit_using_iter(n)[0])
# print("Total steps (using iteration method): ", no_of_Rabbit_using_iter(n)[1])

# # Plotting the results
# arr = [x for x in range(1, n + 1)]
# plt.plot(arr, loopcount1, color='r', label="Using Recursion")
# plt.plot(arr, loopcount2, color='g', label="Using Iteration")
# plt.legend()
# plt.show()


## loops
# import time
# import random
# import matplotlib.pyplot as plt
# import io
# import base64

# # Bubble Sort Algorithm
# def bubblesort(arr):
#     n = len(arr)
#     count = 0
#     for i in range(n):
#         for j in range(n-i-1):
#             count += 1
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return count

# # Insertion Sort Algorithm
# def insertionsort(arr):
#     n = len(arr)
#     count = 0
#     for i in range(1, n):
#         key = arr[i]
#         j = i-1
#         while j >= 0 and key < arr[j]:
#             count += 1
#             arr[j+1] = arr[j]
#             j -= 1  
#         arr[j+1] = key
#     return count

# # Function to time and count steps of a sorting algorithm
# def count(sort_function, arr):
#     start_time = time.time()
#     count = sort_function(arr.copy())
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     return count, elapsed_time

# # Function to create graphs comparing sorting algorithms
# def graph(size, bubblecount, insertioncount, bubbletime, insertiontime):
#     fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

#     # Plot number of comparisons
#     ax1.plot(size, bubblecount, label='Bubble Sort', marker='o', color='b')
#     ax1.plot(size, insertioncount, label='Insertion Sort', marker='s', color='g')
#     ax1.set_xlabel('Number of Elements')
#     ax1.set_ylabel('Number of Comparisons')
#     ax1.set_title('Comparison of Sorting Algorithms')
#     ax1.legend()
#     ax1.grid(True)

#     # Plot execution time
#     ax2.plot(size, bubbletime, label='Bubble Sort', marker='o', color='b')
#     ax2.plot(size, insertiontime, label='Insertion Sort', marker='s', color='g')
#     ax2.set_xlabel('Number of Elements')
#     ax2.set_ylabel('Execution Time (seconds)')
#     ax2.set_title('Time Complexity')
#     ax2.legend()
#     ax2.grid(True)

#     plt.show()

# # Main execution
# if _name_ == '_main_':
#     userinput = input("Enter the sizes of arrays separated by commas: ")

#     try:
#         data_sizes = [int(size.strip()) for size in userinput.split(',')]

#         if all(size > 0 for size in data_sizes):
#             bubblecounts = []
#             insertioncounts = []

#             bubbletimes = []
#             insertiontimes = []

#             results = []

#             # Loop through each data size and apply sorting algorithms
#             for size in data_sizes:
#                 arr = [random.randint(1, 10000) for _ in range(size)]
#                 bubblecount, bubbletime = count(bubblesort, arr)
#                 insertioncount, insertiontime = count(insertionsort, arr)

#                 bubblecounts.append(bubblecount)
#                 insertioncounts.append(insertioncount)

#                 bubbletimes.append(bubbletime)
#                 insertiontimes.append(insertiontime)

#                 results.append({
#                     'size': size,
#                     'bubblecount': bubblecount,
#                     'bubbletime': bubbletime,
#                     'insertioncount': insertioncount,
#                     'insertiontime': insertiontime
#                 })

#             # Print results
#             for result in results:
#                 print(f"Array size: {result['size']}")
#                 print(f"Bubble Sort Comparisons: {result['bubblecount']}, Time: {result['bubbletime']:.6f} seconds")
#                 print(f"Insertion Sort Comparisons: {result['insertioncount']}, Time: {result['insertiontime']:.6f} seconds")
#                 print("-" * 50)

#             # Generate and display graphs
#             graph(data_sizes, bubblecounts, insertioncounts, bubbletimes, insertiontimes)

#         else:
#             print("Error: Please enter positive integer values.")
    
#     except ValueError:
#         print("Error: Invalid input. Please enter numbers separated by commas.")



# Dynamic Programming Python implementation of Matrix
# Chain Multiplication. See the Cormen book for details
# of the following algorithm
import sys

# Matrix Ai has dimension p[i-1] x p[i] for i = 1..n
def MatrixChainOrder(p, n):
	# For simplicity of the program, one extra row and one
	# extra column are allocated in m[][]. 0th row and 0th
	# column of m[][] are not used
	m = [[0 for x in range(n)] for x in range(n)]

	# m[i, j] = Minimum number of scalar multiplications needed
	# to compute the matrix A[i]A[i + 1]...A[j] = A[i..j] where
	# dimension of A[i] is p[i-1] x p[i]

	# cost is zero when multiplying one matrix.
	for i in range(1, n):
		m[i][i] = 0

	# L is chain length.
	for L in range(2, n):
		for i in range(1, n-L + 1):
			j = i + L-1
			m[i][j] = sys.maxsize
			for k in range(i, j):

				# q = cost / scalar multiplications
				q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j]
				if q < m[i][j]:
					m[i][j] = q

	return m[1][n-1]

# Driver program to test above function
arr = [4,10,3,12,20,7]
size = len(arr)

print("Minimum number of multiplications is " +
	str(MatrixChainOrder(arr, size)))
# This Code is contributed by Bhavya Jain
