import pygame
from pygame.locals import *
import time
import random
SIZE = 40

class Apple:
    def __init__(self,parent_screen):
        self.screen = parent_screen

        self.food = pygame.image.load('apple.jpg').convert()
        self.x = SIZE * 4
        self.y = SIZE * 4

    def draw(self):
        self.screen.blit(self.food, (self.x,self.y))
        pygame.display.update()


    def move(self):
        self.x = random.randint(0,20) * SIZE
        self.y = random.randint(0,15) * SIZE

class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.screen = parent_screen
        self.block = pygame.image.load('block.jpg').convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'up'

    def increase_lenth(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_right(self):
        self.direction = 'right'

    def move_left(self):
        self.direction = 'left'

    def draw(self):

        self.screen.fill((25, 155, 255))
        for i in range(self.length):
            self.screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.update()

    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'up':
            self.y[0] -= 40
        if self.direction == 'down':
            self.y[0] += 40
        if self.direction == 'right':
            self.x[0] += 40
        if self.direction == 'left':
            self.x[0] -= 40

        self.draw()


class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((1000, 800))
        self.screen.fill((25, 155, 255))
        self.snake = Snake(self.screen, 1)
        self.snake.draw()
        self.apple = Apple(self.screen)
        self.apple.draw()

    def is_collision(self,x1 ,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False


    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.update()
        if self.is_collision(self.snake.x[0], self.snake.y[0],self.apple.x,self.apple.y):
            self.apple.move()
            self.snake.increase_lenth()

        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                raise 'Game over'


    def show_game_over(self):
        self.screen.fill((25, 155, 255))
        font = pygame.font.SysFont('arial',30)
        line1 = font.render(F"Game is over:your score is {self.snake.length}", True, (255,255,255))
        self.screen.blit(line1, (200,300))
        line2 = font.render('to play again press enter.To exit press Escape!', True, (255,255,255))
        self.screen.blit(line2, (210,350))
        pygame.display.flip()

        pass




    def display_score(self):
        font = pygame.font.SysFont('ariel',30)
        score = font.render(f"score:{self.snake.length}", True, (255,255,255))
        self.screen.blit(score, (800,10))

    def reset(self):
        self.snake = Snake(self.screen, 1)
        self.apple = Apple(self.screen)


    def run(self):
        runner = True
        pause = False
        while runner:

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        runner = False
                    if event.key == K_RETURN:
                        pause = False
                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()
                        if event.key == K_RIGHT:
                            self.snake.move_right()
                        if event.key == K_LEFT:
                            self.snake.move_left()


                elif event.type == QUIT :
                        runner = False


            try:
                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(0.2)

if __name__ == '__main__':
    game = Game()
    game.run()





