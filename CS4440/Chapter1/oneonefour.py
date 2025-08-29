""" Exercise 1.1: 
4. “Design an algorithm for computing √n for any positive integer n. Besides
assignment and comparison, your algorithm may only use the four basic
arithmetical operations.”
    a. “Find gcd(31415, 14142) by applying Euclid’s algorithm.”
    b. “Estimate how many times faster it will be to find gcd(31415, 14142) by Euclid’s algorithm compared with the algorithm based on checking consecutive integers from min{m, n} down to gcd(m, n).”
"""
# https://en.wikipedia.org/wiki/Square_root_algorithms
# Basic Principle - digit by digit calculation
# Binary Numeral System
def isqrt(n):
    if n < 0:
        raise ValueError("input to be non-negative sqrt")

    x = n
    c = 0
    d = 1 << 30
    while d > n:
        d >>= 2

    while d != 0:
        if x >= c + d:
            x -= c + d
            c = (c >> 1) + d
        else:
            c >>= 1
        d >>= 2

    return c


print(isqrt(144))

"""
Exercise 1.2: 
5. “Describe the standard algorithm for finding the binary representation of a
positive decimal integer.”
    a. “in English.”
    b. “in pseudocode.”
"""
"""
Exercise 1.4: 
2. “If you have to solve the searching problem for a list of n numbers, how can you
take advantage of the fact that the list is known to be sorted? Give separate
answers for.”
    a. “lists represented as arrays.”
    b. “lists represented as linked lists.”
4a. “Let A be the adjacency matrix of an undirected graph. Explain what property of the 
matrix indicates that.”
    i. “the graph is complete.”
    ii. “the graph has a loop, i.e., an edge connecting a vertex to itself.”
    iii. “the graph has an isolated vertex, i.e., a vertex with no edges incident
to it.”
9. “For each of the following applications, indicate the most appropriate data structure”:
    a. “answering telephone calls in the order of their known priorities”
    b. “sending backlog orders to customers in the order they have been received”
    c. “implementing a calculator for computing simple arithmetical expressions”
"""