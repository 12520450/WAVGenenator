import pygame
import math
import time

window = pygame.display.set_mode((600, 600))

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

class Line:
    def __init__(self):
        self.points = []

def generateLine(startX, nPoints, length, y):
    line = Line()
    for i in range(nPoints):
        p = Point()
        p.x = startX + ((i / nPoints) * length)
        p.y = y
        line.points.append(p)
    return line

nPoints = 100
line = generateLine(10, nPoints, 590, 300)
start = time.time()
frequency = 100
amplitude = 30
overallY = 300

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    window.fill((255, 255, 255))

    for i in range(1, len(line.points)):
        yStart = (amplitude * math.sin(2 * math.pi * frequency + line.points[i].x)) + overallY
        yEnd = (amplitude * math.sin(2 * math.pi * frequency + line.points[i - 1].x)) + overallY

        pygame.draw.circle(window, (255, 0, 0), (line.points[i].x, yStart), 1)
        pygame.draw.circle(window, (255, 0, 0), (line.points[i - 1].x, yEnd), 1)
        pygame.draw.aaline(window, (0, 0, 0), (line.points[i].x, yStart), (line.points[i - 1].x, yEnd))

    pygame.display.flip()
