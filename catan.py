import random
import numpy as np

class Game():
    def __init__():
        self.game_board = initialize_game_board()

    def setup():
        setup_menu() #Chose the number of players
        intialize_board()

    def initialize_board():
        return something::GameBoard

    def Trade_cards(player,board):


    def is_road_nearby (player, road.coords):
        #DOES NOT WORK FOR BOARD EDGES YET
        (dx,dy)=road.coords
        direc=[(-1, +1),(1, 0),(-1, 0), (1, -1)]
        while road.coords(newx,newy)==0:
            if road.coords < board_edge(road.coords):
                print('Outside board framework')
                return False
            for ddx in direc:
                if direc.index(ddx)>1:
                    (newx,newy)=(dx, tuple(np.add(dy,ddx)))
                else: 
                    (newx,newy)=(tuple(np.add(dx,ddx)), dy)
        return True

    def is_road_legal(board, road.coords, settlement.coords, player):
        
        #If Trade_cards(player, wood)==True:
        #   pass

        def is_settlement_nearby (player, settlement.coords):
            #DOES NOT WORK FOR BOARD EDGES YET
            (dx,dy)=road.coords
            if dx and dy in settlement.coords:
                return True
            return False

        if is_road_nearby(road.coords)==True or is_settlement_nearby (settlement.coords):
            return True 

    def add_road(board,road.coords, player):
        if is_road_legal(board,road.coords, player):
            #For the players road.coords add the new road.coords
            #CHECK SYNTAX
            player.road.coords.append(road.coords)

    def is_settlement_legal(settlement.coords):
        if settlement.coords!=0:
            print('this location is unavailable')
            return False
        else if settlement.coords<board_edge(settlement.coords):
            print('Outside board framework')
            return False
        else if is_settlement_legal_in_direction(settlement.coords):
            return True
            
    def is_settlement_legal_in_direction(settlement.coords):
        
        def is_settlement_nearby(player, settlement.coords):            
            for i in player.settlement.coords:
                i=set(i)
                j=set(settlement.coords)
                if len(i.difference(j))<2:
                    return True
            return False

        def surrounding_road_length(player, settlement.coords):
            if 

        if is_settlement_nearby==False and surrounding_road_length>1:
            return True
    
    def add_settlement(board):
        #adding settlement to the board

    def settlement_resources(player,board):
        
    def add_settlement(settlement.coords):

        
    def longest_road(board):


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


