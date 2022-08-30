from OpenGL.GLUT import *
from OpenGL.GL import *

def desenha():


    glClearColor(1.0, 1.0, 1.0, 1.0)  # Define o fundo branco
    glMatrixMode(GL_MODELVIEW)
    # fundo branco
    glBegin(GL_POLYGON);
    glColor3f(0, 0, 0);
    # inferior esq
    glVertex3f(-1, 1, 0.0);
    # superior esq
    glVertex3f(-1, -1, 0.0);
    # superior direita
    glVertex3f(1, -1, 0.0);
    # inferior direita
    glVertex3f(1, 1, 0.0);
    glEnd();
    glFlush()

    # Quadrado Azul
    glBegin(GL_POLYGON);
    glColor3f(0, 0, 255);
    # inferior esq
    glVertex3f(-0.7, 0.0, 0.0);
    # superior esq
    glVertex3f(-0.7, 0.65, 0.0);
    # superior direita
    glVertex3f(-.3, 0.65, 0.0);
    # inferior direita
    glVertex3f(-.3, 0, 0.0);
    glEnd();
    glFlush()

    # Desenha Triangulo branco
    glBegin(GL_TRIANGLES)
    glColor3f(255.0, 255.0, 255.0)
    #esquerda
    glVertex2f(-0.65, 0.1)
    # topo
    glVertex2f(-.5, .55)
    # direita
    glVertex2f(-.35, 0.1)
    glEnd()
    glFlush()

    # Linha branca superior
    glBegin(GL_POLYGON);
    glColor3f(255, 255, 255);
    # superior esq
    glVertex3f(-.3, .65, 0.0);
    # superior dir
    glVertex3f(.7, .65, 0.0);
    # inferior dir
    glVertex3f(.7, .35, 0.0);
    # inferior esq
    glVertex3f(-.3, .35, 0.0);

    glEnd();
    glFlush()

    # Linha vermelha superior
    glBegin(GL_POLYGON);
    glColor3f(255, 0, 0);
    # inferior esq
    glVertex3f(-.3, 0, 0.0);
    # superior esq
    glVertex3f(-.3, .35, 0.0);
    # superior direita
    glVertex3f(.7, 0.35, 0.0);
    # inferior direita
    glVertex3f(.7, 0, 0.0);
    glEnd();
    glFlush()

    #Linha vermelha inferior
    glBegin(GL_POLYGON);
    glColor3f(255, 0, 0);
    # superior dir
    glVertex3f(.7, -.35, 0.0);
    # inferior dir
    glVertex3f(.7, -.7, 0.0);
    # superior esq
    glVertex3f(-.7, -0.7, 0.0);
    # inferior esq
    glVertex3f(-.7, -.35, 0.0);
    glEnd();
    glFlush()

    # Linha branca inferior
    glBegin(GL_POLYGON);
    glColor3f(255, 255, 255);
    # superior dir
    glVertex3f(.7, 0, 0.0);
    # superior esq
    glVertex3f(-.7, 0, 0.0);
    # inferior esq
    glVertex3f(-.7, -.35, 0.0);
    # inferior dir
    glVertex3f(.7, -.35, 0.0);
    glEnd();
    glFlush()


def render():
    global shaderProgram
    global VAO
    glClearColor(1, 0, 0, 0) #altera cor do fundo
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glUseProgram(shaderProgram)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glUseProgram(0)
    glutSwapBuffers()


#// Programa Principal
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 600)
    glutCreateWindow(b'Bandeira Estado da Bahia')
    glutDisplayFunc(desenha)
    glutMainLoop()

main()


if __name__ == '__main__':
    main()