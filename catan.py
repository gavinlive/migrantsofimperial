import random
import itertools

class Game():
    def __init__(self):
        self.gameboard = self.initialize_board()
        self.players = self.initialize_players(3)
        self.chose_starting_settlements()
        self.game_loop()

    def initialize_board(self):
        return Gameboard(self)

    def initialize_players(self,N):
        """generate Player objects"""
        players = []
        for i in range(N):
            players.append(Player(self.gameboard))
        return players
    
    def chose_starting_settlements(self):
        for player in self.players:
            player.make_settlement()
            player.make_road()

            #player chose settlement

        for player in list(reversed(self.players)):
            player.make_settlement()
            player.make_road()
            #player chose settlements
            #player gets ressource of settlement


    def game_loop(self):
        for player_playing in itertools.cycle(self.players):
            self.run_turn(player_playing)
            if player_playing.has_won()==True:
                print("Congratulations on winning")
                break



    def run_turn(self,player_playing):
        N = roll_dice()
        for player in self.players():
            player.collect_ressources(N)

        player_playing.get_actions()
        player_playing.check_victory()

    def roll_dice(self):
        N_1 = random.randint(1,6)
        N_2 = random.randint(1,6)
        N = N_1+N_2
        return N

    def check_road_valid(self):
        pass

    def check_settlement_valid(self):
        pass

class Gameboard():
    def __init__(self,game):
        self.game = game
        self.tiles = self.create_tiles()
        self.players= []

    def create_tile(self,coords, N, ressource):
        """coord: cordinates of tile
        ressource: ressource type of tile"""
        return Tile(coords,N,ressource)

    def create_tiles(self):
        tiles = []
        ressources = ["wheat"]*4+["ore"]*3+["lumber"]*4+["wool"]*4+["brick"]*3+["desert"]
        Ns = [12,2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
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
    
    def get_tile(self,i,j):
        print("i:{}".format(i))
        print("j:{}".format(j))
        return self.tiles[i][j]


class Tile():
    def __init__(self,coords,N,ressource):
        self.coords = coords
        self.N=N
        self.ressource=ressource

class Settlement():
    def __init__(self,gameboard,player):
        self.gameboard = gameboard
        self.player=player 
        self.tiles = self.set_location()
        self.victory_points = 1
        self.ressources = 1

    def set_location(self):
        """tile_1_i = int(input("First Neighbooring i:"))
        tile_1_j = int(input("First Neighbooring j:"))
        tile_2_i = int(input("Second Neighbooring i:"))
        tile_2_j = int(input("Second Neighbooring j:"))
        tile_3_i = int(input("Third Neighbooring i:"))
        tile_3_j = int(input("Third Neighbooring j:"))"""
        tile_1_i = 1
        tile_1_j = 2 
        tile_2_i = 1
        tile_2_j = 2
        tile_3_i = 1
        tile_3_j = 2
        tiles = [self.gameboard.get_tile(tile_1_i,tile_1_j),self.gameboard.get_tile(tile_2_i,tile_2_j),self.gameboard.get_tile(tile_3_i,tile_3_j)]
        return tiles


class Road():
    def __init__(self,gameboard,player):
        self.gameboard = gameboard
        self.player = player
        self.tiles = self.set_location()

    def set_location(self):
        """tile_1_i = int(input("First Neighbooring i:"))
        tile_1_j = int(input("First Neighbooring j:"))
        tile_2_i = int(input("Second Neighbooring i:"))
        tile_2_j = int(input("Second Neighbooring j:"))"""

        tile_1_i = 2
        tile_1_j = 2
        tile_2_i = 2
        tile_2_j = 2


        tiles = [self.gameboard.get_tile(tile_1_i,tile_1_j),self.gameboard.get_tile(tile_2_i,tile_2_j)]
        return tiles



class Robber():
    def __init__():
        pass

class DevelopmentCard():
    def __init__(self):
        pass


class Player():
    def __init__(self,gameboard):
        self.settlements = [] 
        self.roads = []
        self.development_cards = []
        self.gameboard = gameboard
        self.brick = 0
        self.lumber = 0
        self.wool = 0
        self.ore = 0
        self.wheat = 0
        self.longest_road =False
        self.largest_army=False
        self.is_turn =False
        self.victory_point_development_cards = 0

    def create_road(self,coords):
        if is_turn and self.lumber>=1 and self.wood>=1:
            self.lumber -=1
            self.wood  -=1
            self.roads.append(Road(self.gameboard,self)

    def get_development_card(self):
        if is_turn and self.wool>=1 and self.wheat>=1 and self.ore>=1:
            self.wool -=1
            self.wheat -=1
            self.ore -= 1
            development_cards.append(DevelopmentCard())

    def create_settlement(self,coords):
        if is_turn and self.wool>=1 and self.wheat>=1 and self.lumber>=1 and self.brick>=1:
            self.wool -=1
            self.wheat -=1
            self.ore -= 1
            self.brick -= 1 
            self.settlements.append(Settlement(self.gameboard,self))


    def make_settlement(self):
        """this is a function to make a settlement at the beginning of the game (is a bit redundant)"""
        self.settlements.append(Settlement(self.gameboard,self))


    def make_road(self):
        self.roads.append(Road(self.gameboard,self))
        

    def upgrade_settlement(self,coords):
        pass

    def collect_ressources(self,N):
        for settlement in self.settlements:
            for tile in settlement.tiles:
                if tile.N == N:
                    self.add_ressource(tile.ressource)

    def add_ressource(self,ressource,value=1):
        if "wool":
            self.wool+=value
        if "lumber":
            self.lumber+=value
        if "wheat":
            self.wheat+=value
        if "ore":
            self.ore+=value


    def get_actions(self):
        print("commands are")
        print("end")
        print("settlement")
        print("road")
        print("devcard")

        while commmand != "end":
            command = input("what do you want to do")
            if command =="settlement":
                Player.create_settlement()
            if command =="road":
                Player.create_road()
            if command =="devcard":
                print("Not yet developed")

    def has_won(self):
        victory_points = 0 
        for settlement in self.settlements:
            victory_points += settlement.victory_points
        if self.longest_road ==True:
            #not yet implemented
            victory_points +=2
        if self.largest_army==True:
            victory_points +=2
        victory_points+=victory_point_development_cards

        if victory_points>=10:
            return True
        else:
            return False
