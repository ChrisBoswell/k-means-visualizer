import math

# Function to find the orientation of three points (p, q, r)
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    elif val > 0:
        return 1  # Clockwise
    else:
        return 2  # Counterclockwise
        
# Function to find the point with the lowest y-coordinate
def find_lowest_point(points):
    min_y = float('inf')
    min_idx = -1
    for i, (x, y) in enumerate(points):
        if y < min_y or (y == min_y and x < points[min_idx][0]):
            min_y = y
            min_idx = i
    return min_idx

# Function to calculate the polar angle of a point with respect to the lowest point
def polar_angle(lowest, point):
    x_diff = point[0] - lowest[0]
    y_diff = point[1] - lowest[1]
    return math.atan2(y_diff, x_diff)

# Graham's scan algorithm
def graham_scan(points):
    n = len(points)
    # Find the point with the lowest y-coordinate
    lowest_idx = find_lowest_point(points)
    points[0], points[lowest_idx] = points[lowest_idx], points[0]
    
    # Sort the remaining points based on their polar angles with respect to the lowest point
    points[1:] = sorted(points[1:], key=lambda point: polar_angle(points[0], point))
    
    # Initialize the stack with the first two points
    stack = [points[0], points[1]]
    
    # Process the remaining points
    for i in range(2, n):
        while len(stack) > 1 and orientation(stack[-2], stack[-1], points[i]) != 2:
            stack.pop()
        stack.append(points[i])
    
    return stack
