from task6 import battle_funcs, battle_classes


player1 = battle_classes.Player("John")
player2 = battle_classes.Player("Oleg")

players = [player1, player2]
players_reverse = [player2, player1]

field1 = battle_classes.Field()
field2 = battle_classes.Field()

field1_lst = field1.field
field2_lst = field2.field

fields = [field2, field1]
fields_blank = [field1, field2]
fields_sec = [field1_lst, field2_lst]
fields_check = [field2_lst, field1_lst]

def check_winner(lst):
    for cord in lst:
        tup = cord[0]
        if battle_funcs.has_ship(lst, tup) and len(cord) != 4:
            return False
    return True

print("Game Battleship")

print("Field of {}:".format(player2.name))
print(battle_funcs.field_to_str(field2.field_without_ships()))
print("SECRET FIELD:")
print(field2_lst)
print(battle_funcs.field_to_str(field2_lst))

def player_move(player, player_reverse, def_field, blank_field, sec_field, check_field):
    result = [None, None]

    print(player.name)

    move = player.read_position()

    print("Field of {}".format(player.name))
    print(battle_funcs.field_to_str(blank_field.field_without_ships()))
    # print("SECRET FIELD:")
    # print(sec_field)
    # print(battle_funcs.field_to_str(sec_field))
    # print("\n")

    def_field.shoot_at(move)

    if battle_funcs.has_ship(check_field, move):
        print("YOU HIT THE SHIP")
        def_field.ship_hit(move)
        result[1] = player
        print("ENEMY FIELD:")
        print(battle_funcs.field_to_str(def_field.field_without_ships()))


    if check_winner(check_field):
        print("----------------------\nEND OF THE GAME")
        print("{} has won!".format(player.name))
        print("{}'s field:".format(player.name))
        print(battle_funcs.field_to_str(blank_field.final_field()))
        print("\n{}'s field:".format(player_reverse.name))
        print(battle_funcs.field_to_str(blank_field.final_field()))

        result[0] = True

    return result


winner = None
while not winner:
    for player, player_reverse, def_field, blank_field, sec_field, check_field in zip(players, players_reverse, fields, fields_blank, fields_sec, fields_check):
        winner_lst = player_move(player, player_reverse, def_field, blank_field, sec_field, check_field)
        if winner_lst[1] is not None:
            while winner_lst[1] is not None:
                winner_lst = player_move(player, player_reverse, def_field, blank_field, sec_field, check_field)
        winner = winner_lst[0]
