class Control:
    def enlazar(self,tv):
        self.tv=tv
        tv.setControl(self)
    def getTv(self):
        return self.tv
    def setTv(self,tv):
        self.tv=tv
    def turnOn(self):
        self.tv.estado=True
    def turnOff(self):
        self.tv.estado=False
    def setCanal(self, can:int):
        if self.tv.estado==True and can<=120 and can>=1:
            self.tv.canal=can
    def canalUp(self):
        if self.tv.estado==True and self.tv.canal<120:
            self.tv.canal+=1
    def canalDown(self):
        if self.tv.estado==True and self.tv.canal>1:
            self.tv.canal-=1
    def setVolumen(self, vol:int):
        if self.tv.estado==True and vol<=7 and vol>=0:
            self.tv.volumen=vol
    def volumenUp(self):
        if self.tv.estado==True and self.tv.volumen<7:
            self.tv.volumen+=1
    def volumenDown(self):
        if self.tv.estado==True and self.tv.volumen>0:
            self.tv.volumen-=1