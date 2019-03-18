import battle_funcs

# DATA = battle_funcs.read_field('field.txt')
# DATA = battle.generate_field()
# letter A B C D E F G H I J
# num 1 - 10
# tup = ("J", 3)
# print(DATA)
# print(has_ship(DATA, ("A", 1)))
# print(battle.ship_size(DATA, tup))

# print(battle.field_to_str(DATA))
field = battle_funcs.generate_field()

print(battle_funcs.field_to_str(field))

print(field)
# print(battle_main.field_to_str(DATA))

print(battle_funcs.is_valid(field))