import math
import pygame
import random
import statistics
from convex_hull import graham_scan

pygame.init()

WIDTH, HEIGHT = 960, 360
RADIUS = 5
COLOR = (255, 0, 0)  # Red

# Create a font object for avg distance to cluster center
font = pygame.font.Font(None, 36)

# Set up the pygame display
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
        elif num_clusters > num_data_points:
            print('Please Choose less clusters than data points')
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
    # Uncomment x and y if you want traditional k-means
    # x = random.randint(RADIUS, WIDTH - RADIUS)
    # y = random.randint(RADIUS, HEIGHT - RADIUS)
    x = random.randint(RADIUS, 50 - RADIUS)
    y = random.randint(RADIUS, 50 - RADIUS)
    kmeans.append((x, y))
    border_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    border_colors.append(border_color)
    data_point_clusters.append([])

current_error = 0
new_error = 0

converged = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Flag on convergence to stop iterations, occurs when the current_error == new_error      
    if converged == False:
        screen.fill((255, 255, 255))
        screen.fill((255, 255, 255))
    
        data_point_distances = []
        
        for data_point in data_points:
            closest_cluster_index = 0
            closest_distance = float('inf')
            for i, kmean in enumerate(kmeans):
                # Find the nearest centroid and assign the data point to it
                distance = math.sqrt((data_point[0] - kmean[0]) ** 2 + (data_point[1] - kmean[1]) ** 2)
                if distance < closest_distance:
                    closest_distance = distance
                    closest_cluster_index = i
            data_point_clusters[closest_cluster_index].append(data_point)
            data_point_distances.append(closest_distance)
            pygame.draw.circle(screen, border_colors[closest_cluster_index], data_point, RADIUS)
            
        new_clusters = []
        for i, cluster in enumerate(kmeans):
            data_point_total = len(data_point_clusters[i])
            if data_point_total > 0:
                x_total = y_total = 0
                for data_point in data_point_clusters[i]:
                    x_total = x_total + data_point[0]
                    y_total = y_total + data_point[1]
                new_cluster = (x_total / data_point_total, y_total / data_point_total)
                new_clusters.append(new_cluster)
        
                x = (new_cluster[0] - cluster[0]) / speed_of_convergence
                y = (new_cluster[1] - cluster[1]) / speed_of_convergence
                
                # Move the cluster centroid towards the new center
                cluster = (cluster[0] + x, cluster[1] + y)
                
            kmeans[i] = cluster

            if data_point_total > 2:
                # Draw the convex hull
                convex_hull = graham_scan(data_point_clusters[i])
                color = border_colors[i]
                pygame.draw.lines(screen, color, True, convex_hull)
            
            pygame.draw.circle(screen, border_colors[i], cluster, RADIUS + 2)
            pygame.draw.circle(screen, (0, 0, 0), cluster, RADIUS - 1)


    # Draw avg distance
    mean_error = round(statistics.mean(data_point_distances), 2)

    if current_error == mean_error:
        converged = True
        display_text = "Avg Dist: " + str(mean_error) + " Converged!"
    else: 
        data_point_clusters = [[] for _ in range(num_clusters)]
        display_text = "Avg Dist: " + str(mean_error) 
        current_error = mean_error

    text = font.render(display_text, True, (0, 0, 0))
    text_rect = text.get_rect()
    pygame.draw.rect(screen, (255, 255, 255), (10, 10, text_rect.width, text_rect.height))
    screen.blit(text, (10, 10)) 

    pygame.display.flip()

    pygame.time.delay(100)

pygame.quit()
