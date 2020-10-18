from bangtal import *
import random
import time
import copy


setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

road = Scene("스테이지1", "Images/background.png")
up = Object("Images/up.png")
down = Object("Images/down.png")
car = Object("Images/car.png")
start = Object("images/start.png")
car_y = 270
start.locate(road, 550, 200)
start.setScale(0.4)
car.locate(road, 100, car_y)
car.moved = False
up.locate(road, 950, 40)
down.locate(road, 1050, 40)
rocks = []
rocks_locate = []
corns_locate = []
corns = []
hamburgers = []
hamburgers_locate = []
corn_timers = []
hamburger_timer = []
rock_timer = []

timer = Timer(3)
move_timer = Timer(1)
count = int(1e9)
corn_count = 0
hamburger_count = 0
rock_count = 0

move_count = int(1e9)

car.show()
up.show()
down.show()
start.show()
flag = True


def up_on_mouse_action(x, y, action):
    global car_y, car, road

    if action == MouseAction.CLICK:
        car_y += 50
        car.locate(road, 100, car_y)

def down_on_mouse_action(x, y, action):
    global car_y, car, road

    if action == MouseAction.CLICK:
        car_y -= 50
        car.locate(road, 100, car_y)

def start_on_mouse_action(x, y, action):
    global car, start
    # if action == MouseAction.CLICK:
    car.moved = True
    start.hide()
    timer.start()
    showMessage('화살표를 클릭해 장애물을 피해주세요!')
  

def end_game():
    pass


def make_object():
    random_list = ['corn', 'rock', 'hambuger']
    random_locate = [0, 100, 200, 300, 400, 500, 600]

    for _ in range(300):
        obj_str = random.choice(random_list)
        random_y = random.choice(random_locate)

        object = Object('Images/{}.png'.format(obj_str))
        object.locate(road, 800, random_y)
        if random_list[0] == obj_str:
            corns.append(onject)
            ocnrs_locate.append((800, random_y))
        elif random_list[1] == obj_str:
            rocks[object] = (800, random_y)
        else:
            hamburgers[object] = (800, random_y)

def obj_show():
    global rocks, corns, hamburgers, road, corn_count, rock_count, hamburger_count

    random_list = ['corn', 'rock', 'hambuger']
    obj_str = random.choice(random_list)
    if random_list[0] == obj_str:
        corns[corn_count].show()
    elif random_list[0] == obj_str:
        rocks[rock_count].show()
    elif random_list[0] == obj_str:
        hamburger_count[hamburger_count].show()
    

def random_generator():
    global rocks, corns, hamburgers, road

    random_list = ['corn', 'rock', 'hambuger']
    random_locate = [0, 100, 200, 300, 400, 500, 600]

    obj_str = random.choice(random_list)
    random_y = random.choice(random_locate)

    object = Object('Images/{}.png'.format(obj_str))
    object.locate(road, 800, random_y)
    object.show()
    if random_list[0] == obj_str:
        corns[object] = (800, random_y)
    elif random_list[1] == obj_str:
        rocks[object] = (800, random_y)
    else:
        hamburgers[object] = (800, random_y)


def move():
    global move_count, corns, hamburgers, rocks, temp_corns, temp_hamburgers, temp_rocks
    move_count -= 1

    for corn, locate in corns.items():
        corn.locate(road, locate[0]- 100, locate[1])
        temp_corns[corn] = (locate[0] - 100, locate[1])

    for rock, locate in rocks.items():
        rock.locate(road, locate[0]- 100, locate[1])
        temp_rocks[rock] = (locate[0] - 100, locate[1])

    for ham, locate in hamburgers.items():
        ham.locate(road, locate[0]- 100, locate[1])
        temp_hamburgers[ham] = (locate[0] - 100, locate[1])

    corns = copy.deepcopy(temp_corns)
    hamburgers = copy.deepcopy(hamburgers)
    rocks = copy.deepcopy(rocks)


def check_colision():
    pass

def mytime_on_timeout():
    global count
    count = count - 1
 
    if count > 0:
        random_generator()
        timer.set(5)
        timer.start()

timer.onTimeout= mytime_on_timeout

up.onMouseAction = up_on_mouse_action
down.onMouseAction = down_on_mouse_action
start.onMouseAction = start_on_mouse_action


startGame(road)
