import pygame

class Snake:
    border_color = (200, 200, 200)
    border_size = 2
    body_color = (255, 255, 255)
    grid_x = 10
    grid_y = 16
    direction = ''
    grow = False

    def __init__(self, gridsize):
        self.size = gridsize
        self.x, self.y = self.grid_x * gridsize, self.grid_y * gridsize
        self.part1 = pygame.Rect(self.x, self.y, self.size, self.size)
        self.part2 = pygame.Rect(self.x + self.size, self.y, self.size, self.size)
        self.part3 = pygame.Rect(self.x + self.size*2, self.y, self.size, self.size)
        self.part4 = pygame.Rect(self.x + self.size*3, self.y, self.size, self.size)
        self.body = [self.part1, self.part2, self.part3, self.part4]

    def draw(self, screen):
        for part in self.body:
            pygame.draw.rect(screen, self.border_color, part)
            inner_x = part.x + self.border_size
            inner_y = part.y + self.border_size
            inner_w = part.width - (self.border_size * 2)
            inner_h = part.height - (self.border_size * 2)
            inner_rect = pygame.Rect(inner_x, inner_y, inner_w, inner_h)
            pygame.draw.rect(screen, self.body_color, inner_rect)

    def move(self):
        if self.grow == False:
            # Shift the list towards left by popping
            self.body.pop(0)

            head_x = self.body[-1].x
            head_y = self.body[-1].y

            # Create a new head based on direction of the snake
            if self.direction == 'R':
                head_x += self.size
            elif self.direction == 'L':
                head_x -= self.size
            elif self.direction == 'U':
                head_y -= self.size
            elif self.direction == 'D':
                head_y += self.size
        else:
            head_x = self.body[-1].x
            head_y = self.body[-1].y

            # Create a new head based on direction of the snake
            if self.direction == 'R':
                head_x += self.size
            elif self.direction == 'L':
                head_x -= self.size
            elif self.direction == 'U':
                head_y -= self.size
            elif self.direction == 'D':
                head_y += self.size  

            self.grow = False          


        # Add the new head into the list
        new_head = pygame.Rect(head_x, head_y, self.size, self.size)
        self.body.append(new_head)

    def munched(self, snack):
        return pygame.Rect.colliderect(self.body[-1], snack.rect)

    def ifTouchingEdge(self, screen):
        screen_rect = screen.get_rect()
        head_rect = self.body[-1]
        if head_rect.right >= screen_rect.right or head_rect.left <= screen_rect.left or head_rect.top <= screen_rect.top or head_rect.bottom >= screen_rect.bottom:
            return True

    def ifTouchingSelf(self):
        for rect in self.body[:-1]:
            if rect.colliderect(self.body[-1]):
                return True
        return False


    def reset(self, gridsize):
        self.size = gridsize
        self.x, self.y = self.grid_x * gridsize, self.grid_y * gridsize
        self.part1 = pygame.Rect(self.x, self.y, self.size, self.size)
        self.part2 = pygame.Rect(self.x + self.size, self.y, self.size, self.size)
        self.part3 = pygame.Rect(self.x + self.size*2, self.y, self.size, self.size)
        self.part4 = pygame.Rect(self.x + self.size*3, self.y, self.size, self.size)
        self.body = [self.part1, self.part2, self.part3, self.part4]     