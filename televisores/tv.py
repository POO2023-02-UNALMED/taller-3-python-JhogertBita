class TV:
  numTV = 0

  def __init__(self, marca, estado):
    self.marca=marca
    self.estado=estado
    self.canal=1
    self.volumen=1
    self.precio=500
    TV.numTV+=1

  @classmethod
  def getNumTV(cls):
    return cls.numTV

  @classmethod
  def setNumTV(cls, numTV):
    cls.numTV=numTV

  def getPrecio(self):
    return self.precio

  def setPrecio(self, precio):
    self.precio=precio

  def getMarca(self):
    return self.marca

  def setMarca(self, marca):
    self.marca=marca

  def getCanal(self):
    return self.canal

  def setCanal(self, canal):
    if self.estado==True and canal>=1 and canal<=120:
      self.canal=canal

  def getVolumen(self):
    return self.volumen

  def setVolumen(self, volumen):
    if self.estado==True and volumen<=7 and volumen>=0:
      self.volumen=volumen

  def getControl(self):
    return self.control

  def setControl(self, control):
    self.control=control

  def turnOn(self):
    self.estado=True

  def turnOff(self):
    self.estado=False

  def getEstado(self):
    return self.estado

  def canalUp(self):
    if self.estado==True and self.canal<120:
      self.canal+=1

  def canalDown(self):
    if self.estado==True and self.canal>1:
      self.canal-=1

  def volumenUp(self):
    if self.estado==True and self.volumen<7:
      self.volumen+=1

  def volumenDown(self):
    if self.estado==True and self.volumen>0:
      self.volumen-=1
