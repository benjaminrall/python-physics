import pygame

class Camera:

    def __init__(self, win, x, y, zoom):
        self.zoom = zoom
        self.win = win
        self.win_width = win.get_width()
        self.win_height =  win.get_height()
        self.width = self.win_width / zoom
        self.height = self.win_height / zoom
        self.x = x
        self.y = y

    def DrawRect(self, rect, colour):
        pygame.draw.rect(self.win, colour, self.GetScreenRect(rect))

    def GetScreenRect(self, rect):
        w = rect[2] * self.zoom
        h = rect[3] * self.zoom
        x = (-self.x * self.zoom) + ((rect[0] + (self.width / 2)) * self.zoom)
        y = (-self.y * self.zoom) + ((rect[1] + (self.height / 2)) * self.zoom)
        return (x, y, w, h)

    def ZoomOut(self):
        self.zoom = max(self.zoom / 2, 1)
        self.width = self.win_width / self.zoom
        self.height = self.win_height / self.zoom
    
    def ZoomIn(self):
        self.zoom = min(self.zoom * 2, 1024)
        self.width = self.win_width / self.zoom
        self.height = self.win_height / self.zoom
    
    def Pan(self, pos):
        self.x -= pos[0] / self.zoom
        self.y -= pos[1] / self.zoom