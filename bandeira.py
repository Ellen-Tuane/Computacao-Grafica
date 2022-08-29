from OpenGL.GLUT import *
from OpenGL.GL import *

def desenha():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Define o fundo branco
    glMatrixMode(GL_MODELVIEW)
    # fundo branco
    glBegin(GL_POLYGON);
    glColor3f(255, 255, 255);
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


    glBegin(GL_POLYGON);
    glColor3f(0, 0, 255);
    # inferior esq
    glVertex3f(-1, 0.0, 0.0);
    # superior esq
    glVertex3f(-1, 1, 0.0);
    # superior direita
    glVertex3f(-.3, 1, 0.0);
    # inferior direita
    glVertex3f(-.3, 0, 0.0);
    glEnd();
    glFlush()

    # Desenha Triangulo branco
    glBegin(GL_TRIANGLES)
    glColor3f(255.0, 255.0, 255.0)
    #esquerda
    glVertex2f(-0.9, 0.2)
    # topo
    glVertex2f(-.65, .9)
    # direita
    glVertex2f(-.4, 0.2)
    glEnd()
    glFlush()

    glBegin(GL_POLYGON);
    glColor3f(255, 0, 0);
    # inferior esq
    glVertex3f(-.3, 0, 0.0);
    # superior esq
    glVertex3f(-.3, .5, 0.0);
    # superior direita
    glVertex3f(1, 0.5, 0.0);
    # inferior direita
    glVertex3f(1, 0, 0.0);
    glEnd();
    glFlush()

    glBegin(GL_POLYGON);
    glColor3f(255, 0, 0);
    # inferior dir
    glVertex3f(1, -1, 0.0);
    # superior esq
    glVertex3f(1, -.5, 0.0);

    # superior esq
    glVertex3f(-1, -0.5, 0.0);
    # inferior esq
    glVertex3f(-1, -1, 0.0);
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
    glutInitWindowSize(500,300)
    glutCreateWindow(b'Bandeira Estado da Bahia')
    glutDisplayFunc(desenha)
#    glutDisplayFunc(DesenhaTriangulo)
#    glutDisplayFunc(DesenhaTriangulo2)
#    glutDisplayFunc(TeladeFundo)
    glutMainLoop()

main()


if __name__ == '__main__':
    main()