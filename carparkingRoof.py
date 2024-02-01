#/usr/bin/env python3
def carParkingRoof(cars, k):
    # Ensuring the constraints are met
    assert 1 <= len(cars) <= 10 ** 5, "Number of cars must be between 1 and 10^5"
    assert 1 <= k <= len(cars), "Number of cars to cover must be between 1 and the total number of cars"
    assert all(1 <= spot <= 10 ** 14 for spot in cars), "All parking spots must be between 1 and 10^14"
    assert len(set(cars)) == len(cars), "All spots taken by cars must be unique"

    cars.sort()  # Sort the parking spots in ascending order
    min_length = float('inf')  # Initialize the minimum length to infinity
    n = len(cars)

    # Iterate through the parking spots
    for i in range(n - k + 1):
        length = cars[i + k - 1] - cars[i] + 1  # Calculate the length of the current roof
        min_length = min(min_length, length)  # Update the minimum length

    return min_length


# Test the function with the given example
cars = [6, 2, 12, 7,]
k = 3
print(carParkingRoof(cars, k))  # Output: 6
