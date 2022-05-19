import math

class Vector(object):

  def __init__(self,x,y):
    self.x = x
    self.y = y

  @classmethod
  def from_polar(self,m,t):
    x = math.cos(t)*m
    y = math.sin(t)*m
    return Vector(x,y)

  def __str__(self):
    return f"(x={self.x},y={self.y})"

  __repr__ = __str__

  def __add__(self,pt):
    nx = self.x + pt.x
    ny = self.y + pt.y
    return Vector(nx,ny)

  def __sub__(self,pt):
    nx = self.x - pt.x
    ny = self.y - pt.y
    return Vector(nx,ny)

  # Scalar multiplication
  def __mul__(self,a):
    nx = self.x * a
    ny = self.y * a
    return Vector(nx,ny)

  def __rmul__(self,a):
    return self.__mul__(a)

  # Scalar division
  def __div__(self,a):
    nx = self.x / a
    ny = self.y / a
    return Vector(nx,ny)

  # rotate 90º
  def rotate(self):
    nx = -self.y
    ny = self.x
    return Vector(nx,ny)

  @property
  def unit(self):
    m = self.module
    nx = self.x/m
    ny = self.y/m
    return Vector(nx,ny)

    

  @property
  def module(self):
    return math.sqrt(self.x*self.x + self.y*self.y)

  @property
  def theta(self):
    return math.atan2(self.y,self.x)






def find_circle(A,B,th):
  E = (A+B)*0.5
  BE = B-E
  mBE = BE.module
  mBS = mBE/math.sin(th/2)
  mSE = mBS*math.cos(th/2)
  mDE = math.tan(th/2)*mBE
  mDS = mDE+mSE
  

  r = mDS/2
  mEC = r - mDE

  C = BE.unit.rotate()*mEC + E
  return C,r
  

def circle_intersection(C1,r1,C2,r2):
  d = (C2-C1).module

  x = (d*d - r2*r2 + r1*r1)/(2*d)
  a = 1/d*math.sqrt(4*d*d*r1*r1 - (d*d-r2*r2+r1*r1)**2)

  u = (C2-C1).unit
  u2 = u.rotate()
  u1 = u2*(-1)

  i1 = C1 + u*x + a/2*u1
  i2 = C1 + u*x + a/2*u2

  return i1,i2

  



if __name__=='__main__':


  
  pi = 3.141592653589
  
  A = Vector(3,0.5)
  B = Vector(2.25,2)
  C = Vector(0,1.5)

  C1,r1 = find_circle(A,B,26.57*pi/180)
  C2,r2 = find_circle(B,C,270*pi/180)

  i1,i2 = circle_intersection(C1,r1,C2,r2)

  #print(i1)
  print(i2)
  
  
  
