import sys
import pygame
import random
import threading
import pygame
from pygame.locals import MOUSEBUTTONDOWN

pygame.init()
w = 500
h = 500
screencaption = pygame.display.set_caption('bf control')
screen = pygame.display.set_mode((w,h))
screen_size = [w, h]
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (211, 211, 211)
P = (117, 64, 154)
x_speed = 1
y_speed = 0

box = []
boy = []

for j in range(20):
        x = random.randint(0, (w / (22+3))-1) * (22+3)
        y = random.randint(0, (h / (22+3))-1) * (22+3)
        box.append(x)
        boy.append(y)

class Square:

    def __init__(self, x, y, color, width):
        self.x = x
        self.y = y
        self.color = color
        self.width = width

    def draw_it(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width), 0)


class Grid:

    def __init__(self, size, distance, color):
        self.size = size
        self.distance = distance
        self.color = color
        self.square = []
        x = 0
        y = 0
        for i in range(self.size**2):
            self.square.append(Square(x, y, self.color, self.size))
            x += self.size + self.distance
            if x >= w:
                x = 0
                y += self.size + self.distance

    def draw_gird(self, color):
        for i in range(self.size**2):
            self.square[i].color = color
            self.square[i].draw_it()


class Snake:
    def __init__(self, length, color):
        self.square = []
        self.color = color
        self.length = length
        self.points = length
        #x = 10
        #y = 10
        x = random.randint(0, (w / (grid.size+grid.distance))-1) * (grid.size+grid.distance)
        y = random.randint(0, (h / (grid.size+grid.distance))-1) * (grid.size+grid.distance)
        for i in range(length):
            self.square.append(Square(x, y, color, grid.size))
            x -= grid.size + grid.distance

    def draw_it(self, color):
        for i in range(len(self.square)):
            if i == 0:
                self.square[0].color = BLUE
            self.square[i].draw_it()

    def move_it(self):
        for i in range(len(self.square)-1, 0, -1):
            self.square[i].x = self.square[i-1].x
            self.square[i].y = self.square[i-1].y
        self.square[0].x += (grid.size + grid.distance) * x_speed
        self.square[0].y += (grid.size + grid.distance) * y_speed
#        if self.square[0].x >= w:
#            self.square[0].x = 0
#        if self.square[0].y >= h:
#            self.square[0].y = 0
#        if self.square[0].x < 0:
#            self.square[0].x = w - (grid.size + grid.distance)
#        if self.square[0].y < 0:
#            self.square[0].y = w - (grid.size + grid.distance)


    def check_food(self):
        if self.square[0].x == apple.x and self.square[0].y == apple.y:
            apple_xy()
            self.points += 1
            self.square.append(Square(-100, -100, self.color, grid.size))

    def check_die(self):
        for i in range(1, len(self.square), 1):
            if self.square[0].x == self.square[i].x and self.square[0].y == self.square[i].y:
                print(self.points)
                clock.tick(5)
                for j in range(len(self.square)-1, self.length-1, -1):
                    del self.square[j]
                    self.points = self.length
                self.square[0].x = random.randint(0, (w / (grid.size+grid.distance))-1) * (grid.size+grid.distance)
                self.square[0].y = random.randint(0, (h / (grid.size+grid.distance))-1) * (grid.size+grid.distance)
                apple_xy()
                obstacles_xy()
                break
        for j in range(len(box)):
            if self.square[0].x == box[j] and self.square[0].y == boy[j]:
                print(self.points)
                clock.tick(5)
                for k in range(len(self.square)-1, self.length-1, -1):
                    del self.square[k]
                    self.points = self.length
                self.square[0].x = random.randint(0, (w / (grid.size+grid.distance))-1) * (grid.size+grid.distance)
                self.square[0].y = random.randint(0, (h / (grid.size+grid.distance))-1) * (grid.size+grid.distance)
                apple_xy()
                obstacles_xy()
                break

            if self.square[0].x >= w:
                print("End: ",self.points)
                clock.tick(5)
                for j in range(len(self.square)-1, self.length-1, -1):
                    del self.square[j]
                    self.points = self.length
                self.square[0].x = random.randint(0, (w / (grid.size+grid.distance))-1) * (grid.size+grid.distance)
                self.square[0].y = random.randint(0, (h / (grid.size+grid.distance))-1) * (grid.size+grid.distance)
                apple_xy()
                obstacles_xy()
                break
            if self.square[0].y >= h:
                print("End: ",self.points)
                clock.tick(5)
                for j in range(len(self.square)-1, self.length-1, -1):
                    del self.square[j]
                    self.points = self.length
                self.square[0].x = random.randint(0, (w / (grid.size+grid.distance))-1) * (grid.size+grid.distance)
                self.square[0].y = random.randint(0, (h / (grid.size+grid.distance))-1) * (grid.size+grid.distance)
                apple_xy()
                obstacles_xy()
                break

            if self.square[0].x < 0:
                print("End: ",self.points)
                clock.tick(5)
                for j in range(len(self.square)-1, self.length-1, -1):
                    del self.square[j]
                    self.points = self.length
                self.square[0].x = random.randint(0, (w / (grid.size+grid.distance))-1) * (grid.size+grid.distance)
                self.square[0].y = random.randint(0, (h / (grid.size+grid.distance))-1) * (grid.size+grid.distance)
                apple_xy()
                obstacles_xy()
                break

            if self.square[0].y < 0:
                print("End: ",self.points)
                clock.tick(5)
                for j in range(len(self.square)-1, self.length-1, -1):
                    del self.square[j]
                    self.points = self.length
                self.square[0].x = random.randint(0, (w / (grid.size+grid.distance))-1) * (grid.size+grid.distance)
                self.square[0].y = random.randint(0, (h / (grid.size+grid.distance))-1) * (grid.size+grid.distance)
                apple_xy()
                obstacles_xy()
                break

def pause():
    paused = True
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                    quit()

        #gameDisplay.fill(white)

    clock.tick(5)

def movement():
    global x_speed
    global y_speed
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y_speed != 1:
                    x_speed = 0
                    y_speed = 0
                    y_speed = -1
                    break
            if event.key == pygame.K_DOWN:
                if y_speed != -1:
                    x_speed = 0
                    y_speed = 0
                    y_speed = 1
                    break
            if event.key == pygame.K_RIGHT:
                if x_speed != -1:
                    x_speed = 0
                    y_speed = 0
                    x_speed = 1
                    break
            if event.key == pygame.K_LEFT:
                if x_speed != 1:
                    x_speed = 0
                    y_speed = 0
                    x_speed = -1
                    break
            if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                    quit()


def apple_xy():
    apple.x = random.randint(0, (w / (grid.size+grid.distance))-1) * (grid.size+grid.distance)
    apple.y = random.randint(0, (h / (grid.size+grid.distance))-1) * (grid.size+grid.distance)
#    for i in range(len(snake.square)):
#        if apple.x == box[i] and apple.y == boy[i]:
#            apple_xy()

def obstacles_xy():
    for k in range(len(box)):
        pygame.draw.rect(screen, P, (box[k], boy[k], grid.size, grid.size), 0)

#################################################################################################3
#class BFControlId(object):
#    _instance_lock = threading.Lock()
#    def __init__(self):
#        self.id = 1

#    @classmethod
#    def instance(cls, *args, **kwargs):
#        if not hasattr(BFControlId, "_instance"):
#            BFControlId._instance = BFControlId(*args, **kwargs)
#        return BFControlId._instance

#    def get_new_id(self):
#        self.id += 1
#        return self.id

#CLICK_EFFECT_TIME = 100
#class BFButton(object):
#    def __init__(self, parent, rect, text='Button', click=None):
#        self.x,self.y,self.width,self.height = rect
#        self.bg_color = (225,225,225)
#        self.parent = parent
#        self.surface = parent.subsurface(rect)
#        self.is_hover = False
#        self.in_click = False
#        self.click_loss_time = 0
#        self.click_event_id = -1
#        self.ctl_id = BFControlId().instance().get_new_id()
#        self._text = text
#        self._click = click
#        self._visible = True
#        self.init_font()

#    def init_font(self):
#        font = pygame.font.SysFont('arial',28)
#        white = 100, 100, 100
#        self.textImage = font.render(self._text, True, white)
#        w, h = self.textImage.get_size()
#        self._tx = (self.width - w) / 2
#        self._ty = (self.height - h) / 2


#    @property
#    def text(self):
#        return self._text

#    @text.setter
#    def text(self, value):
#        self._text = value
#        self.init_font()

#    @property
#    def click(self):
#        return self._click

#    @click.setter
#    def click(self, value):
#        self._click = value

#    @property
#    def visible(self):
#        return self._visible

#    @visible.setter
#    def visible(self, value):
#        self._visible = value

#    def update(self, event):
#        if self.in_click and event.type == self.click_event_id:
#            if self._click: self._click(self)
#            self.click_event_id = -1
#            return

#        x, y = pygame.mouse.get_pos()
#        if x > self.x and x < self.x + self.width and y > self.y and y < self.y + self.height:
#            self.is_hover = True
#            if event.type == MOUSEBUTTONDOWN:
#                pressed_array = pygame.mouse.get_pressed()
#                if pressed_array[0]:
#                    self.in_click = True
#                    self.click_loss_time = pygame.time.get_ticks() + CLICK_EFFECT_TIME
#                    self.click_event_id = pygame.USEREVENT+self.ctl_id
#                    pygame.time.set_timer(self.click_event_id,CLICK_EFFECT_TIME-10)
#        else:
#            self.is_hover = False

#    def draw(self):
#        if self.in_click:
#            if self.click_loss_time < pygame.time.get_ticks():
#                self.in_click = False
#        if not self._visible:
#            return
#        if self.in_click:
#            r,g,b = self.bg_color
#            k = 0.95
#            self.surface.fill((r*k, g*k, b*k))
#        else:
#            self.surface.fill(self.bg_color)
#        if self.is_hover:
#            pygame.draw.rect(self.surface, (0,0,0), (0,0,self.width,self.height), 1)
#            pygame.draw.rect(self.surface, (100,100,100), (0,0,self.width-1,self.height-1), 1)
#            layers = 5
#            r_step = (210-170)/layers
#            g_step = (225-205)/layers
#            for i in range(layers):
#                pygame.draw.rect(self.surface, (170+r_step*i, 205+g_step*i, 255), (i, i, self.width - 2 - i*2, self.height - 2 - i*2), 1)
#        else:
#            self.surface.fill(self.bg_color)
#            pygame.draw.rect(self.surface, (0,0,0), (0,0,self.width,self.height), 1)
#            pygame.draw.rect(self.surface, (100,100,100), (0,0,self.width-1,self.height-1), 1)
#            pygame.draw.rect(self.surface, self.bg_color, (0,0,self.width-2,self.height-2), 1)

#        self.surface.blit(self.textImage, (self._tx, self._ty))
###################################################################################################################################

#def do_click1(btn):
#    game_active()
#    pygame.display.update()
#    clock.tick(8)
#    btn.visible = False
#

#def do_click2(btn):
#    btn.visible = False

#def do_click3(btn):
#    pygame.quit()
#    exit()

#def game_active():
#    pygame.draw.rect(screen, BLACK, (0, 0, w, h), 0)
#    grid.draw_gird(GREY)
#    movement()
#    snake.move_it()
#    snake.check_die()
#    snake.check_food()
#    snake.draw_it(GREEN)
#    apple.draw_it()
#    obstacles_xy()
#    #for i in range(20):
#    #if self.square[0].x != obstacles.x and self.square[0].y != obstacles.y:
#    #obstacles_xy(20)
#    text = font.render(str(snake.points), True, (0, 0, 0))
#    """Show the programs FPS in the window handle."""
#    caption = "FPS: {:.2f}".format(clock.get_fps())
#    pygame.display.set_caption(caption)
#    screen.blit(text, (0, 0))
#
#button1 = BFButton(screen, (120,100,160,40))
#button1.text = 'Mode 1'
#button1.click = do_click1
#button2 = BFButton(screen, (120,180,160,40),text='Mode 2',click=do_click2)
#button3 = BFButton(screen, (120,260,160,40),text='Quit',click=do_click3)

grid = Grid(22, 3, GREY)
snake = Snake(4, GREEN)
apple = Square(-100, -100, RED, grid.size)
obstacles = Square(-100, -100, P, grid.size)
font = pygame.font.SysFont("courier new", 20)
apple_xy()
obstacles_xy()


while True:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#        button1.update(event)
#        button2.update(event)
#        button3.update(event)

#    #screen.fill((255,255,255))
#    button1.draw()
#    button2.draw()
#    button3.draw()
    pygame.draw.rect(screen, BLACK, (0, 0, w, h), 0)
    grid.draw_gird(GREY)
    movement()
    snake.move_it()
    snake.check_die()
    snake.check_food()
    snake.draw_it(GREEN)
    apple.draw_it()
    obstacles_xy()
    #for i in range(20):
    #if self.square[0].x != obstacles.x and self.square[0].y != obstacles.y:
    #obstacles_xy(20)
    text = font.render(str(snake.points), True, (0, 0, 0))
    """Show the programs FPS in the window handle."""
    caption = "FPS: {:.2f}".format(clock.get_fps())
    pygame.display.set_caption(caption)
    screen.blit(text, (0, 0))

    pygame.display.update()

    clock.tick(8)

pygame.quit()
quit()
