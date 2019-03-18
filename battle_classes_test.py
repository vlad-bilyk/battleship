import battle_classes
import battle_funcs

ship = battle_classes.Ship(("A", 1), True, 3)
ship1 = battle_classes.Ship(("B", 3), False, 2)
# print(ship._ship)
tup = ("A", 1)
# print("mesht")

# tup = ("G", 1)
# print(ship.shoot_at(tup))
# print(ship._hit)

lst = [ship, ship1]

field = battle_classes.Field(lst)
field.shoot_at(tup)
field.shoot_at(("B", 1))
print(field.field)
print(battle_funcs.field_to_str(field.field))
print("\n")
print(battle_funcs.field_to_str(field.field_with_ships()))
# print(field.field_without_ships())
# print(battle_funcs.field_to_str(field.field_without_ships()))
# ship.shoot_at(tup)
# ship1.shoot_at(("B", 4))
# print(ship._hit)
# print(ship1._hit)