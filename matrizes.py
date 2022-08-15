import numpy as np
import math


print("1. Calcule a transposta destas matrizes:")
a = np.array([[1,2], [3,4]])
print("matriz a = \n", a, "\n")
print("transpose a = \n", a.transpose())

b = np.array([[5, 7], [13, 8], [9, 1]])
print("\n matriz b = \n", b, "\n")
print("transpose b = \n", b.transpose())

c = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print("\n matriz c = \n", c, "\n")
print("transpose c = \n", c.transpose())

print("\n---------------------------\n")
print("2. Calcule as operações entre matrizes")

aa = np.array([[1, 2], [3, 4]])
print("a)",5*aa, "\n")

bb = np.array([[2, 5], [10, 6]])
bb2 = np.array([[3, 119], [18, 20]])
print("b)", bb+bb2, "\n")

cc = np.array([[2, 5], [10, 6]])
cc2 = np.array([[3, 119], [18, 20]])
print("c)", bb-bb2, "\n")

dd = np.array([[2,5], [4,6]])
dd2 = np.array([[3,9], [8,20]])
print("d)", dd.dot(dd2), "\n")

ee = np.array([[2,5], [10,6]])
ee2 = np.array([[3],[18]])
print("e)", ee+ee2, "\n")

ff = np.array([[2, 5], [10, 6], [8, 11]])
ff2 = np.array([[3, 4], [7, 20]])
print("f)", ff.dot(ff2), "\n")

print("---------------------------\n")
print("3. Realize as seguintes transformações: Translação, rotação, escala e reflexão. \n"
      "Nos vetores abaixo. E no final construa uma matriz homogênea sobre esta matriz")

aaa = np.array([[10], [30]])
aaa_trans = np.array([[5], [15]])
aaa_rot = np.array([[np.cos(30), np.sin(30)], [-np.sin(30), np.cos(30)]])
aaa_esc = np.array([[2, 0], [0, 2]])
aaa_ref = np.array([[-1,0],[0,-1]])
print("Translação a:\n", aaa+aaa_trans, "\n")
print("Rotação a:\n", aaa_rot.dot(aaa), "\n")
print("Escala a:\n", aaa_esc.dot(aaa), "\n")
print("Reflexão a:\n", aaa_ref.dot(aaa), "\n")

bbb = np.array([[21], [45], [10]])
bbb_trans = np.array([[5], [15], [2]])
bbb_rot1 = np.array([[np.cos(30), np.sin(30), 0], [-np.sin(30), np.cos(30), 0], [0, 0, 1]])
bbb_rot2 = np.array([[1, 0, 0], [0, np.cos(30), np.sin(30)], [0, -np.sin(30), np.cos(30)]])
bbb_rot3 = np.array([[np.cos(30), 0, -np.sin(30)], [0, 1, 0], [np.sin(30), 0, np.cos(30)]])
bbb_escala = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 1]])
bbb_ref = np.array([[-1,0,0],[0,-1,0],[0,0,1]])
print("Translação b:\n", bbb+bbb_trans, "\n")
print("Rotação b:\n", bbb_rot1.dot(bbb), "\n")
print("Rotação b:\n", bbb_rot2.dot(bbb), "\n")
print("Rotação b:\n", bbb_rot3.dot(bbb), "\n")
print("Escala b:\n", esc.dot(aaa), "\n")
print("Reflexão b:\n", aaa_ref.dot(aaa), "\n")
