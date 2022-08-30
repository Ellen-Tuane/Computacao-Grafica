from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def AlteraTamanhoJanela(w, h):
#Evita a divisao por zero
    if(h == 0): h = 1
#Especifica as dimensões da Viewport
    glViewport(0, 0, w, h)
#Inicializa o sistema de coordenadas
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    print(w, h, "\n")
#Estabelece a janela de seleção (left, right, bottom, top)
    gluOrtho2D(0.0, 100.0, 100.0, 0.0)


def Desenha():

    glClearColor(1.0, 0.5, 0.0, 1.0) #Define a cor de fundo da janela de visualização como preta
    glClear(GL_COLOR_BUFFER_BIT) #Limpa a janela de visualização com a cor de fundo especificada
    glFlush() #Executa os comandos OpenGL

#// Programa Principal
def main():
    glutInit(sys.argv)
    glutCreateWindow(b'Ola Mundo OpenGL')
    glutInitWindowSize(700, 350)
    glutReshapeFunc(AlteraTamanhoJanela(700,350))
    glutDisplayFunc(Desenha)
    glutMainLoop()
main()