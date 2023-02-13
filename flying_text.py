import pygame
import sys
import random

chat_arr = []

WIDTH = 1600
HEIGHT = 900

TARGET_FPS = 60

class Text():
    def __init__(self, text, color, start_time, end_time, y_position, x_increment):
        self.text = text
        self.color = color
        self.start_time = start_time
        self.end_time = end_time
        self.y_position = y_position
        self.x_increment = x_increment

def append_text(text, arr):
    # color = (255, 0, 0)
    color = "#FFFFFF"
    start_time = pygame.time.get_ticks()
    end_time = pygame.time.get_ticks() + 20000 # temp solution
    y_position = random.randint(0, HEIGHT - 50)
    x_increment = random.randint(13, 17)
    arr.append(Text(text, color, start_time, end_time, y_position, x_increment))

def setup_pygame(data_queue):
    pygame.init()

    font = pygame.font.SysFont('Arias', 50)

    fps_clock = pygame.time.Clock()

    screen = pygame.display.set_mode([WIDTH, HEIGHT], flags=pygame.NOFRAME)
    screen.fill((0, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if data_queue.qsize() > 0:
            append_text(data_queue.get(), chat_arr)
        # print(data_queue.qsize())

        screen.fill((0, 0, 0))

        cur_time = pygame.time.get_ticks()

        # updates all the text
        for chat in chat_arr:
            text_string = chat.text
            text_color = chat.color
            text_x = WIDTH - ((cur_time - chat.start_time) / TARGET_FPS) * chat.x_increment
            text_y = chat.y_position
            text_surface = font.render(text_string, True, text_color)
            screen.blit(text_surface, (text_x, text_y))

        # removes unnecessary items from array
        chat_arr[:] = [chat for chat in chat_arr if cur_time <= chat.end_time]

        # testing
        # if cur_time % 170 == 0:
        #     append_text("This is a test message that is being shown", chat_arr)

        pygame.display.update()
        fps_clock.tick(TARGET_FPS)

# if __name__ == '__main__':
#     main()