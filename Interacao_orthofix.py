from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global xf, yf, win, view_w, view_h,rsize
rsize=25
# Função callback chamada para fazer o desenho
def Desenha():
     global xf, yf
                   
     glClear(GL_COLOR_BUFFER_BIT)
     # Desenha um retângulo preenchido com a cor corrente
     glBegin(GL_POLYGON)
     glVertex2f(xf, yf)
     glVertex2f(xf, yf+rsize)
     glVertex2f(xf+rsize, yf+rsize)
     glVertex2f(xf+rsize, yf)
     glEnd()
     glFlush()

# Inicializa parâmetros de rendering
def Inicializa ():
    global xf, yf, win
    # Define a cor de fundo da janela de visualização como preta
    glClearColor(0.0, 0.0, 0.0, 1.0)
    xf=5.0
    yf=5.0
    win=100.0

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
    gluOrtho2D (0, 100, 0, 100)

# Função callback chamada para gerenciar eventos de teclado
def GerenciaTeclado(key, x, y):
    if(key==b'R' or key ==b'r'):
        glColor3f(1.0, 0.0, 0.0)
    elif (key==b'G' or key ==b'g'):
        glColor3f(0.0, 1.0, 0.0)
    elif (key==b'B' or key ==b'b'):
        glColor3f(0.0, 0.0, 1.0)
    glutPostRedisplay()
           
# Função callback chamada para gerenciar eventos do mouse
def GerenciaMouse(button, state, x, y):
    global xf, yf, win, view_w, view_h
    if (button == GLUT_LEFT_BUTTON):
         if (state == GLUT_DOWN):
                  # Troca o tamanho do retângulo, que vai do centro da 
                  # janela até a posição onde o usuário clicou com o mouse
                  escalax = 100.0/(view_w);
                  xf = x*escalax;
                  escalay= 100.0/(view_h);
                  yf = 100-(y*escalay);
    glutPostRedisplay()

#// Função callback chamada para gerenciar eventos do teclado   
#// para teclas especiais, tais como F1, PgDn e Home
def TeclasEspeciais(key, x, y):
    global xf, yf, win
    if(key == GLUT_KEY_UP):
           yf=yf+2
           if (yf+rsize>win): yf=win-rsize

    if(key == GLUT_KEY_DOWN):
           yf=yf-2
           if (yf<0): yf=0

    if(key == GLUT_KEY_LEFT):
           xf=xf-2
           if (xf<0): xf=0
           
    if(key == GLUT_KEY_RIGHT):
           xf=xf+2
           if (xf+rsize>win): xf=win-rsize

    glutPostRedisplay()
                      
#// Programa Principal 
def main():
     glutInit(sys.argv)
     glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
     glutInitWindowSize(350,300)
     glutInitWindowPosition(10,10)
     glutCreateWindow(b"Exemplo de Interacao")
     glutDisplayFunc(Desenha)
     glutReshapeFunc(AlteraTamanhoJanela)
     glutKeyboardFunc(GerenciaTeclado)
     glutMouseFunc(GerenciaMouse)
     glutSpecialFunc(TeclasEspeciais)
     Inicializa()
     glutMainLoop()

main()
