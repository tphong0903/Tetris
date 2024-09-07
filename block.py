from colors import Colors
import pygame
from positon import Position
class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cellSize = 30
        self.rowOffset = 0
        self.colOffset = 0
        self.rotationState = 0
        self.colors = Colors.getCellColors()

    def draw(self,screen, offsetX, offsetY):
        tiles = self.getCellPositions()
        for tile in tiles:
            tileRect = pygame.Rect(offsetX + tile.column*self.cellSize,  offsetY + tile.row*self.cellSize,self.cellSize-1,self.cellSize-1)
            pygame.draw.rect(screen,self.colors[self.id],tileRect)
    
    def move(self, rows, columns):
        self.rowOffset += rows
        self.colOffset += columns
    
    def getCellPositions(self):
        tiles = self.cells[self.rotationState]
        movedTile = []
        for position in tiles:
            position = Position(position.row + self.rowOffset, position.column + self.colOffset)
            movedTile.append(position)
        return movedTile

    def rotateBlock(self):
        self.rotationState +=1
        if(self.rotationState == len(self.cells)):
            self.rotationState = 0
    def undoRotate(self):
        self.rotationState -=1
        if(self.rotationState < 0):
            self.rotationState = len(self.cells)-1
    