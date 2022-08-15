from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def Desenha():

    glClearColor(1.0, 0.5, 0.0, 1.0) #Define a cor de fundo da janela de visualização como preta
    glClear(GL_COLOR_BUFFER_BIT) #Limpa a janela de visualização com a cor de fundo especificada
    glFlush() #Executa os comandos OpenGL

#// Programa Principal
def main():
#glutInit(sys.argv)
    glutCreateWindow(b'Ola Mundo OpenGL')
    glutDisplayFunc(Desenha)
    glutMainLoop()
main()