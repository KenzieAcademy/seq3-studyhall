import turtle
import time
from car import Car

done = False
# main window setup
width = 1000
height = 600
screen = turtle.Screen()
screen.setup(width, height)
screen.setworldcoordinates(0, 600, 1000, 0)
# car setup
distance = 40
car_length = 100
car_width = 100
car_icon_east = "img/car-east.gif"
car_icon_north = "img/car-north.gif"
car_icon_west = "img/car-west.gif"
car_icon_south = "img/car-south.gif"
car_icon_smashed = "img/car-smashed.gif"
screen.register_shape(car_icon_east)
screen.register_shape(car_icon_north)
screen.register_shape(car_icon_west)
screen.register_shape(car_icon_south)
screen.register_shape(car_icon_smashed)
t_car = turtle.Turtle()
t_car.shape(car_icon_east)

car = Car('2020', 'Chevrolet', 'Camaro', 'red')


def car_init():
    t_car.hideturtle()
    t_car.shape(car_icon_east)
    t_car.setheading(0)
    t_car.penup()
    t_car.goto(width // 2, height // 2)
    t_car.showturtle()


def game_over():
    t_car.shape(car_icon_smashed)
    time.sleep(2)
    car_init()


def detect_collision(direction):
    pos = t_car.pos()
    current_heading = t_car.heading()
    correction_amt = 8

    # detect top collision, front or rear
    if (direction == 'forward' and current_heading == 90) \
       or (direction == 'backward' and current_heading == 270):
        collision_diff = pos[1] - distance
        collision_diff -= car_length // 2 - correction_amt
        if collision_diff <= 0:
            print('TOP COLLISION!')
            game_over()
            return True
    # detect bottom collision, front or rear
    if (direction == 'forward' and current_heading == 270) \
       or (direction == 'backward' and current_heading == 90):
        collision_diff = pos[1] + distance
        collision_diff += car_length // 2
        if collision_diff >= height - 1:
            print('BOTTOM COLLISION!')
            game_over()
            return True
    # detect left collision, front or rear
    if (direction == 'forward' and current_heading == 180) \
       or (direction == 'backward' and current_heading == 0):
        collision_diff = pos[0] - distance
        collision_diff -= car_length // 2 - correction_amt
        if collision_diff <= 0:
            print('LEFT COLLISION!')
            game_over()
            return True
    # detect right collision, front or rear
    if (direction == 'forward' and current_heading == 0) \
       or (direction == 'backward' and current_heading == 180):
        collision_diff = pos[0] + distance
        collision_diff += car_length // 2
        if collision_diff >= width:
            print('RIGHT COLLISION!')
            game_over()
            return True
    return False


def accelerate():
    t_car.speed(1)
    if detect_collision(direction="forward"):
        return
    current_heading = t_car.heading()
    if current_heading == 90:
        t_car.forward(-distance)
    elif current_heading == 270:
        t_car.backward(distance)
    else:
        t_car.forward(distance)


def reverse():
    t_car.speed(1)
    if detect_collision(direction="backward"):
        return
    current_heading = t_car.heading()
    if current_heading == 90:
        t_car.forward(distance)
    elif current_heading == 270:
        t_car.backward(-distance)
    else:
        t_car.forward(-distance)


def brake():
    pass


def turn_left():
    current_heading = t_car.heading()
    if current_heading == 0:
        t_car.setheading(90)
        t_car.tiltangle(90)
        t_car.shape(car_icon_north)
    elif current_heading == 90:
        t_car.setheading(180)
        t_car.tiltangle(180)
        t_car.shape(car_icon_west)
    elif current_heading == 180:
        t_car.setheading(270)
        t_car.tiltangle(270)
        t_car.shape(car_icon_south)
    elif current_heading == 270:
        t_car.setheading(0)
        t_car.tiltangle(0)
        t_car.shape(car_icon_east)


def turn_right():
    current_heading = t_car.heading()
    if current_heading == 0:
        t_car.setheading(270)
        t_car.tiltangle(270)
        t_car.shape(car_icon_south)
    elif current_heading == 90:
        t_car.setheading(0)
        t_car.tiltangle(0)
        t_car.shape(car_icon_east)
    elif current_heading == 180:
        t_car.setheading(90)
        t_car.tiltangle(90)
        t_car.shape(car_icon_north)
    elif current_heading == 270:
        t_car.setheading(180)
        t_car.tiltangle(180)
        t_car.shape(car_icon_west)


def end_program():
    global done
    done = True


def main():
    # define key handlers
    screen.onkey(accelerate, "Up")
    screen.onkey(reverse, "Down")
    screen.onkey(turn_left, "Left")
    screen.onkey(turn_right, "Right")
    screen.onkey(end_program, "q")
    screen.listen()

    car_init()
    # while not done:
    #     print('Driving...')
    #     time.sleep(0.5)

    # screen.bye()
    turtle.done()


if __name__ == '__main__':
    main()
