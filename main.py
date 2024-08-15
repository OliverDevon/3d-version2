import pygame
import math
from settings import *
from cube import Cube
# Initialize Pygame
pygame.init()

# Screen dimensions

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Cubes with Movement")

# Colors


# Cube vertices (one centered at the origin, one shifted along the x-axis)
cube1_vertices = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1],
]

cube2_vertices = [
    [x + 3, y, z] for x, y, z in cube1_vertices  # Shift by 3 units along the x-axis
]

cube3_vertices = [
    [x, y + 3, z] for x, y, z in cube2_vertices  # Shift by 3 units along the y-axis
]
cube4_vertices = [
    [x, y+3, z] for x, y, z in cube1_vertices  # Shift by 3 units along the x and y axes
]
cube5_vertices = [
    [x + 3, y, z+3] for x, y, z in cube1_vertices  # Shift by 3 units along the x-axis
]
cube6_vertices = [
    [x, y + 3, z+3] for x, y, z in cube2_vertices  # Shift by 3 units along the y-axis
]
cube7_vertices = [
    [x, y + 3, z+3]
    for x, y, z in cube1_vertices  # Shift by 3 units along the x and y axes
]
cube8_vertices = [
    [x, y, z + 3] for x, y, z in cube1_vertices  # Shift by 3 units along the x-axis
]

# Cube edges connecting the vertices
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),  # Back face
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),  # Front face
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7),  # Connecting edges
]


# Projection function (3D to 2D)
def project_3d_to_2d(point, camera_x, camera_y, camera_z, angle_x, angle_y, distance):
    x, y, z = point

    # Apply camera position (translation)
    x -= camera_x
    y -= camera_y
    z -= camera_z

    # Rotate around the Y axis
    temp_x = x * math.cos(angle_y) - z * math.sin(angle_y)
    temp_z = x * math.sin(angle_y) + z * math.cos(angle_y)
    x, z = temp_x, temp_z

    # Rotate around the X axis
    temp_y = y * math.cos(angle_x) - z * math.sin(angle_x)
    temp_z = y * math.sin(angle_x) + z * math.cos(angle_x)
    y, z = temp_y, temp_z

    # Projection transformation
    factor = distance / (distance + z)
    x_proj = int(WIDTH / 2 + x * factor * 200)
    y_proj = int(HEIGHT / 2 - y * factor * 200)

    return (x_proj, y_proj)


def main():
    running = True
    clock = pygame.time.Clock()

    # Camera settings
    camera_x, camera_y, camera_z = (
        0,
        0,
        -5,
    )  # Start camera slightly back from the origin
    angle_x = 0
    angle_y = 0
    movement_speed = 0.1

    while running:
        screen.fill(BLACK)
        cube1 = Cube(
            screen, edges, cube1_vertices, RED, (camera_x, camera_y, camera_z), angle_x, angle_y, 3
        )
        cube2 = Cube(
            screen, edges, cube2_vertices, WHITE, (camera_x, camera_y, camera_z), angle_x, angle_y, 3
        )
        cube3 = Cube(
            screen, edges, cube3_vertices, WHITE, (camera_x, camera_y, camera_z), angle_x, angle_y, 3
        )
        cube4 = Cube(
            screen, edges, cube4_vertices, GREEN, (camera_x, camera_y, camera_z), angle_x, angle_y, 3
        )
        cube5 = Cube(
            screen, edges, cube5_vertices, RED, (camera_x, camera_y, camera_z), angle_x, angle_y, 3
        )
        cube6 = Cube(
            screen, edges, cube6_vertices, RED, (camera_x, camera_y, camera_z), angle_x, angle_y, 3
        )
        cube7 = Cube(
            screen,
            edges,
            cube7_vertices,
            WHITE,
            (camera_x, camera_y, camera_z),
            angle_x,
            angle_y,
            3,
        )
        cube8 = Cube(
            screen,
            edges,
            cube8_vertices,
            GREEN,
            (camera_x, camera_y, camera_z),
            angle_x,
            angle_y,
            3,
        )
    
        cubes = [cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle movement and rotation
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            angle_y -= 0.02
        if keys[pygame.K_RIGHT]:
            angle_y += 0.02
        if keys[pygame.K_UP]:
            angle_x -= 0.02
        if keys[pygame.K_DOWN]:
            angle_x += 0.02
        if keys[pygame.K_w]:  # Move forward
            camera_x += movement_speed * math.sin(angle_y)
            camera_z += movement_speed * math.cos(angle_y)
        if keys[pygame.K_s]:  # Move backward
            camera_x -= movement_speed * math.sin(angle_y)
            camera_z -= movement_speed * math.cos(angle_y)
        if keys[pygame.K_a]:  # Strafe left
            camera_x -= movement_speed * math.cos(angle_y)
            camera_z += movement_speed * math.sin(angle_y)
        if keys[pygame.K_d]:  # Strafe right
            camera_x += movement_speed * math.cos(angle_y)
            camera_z -= movement_speed * math.sin(angle_y)
        if keys[pygame.K_q]:
            camera_y += movement_speed * math.cos(angle_x)
            camera_z += movement_speed * math.sin(angle_x)
        if keys[pygame.K_e]:
            camera_y -= movement_speed * math.cos(angle_x)
            camera_z -= movement_speed * math.sin(angle_x)

        # projects both the cubes
        for cube in cubes:
            cube.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
