import pygame
import random
import math
import statistics

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
RADIUS = 5
COLOR = (255, 0, 0)  # Red

# Create a font object
font = pygame.font.Font(None, 36)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Ask for the number of circles
num_circles = int(input("Enter the number of circles: "))

# Ask for the number of K-means
num_kmeans = int(input("Enter the number of K-means: "))

# Ask for the number of K-means
speed_of_convergence = int(input("Enter the speed of convergence: "))

# Generate the circles
circles = []
for _ in range(num_circles):
    x = random.randint(RADIUS, WIDTH - RADIUS)
    y = random.randint(RADIUS, HEIGHT - RADIUS)
    circles.append((x, y))

# Generate the K-means and their border colors
kmeans = []
border_colors = []
data_point_clusters = []
for _ in range(num_kmeans):
    x = random.randint(RADIUS, WIDTH - RADIUS)
    y = random.randint(RADIUS, HEIGHT - RADIUS)
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

    # White background
    screen.fill((255, 255, 255))

    data_point_distances = []
    
    for circle in circles:
        closest_kmean_index = 0
        closest_distance = float('inf')
        for i, kmean in enumerate(kmeans):
            distance = math.sqrt((circle[0] - kmean[0]) ** 2 + (circle[1] - kmean[1]) ** 2)
            if distance < closest_distance:
                closest_distance = distance
                closest_kmean_index = i
        data_point_clusters[closest_kmean_index].append(circle)
        data_point_distances.append(closest_distance)
        pygame.draw.circle(screen, border_colors[closest_kmean_index], circle, RADIUS)
    new_kmeans = []
    for i, kmean in enumerate(kmeans):
        if data_point_total > 0:
            x_total = y_total = 0
            data_point_total = len(data_point_clusters[i])
            for data_point in data_point_clusters[i]:
                x_total = x_total + data_point[0]
                y_total = y_total + data_point[1]
            new_kmean = (x_total / data_point_total, y_total / data_point_total)
            new_kmeans.append(new_kmean)
    
            # Move the kmean towards the new position
            x = (new_kmean[0] - kmean[0]) / speed_of_convergence
            y = (new_kmean[1] - kmean[1]) / speed_of_convergence
            
            kmean = (kmean[0] + x, kmean[1] + y)
        kmeans[i] = kmean
            
        pygame.draw.circle(screen, border_colors[i], kmean, RADIUS + 2)
        pygame.draw.circle(screen, (0, 0, 0), kmean, RADIUS - 1)

    # kmeans = new_kmeans
    data_point_clusters = [[] for _ in range(num_kmeans)]

    # Render the text
    text = font.render("Avg Dist: " + str(round(statistics.mean(data_point_distances), 2)), True, (0, 0, 0))

    # Calculate the size of the text
    text_rect = text.get_rect()

    # Draw a white rectangle behind the text
    pygame.draw.rect(screen, (255, 255, 255), (10, 10, text_rect.width, text_rect.height))

    screen.blit(text, (10, 10))  # Position the text at (10, 10)
    
    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(100)

# Quit Pygame
pygame.quit()
