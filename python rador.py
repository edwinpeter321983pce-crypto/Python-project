import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Radar Scanner")

clock = pygame.time.Clock()

CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 300

DARK_GREEN = (0, 60, 0)
BLACK = (0, 0, 0)
GREEN =(0, 225, 0)

enemies = []

for _ in range(5):
    angle = random.uniform(0, 360)
    dist = random.uniform(70, RADIUS - 20)
    
    x = CENTER[0] + math.cos(math.radians(angle)) * dist
    y = CENTER[1] + math.sin(math.radians(angle)) * dist
    
    enemies.append((x, y))

enemy_memory = [[0] * len(enemies)]

radar_angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    screen.fill(BLACK)
    
    for r in range(80, RADIUS + 1, 80):
        pygame.draw.circle(screen, DARK_GREEN, CENTER, r, 1)
        
    pygame.draw.line(screen, DARK_GREEN, (0, CENTER[1]), (WIDTH, CENTER[1]), 1)
    pygame.draw.line(screen, DARK_GREEN, (CENTER[0], 0), (CENTER[0], HEIGHT), 1)
    
    for i in range(45):
        a = radar_angle - i * 2
        alpha = max(0, 100 - i * 4)
        
        sweep = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        p1 = CENTER
        
        p2 = (
            CENTER[0] + math.cos(math.radians(a + 1)) * RADIUS,
            CENTER[1] + math.sin(math.radians(a + 1)) * RADIUS
        )
        
        p3 = (
            CENTER[0] + math.cos(math.radians(a - 1)) * RADIUS,
            CENTER[1] + math.sin(math.radians(a - 1)) * RADIUS
        )
        
        pygame.draw.polygon(
            sweep,
            (0, 255, 70, alpha),
            [p1, p2, p3]
        )
        
        screen.blit(sweep, (0, 0))
        
    pygame.draw.circle(screen, GREEN, CENTER, RADIUS, 2)
    
    for i, (x, y) in enumerate(enemies):
        enemy_angle = math.degrees(
            math.atan2(CENTER[1] - y, x - CENTER[0])
        )
        
        diff = abs((radar_angle - enemy_angle + 180) % 360 - 180)
        
        if diff < 2:
            enemy_memory[i] = 10
            
        if enemy_memory[i] > 0:
            enemy_memory[i] -= 1
            
            glow = pygame.Surface((40, 40), pygame.SRCALPHA)
            pygame.draw.circle(
                glow,
                (0, 255, 70, 70),
                (20, 20),
                14,
            )
            
            screen.blit(glow, (x - 20, y - 20))
            
            pygame.draw.circle(
                screen,
                (200, 255, 200),
                (int(x), int(y)),
                6,
            )
            
    radar_angle += 0.8
    radar_angle %= 360
    
    pygame.display.flip()
    clock.tick(60)
