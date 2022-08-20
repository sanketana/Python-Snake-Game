import pygame

class Snake:
    size = 15
    color = (255, 255, 255)
    x = 100
    y = 100
    direction = ''
    #body = pygame.Rect(x, y, size, size)
    part1 = pygame.Rect(100, 100, size, size)
    part2 = pygame.Rect(115, 100, size, size)
    part3 = pygame.Rect(130, 100, size, size)
    part4 = pygame.Rect(130, 115, size, size)
    body = [part1, part2, part3, part4]
    grow = False

    def draw(self, screen):
        for part in self.body:
            pygame.draw.rect(screen, self.color, part)

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