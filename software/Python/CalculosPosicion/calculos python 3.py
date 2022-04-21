import math

## Calcular las distancias a partir de las coordenadas de los espejos y el ángulo
##espejos=[[A, x1, y1],[B, x2, y2],[C, x3, y3]] //coordenadas de los 3 espejos

##Está calculado el valor del radio, falta hallar el centro

x1=3
y1=0
x2=3
y2=2
x3=0
y3=2
alpha=1.176 ##radianes
h1=1.5
k1=1.5
h2=1
k2=2.5

espejo_a=[x1, y1]
espejo_b=[x2, y2]
espejo_c=[x3, y3]
angulo=alpha  																	##tiene que estar en radianes!
dist_ab=((espejo_b[0]-espejo_a[0])**2+(espejo_b[1]-espejo_a[1])**2)**0.5 		##distancia entre los espejos a y b
dist_bc=((espejo_c[0]-espejo_b[0])**2+(espejo_c[1]-espejo_b[1])**2)**0.5 		##distancia entre los espejos a y b


def RadioCircunferencia(angulo,dist_espejos):
	dist_s2=dist_espejos/(2*math.sin(angulo/2)) 								##dist espejo 2 y sensor
	dist_se=dist_s2*math.cos(angulo/2) 											##dist sensor y punto medio de la recta entre los espejos
	dist_2d=dist_espejos/(2*math.cos(angulo/2)) 								##dist espejo 2 y extremo opuesto al sensor en la circunferencia
	dist_de=((dist_2d)**2-(dist_espejos/2)**2)**0.5 							##dist punto medio de la recta entre los espejos y el extremo de la circunferencia opuesto al sensor
	r=(dist_se+dist_de)/2 														##valor del radio de la circunferencia
	return r


r1=RadioCircunferencia(angulo,dist_ab)
r2=RadioCircunferencia(angulo,dist_bc)
print("El radio de la primera circunferencia es:", r1)
print("El radio de la segunda circunferencia es:", r2)

## def CentroCircunferencia(r,espejo_1,espejo_2):
##         ##resolviendo la ecuacion de la circunferencia obtendríamos las coordenadas x(h) e y(k)
##         return h,k


def CentroCircunferencia(a,b,c,d,e,f,espejo_b):
	J=((d-b)**2)+((c-a)**2)
	G=-(((c**2)+(d**2)-(a**2)-(b**2))*(d-b))+(2*a*(c-a)*(d-b))-(2*b*((c-a)**2))
	H=((r**2)*((c-a)**2))-(((((c**2)+(d**2)-(a**2)-(b**2))/2)-a*(c-a))**2)-((b**2)*((c-a)**2))
	y1=(-G+(((G**2)-(4*J*H))**0.5))/(2*J)
	y2=(-G-(((G**2)-(4*J*H))**0.5))/(2*J)
	N=((c**2)+(d**2)-(a**2)-(b**2))/2
	x1=(N-y1*(d-b))/(c-a)
	x2=(N-y2*(d-b))/(c-a)
	return y1,y2,x1,x2


def IntersecciónCircunferencias(a,b,c,d,e,f,espejo_b):
	N=(c**2)-(f**2)-(a**2)+(d**2)-(b**2)+(e**2)
	O=(4*((e-b)**2))-(4*((d-a)**2))
	P=-(4*N*(e-b))+(8*a*(d-a)*(e-b))-(8*b*((d-a)**2))
	Q=-(4*((d-a)**2)*((c**2)-(a**2)-(b**2))-(N**2)+4*(d-a)*N*a)
	y=(-P+(((P**2)-(4*O*Q))**0.5))/(2*O)
	if y==espejo_b[1]:
		y=(-P-(((P**2)-(4*O*Q))**0.5))/(2*O)
	x=((c**2)-(f**2)-(a**2)+(d**2)-(2*y*(e-b))-(b**2)+(e**2))/(2*(d-a))
	return x,y

pos_sensor_x,pos_sensor_y=IntersecciónCircunferencias(h1,k1,r1,h2,k2,r2,espejo_b)
print("La posición del sensor en x e y es:",pos_sensor_x,pos_sensor_y)
