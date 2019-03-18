import random


def read_field(filename):
    result = []
    # reading from file
    with open(filename, 'r') as file:
        file = file.readlines()

    # counter for rows
    num = 1
    # loop for creating a list with coordinates
    for lst in file:
        # counter for columns (A, B, C, ....., J)
        letter = 0
        # 65 to 74 ascii
        for i in lst:
            # special check so 11th column won't exist
            if i != "\n":
                newlst = [(chr(letter + 65), num), i]
                result.append(newlst)
                letter += 1
        num += 1

    return result

# function for checking if ship exists at current coordinate
def has_ship(data, tup):
    for lst in data:
        if tup in lst:
            return lst[1] == u"\u25A1"


# creating functions for each direction
def check_left(data, tup):
    letter = tup[0]
    num = tup[1]
    try:
        newtupp = (chr(ord(letter) - 1), num)
        return (has_ship(data, newtupp), newtupp)

    # exception if the coordinate is out of borders
    # example: (A, 11). this point doesn't exist
    except:
        print("Out of board borders")
        return (None, newtupp)


def check_right(data, tup):
    letter = tup[0]
    num = tup[1]
    try:
        newtupp = (chr(ord(letter) + 1), num)
        return (has_ship(data, newtupp), newtupp)
    except:
        print("Out of board borders")
        return (None, newtupp)


def check_up(data, tup):
    letter = tup[0]
    num = tup[1]
    try:
        newtupp = (letter, num - 1)
        return (has_ship(data, newtupp), newtupp)
    except:
        print("Out of board borders")
        return (None, newtupp)


def check_down(data, tup):
    letter = tup[0]
    num = tup[1]
    try:
        newtupp = (letter, num + 1)
        return (has_ship(data, newtupp), newtupp)
    except:
        print("Out of board borders")
        return (None, newtupp)


# SHIP_SIZE FUNCTION
# WRITTEN IN 3 HOURS
# KILL ME
def ship_size(data, tup, direction=None):
    letter = tup[0]
    num = tup[1]

    # don't pay attention to these comments
    # letters A-J
    # nums 1-10
    size = 0

    # separating functions
    func_r_l = [check_right, check_left]
    func_u_d = [check_up, check_down]

    # checking if the ship can exist at current coordinate
    if has_ship(data, tup):
        size = 1

        # function for checking in RIGHT and LEFT directions
        def check_r_l():
            size = 1
            # static_counter is created so you can go right and then change to left
            # u will see how it works below
            static_counter = 1

            # check for right and left directions
            # this loop has 2 iterations
            # first: check_right
            # second: check_left
            for func in func_r_l:
                # counter with which we will change letters
                # example A -> B or B -> A
                counter = 0

                new_letter = letter

                # the loop for going through the field
                # first iteration in the for loop above: check_right
                # this while loop will check if there is a ship on the right side of our coordinate
                # the same when iteration in the for loop will be: check_left
                # it will check if there is a ship on the left side
                while True:

                    # print("---------")
                    # print(func.__name__)
                    tup1 = (new_letter, num)
                    check = func(data, tup1)[0]
                    if check:
                        # print("check worked")
                        size += 1
                        counter += 1 * static_counter
                    else:
                        # print("check didnt work")
                        # print("size: ", size)

                        # here i change the static_counter to -1 because previous if check didn't work
                        # and it means that there is no ship on the right side
                        # so by changing the static_counter to -1 we will start searching if there are ships on the left
                        static_counter = -1


                        # print("counter: ", counter)


                        # and after we changed the static_counter we want to break out of the while loop
                        # we do that because we want to change the checking direction
                        # so we need to go for the next iteration in the for loop
                        # that's why we use break here
                        break


                    # print("counter: ", counter)
                    # print("static_counter: ", static_counter)


                    # that's how we change the letter
                    new_letter = chr(ord(letter) + counter)


                    # print("new_letter changed: ", new_letter)
                    # print("size: ", size)
                    # print("---------")

            # this check is made because we want to know if we found anything on the right or left sides
            # if size still is 1, we go to the next loop where we search for ships that can be up or down
            return size

        # function for checking in UP and DOWN directions
        def check_u_d():
            size = 1
            # the same story with static_counter here
            # but here it's -1 and not 1 because we firstly check for UP and then for DOWN in our for loop
            # explanation:
            # our point: (C,3)
            # we search for UP, that will be (C,2)
            # see? we had 3 and we have 2, 3-1 = 2
            # that's why static_counter = -1
            static_counter = -1


            # start of our for loop
            for func in func_u_d:

                counter = 0
                new_num = num

                while True:
                    # print("---------")
                    # print(func.__name__)

                    tup1 = (letter, new_num)
                    check = func(data, tup1)[0]
                    if check:
                        # print("check worked")
                        size += 1
                        counter += 1 * static_counter
                    else:
                        # print("check didnt work")
                        # print("size: ", size)


                        # the previous check didn't work so
                        # now here we change static_counter to 1
                        # as i said above
                        # we didn't find anything UP
                        # so we start looking DOWN
                        # on the field (C,4) is under (C,3)
                        # static_counter is 1 and counter += 1 * static_counter
                        # so 3 + 1*1 = 4
                        static_counter = 1


                        # print("counter: ", counter)


                        # here we break like we did in previous loop with right and left
                        break


                    # print("counter: ", counter)
                    # print("static_counter: ", static_counter)


                    # that's how we change the num
                    # the same we did with letter
                    new_num = num + counter


                    # print("new_num changed: ", new_num)
                    # print("size: ", size)
                    # print("---------")

            return size

        # if function direction argument is "r_l" --> check if ship exists in RIGHT or LEFT direction
        if direction == "r_l":
            size = check_r_l()

        # if function direction argument is "u_d" --> check if ship exists in UP or DOWN direction
        elif direction == "u_d":
            size = check_u_d()

        # if function direction argument is None --> check in all directions
        else:
            size = check_r_l()

            # if check_r_l() didn't find anything
            if size == 1:
                size = check_u_d()

    return size


# function for checking if the field exists
def is_valid(data):
    check_right_left = "r_l"
    check_up_down = "u_d"
    exists = True
    sizes = []

    field = field_to_str(data)
    field = field.split("\n")
    # print(field)
    num_check = len(field) == 10
    letters_check = [len(i) for i in field] == [10 for i in range(10)]
    if not num_check or not letters_check:
        print("Field doesn't exist :(")
        exists = False
        return exists

    for lst in data:
        symbol = lst[1]
        tup = lst[0]
        letter = tup[0]
        num = tup[1]

        # adding all ship sizes to the list
        sizes.append(ship_size(data, tup))
        # check for the rule, when ship can't exist vertically and horizontally in the same coordinate
        if ship_size(data, tup, check_right_left) > 1 and ship_size(data, tup, check_up_down) > 1:
            exists = False
            print("ship_size fail")
            print("THIS COORDINATE FAILED:", tup)
            print("Field doesn't exist :(")
            return exists


    four_c = 1 * 4
    three_c = 2 * 3
    two_c = 3 * 2
    one_c = 4 * 1
    cells = [one_c, two_c, three_c, four_c]

    # check if the number of ships of given size is correct
    # 1 ship sized [4], 2 ships sized [3] and etc.
    for n, c in zip(range(1,5), cells):
        if sizes.count(n) != c:
            print("ship with size {} appears {} time(s), instead of {} time(s)".format(n, int(sizes.count(n) / n), int(c / n)))
            print("Field doesn't exist :(")
            exists = False
            return exists



    up_right = [check_up, check_right]
    up_left = [check_up, check_left]
    down_right = [check_down, check_right]
    down_left = [check_down, check_left]

    checks = []

    def check_diagonal(lst):
        exists = True
        for check in lst:
            newtup = tup
            for ch in check:
                checker = ch(data, newtup)
                newtup = checker[1]
            if checker[0]:
                print("check_diagonal fail")
                # print(ch.__name__)
                print("THIS COORDINATE FAILED: ", newtup)
                print("Field doesn't exist :(")
                exists = False
                return exists
        return exists


    for lst in data:
        symbol = lst[1]
        tup = lst[0]
        letter = tup[0]
        num = tup[1]

        if has_ship(data, tup):

            if num == 1:
                checks = [down_left, down_right]
            elif num == 10:
                checks = [up_left, up_right]
            if letter == "A":
                checks = [up_right, down_right]
            elif letter == "J":
                checks = [up_left, down_left]
            else:
                checks = [up_right, up_left, down_left, down_right]

            # print(checks)
            if not check_diagonal(checks):
                print(lst[0])
                exists = False
                return exists


    print("Field exists!")
    return exists


def field_to_str(data):
    field = ""
    for lst in data:
        symbol = lst[1]
        tup = lst[0]
        field += symbol
        if tup[0] == "J" and tup[1] != 10:
            field += "\n"

    return field


def generate_field():
    field = []
    for num in range(1, 11):
        for let in "ABCDEFGHIJ":
            symbol = '0'
            tup = (let, num)
            lst = [tup, symbol]
            field.append(lst)

    coordinates = [i[0] for i in field]
    ships = [(4, 1), (3, 2), (2, 3), (1, 4)]
    directions = ["V", "H"]
    # sizes = [4, 3, 2, 1]
    for ship in ships:
        size = ship[0]
        number = ship[1]
        for i in range(number):
            while True:
                rand_cord = random.choice(coordinates)
                rand_direct = random.choice(directions)
                letter = rand_cord[0]
                num = rand_cord[1]
                if rand_direct == "V":
                    check = size + num <= 11
                    if check:
                        myship = [(letter, num + i) for i in range(size)]
                        if set(myship) & set(coordinates) == set(myship):
                            break

                elif rand_direct == "H":
                    check = size + ord(letter) - 64 <= 11
                    if check:
                        myship = [(chr(ord(letter) + i), num) for i in range(size)]
                        if set(myship) & set(coordinates) == set(myship):
                            break

            if rand_direct == "V":
                for cord in myship:
                    coordinates.remove(cord)
                    for lst in field:
                        if cord in lst:
                            lst[1] = u"\u25A1"

                to_delete = []
                for i in range(size + 2):
                    to_delete.append((chr(ord(letter) + 1), num - 1 + i))
                    to_delete.append((chr(ord(letter) - 1), num - 1 + i))

                to_delete.append((letter, num - 1))
                to_delete.append((letter, num + size))

                for i in to_delete:
                    try:
                        coordinates.remove(i)
                    except:
                        pass


            elif rand_direct == "H":
                for cord in myship:
                    try:
                        coordinates.remove(cord)
                    except:
                        pass
                    for lst in field:
                        if cord in lst:
                            lst[1] = u"\u25A1"

                to_delete = []
                for i in range(size + 2):
                    to_delete.append((chr(ord(letter) - 1 + i), num + 1))
                    to_delete.append((chr(ord(letter) - 1 + i), num - 1))

                to_delete.append((chr(ord(letter) - 1), num))
                to_delete.append((chr(ord(letter) + size), num))

                for i in to_delete:
                    try:
                        coordinates.remove(i)
                    except:
                        pass

            # print("My ship: ", myship)
            # print("to delete: ", to_delete)
            # print("size: ", size)
            # print(rand_cord)
            # print(rand_direct)
            # print("coordinates: ", coordinates)

    # print(coordinates)
    # print(rand_cord)

    return field

#don't pay attention to these

# DATA = read_field('field.txt')
# # letter A B C D E F G H I J
# # num 1 - 10
# tup = ("A", 3)
# print(DATA)
# # print(has_ship(DATA, ("A", 1)))
# print(ship_size(DATA, tup))