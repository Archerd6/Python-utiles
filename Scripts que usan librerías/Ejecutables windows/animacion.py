import tkinter as tk

class AnimatedWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()
        
        self.ball = self.canvas.create_oval(50, 50, 100, 100, fill='red')
        self.dx = 1  # Cambio en la posición horizontal
        self.dy = 1  # Cambio en la posición vertical
        
        self.animate()
    
    def animate(self):
        self.canvas.move(self.ball, self.dx, self.dy)
        pos = self.canvas.coords(self.ball)
        
        if pos[0] <= 0 or pos[2] >= 400:
            self.dx *= -1
        if pos[1] <= 0 or pos[3] >= 400:
            self.dy *= -1
        
        self.after(10, self.animate)

if __name__ == "__main__":
    app = AnimatedWindow()
    app.mainloop()
