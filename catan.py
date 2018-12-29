import random

class Game():
    def __init__():
        self.game_board = initialize_game_board()

    def setup():
        setup_menu() #Chose the number of players
        intialize_board()

    def initialize_board():
        return something::GameBoard

    def check_road_valid():
        pass
    def check_settlement_valid():
        pass

class GameBoard():
    def __init__(self):
        self.tiles = self.create_tiles()
        self.players= []

    def create_tile(self,coords, N, ressource):
        """coord: cordinates of tile
        ressource: ressource type of tile"""
        return Tile(coords,N,ressource)

    def create_tiles(self):
        tiles = []
        ressources = ["wheat"]*4+["ore"]*3+["lumber"]*4+["wool"]*4+["brick"]*3+["desert"]
        Ns = list(range(1,20))
        random.shuffle(ressources)
        random.shuffle(Ns)
        for i in range(5):
            tiles.append([])
            for j in range(5):
                if (i==0 and j==0) or (i==0 and j==1) or (i==1 and j==0) or (i==4 and j==3) or (i==3 and j==4) or (i==4 and j==4):
                    tile = self.create_tile(coords=[i,j],N=0,ressource="ocean")
                    tiles[-1].append(tile)
                else:
                    N_val = Ns.pop(0)
                    ressource_val = ressources.pop(0) 
                    tile = self.create_tile(coords=[i,j],N=N_val,ressource=ressource_val)
                    tiles[-1].append(tile)
        return tiles




class Tile():
    def __init__(self,coords,N,ressource):
        self.coords = coords
        self.N=N
        self.ressource=ressource

class Settlement():
    def __init__():
        pass
    def 

class Road():
    def __init__():
        self.coords=

    def nearest

class Robber():
    def __init__():
        pass

class DevelopmentCard():
    def __init__(self):
        pass


class Player():
    def __init__():
        self.settlements = [] 
        self.roads = []
        self.development_cards = []
        self.brick = 0
        self.lumber = 0
        self.wool = 0
        self.ore = 0
        self.wheat = 0
        self.is_turn= False
    def create_road(coords):
        if is_turn and self.lumber>=1 and self.wood>=1:
            self.lumber -=1
            self.wood = -=1
            self.roads.append = Road(coords)
    def get_development_card():
        if is_turn and self.wool>=1 and self.wheat>=1 and self.ore>=1:
            self.wool -=1
            self.wheat -=1
            self.ore -= 1
            development_cards.append(DevelopmentCard())
    def create_settlement(coords):
        if is_turn and self.wool>=1 and self.wheat>=1 and self.lumber>=1 and self.brick>=1:
            self.wool -=1
            self.wheat -=1
            self.ore -= 1
            self.brick -= 1 
            settlements.append(Settlement(coords))


