from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global windowWidth,windowHeight,x1,y1,rsize,xstep,ystep

#Tamanho e posição inicial do quadrado

x1 = 100.0
y1 = 150.0
rsize = 50                                                 

#Tamanho do incremento nas direções x e y 
#(número de pixels para se mover a cada
#intervalo de tempo)
xstep = 1.0
ystep = 1.0

#Largura e altura da janela

def Desenha():
    global windowWidth,windowHeight,x1,y1,rsize,xstep,ystep
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
                 
    #Limpa a janela de visualização com a cor de fundo especificada
    glClear(GL_COLOR_BUFFER_BIT)

    #Especifica que a cor corrente é vermelha
    #         R     G     B
    glColor3f(1.0, 0.0, 0.0)
  
    # Desenha um quadrado preenchido com a cor corrente
    glBegin(GL_QUADS)
    glVertex2i(int(x1),int(y1+rsize))
    glVertex2i(int(x1),int(y1))
    # Especifica que a cor corrente é azul
    glColor3f(0.0, 0.0, 1.0)
    glVertex2i(int(x1+rsize),int(y1))
    glVertex2i(int(x1+rsize),int(y1+rsize))
    glEnd()

     # Executa os comandos OpenGL
    glutSwapBuffers()

def Timer(value):
   global windowWidth,windowHeight,x1,y1,rsize,xstep,ystep
   # Muda a direção quando chega na borda esquerda ou direita
   if(x1 > windowWidth-rsize or x1 < 0):
            xstep = -xstep

   # Muda a direção quando chega na borda superior ou inferior
   if(y1 > windowHeight-rsize or y1 < 0):
          ystep = -ystep
          
   # Verifica as bordas.  Se a window for menor e o 
   # quadrado sair do volume de visualização 
   if(x1 > windowWidth-rsize):
         x1 = windowWidth-rsize-1

   if(y1 > windowHeight-rsize):
         y1 = windowHeight-rsize-1

   # Move o quadrado
   x1 += xstep
   y1 += ystep

   # Redesenha o quadrado com as novas coordenadas 
   glutPostRedisplay()
   glutTimerFunc(33,Timer, 1)
    
# Inicializa parâmetros de rendering
def Inicializa():   
    glClearColor(0.0, 0.0, 0.0, 1.0)#; // Define a cor de fundo da janela de visualização como preta

def AlteraTamanhoJanela(w, h):
    global windowWidth,windowHeight,x1,y1,rsize,xstep,ystep
    # Evita a divisao por zero
    if(h == 0):
        h = 1
                           
    # Especifica as dimensões da Viewport
    glViewport(0, 0, w, h)

    # Inicializa o sistema de coordenadas
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # Estabelece a janela de seleção (left, right, bottom, top)     
    if (w <= h):
        windowHeight = 250.0*h/w
        windowWidth = 250.0
    else:
        windowWidth = 250.0*w/h
        windowHeight = 250.0

    #windowWidth = w
    #windowHeight = h
    gluOrtho2D(0.0, windowWidth, 0.0, windowHeight)
    
#// Programa Principal 
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(400,350);
    glutInitWindowPosition(10,10);
    glutCreateWindow(b"Anima");
    glutDisplayFunc(Desenha);
    glutReshapeFunc(AlteraTamanhoJanela);
    glutTimerFunc(33, Timer, 1);
    Inicializa();
    glutMainLoop();

main()
