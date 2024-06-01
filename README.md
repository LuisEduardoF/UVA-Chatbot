
# UVA Chatbot with Python

This project implements a chatbot designed to assist with questions from the UVA competitive programming book. 

It leverages Python, Langchain, ChatGPT, Pinecone, and Streamlit to provide solutions, explanations, and hints for UVA coding problems.

## Demo

<div align="center">
  <img src="https://github.com/LuisEduardoF/UVA-Chatbot/blob/main/Gravando-2024-05-31-212047.gif" alt="Chatbot Demo" width="500" height="400"/>
</div>

## Purpose

The UVA Chatbot is an AI assistant created to help students with competitive programming problems from the UVA book. The chatbot's primary functions include:

1. **Understanding the Problem**: Read and understand the problem statement.
2. **Providing a Solution**: Deliver a well-commented solution in C++ or Python.
3. **Explaining the Solution**: Provide a step-by-step explanation of the approach and logic.
4. **Offering Hints**: Guide students with incremental hints without giving away the entire solution.
5. **Considering Constraints**: Pay attention to constraints like time limits, memory limits, and input size.

## Architecture
<div align="center">
  <img src="https://github.com/LuisEduardoF/UVA-Chatbot/blob/main/Gravando-2024-05-31-212047.gif" alt="Chatbot Demo" width="500" height="400"/>
</div>
## Features

- **Problem Understanding**: The chatbot thoroughly reads and understands the problem statement.
- **Solution Delivery**: Provides well-commented solutions in C++ or Python.
- **Explanation**: Explains the approach and logic behind the solution in a clear, step-by-step manner.
- **Hint Provision**: Offers incremental hints to guide students towards the solution.
- **Constraint Awareness**: Considers problem constraints such as time limits, memory limits, and input size.

## Example Interactions

### Question: Can you give me some examples for graph questions?

**Answer:**

Sure! Here are a few example questions from the UVA competitive programming book that involve graph algorithms:

1. **UVA 558 - Wormholes**:
    - **Problem Statement**: Given a directed graph representing a series of wormholes, determine if there is a time loop (negative weight cycle).
    - **Solution Approach**: This problem can be solved using the Bellman-Ford algorithm, which is capable of detecting negative weight cycles in a graph.
    - **Hint**: Implement the Bellman-Ford algorithm and check if you can relax any edge after V-1 iterations, where V is the number of vertices.

2. **UVA 11902 - Dominator**:
    - **Problem Statement**: Given a directed graph, determine which vertices are reachable from a given start vertex and find out which vertices can still be reached when each vertex is removed one by one.
    - **Solution Approach**: This problem involves performing multiple DFS/BFS searches from the start vertex and simulating the removal of each vertex.
    - **Hint**: Start by performing a DFS/BFS from the given start vertex to identify initially reachable vertices. Then, for each vertex, temporarily remove it and perform another DFS/BFS to see the impact.

3. **UVA 11957 - Checkers**:
    - **Problem Statement**: Given an N x N board with checkers, find the number of ways a checker can move from the top-left corner to the bottom-right corner.
    - **Solution Approach**: Use dynamic programming to count the number of ways to reach each cell, considering the allowed moves of the checker.
    - **Hint**: Create a DP table where each cell (i, j) represents the number of ways to reach that cell. Use the moves of the checker to update the table.

### Question: Can you help me solve UVA 821 - Page Hopping?

**Answer:**

Absolutely! Let's break down the problem and solve it step-by-step.

1. **Problem Statement**: Given a list of directed edges representing links between pages, calculate the average shortest path length between all pairs of pages. If a page is not reachable from another, it should not be considered in the average.

2. **Step-by-Step Solution**:

   - **Understanding the Problem**: You need to calculate the shortest paths between all pairs of pages using the given directed edges. This is a classic application of the Floyd-Warshall algorithm, which is used to find shortest paths in a weighted graph with both positive and negative weights (but no negative weight cycles).

   - **Solution in Python**:

     ```python
     INF = float('inf')

     def floyd_warshall(n, graph):
         dist = [[INF] * n for _ in range(n)]
         for u in range(n):
             dist[u][u] = 0
         for u, v, w in graph:
             dist[u][v] = w
         for k in range(n):
             for i in range(n):
                 for j in range(n):
                     if dist[i][j] > dist[i][k] + dist[k][j]:
                         dist[i][j] = dist[i][k] + dist[k][j]
         return dist

     def average_shortest_path_length(n, dist):
         total_sum = 0
         count = 0
         for i in range(n):
             for j in range(n):
                 if i != j and dist[i][j] != INF:
                     total_sum += dist[i][j]
                     count += 1
         return total_sum / count if count != 0 else 0

     # Example usage
     n = 4  # number of nodes
     graph = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1)]
     dist = floyd_warshall(n, graph)
     avg_length = average_shortest_path_length(n, dist)
     print('Average shortest path length:', avg_length)
     ```

   - **Explanation**:
     - **Floyd-Warshall Algorithm**: Initialize the distance matrix with infinite values, set the distance to zero for self-loops, and update the distance for direct edges. Use three nested loops to update the shortest paths considering each node as an intermediate point.
     - **Average Calculation**: Sum the shortest path lengths for all pairs of nodes (excluding self-loops) and divide by the number of valid paths to get the average length.

   - **Hints**:
     - **Hint 1**: Start by initializing the distance matrix and filling in the direct edges.
     - **Hint 2**: Use the Floyd-Warshall algorithm to update the shortest paths between all pairs of nodes.
     - **Hint 3**: Calculate the average of the shortest path lengths, ignoring any pairs where a path does not exist.

## How to Run the Project

1. **Install Required Libraries**:
   ```bash
   pip install -r requirements.txt
   ``
2. **Setup enviroment keys**:
   ```bash
    PINECONE_API_KEY=""
    PINECONE_INDEX_NAME=""
    OPENAI_API_KEY=""
   ```
3. **Run Streamlit App**
