import pygame
import random
import math

pygame.init()

# Window setup
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pro Cursor Animation")

clock = pygame.time.Clock()

# Colors
BG_COLOR = (10, 10, 20)
WHITE = (255, 255, 255)

# Hide default cursor
pygame.mouse.set_visible(False)


# ----------------------------
# Trail Class
# ----------------------------
class Trail:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.radius = random.randint(4, 8)
        self.alpha = 255
        self.color = color

    def update(self):
        self.radius += 0.2
        self.alpha -= 8

    def draw(self, surface):
        if self.alpha > 0:
            trail_surface = pygame.Surface((50, 50), pygame.SRCALPHA)
            pygame.draw.circle(
                trail_surface,
                (*self.color, max(0, self.alpha)),
                (25, 25),
                int(self.radius)
            )
            surface.blit(trail_surface, (self.x - 25, self.y - 25))

    def is_dead(self):
        return self.alpha <= 0


# ----------------------------
# Particle Class
# ----------------------------
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.size = random.randint(2, 5)
        self.speed_x = random.uniform(-4, 4)
        self.speed_y = random.uniform(-4, 4)
        self.life = 40
        self.color = color

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.life -= 1
        self.size *= 0.95

    def draw(self, surface):
        if self.life > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.size))

    def is_dead(self):
        return self.life <= 0


# ----------------------------
# Ripple Effect
# ----------------------------
class Ripple:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.radius = 5
        self.alpha = 255
        self.color = color

    def update(self):
        self.radius += 3
        self.alpha -= 10

    def draw(self, surface):
        if self.alpha > 0:
            ripple_surface = pygame.Surface((200, 200), pygame.SRCALPHA)
            pygame.draw.circle(
                ripple_surface,
                (*self.color, max(0, self.alpha)),
                (100, 100),
                int(self.radius),
                2
            )
            surface.blit(ripple_surface, (self.x - 100, self.y - 100))

    def is_dead(self):
        return self.alpha <= 0


# ----------------------------
# Cursor Class
# ----------------------------
class Cursor:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.size = 12
        self.target_size = 12
        self.speed = 0.18
        self.trails = []
        self.particles = []
        self.ripples = []
        self.hue = 0

    def get_dynamic_color(self):
        self.hue += 1
        if self.hue > 360:
            self.hue = 0

        r = int((math.sin(math.radians(self.hue)) + 1) * 127)
        g = int((math.sin(math.radians(self.hue + 120)) + 1) * 127)
        b = int((math.sin(math.radians(self.hue + 240)) + 1) * 127)

        return (r, g, b)

    def update(self):
        mx, my = pygame.mouse.get_pos()

        # Smooth follow
        self.x += (mx - self.x) * self.speed
        self.y += (my - self.y) * self.speed

        # Smooth size transition
        self.size += (self.target_size - self.size) * 0.15

        color = self.get_dynamic_color()

        # Add trail
        self.trails.append(Trail(self.x, self.y, color))

        for trail in self.trails[:]:
            trail.update()
            if trail.is_dead():
                self.trails.remove(trail)

        for particle in self.particles[:]:
            particle.update()
            if particle.is_dead():
                self.particles.remove(particle)

        for ripple in self.ripples[:]:
            ripple.update()
            if ripple.is_dead():
                self.ripples.remove(ripple)

    def click_effect(self):
        color = self.get_dynamic_color()

        for _ in range(15):
            self.particles.append(Particle(self.x, self.y, color))

        self.ripples.append(Ripple(self.x, self.y, color))

    def hover_effect(self, hovering):
        if hovering:
            self.target_size = 22
        else:
            self.target_size = 12

    def draw(self, surface):
        color = self.get_dynamic_color()

        # Draw trails
        for trail in self.trails:
            trail.draw(surface)

        # Draw particles
        for particle in self.particles:
            particle.draw(surface)

        # Draw ripples
        for ripple in self.ripples:
            ripple.draw(surface)

        # Glow effect
        for glow in range(3):
            glow_surface = pygame.Surface((100, 100), pygame.SRCALPHA)
            pygame.draw.circle(
                glow_surface,
                (*color, 60 - glow * 15),
                (50, 50),
                int(self.size + glow * 6)
            )
            surface.blit(glow_surface, (self.x - 50, self.y - 50))

        # Main ring cursor
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), int(self.size), 2)


# ----------------------------
# UI Button
# ----------------------------
button_rect = pygame.Rect(400, 300, 200, 80)

cursor = Cursor()

running = True
while running:
    screen.fill(BG_COLOR)

    mouse_pos = pygame.mouse.get_pos()

    # Check hover
    hovering = button_rect.collidepoint(mouse_pos)
    cursor.hover_effect(hovering)

    # Draw button
    pygame.draw.rect(screen, (40, 40, 80), button_rect, border_radius=15)
    font = pygame.font.SysFont("Arial", 28)
    text = font.render("Hover Me", True, WHITE)
    screen.blit(text, (button_rect.x + 45, button_rect.y + 25))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            cursor.click_effect()

    cursor.update()
    cursor.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()