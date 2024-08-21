class Ball:
    def __init__(self,canvas,x,y,diameter,xV,yV,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xV = xV
        self.yV = yV

    def move(self):
        coordinates = self.canvas.coords(self.image)
        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.xV = -self.xV
        if (coordinates[3] >= (self.canvas.winfo_height()) or coordinates[1] < 0):
            self.yV = -self.yV

        self.canvas.move(self.image,self.xV,self.yV)