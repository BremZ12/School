import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# ================= KUBUS 3D =================
cube_vertices = [
    (-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),
    (-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)
]

cube_edges = [
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7)
]

cube_tx, cube_ty, cube_tz = -3, 0, -10
cube_rx = cube_ry = cube_rz = 0
cube_scale = 1.0

# ================= PERSEGI 2D =================
square = [(-0.5,-0.5),(0.5,-0.5),(0.5,0.5),(-0.5,0.5)]
sq_tx, sq_ty = 3, 0
sq_rot = 0
sq_scale = 1
shear = 0
reflect = 1

# ================= DRAW FUNCTIONS =================
def draw_cube():
    glPushMatrix()
    glTranslatef(cube_tx, cube_ty, cube_tz)
    glRotatef(cube_rx,1,0,0)
    glRotatef(cube_ry,0,1,0)
    glRotatef(cube_rz,0,0,1)
    glScalef(cube_scale, cube_scale, cube_scale)

    glBegin(GL_LINES)
    glColor3f(1,1,1)
    for e in cube_edges:
        for v in e:
            glVertex3fv(cube_vertices[v])
    glEnd()
    glPopMatrix()

def draw_square():
    glPushMatrix()
    glTranslatef(sq_tx, sq_ty, -5)
    glRotatef(sq_rot,0,0,1)
    glScalef(reflect*sq_scale, sq_scale, 1)

    glMultMatrixf([
        1, shear, 0, 0,
        0, 1,     0, 0,
        0, 0,     1, 0,
        0, 0,     0, 1
    ])

    glBegin(GL_QUADS)
    glColor3f(0,1,0)
    for v in square:
        glVertex2fv(v)
    glEnd()
    glPopMatrix()

# ================= MAIN =================
def main():
    global cube_tx, cube_ty, cube_tz
    global cube_rx, cube_ry, cube_rz, cube_scale
    global sq_tx, sq_ty, sq_rot, sq_scale, shear, reflect

    pygame.init()
    pygame.display.set_mode((800,600), DOUBLEBUF|OPENGL)
    gluPerspective(45, 800/600, 0.1, 50)
    glEnable(GL_DEPTH_TEST)

    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                quit()

            if e.type == KEYDOWN:
                # ===== KUBUS 3D =====
                if e.key == K_w: cube_ty += 0.2
                if e.key == K_s: cube_ty -= 0.2
                if e.key == K_a: cube_tx -= 0.2
                if e.key == K_d: cube_tx += 0.2
                if e.key == K_q: cube_tz += 0.2
                if e.key == K_e: cube_tz -= 0.2
                if e.key == K_x: cube_rx += 10
                if e.key == K_y: cube_ry += 10
                if e.key == K_z: cube_rz += 10
                if e.key == K_EQUALS: cube_scale += 0.1
                if e.key == K_MINUS: cube_scale -= 0.1

                # ===== PERSEGI 2D =====
                if e.key == K_i: sq_ty += 0.2
                if e.key == K_k: sq_ty -= 0.2
                if e.key == K_j: sq_tx -= 0.2
                if e.key == K_l: sq_tx += 0.2
                if e.key == K_r: sq_rot += 10
                if e.key == K_u: sq_scale += 0.1
                if e.key == K_o: sq_scale -= 0.1
                if e.key == K_h: shear += 0.2
                if e.key == K_f: reflect *= -1

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_cube()
        draw_square()
        pygame.display.flip()
        pygame.time.wait(10)

main()
