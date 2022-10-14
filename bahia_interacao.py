from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global xf, yf, win, view_w, view_h, rsize
rsize = 0


# Função callback chamada para fazer o desenho
def Desenha():
    global xf, yf

    glClear(GL_COLOR_BUFFER_BIT)
    # Retângulo Branco
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex2f(xf, yf)
    glVertex2f(xf, 25 + yf)
    glVertex2f(50 + xf, 25 + yf)
    glVertex2f(50 + xf, yf)
    glEnd()

    # Quadrado Azul
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    # superior esquerdo
    glVertex2i(int(xf), int(yf + 25))
    # superior direita
    glVertex2i(int(xf + 12), int(yf + 25))
    # inferior direita
    glVertex2i(int(xf + 12), int(yf + 12))
    # inferior esq
    glVertex2i(int(xf), int(yf + 12))

    glEnd()

    # Desenha Triangulo branco
    glBegin(GL_TRIANGLES)
    glColor3f(255.0, 255.0, 255.0)
    # esquerda
    glVertex2f(1 + xf, 14 + yf)
    # topo
    glVertex2f(6 + xf, 24 + yf)
    # direita
    glVertex2f(11 + xf, 14 + yf)
    glEnd()

    # faixa Vermelha 1
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(xf, yf)
    glVertex2f(50 + xf, yf)
    glVertex2f(50 + xf, 6 + yf)
    glVertex2f(xf, 6 + yf)
    glEnd()

    # faixa Vermelha 1
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(xf + 12, yf + 12)
    glVertex2f(xf + 50, yf + 12)
    glVertex2f(xf + 50, yf + 19)
    glVertex2f(xf + 12, yf + 19)
    glEnd()

    glutSwapBuffers()


# Inicializa parâmetros de rendering
def Inicializa():
    global xf, yf, win
    # Define a cor de fundo da janela de visualização como preta
    glClearColor(0.0, 0.0, 0.0, 1.0)
    xf = 0
    yf = 0
    win = 100.0


# Função callback chamada quando o tamanho da janela é alterado
def AlteraTamanhoJanela(w, h):
    global xf, yf, view_w, view_h
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
    global xf, yf, win, view_w, view_h
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
            # Troca o tamanho do retângulo, que vai do centro da
            # janela até a posição onde o usuário clicou com o mouse
            escalax = 100.0 / (view_w);

            xf = x * escalax;

            escalay = 100.0 / (view_h);

            yf = 100 - (y * escalay);
    glutPostRedisplay()


# // Função callback chamada para gerenciar eventos do teclado
# // para teclas especiais, tais como F1, PgDn e Home
def TeclasEspeciais(key, x, y):
    global xf, yf, win
    if (key == GLUT_KEY_UP):
        yf = yf + 2
        if (yf + rsize > win): yf = win - rsize

    if (key == GLUT_KEY_DOWN):
        yf = yf - 2
        if (yf < 0): yf = 0

    if (key == GLUT_KEY_LEFT):
        xf = xf - 2
        if (xf < 0): xf = 0

    if (key == GLUT_KEY_RIGHT):
        xf = xf + 2
        if (xf + rsize > win): xf = win - rsize

    glutPostRedisplay()


# // Programa Principal
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1500, 1000)
    glutInitWindowPosition(100, 10)
    glutCreateWindow(b"Exemplo de Interacao")
    glutDisplayFunc(Desenha)
    glutReshapeFunc(AlteraTamanhoJanela)
    glutKeyboardFunc(GerenciaTeclado)
    glutMouseFunc(GerenciaMouse)
    glutSpecialFunc(TeclasEspeciais)
    Inicializa()
    glutMainLoop()


main()
