import pygame
import random
import math
import statistics

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 960, 360
RADIUS = 5
COLOR = (255, 0, 0)  # Red

# Create a font object for avg distance to cluster center
font = pygame.font.Font(None, 36)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    try:
        num_data_points = int(input("Enter the number of data points: "))
        if num_data_points < 0:
            print('Please Choose a non-negative value for the number of data points')
        else: 
            break
    except:
        print('Please Choose a pick a new number of data points')
        
while True:
    try:
        num_clusters = int(input("Enter the number of clusters: "))
        if num_clusters < 0:
            print('Please Choose a non-negative value for the number of clusters')
        else: 
            break
    except:
        print('Please Choose a pick a new number of clusters')

print('The centroid convergence speed goes up as the input value goes down, speed of 1 being the fastest')
while True:
    try:
        speed_of_convergence = int(input("Enter the desired speed of convergence: "))
        if speed_of_convergence < 0:
            print('Please Choose a non-negative value for the speed of convergence')
        else: 
            break
    except:
        print('Please Choose a pick a new value for the speed')


# Generate the datapoints
data_points = []
for _ in range(num_data_points):
    x = random.randint(RADIUS, WIDTH - RADIUS)
    y = random.randint(RADIUS, HEIGHT - RADIUS)
    data_points.append((x, y))

# Generate the clusters and their border colors
kmeans = []
border_colors = []
data_point_clusters = []
for _ in range(num_clusters):
    # x = random.randint(RADIUS, WIDTH - RADIUS)
    # y = random.randint(RADIUS, HEIGHT - RADIUS)
    x = random.randint(RADIUS, 50 - RADIUS)
    y = random.randint(RADIUS, 50 - RADIUS)
    kmeans.append((x, y))
    border_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    border_colors.append(border_color)
    data_point_clusters.append([])

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    data_point_distances = []
    
    for data_point in data_points:
        closest_kmean_index = 0
        closest_distance = float('inf')
        for i, kmean in enumerate(kmeans):
            distance = math.sqrt((data_point[0] - kmean[0]) ** 2 + (data_point[1] - kmean[1]) ** 2)
            if distance < closest_distance:
                closest_distance = distance
                closest_kmean_index = i
        data_point_clusters[closest_kmean_index].append(data_point)
        data_point_distances.append(closest_distance)
        pygame.draw.circle(screen, border_colors[closest_kmean_index], data_point, RADIUS)
    new_kmeans = []
    for i, kmean in enumerate(kmeans):
        data_point_total = len(data_point_clusters[i])
        if data_point_total > 0:
            x_total = y_total = 0
            for data_point in data_point_clusters[i]:
                x_total = x_total + data_point[0]
                y_total = y_total + data_point[1]
            new_kmean = (x_total / data_point_total, y_total / data_point_total)
            new_kmeans.append(new_kmean)
    
            x = (new_kmean[0] - kmean[0]) / speed_of_convergence
            y = (new_kmean[1] - kmean[1]) / speed_of_convergence
            
            # Move the cluster centroid towards the new center
            kmean = (kmean[0] + x, kmean[1] + y)
            
        kmeans[i] = kmean
            
        pygame.draw.circle(screen, border_colors[i], kmean, RADIUS + 2)
        pygame.draw.circle(screen, (0, 0, 0), kmean, RADIUS - 1)

    data_point_clusters = [[] for _ in range(num_clusters)]

    # Draw avg distance
    text = font.render("Avg Dist: " + str(round(statistics.mean(data_point_distances), 2)), True, (0, 0, 0))
    text_rect = text.get_rect()
    pygame.draw.rect(screen, (255, 255, 255), (10, 10, text_rect.width, text_rect.height))
    screen.blit(text, (10, 10)) 
    
    pygame.display.flip()

    pygame.time.delay(100)

pygame.quit()
