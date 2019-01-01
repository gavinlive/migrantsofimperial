def load_game():
    return None


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
    def get_game_state():
        game_token: varchar(255)
        tiles: []
        for tile in tiles:
            # Tiles have column table values:
            [game_token] game_token id
            [scalar] tile number
            [list] neighbouring tiles
            [list] neighbouring roads # -1 or else player ID
            [list] neighbouring cities # -1 or else player ID
            [list] neighbouring settlements # -1 or else player ID
            [scalar] has_robber
            [scalar] get_resource_id(resource_type) # desert is -1, ocean
            [scalar] position_x
            [scalar] position_y
            db.add_row('tiles', [game_token_id, scalar, neighbouring_tiles, neighbouring_roads, resource_type, position_x, position_y])
        cards: []
        cards = [get_card_id(x) for x in cards]
        db.add_row('cards', [game_token_id, cards])
        players: []
        for player in players:
            [scalar] points
            [boolean] longest_road
            [boolean] largest_army
            [list] dev_cards
            db.add_row('players', [game_token_id, points, longest_road, largest_army, dev_cards])

    def restore_game_state():
        pass
        game_token: varchar(255)
        tile_ids = get_tiles_list()
        tiles = []
        for tile_id in tile_ids:
            tiles.append(NewTile(tile_id,))


NOTE

db.add_row=>(table, values):
    get_table_columns
    map_reduce
    have a unique id


db.get_row(table, game_token_id):
    get row with the highest ID and the game_token_id
