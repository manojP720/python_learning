import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Setup screen
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aesthetic Cursor Trail")
clock = pygame.time.Clock()

# Hide the default system cursor
pygame.mouse.set_visible(False)

# Colors (Hex: #0F0C1B background, Pastel/Neon trail)
BG_COLOR = (15, 12, 27)
CURSOR_COLOR = (255, 255, 255)  # Crisp white core
TRAIL_COLOR = (147, 197, 253)   # Aesthetic soft blue

# Store trail history: list of [x, y, radius]
trail_particles = []
MAX_TRAIL_LENGTH = 20

def draw_glow(surface, color, pos, radius):
    """Creates a soft glow effect by layering transparent circles."""
    glow_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    # Layer circles with decreasing opacity
    for r in range(radius, 0, -2):
        alpha = int(55 * (1 - r / radius))  # Soft subtle alpha
        pygame.draw.circle(glow_surface, (*color, alpha), (radius, radius), r)
    surface.blit(glow_surface, (pos[0] - radius, pos[1] - radius))

# Main game loop
running = True
while running:
    screen.fill(BG_COLOR)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Get current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Add current position to trail
    trail_particles.append([mouse_x, mouse_y, 12.0])

    # Restrict trail length
    if len(trail_particles) > MAX_TRAIL_LENGTH:
        trail_particles.pop(0)

    # 1. Draw the Trailing Particles (Back to Front)
    for i, particle in enumerate(trail_particles):
        # Calculate fade factors based on age (index)
        progress = i / len(trail_particles)
        
        # Smoothly shrink and fade the trail
        current_radius = int(particle[2] * progress)
        alpha = int(200 * progress)
        
        if current_radius > 0:
            # Create a temporary surface for transparent circles
            particle_surface = pygame.Surface((current_radius * 2, current_radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(particle_surface, (*TRAIL_COLOR, alpha), (current_radius, current_radius), current_radius)
            screen.blit(particle_surface, (particle[0] - current_radius, particle[1] - current_radius))

    # 2. Draw Ambient Glow around the main pointer
    draw_glow(screen, TRAIL_COLOR, (mouse_x, mouse_y), 35)

    # 3. Draw the Core Sharp Pointer
    pygame.draw.circle(screen, CURSOR_COLOR, (mouse_x, mouse_y), 4)

    # Update display (Locked at smooth 144Hz/FPS if possible)
    pygame.display.flip()
    clock.tick(144)

pygame.quit()
sys.exit()