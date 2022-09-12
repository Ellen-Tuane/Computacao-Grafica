from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global x1, y1, win, view_w, view_h, rsize
rsize = 25

# Função callback chamada para fazer o desenho
def Desenha():
    global x1, y1

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Limpa a janela de visualização com a cor de fundo especificada
    glClear(GL_COLOR_BUFFER_BIT)
    # glClearColor(1.0, 1.0, 1.0, 1.0)  # Define o fundo branco
    glMatrixMode(GL_MODELVIEW)

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


# Inicializa parâmetros de rendering
def Inicializa():
    global x1, y1, win
    # Define a cor de fundo da janela de visualização como preta
    glClearColor(0.0, 0.0, 0.0, 1.0)
    x1 = 1.0
    y1 = 1.0
    win = 250


# Função callback chamada quando o tamanho da janela é alterado
def AlteraTamanhoJanela(w, h):
    global x1, y1, view_w, view_h
    # Especifica as dimensões da Viewport
    glViewport(0, 0, w, h)
    view_w = w
    view_h = h

    # Inicializa o sistema de coordenadas
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 100, 0, 100)


# Função callback chamada para gerenciar eventos de teclado
def GerenciaTeclado(key, x, y):
    if (key == b'R' or key == b'r'):
        glColor3f(1.0, 0.0, 0.0)
    elif (key == b'G' or key == b'g'):
        glColor3f(0.0, 1.0, 0.0)
    elif (key == b'B' or key == b'b'):
        glColor3f(0.0, 0.0, 1.0)
    glutPostRedisplay()


# Função callback chamada para gerenciar eventos do mouse
def GerenciaMouse(button, state, x, y):
    global x1, y1, win, view_w, view_h
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
            # Troca o tamanho do retângulo, que vai do centro da
            # janela até a posição onde o usuário clicou com o mouse
            escalax = 100.0 / (view_w)

            x1 = x * escalax

            escalay = 100.0 / (view_h)

            y1 = 100 - (y * escalay)
    glutPostRedisplay()


# // Função callback chamada para gerenciar eventos do teclado
# // para teclas especiais, tais como F1, PgDn e Home
def TeclasEspeciais(key, x, y):
    global x1, y1, win
    if (key == GLUT_KEY_UP):
        y1 = y1 + 2
        if (y1 + rsize > win): y1 = win - rsize

    if (key == GLUT_KEY_DOWN):
        y1 = y1 - 2
        if (y1 < 0): yf = 0

    if (key == GLUT_KEY_LEFT):
        x1 = x1 - 2
        if (x1 < 0): x1 = 0

    if (key == GLUT_KEY_RIGHT):
        x1 = x1 + 2
        if (x1 + rsize > win): x1 = win - rsize

    glutPostRedisplay()


# // Programa Principal
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(350, 300)
    glutInitWindowPosition(10, 10)
    glutCreateWindow(b"Exemplo de Interacao")
    glutDisplayFunc(Desenha)
    glutReshapeFunc(AlteraTamanhoJanela)
    glutKeyboardFunc(GerenciaTeclado)
    glutMouseFunc(GerenciaMouse)
    glutSpecialFunc(TeclasEspeciais)
    Inicializa()
    glutMainLoop()


main()