import numpy as np

class Game():
    def __init__():
        self.game_board = initialize_game_board()

    def setup():
        setup_menu() #Chose the number of players
        intialize_board()

    def initialize_board():
        return something::GameBoard

    def is_road_legal(board,road.coords, player):
        for ddx in [(-1, -1), (0, 0),(1,-1)]:
            for ddy in [(-1, 0), (0, 0), (1, 0)]:
                if (i !=(0,0) or j!=(0,0)):
                   (dx,dy)=road.coords
                    if roads.(np.add(dx,ddx), np.add(dy,ddx))!=0:
                        return True
                    else:
                        print("This is not a legal move")
                        return False

    def add_road(board,road.coords, player):
        if is_road_legal(board,road.coords, player):
            road.coords.append(road.coords)

    def is_settlement_legal(settlement.coords):
        if settlement.coords!=0:
            return False
        if is_settlement_legal_in_direction(settlement.coords):
            return True
            
    def is_settlement_legal_in_direction(settlement.coords):


        #if vertice has at least two roads of player roads
            #return True
        #if vertice is populated as house, +input is upgrade to city
            #return True
    
    def add_settlement(settlement.coords):

        
        for dir in range(3):
            (drow,dcol) = dirs[dir]
            i = 1
            while True: #while it is not on the edge
                row = startRow + i*drow
                col = startCol + i*dcol
    def longest_road(board):


class GameBoard():
    def __init__():
        self.tiles = []
        self.players= []
    def create_tile(coords, N, ressource):
        """coord: cordinates of tile
        ressource: ressource type of tile"""
        return Tile(coords,N,ressource)

class Tile():
    def __init__(self):
        self.coords = coords
        self.N=N
        self.ressource=ressource

#    def get_neighboors(self):
#        self.N+1

class Settlement():
    def __init__():
        pass
    def 

class Road():
    def __init__():
        self.coords=

class Robber():
    def __init__():
        pass

class DevelopmentCards():
    def __init__():
        pass


class Player():
    def __init__():
        self.settlements = [] 
        self.roads = [road1,road2]
        self.brick
        self.lumber
        self.wool
        self.ore
        self.wheat
        self.development_cards
        self.is_turn= False
    def create_road(coords):
        self.lumber -=1
        self.wood = -=1
        roads.append = Road(coords)
        pass
    def get_development_card():
        development_cards.append(DevelopmentCards())

    
    def create_settlement(coords):
        pass

