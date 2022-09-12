from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

global windowWidth, windowHeight, x1, y1, win, view_w, view_h, texto, r, g, b, r1, g1, b1, r2, g2, b2, r3, g3, b3, r4, g4, b4
global teclasHabilitadas
teclasHabilitadas = False
x1 = 0
y1 = 0


def inicializa():
    global win, texto, r, g, b, r1, g1, b1, r2, g2, b2, r3, g3, b3, r4, g4, b4
    glClearColor(0, 0, 0, 1)
    win = 200
    r = 0
    g = 0
    b = 1.0
    r1 = 1.0
    g1 = 1.0
    b1 = 1.0
    r2 = 1
    g2 = 0.0
    b2 = 0.0
    texto = '(0,0)'


def alteraTamanhoJanela(w, h):
    global windowWidth, windowHeight, x1, y1, view_w, view_h
    if (h == 0): h = 1
    glViewport(0, 0, w, h)
    view_w = w
    view_h = h
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if (w <= h):
        windowHeight = 250 * h / w
        windowWidth = 250.0
    else:
        windowHeight = 250.0 * w / h
        windowWidth = 250.0

    # gluOrtho2D(0,windowWidth,windowHeight,0)
    gluOrtho2D(-win, win, win, -win)


def GerenciaMouse(button, state, x, y):
    if (button == GLUT_RIGHT_BUTTON):
        if (state == GLUT_DOWN):  CriaMenu()
    glutPostRedisplay()


def MoveMouseBotaoPressionado(x, y):
    global texto
    #    texto= "Botao pressionado ("+str(x)+","+str(y)+")"
    texto = "Botao pressionado ({0:d},{1:d})".format(x, y)
    glutPostRedisplay()


def MoveMouse(x, y):
    global texto
    texto = "(" + str(x) + "," + str(y) + ")"
    glutPostRedisplay();


def desenhaTexto(string):
    glPushMatrix()
    # Posição no universo onde o texto será colocado
    glRasterPos2f(-win, win - (win * 0.18))
    # Exibe caracter a caracter

    for char in string:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))
        # glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_10,string)
    glPopMatrix()


def desenhaBandeira():
    global windowWidth, windowHeight, x1, y1, win, view_w, view_h, texto, r, g, b, r1, g1, b1, r2, g2, b2, r3, g3, b3, r4, g4, b4

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


def desenha():  # Função callback chamada para fazer o desenho

    global windowWidth, windowHeight, x1, y1, win, view_w, view_h, texto
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)  # Limpa imagem
    desenhaBandeira()
    glColor3f(1.0, 1.0, 1.0)
    desenhaTexto(texto)
    glutSwapBuffers()


# // Função callback chamada para gerenciar eventos do teclado
# // para teclas especiais, tais como F1, PgDn e Home
def TeclasEspeciais(key, x, y):
    global win, teclasHabilitadas

    if (teclasHabilitadas):
        if (key == GLUT_KEY_UP):
            win -= 10
            if (win < 10): win = 10
            glMatrixMode(GL_PROJECTION);
            glLoadIdentity()

            gluOrtho2D(-win, win, win, -win)
            # gluOrtho2D(0,windowWidth,windowHeight,0)

        if (key == GLUT_KEY_DOWN):
            win += 10
            if (win > 500): win = 500;

            glMatrixMode(GL_PROJECTION);
            glLoadIdentity()
            gluOrtho2D(-win, win, win, -win)
            # gluOrtho2D(0,windowWidth,windowHeight,0)

    glutPostRedisplay()


# Gerenciamento do menu com as opções de cores

def MenuTriangulo(op):
    global r1, g1, b1
    if (op == 0):
        r1 = 1.0; g1 = 1.0; b1 = 1.0;
    elif (op == 1):
        r1 = 0.0; g1 = 1.0; b1 = 0.0;
    elif (op == 2):
        r1 = 0.0; g1 = 0.0; b1 = 1.0;
    glutPostRedisplay();
    return 0;


def MenuListrasBrancas(op):
    global r1, g1, b1
    if (op == 0):
        r1 = 1.0; g1 = 1.0; b1 = 1.0;
    elif (op == 1):
        r1 = 0.0; g1 = 1.0; b1 = 0.0;
    elif (op == 2):
        r1 = 0.0; g1 = 0.0; b1 = 1.0;
    glutPostRedisplay();
    return 0;


def MenuListrasVermelhas(op):
    global r2, g2, b2
    if (op == 0):
        r2 = 0.8; g2 = 0.0; b2 = 0.0;
    elif (op == 1):
        r2 = 0.0; g2 = 1.0; b2 = 0.0;
    elif (op == 2):
        r2 = 0.0; g2 = 0.0; b2 = 1.0;
    glutPostRedisplay();
    return 0;

def MenuQuadrado(op):
    global r, g, b
    if (op == 0):
        r = 0.0; g = 0.0; b = 0.6
    elif (op == 1):
        r = 0.0; g = 1.0; b = 0.0
    elif (op == 2):
        r = 1.0; g = 0.0; b = 0.0
    glutPostRedisplay()
    return 0


def redimensionar(op):
    global teclasHabilitadas
    if (op == 0):
        teclasHabilitadas = True
    elif (op == 1):
        teclasHabilitadas = False
    glutPostRedisplay();
    return 0;


def MenuPrincipal(op):
    return 0


def CriaMenu():
    # Criação do Menu

    submenu1 = glutCreateMenu(MenuTriangulo)
    glutAddMenuEntry("Branco", 0)
    glutAddMenuEntry("Verde", 1)
    glutAddMenuEntry("Azul", 2)

    submenu2 = glutCreateMenu(MenuListrasBrancas)
    glutAddMenuEntry("Branco", 0)
    glutAddMenuEntry("Verde", 1)
    glutAddMenuEntry("Azul", 2)

    submenu3 = glutCreateMenu(MenuListrasVermelhas)
    glutAddMenuEntry("Vermelho", 0)
    glutAddMenuEntry("Verde", 1)
    glutAddMenuEntry("Azul", 2)

    submenu5 = glutCreateMenu(MenuQuadrado)
    glutAddMenuEntry("Azul", 0)
    glutAddMenuEntry("Verde", 1)
    glutAddMenuEntry("Vermelho", 2)

    submenu6 = glutCreateMenu(redimensionar)
    glutAddMenuEntry("Habilitar", 0)
    glutAddMenuEntry("Desabilitar", 1)

    menu = glutCreateMenu(MenuPrincipal)
    glutAddSubMenu("Triângulo", submenu1)
    glutAddSubMenu("Listras Brancas", submenu2)
    glutAddSubMenu("Listras Vermelhas", submenu3)
    glutAddSubMenu("Quadrado", submenu5)
    glutAddSubMenu("Redimencionar", submenu6)
    glutAttachMenu(GLUT_RIGHT_BUTTON)
    return 0


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b'Bandeira')
    glutDisplayFunc(desenha)
    glutReshapeFunc(alteraTamanhoJanela)
    glutMotionFunc(MoveMouseBotaoPressionado)
    glutPassiveMotionFunc(MoveMouse)
    glutMouseFunc(GerenciaMouse)
    glutSpecialFunc(TeclasEspeciais)
    inicializa()
    glutMainLoop()


main()
