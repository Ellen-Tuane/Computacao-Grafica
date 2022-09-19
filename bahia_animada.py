from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global windowWidth,windowHeight,x1,y1,rsize,xstep,ystep

#Tamanho e posição inicial do quadrado

x1 = 0
y1 = 0

#Tamanho do incremento nas direções x e y
#(número de pixels para se mover a cada
#intervalo de tempo)
xstep = 1
ystep = 1
def desenha():
    global windowWidth, windowHeight, x1, y1, xstep, ystep
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1, 1, 1)  # Retângulo Branco
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x1, 50 + y1)
    glVertex2f(100 + x1, 50 + y1)
    glVertex2f(100 + x1, y1)
    glEnd()


    # Quadrado Azul
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    # superior esquerdo
    glVertex2i(int(x1), int(y1 + 50))
    # superior direita
    glVertex2i(int(x1 + 25), int(y1 + 50))
    # inferior direita
    glVertex2i(int(x1 + 25), int(y1 + 25))
    # inferior esq
    glVertex2i(int(x1), int(y1 + 25))

    glEnd()

    # Desenha Triangulo branco
    glBegin(GL_TRIANGLES)
    glColor3f(255.0, 255.0, 255.0)
    # esquerda
    glVertex2f(3 + x1, 30 + y1)
    # topo
    glVertex2f(12.5 + x1, 47 + y1)
    # direita
    glVertex2f(22 + x1, 30 + y1)
    glEnd()

    # faixa Vermelha 1
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(100 + x1, y1)
    glVertex2f(100 + x1, 12.5 + y1)
    glVertex2f(x1, 12.5 + y1)
    glEnd()

    # faixa Vermelha 1
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(x1 + 25, y1 + 25)
    glVertex2f(x1 + 100, y1 + 25)
    glVertex2f(x1 + 100, y1 + 37.5)
    glVertex2f(x1 + 25, y1 + 37.5)
    glEnd()


    glutSwapBuffers()


def Timer(value):
    global windowWidth, windowHeight, x1, y1, xstep, ystep
    if (x1 > windowWidth - 100 or x1 < 0): xstep = -xstep

    if (y1 > windowHeight - 50 or y1 < 0): ystep = -ystep

    if (x1 > windowWidth - 100): x1 = windowWidth - 100 - 1

    if (y1 > windowHeight - 50): y1 = windowHeight - 50 - 1

    x1 += xstep
    y1 += ystep

    glutPostRedisplay()
    glutTimerFunc(33, Timer, 1)


# Inicializa parâmetros de rendering
def Inicializa():
    glClearColor(0.0, 0.0, 0.0, 1)  # ; // Define a cor de fundo da janela de visualização como preta


def AlteraTamanhoJanela(w, h):
    global windowWidth, windowHeight, x1, y1, xstep, ystep
    # Evita a divisao por zero
    if (h == 0):
        h = 1

    # Especifica as dimensões da Viewport
    glViewport(0, 0, w, h)

    # Inicializa o sistema de coordenadas
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Estabelece a janela de seleção (left, right, bottom, top)
    if (w <= h):
        windowHeight = 250 * h / w
        windowWidth = 250.0
    else:
        windowWidth = 250 * w / h
        windowHeight = 250.0

    # windowWidth = w
    # windowHeight = h
    gluOrtho2D(0.0, windowWidth, 0.0, windowHeight)

# // Programa Principal
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 525)
    glutInitWindowPosition(10, 10)
    glutCreateWindow(b'Bandeira Estado da Bahia Animada')
    glutDisplayFunc(desenha)
    glutReshapeFunc(AlteraTamanhoJanela)
    glutTimerFunc(33, Timer, 1)
    Inicializa()
    glutMainLoop()

main()

if __name__ == '__main__':
    main()