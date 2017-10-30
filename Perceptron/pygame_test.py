import sys, pygame
from point import Point
from perceptron import Perceptron
from utils import f
def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

if __name__ == "__main__":
    pygame.init()
    size = width, height = 800, 600
    black = 0, 0, 0
    white = 255, 255, 255
    red = 255, 0, 0
    green = 0, 255, 0
    screen = pygame.display.set_mode(size)
    points = []
    p = Perceptron(3)
    for i in range(1000):
        points.append(Point(size))
    while True:
        checkEvents()
        screen.fill(white)
        p1 = Point(size, (-1,f(-1)))
        p2 = Point(size, (1,f(1)))
        pygame.draw.line(screen, black, p1.pos(), p2.pos(), 1)
        p3 = Point(size, (-1, p.guessF(-1)))
        p4 = Point(size, (1, p.guessF(1)))
        pygame.draw.line(screen, black, p3.pos(),p4.pos(), 1)
        for point in points:
            pos = (point.pixelX(), point.pixelY())
            inputs = (point.x, point.y, point.bias)
            pygame.draw.circle(screen, black, pos, 5, 1 if point.label == 1 else 0)
            p.train(inputs, point.label)
            guess = p.guess(inputs)
            pygame.draw.circle(screen,green if guess == point.label else red,(point.pixelX(), point.pixelY()),3)
        pygame.display.update()