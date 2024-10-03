def mcm(d):
    n = len(d) - 1
    
    # Initialize the table m to store minimum costs and s to store split points
    m = {(i, j): float('inf') for i in range(1, n + 1) for j in range(i, n + 1)}
    s = {}  # Stores the optimal split points
    
    # Set the diagonal to 0, since multiplying one matrix requires no cost
    for i in range(1, n + 1):
        m[(i, i)] = 0

    # Fill the table using a bottom-up approach
    for l in range(2, n + 1):  # l is the chain length
        for i in range(1, n - l + 2):  # i is the starting index
            j = i + l - 1  # j is the ending index
            for k in range(i, j):
                q = m[(i, k)] + m[(k + 1, j)] + d[i - 1] * d[k] * d[j]
                if q < m[(i, j)]:
                    m[(i, j)] = q
                    s[(i, j)] = k  # Store the split point

    # Function to build the optimal parenthesization
    def build_optimal_parens(s, i, j):
        if i == j:
            return f"M{i}"  # Single matrix
        else:
            k = s[(i, j)]
            left_part = build_optimal_parens(s, i, k)
            right_part = build_optimal_parens(s, k + 1, j)
            return f"({left_part} x {right_part})"

    # Function to display the cost matrix
    def display_matrix(m, n):
        print("\nCost Matrix (Minimum Multiplications):")
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i > j:
                    print("   -  ", end=" ")  # For invalid entries (i > j)
                else:
                    print(f"{m[(i, j)]:6}", end=" ")
            print()

    # Call the function to return the optimal parenthesization
    optimal_parens = build_optimal_parens(s, 1, n)

    # Display the matrix
    display_matrix(m, n)

    return m[(1, n)], optimal_parens

# Function to take input for matrix dimensions
def take_input():
    n = int(input("Enter the number of matrices: "))
    dimensions = []
    print("Enter the dimensions of matrices (for n matrices, provide n+1 dimensions):")
    for i in range(n + 1):
        dim = int(input(f"Dimension {i + 1}: "))
        dimensions.append(dim)
    return dimensions

# Take input from the user
dimensions = take_input()

# Call the matrix chain multiplication function and print the result
min_cost, optimal_parenthesization = mcm(dimensions)
print(f"\nThe minimum number of multiplications is: {min_cost}")
print(f"The optimal parenthesization is: {optimal_parenthesization}")

