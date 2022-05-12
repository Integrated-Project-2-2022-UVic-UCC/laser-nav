##RESUMEN DE DONDE LO DEJE
##	El radio lo hallamos bien
##  Los centros de las circunferencias no los halla bien
##  Aun no he podido comprobar la interseccion de las circunferencias




## Calcular las distancias a partir de las coordenadas de los espejos y el ángulo

## Valores de prueba:
x1=3
y1=0.5
x2=2.25
y2=2
x3=0
y3=1.5
alpha1=0.68573986310857209077331810293918 		##radianes
alpha2=1.1658799403322121573850254333504 		##radianes


## EL CODIGO EMPIEZA AQUI

import math

l1=3 		##medida del eje x de la superficie considerada
l2=2 		##medida del eje y de la superficie considerada
espejo_a=[x1, y1]
espejo_b=[x2, y2]
espejo_c=[x3, y3]
angulo1=alpha1 		##tiene que estar en radianes!
angulo2=alpha2 		##tiene que estar en radianes!
dist_ab=((espejo_b[0]-espejo_a[0])**2+(espejo_b[1]-espejo_a[1])**2)**0.5 		##distancia entre los espejos a y b
dist_bc=((espejo_c[0]-espejo_b[0])**2+(espejo_c[1]-espejo_b[1])**2)**0.5 		##distancia entre los espejos a y b


print("La distancia AB es:", dist_ab)
print("La distancia BC es:", dist_bc)

def RadioCircunferencia(angulo,dist_espejos):
	dist_s2=dist_espejos/(2*math.sin(angulo/2)) 		##dist espejo 2 y sensor
	dist_se=dist_s2*math.cos(angulo/2) 		##dist sensor y punto medio de la recta entre los espejos
	dist_2d=dist_espejos/(2*math.cos(angulo/2)) 		##dist espejo 2 y extremo opuesto al sensor en la circunferencia
	dist_de=((dist_2d)**2-(dist_espejos/2)**2)**0.5 		##dist punto medio de la recta entre los espejos y el extremo de la circunferencia opuesto al sensor
	r=(dist_se+dist_de)/2 		##valor del radio de la circunferencia
	return r

r1=RadioCircunferencia(angulo1,dist_ab)
r2=RadioCircunferencia(angulo2,dist_bc)
print("\nEl radio de la primera circunferencia es:", r1)
print("El radio de la segunda circunferencia es:", r2)


## Ya funciona! Solo hay que ver que par de valores es valido
def CentroCircunferencia(a,b,c,d,r):
	E=c*c+d*d-a*a-b*b
	F=d-b
	G=c-a

	P=4*(F*F+G*G)
	Q=4*(-E*F+2*a*F*G-2*b*G*G)
	R=E*E+4*G*(-a*E+a*a*G+b*b*G-r*r*G)

	N=Q*Q-4*P*R
	if N>=0:
		y1=(-Q+(N**0.5))/(2*P)
		y2=(-Q-(N**0.5))/(2*P)
		x1=(E-2*F*y1)/(2*G)
		x2=(E-2*F*y2)/(2*G)
	else:
		y1="\tAlgo va mal\t"
		x1="\tAlgo va mal\t"
		y2="\tAlgo va mal\t"
		x2="\tAlgo va mal\t"
	return x1,y1,x2,y2

xc11,yc11,xc12,yc12=CentroCircunferencia(x1,y1,x2,y2,r1)
xc21,yc21,xc22,yc22=CentroCircunferencia(x2,y2,x3,y3,r2)
print("\nLas posibles coordenadas del centro de la primera circunferencia son:")
print("\tPrimer par (x,y):",xc11,yc11)
print("\tSegundo par (x,y):",xc12,yc12)
print("Las posibles coordenadas del centro de la segunda circunferencia son:")
print("\tPrimer par (x,y):",xc21,yc21)
print("\tSegundo par (x,y):",xc22,yc22)


##  Lo he cambiado muchas veces. Puede estar mal!
def IntersecciónCircunferencias(a,b,c,d,e,f,espejo_b,l1,l2):
	## (x-a)**2+(y-b)**2=c**2
	## (x-d)**2+(y-e)**2=f**2
	
	# A=d-a
	# B=e-b
	# C=c*c-f*f-a*a+d*d-b*b+e*e

	# P=4*(A*A-B*B)
	# Q=-8*(A*B*a+A*A*b)
	# R=C*C-4*A*(a*C+A*a*a+A*b*b-A*c*c)


	# N=Q*Q-4*P*R
	# if N>=0:
	# 	y=(-Q+(N**0.5))/(2*P)
	# 	if y<0 or y==espejo_b[1] or y>l2:
	# 		y=(-Q-(N**0.5))/(2*P)
	# 	x=(C-2*B*y)/(2*A)
	# else:
	# 	y=l2+1
	# 	x=-1



	N=(c**2)-(f**2)-(a**2)+(d**2)-(b**2)+(e**2)
	O=(4*((e-b)**2))-(4*((d-a)**2))
	P=-(4*N*(e-b))+(8*a*(d-a)*(e-b))-(8*b*((d-a)**2))
	Q=-(4*((d-a)**2)*((c**2)-(a**2)-(b**2))-(N**2)+4*(d-a)*N*a)
	y=(-P+(((P**2)-(4*O*Q))**0.5))/(2*O)
	if y<0 or y==espejo_b[1] or y>l2:
##		y=(-Q-(((Q**2)-(4*P*R))**0.5))/(2*P)
		y=(-P-(((P**2)-(4*O*Q))**0.5))/(2*O)
	x=((c**2)-(f**2)-(a**2)+(d**2)-(2*y*(e-b))-(b**2)+(e**2))/(2*(d-a))



	if x<0 or x>l1:
		x="\tAlgo va mal\t"
	if y<0 or y>l2:
		y="\tAlgo va mal\t"
	return x,y

pos_sensor_x1,pos_sensor_y1=IntersecciónCircunferencias(xc11,yc11,r1,xc21,yc21,r2,espejo_b,l1,l2)
pos_sensor_x2,pos_sensor_y2=IntersecciónCircunferencias(xc12,yc12,r1,xc22,yc22,r2,espejo_b,l1,l2)

pos_sensor_x3,pos_sensor_y3=IntersecciónCircunferencias(xc11,yc11,r1,xc22,yc22,r2,espejo_b,l1,l2)
pos_sensor_x4,pos_sensor_y4=IntersecciónCircunferencias(xc12,yc12,r1,xc21,yc21,r2,espejo_b,l1,l2)

print("\nLa posición del sensor en x e y es:",pos_sensor_x1,pos_sensor_y1)
print("\nLa posición del sensor en x e y es:",pos_sensor_x2,pos_sensor_y2)   ## Este es el valor que debe dar! (0.5 , 0.25)

print("\nLa posición del sensor en x e y es:",pos_sensor_x3,pos_sensor_y3)
print("\nLa posición del sensor en x e y es:",pos_sensor_x4,pos_sensor_y4)
