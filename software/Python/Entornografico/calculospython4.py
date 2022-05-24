##RESUMEN DE DONDE LO DEJE
##	No tengo clara la necesidad de hallar el centro de las circunferencias, ya que no se le da ningun uso
##	Si es de utilidad encontrar el centro de las circunferencias, entonces he hallado mal la posicion del sensor
##	Que puntos habria que introducir para hallar la posicion del sensor? A y C?
##	Ya esta listo para comprobar si funciona, pero para eso necesitaria que hiciesemos simulaciones (sino no se que angulos poner para comprobar)




## Calcular las distancias a partir de las coordenadas de los espejos y el ángulo
import math
## Valores de prueba:
x1=3
y1=0.5
x2=2.25
y2=2
x3=0
y3=1.5
alpha1=float(input("alpha 1: "))*math.pi/180#0.8148269164 		##radianes
alpha2=float(input("alpha 2: "))*math.pi/180#0.6689640743 		##radianes
print(alpha1)
print(alpha2)


## EL CODIGO EMPIEZA AQUI



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


##Esto es realmente necesario calcularlo? No se le da ningun uso!
def CentroCircunferencia(a,b,c,d,r):
	J=((d-b)**2)+((c-a)**2)
	G=-(((c**2)+(d**2)-(a**2)-(b**2))*(d-b))+(2*a*(c-a)*(d-b))-(2*b*((c-a)**2))
	H=((r**2)*((c-a)**2))-(((((c**2)+(d**2)-(a**2)-(b**2))/2)-a*(c-a))**2)-((b**2)*((c-a)**2))
	y1=(-G+(((G**2)-(4*J*H))**0.5))/(2*J)
##	if y<0:
	y2=(-G-(((G**2)-(4*J*H))**0.5))/(2*J)
	x1=((((c**2)+(d**2)-(a**2)-(b**2))/2)-y1*(d-b))/(c-a)
	x2=((((c**2)+(d**2)-(a**2)-(b**2))/2)-y2*(d-b))/(c-a)
	return x1,y1,x2,y2

xc11,yc11,xc12,yc12=CentroCircunferencia(x1,y1,x2,y2,r1)
xc21,yc21,xc22,yc22=CentroCircunferencia(x2,y2,x3,y3,r2)
print("\nLas posibles coordenadas del centro de la primera circunferencia son:")
print("\tPrimer par:",xc11,yc11)
print("\tSegundo par:",xc12,yc12)
print("Las posibles coordenadas del centro de la segunda circunferencia son:")
print("\tPrimer par:",xc21,yc21)
print("\tSegundo par:",xc22,yc22)



def IntersecciónCircunferencias(a,b,c,d,e,f,espejo_b,l1,l2):
	N=(c**2)-(f**2)-(a**2)+(d**2)-(b**2)+(e**2)
	O=(4*((e-b)**2))-(4*((d-a)**2))
	P=-(4*N*(e-b))+(8*a*(d-a)*(e-b))-(8*b*((d-a)**2))
	Q=-(4*((d-a)**2)*((c**2)-(a**2)-(b**2))-(N**2)+4*(d-a)*N*a)
	y=(-P+(((P**2)-(4*O*Q))**0.5))/(2*O)
	if y<0 or y==espejo_b[1] or y>l2:
		y=(-P-(((P**2)-(4*O*Q))**0.5))/(2*O)
	x=((c**2)-(f**2)-(a**2)+(d**2)-(2*y*(e-b))-(b**2)+(e**2))/(2*(d-a))
	if x<=0 or x>l1:
		print("\tAlgo va mal\t")
	return x,y

pos_sensor_x,pos_sensor_y=IntersecciónCircunferencias(espejo_a[0],espejo_a[1],r1,espejo_c[0],espejo_c[1],r2,espejo_b,l1,l2)
print("\nLa posición del sensor en x e y es:",pos_sensor_x,pos_sensor_y)
