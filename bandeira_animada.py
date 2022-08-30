from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global windowWidth,windowHeight,x1,y1,rsize,xstep,ystep

#Tamanho e posição inicial do quadrado

x1 = 1
y1 = 1

#Tamanho do incremento nas direções x e y
#(número de pixels para se mover a cada
#intervalo de tempo)
xstep = 1
ystep = 1
def desenha():
    global windowWidth, windowHeight, x1, y1, xstep, ystep
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Limpa a janela de visualização com a cor de fundo especificada
    glClear(GL_COLOR_BUFFER_BIT)
    #glClearColor(1.0, 1.0, 1.0, 1.0)  # Define o fundo branco
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
    glVertex2f(-.35 + x1, 0.1+ y1)
    glEnd()


    # Linha branca superior
    glBegin(GL_POLYGON);
    glColor3f(255, 255, 255);
    # superior esq
    glVertex3f(-.3 + x1, .65+ y1, 0.0);
    # superior dir
    glVertex3f(.7 + x1, .65+ y1, 0.0);
    # inferior dir
    glVertex3f(.7 + x1, .35+ y1, 0.0);
    # inferior esq
    glVertex3f(-.3 + x1, .35+ y1, 0.0);
    glEnd();


    # Linha vermelha superior
    glBegin(GL_POLYGON);
    glColor3f(255, 0, 0);
    # inferior esq
    glVertex3f(-.3 + x1, 0+ y1, 0.0);
    # superior esq
    glVertex3f(-.3 + x1, .35+ y1, 0.0);
    # superior direita
    glVertex3f(.7 + x1, 0.35+ y1, 0.0);
    # inferior direita
    glVertex3f(.7 + x1, 0+ y1, 0.0);
    glEnd();


    # Linha vermelha inferior
    glBegin(GL_POLYGON);
    glColor3f(255, 0, 0);
    # superior dir
    glVertex3f(.7 + x1, -.35+ y1, 0.0);
    # inferior dir
    glVertex3f(.7 + x1, -.7+ y1, 0.0);
    # superior esq
    glVertex3f(-.7 + x1, -0.7+ y1, 0.0);
    # inferior esq
    glVertex3f(-.7 + x1, -.35+ y1, 0.0);
    glEnd();


    # Linha branca inferior
    glBegin(GL_POLYGON);
    glColor3f(255, 255, 255);
    # superior dir
    glVertex3f(.7 + x1, 0+ y1, 0.0);
    # superior esq
    glVertex3f(-.7 + x1, 0+ y1, 0.0);
    # inferior esq
    glVertex3f(-.7 + x1, -.35+ y1, 0.0);
    # inferior dir
    glVertex3f(.7 + x1, -.35+ y1, 0.0);
    glEnd();

    glutSwapBuffers()

def Timer(value):
    global windowWidth, windowHeight, x1, y1, xstep, ystep
    # Muda a direção quando chega na borda esquerda ou direita
    if (x1 > windowWidth or x1 < 0):
        xstep = -xstep

    # Muda a direção quando chega na borda superior ou inferior
    if (y1 > windowHeight or y1 < 0):
        ystep = -ystep

    # Verifica as bordas.  Se a window for menor e o
    # quadrado sair do volume de visualização
    if (x1 > windowWidth):
        x1 = windowWidth - 1

    if (y1 > windowHeight):
        y1 = windowHeight - 1

    # Move o quadrado
    x1 += xstep
    y1 += ystep

    # Redesenha o quadrado com as novas coordenadas
    glutPostRedisplay()
    glutTimerFunc(500, Timer, 1)


# Inicializa parâmetros de rendering
def Inicializa():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # ; // Define a cor de fundo da janela de visualização como preta


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
        windowHeight = 7.5 * h / w
        windowWidth = 15
    else:
        windowWidth = 7.5 * w / h
        windowHeight = 15

    # windowWidth = w
    # windowHeight = h
    gluOrtho2D(0.0, windowWidth, 0.0, windowHeight)

# // Programa Principal
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(400, 350)
    glutInitWindowPosition(5, 100)
    glutCreateWindow(b'Bandeira Estado da Bahia Animada')
    glutDisplayFunc(desenha)
    glutReshapeFunc(AlteraTamanhoJanela)
    glutTimerFunc(33, Timer, 1)
    Inicializa()
    glutMainLoop()

main()

if __name__ == '__main__':
    main()