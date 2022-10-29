import chess
import pygame

dimensions=8
height=480
width=480
sqsize=(height//8,width//8)
print(sqsize)

maxfpx=30
images={}

def chess_pieces():
    global images
    pieces=['b','k','n','q','p','r','B','K','N','R','P','Q']
    for i in pieces:
        if i.islower()==True:
            images[i]=pygame.transform.scale(pygame.image.load("chess_pieces/"+i+".png"),sqsize)
        else:
            images[i]=pygame.transform.scale(pygame.image.load("chess_pieces/w"+i+".png"),sqsize)    


board=chess.Board()
print(board)

def main():
    pygame.init()
    screen=pygame.display.set_mode((width,height))
    screen.fill(pygame.color('white'))
    running=True
    chess_pieces()
    board=chess.Board()
    print(board)




