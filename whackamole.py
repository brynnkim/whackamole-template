import pygame
import random

def draw_grid(screen, grid_size, cell_size, color):
    for x in range(0, grid_size[0] * cell_size, cell_size):
        pygame.draw.line(screen, color, (x, 0), (x, grid_size[1] * cell_size))  # Vertical lines
    for y in range(0, grid_size[1] * cell_size, cell_size):
        pygame.draw.line(screen, color, (0, y), (grid_size[0] * cell_size, y))  # Horizontal lines

def get_cell_from_position(pos, cell_size):
    return pos[0] // cell_size, pos[1] // cell_size

def main():
    pygame.init()
    grid_size = (20, 16)
    cell_size = 45
    screen_width = grid_size[0] * cell_size
    screen_height = grid_size[1] * cell_size
    grid_color = (0, 0, 0)
    bg_color = (144, 238, 144)
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    mole_image = pygame.image.load("mole.png")
    mole_rect = mole_image.get_rect(topleft=(0, 0))
    mole_position = (0, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if mole_rect.collidepoint(mouse_pos):
                    mole_position = (random.randrange(grid_size[0]), random.randrange(grid_size[1]))
                    mole_rect.topleft = mole_position[0] * cell_size, mole_position[1] * cell_size

        screen.fill(bg_color)
        draw_grid(screen, grid_size, cell_size, grid_color)
        screen.blit(mole_image, mole_rect)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
