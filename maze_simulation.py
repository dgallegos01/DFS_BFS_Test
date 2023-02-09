import pygame
import time
import button
import algorithms

pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 750
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255)

visited = [] # all locations visited
position = (350, 550) # start position
destination = (350,150) # end goal
adj_list = {} # used to generate the node graph


# Set up the drawing window
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

MAZE_FOR_GRAPHICS = [
    ((100,100), (300,100)), ((100,100), (100,600)), 
    ((100,600), (300,600)), ((100,200), (300,200)), 
    ((300,200), (300,300)), ((300,300), (500,300)), 
    ((400,100), (400,200)), ((400,200), (500,200)), 
    ((100,400), (200,400)), ((200,300), (200,400)), 
    ((300,400), (300,500)), ((300,400), (400,400)), 
    ((200,500), (500,500)), ((500,400), (500,500)),
    ((400,500), (400,600)), ((400,100), (600,100)),
    ((600,100), (600,600)), ((400,600), (600,600))
    ]

MAZE_FOR_ALGORITHM = [
    ((100,100), (600,100)), ((100,100), (100,600)), 
    ((100,600), (600,600)), ((100,200), (300,200)), 
    ((300,200), (300,300)), ((300,300), (500,300)), 
    ((400,100), (400,200)), ((400,200), (500,200)), 
    ((100,400), (200,400)), ((200,300), (200,400)), 
    ((300,400), (300,500)), ((300,400), (400,400)), 
    ((200,500), (500,500)), ((500,400), (500,500)),
    ((400,500), (400,600)), ((600,100), (600,600))
    ]

def draw_circle(circle_x_y, color):
    return pygame.draw.circle(SCREEN, color, circle_x_y, 20, 0)

def show_algorithm():
    for location in visited:
        draw_circle(location, BLUE)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(250)
    time.sleep(1)
    for path in find_path:
        draw_circle(path, GREEN)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(250)
        
    pygame.time.delay(3000)
    

algorithms.dfs(MAZE_FOR_ALGORITHM, position, visited, adj_list) # search all possible locations
find_path = algorithms.bfs(adj_list, position, destination) # find the shortest path

pygame.display.set_caption("Maze Simulator")

start_img = pygame.image.load('start_btn.png').convert_alpha()

clock = pygame.time.Clock()

start_button = button.Button(270, 660, start_img, 0.6)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    SCREEN.fill(WHITE)

    for x in MAZE_FOR_GRAPHICS:
        wall = pygame.draw.line(SCREEN, BLACK, x[0], x[1], 10)
    
    if start_button.draw(SCREEN):
        show_algorithm()
 
    pygame.display.update()
    clock.tick(60)

pygame.quit()