from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global wo, ho, windowWidth, windowHeight, x1, y1, xstep, ystep, x2, y2, win

x1 = 0
y1 = 0
x2 = 0
y2 = 0
xstep = 1
ystep = 1


# Funcao callback chamada para fazer o desenho
def Desenha():
    global wo, ho, windowWidth, windowHeight, x2, y2, x1, y1
    glClear(GL_COLOR_BUFFER_BIT)
    glViewport(0, 0, int(wo / 2), int(ho))
    # Inicializa o sistema de coordenadas
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    if (wo <= ho):
        windowHeight = 500 * ho / wo
        windowWidth = 250
    else:
        windowWidth = 250 * wo / ho
        windowHeight = 250
    gluOrtho2D(0.0, windowWidth, windowHeight, 0.0);

    # Quadrado Azul
    glBegin(GL_POLYGON);
    glColor3f(0, 0, 255);
    # inferior esq
    glVertex3f(-0.7 + x1, 0.0 + y1, 0.0);
    # superior esq
    glVertex3f(-0.7 + x1, 0.65 + y1, 0.0);
    # superior direita
    glVertex3f(-.3 + x1, 0.65 + y1, 0.0);
    # inferior direita
    glVertex3f(-.3 + x1, 0 + y1, 0.0);
    glEnd();

    # Desenha Triangulo branco
    glBegin(GL_TRIANGLES)
    glColor3f(255.0, 255.0, 255.0)
    # esquerda
    glVertex2f(-0.65 + x1, 0.1 + y1)
    # topo
    glVertex2f(-.5 + x1, .55 + y1)
    # direita
    glVertex2f(-.35 + x1, 0.1 + y1)
    glEnd()

    # Linha branca superior
    glBegin(GL_POLYGON);
    glColor3f(255, 255, 255);
    # superior esq
    glVertex3f(-.3 + x1, .65 + y1, 0.0);
    # superior dir
    glVertex3f(.7 + x1, .65 + y1, 0.0);
    # inferior dir
    glVertex3f(.7 + x1, .35 + y1, 0.0);
    # inferior esq
    glVertex3f(-.3 + x1, .35 + y1, 0.0);
    glEnd();

    # Linha vermelha superior
    glBegin(GL_POLYGON);
    glColor3f(255, 0, 0);
    # inferior esq
    glVertex3f(-.3 + x1, 0 + y1, 0.0);
    # superior esq
    glVertex3f(-.3 + x1, .35 + y1, 0.0);
    # superior direita
    glVertex3f(.7 + x1, 0.35 + y1, 0.0);
    # inferior direita
    glVertex3f(.7 + x1, 0 + y1, 0.0);
    glEnd();

    # Linha vermelha inferior
    glBegin(GL_POLYGON);
    glColor3f(255, 0, 0);
    # superior dir
    glVertex3f(.7 + x1, -.35 + y1, 0.0);
    # inferior dir
    glVertex3f(.7 + x1, -.7 + y1, 0.0);
    # superior esq
    glVertex3f(-.7 + x1, -0.7 + y1, 0.0);
    # inferior esq
    glVertex3f(-.7 + x1, -.35 + y1, 0.0);
    glEnd();

    # Linha branca inferior
    glBegin(GL_POLYGON);
    glColor3f(255, 255, 255);
    # superior dir
    glVertex3f(.7 + x1, 0 + y1, 0.0);
    # superior esq
    glVertex3f(-.7 + x1, 0 + y1, 0.0);
    # inferior esq
    glVertex3f(-.7 + x1, -.35 + y1, 0.0);
    # inferior dir
    glVertex3f(.7 + x1, -.35 + y1, 0.0);
    glEnd();

    glutSwapBuffers()

    #    //Segunda View port
    glViewport(int(wo / 2), 0, int(wo / 2), ho);
    #    // Inicializa o sistema de coordenadas
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    gluOrtho2D(0.0, windowWidth, windowHeight, 0.0);

    # Quadrado Azul
    glBegin(GL_POLYGON);
    glColor3f(0, 0, 255);
    # inferior esq
    glVertex3f(-0.7 + x2, 0.0 + y2, 0.0);
    # superior esq
    glVertex3f(-0.7 + x2, 0.65 + y2, 0.0);
    # superior direita
    glVertex3f(-.3 + x2, 0.65 + y2, 0.0);
    # inferior direita
    glVertex3f(-.3 + x2, 0 + y2, 0.0);
    glEnd();

    # Desenha Triangulo branco
    glBegin(GL_TRIANGLES)
    glColor3f(255.0, 255.0, 255.0)
    # esquerda
    glVertex2f(-0.65 + x2, 0.1 + y2)
    # topo
    glVertex2f(-.5 + x2, .55 + y2)
    # direita
    glVertex2f(-.35 + x2, 0.1 + y2)
    glEnd()

    # Linha branca superior
    glBegin(GL_POLYGON);
    glColor3f(255, 255, 255);
    # superior esq
    glVertex3f(-.3 + x2, .65 + y2, 0.0);
    # superior dir
    glVertex3f(.7 + x2, .65 + y2, 0.0);
    # inferior dir
    glVertex3f(.7 + x2, .35 + y2, 0.0);
    # inferior esq
    glVertex3f(-.3 + x2, .35 + y2, 0.0);
    glEnd();

    # Linha vermelha superior
    glBegin(GL_POLYGON);
    glColor3f(255, 0, 0);
    # inferior esq
    glVertex3f(-.3 + x2, 0 + y2, 0.0);
    # superior esq
    glVertex3f(-.3 + x2, .35 + y2, 0.0);
    # superior direita
    glVertex3f(.7 + x2, 0.35 + y2, 0.0);
    # inferior direita
    glVertex3f(.7 + x2, 0 + y2, 0.0);
    glEnd();

    # Linha vermelha inferior
    glBegin(GL_POLYGON);
    glColor3f(255, 0, 0);
    # superior dir
    glVertex3f(.7 + x2, -.35 + y2, 0.0);
    # inferior dir
    glVertex3f(.7 + x2, -.7 + y2, 0.0);
    # superior esq
    glVertex3f(-.7 + x2, -0.7 + y2, 0.0);
    # inferior esq
    glVertex3f(-.7 + x2, -.35 + y2, 0.0);
    glEnd();

    # Linha branca inferior
    glBegin(GL_POLYGON);
    glColor3f(255, 255, 255);
    # superior dir
    glVertex3f(.7 + x2, 0 + y2, 0.0);
    # superior esq
    glVertex3f(-.7 + x2, 0 + y2, 0.0);
    # inferior esq
    glVertex3f(-.7 + x2, -.35 + y2, 0.0);
    # inferior dir
    glVertex3f(.7 + x2, -.35 + y2, 0.0);
    glEnd();

    glutSwapBuffers()
def Inicializa():
    global win
    win = 250
    glClearColor(0.0, 0.0, 0.0, 1.0)


def AlteraTamanhoJanela(w, h):
    global wo, ho
    if (h == 0): h = 1
    wo = w
    ho = h


def Timer(value):
    global windowWidth, windowHeight, x1, y1, xstep, ystep
    if (x1 > windowWidth - 70 or x1 < 0): xstep = -xstep

    if (y1 > windowHeight - 45 or y1 < 0): ystep = -ystep

    if (x1 > windowWidth - 70): x1 = windowWidth - 70 - 1

    if (y1 > windowHeight - 45): y1 = windowHeight - 45 - 1

    x1 += xstep
    y1 += ystep

    glutPostRedisplay()
    glutTimerFunc(33, Timer, 1)


def GerenciaTeclado(key, x, y):
    if (key == b'R' or key == b'r'):
        glColor3f(1.0, 0.0, 0.0)
    elif (key == b'G' or key == b'g'):
        glColor3f(0.0, 1.0, 0.0)
    elif (key == b'B' or key == b'b'):
        glColor3f(0.0, 0.0, 1.0)
    glutPostRedisplay()


def GerenciaMouse(button, state, x, y):
    global x2, y2, win, wo, ho
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
            # Troca o tamanho do retângulo, que vai do centro da
            # janela até a posição onde o usuário clicou com o mouse
            escalax = (500) / (wo)

            x2 = (x - wo / 2) * escalax

            escalay = 500 / (ho)

            y2 = y * escalay
    glutPostRedisplay()


def TeclasEspeciais(key, x, y):
    global x2, y2, win
    if (key == GLUT_KEY_UP):
        y2 = y2 - 2
        if (y2 < 0): y2 = 0
    if (key == GLUT_KEY_DOWN):
        y2 = y2 + 2
        if (y2 > 455): y2 = 455

    if (key == GLUT_KEY_LEFT):
        x2 = x2 - 2
        if (x2 < 0): x2 = 0

    if (key == GLUT_KEY_RIGHT):
        x2 = x2 + 2
        if (x2 + 70 > win): x2 = win - 70

    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(10, 10)
    glutCreateWindow(b"Multiplas ViewPorts")
    glutDisplayFunc(Desenha)
    glutReshapeFunc(AlteraTamanhoJanela)
    glutTimerFunc(33, Timer, 1)
    glutKeyboardFunc(GerenciaTeclado)
    glutMouseFunc(GerenciaMouse)
    glutSpecialFunc(TeclasEspeciais)
    Inicializa()
    glutMainLoop()


main()
