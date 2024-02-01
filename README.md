# Algorithm-test
## Test 1: Map Countries Identifier
Overview
This Python program is designed to identify the number of different countries represented on a
rectangular map. It determines the number of countries based on the colors of areas 
on the map, considering areas of the same color to belong to the same country if
they are connected orthogonally (north, south, east, west) without passing through areas of a different color.

Program Functionality:-
-Class Definition: The program defines a class called Solution to encapsulate the solution logic.

-Solution Method: Within the Solution class, there's a method named solution(self, A) which takes a 2D matrix A as input and returns the number of different countries represented on the map.

-DFS Traversal: Depth-First Search (DFS) traversal is used to explore the map and identify connected areas of the same color. Visited areas are marked by changing their color in the input matrix.

-Stack-Based DFS: DFS traversal is implemented using a stack-based approach to avoid potential issues with large recursion depths.

-Main Logic: The program iterates through each cell of the input matrix A. If an unvisited area is 
 encountered, it starts DFS traversal from that area to explore all connected areas of the same color. It increments the count of countries encountered during traversal.

-Output: The program returns the total count of different countries found on the map.

Input Constraints
The input matrix A represents a rectangular map consisting of areas painted with different colors.
The dimensions of the matrix A are within the range [1..300,000].
Each element of the matrix A is an integer within the range [-1,000,000,000.. 1,000,000,000].

Efficiency
Time Complexity: O(N * M), where N is the number of rows and M is the number of columns in the matrix. This is because the program iterates through each cell of the matrix once during DFS traversal.
Space Complexity: O(1), meaning it uses a constant amount of extra space, regardless of the size of
the input matrix. This is achieved by marking visited areas directly in the input matrix.

Usage
The program can be run in any Python environment without the need for additional modules.
Simply copy the provided code and execute it in a Python environment to identify countries on a
given map.




## Test2 : Car Parking Roof Function
Overview:
The carParkingRoof function is designed to solve the "Parking Dilemma" problem. This problem arises in a scenario where there are multiple cars parked in a straight-line parking lot, with a parking spot for every meter. The goal is to cover at least a specified number of cars with a roof and determine the minimum length of the roof required to achieve this.

Functionality:
The function takes two parameters:

cars: A list representing the positions of parked cars in the parking lot.
k: An integer indicating the minimum number of cars that must be covered by the roof.
The function iterates through the sorted list of parking spots, calculating the length of the roof required to cover k consecutive cars starting from each spot. It then returns the minimum length among all these calculations.

Constraints:
The function adheres to the following constraints:
-The number of cars (n) must be between 1 and 10^5.
-The minimum number of cars to be covered by the roof (k) must be between 1 and the total number of cars.
-Each parking spot must be within the range of 1 to 10^14.
-All parking spots taken by cars must be unique.
