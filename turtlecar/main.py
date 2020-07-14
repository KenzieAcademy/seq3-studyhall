import turtle
import time
from car import Car

done = False
# main window setup
screen = turtle.Screen()
screen.setup(1000, 600)
# car setup
car_icon_east = "img/car-east.gif"
car_icon_north = "img/car-north.gif"
car_icon_west = "img/car-west.gif"
car_icon_south = "img/car-south.gif"
screen.register_shape(car_icon_east)
screen.register_shape(car_icon_north)
screen.register_shape(car_icon_west)
screen.register_shape(car_icon_south)
t_car = turtle.Turtle()
t_car.shape(car_icon_east)
t_car.penup()

car = Car('2020', 'Chevrolet', 'Camaro', 'red')


def accelerate():
    t_car.speed(1)
    t_car.forward(50)


def reverse():
    t_car.speed(1)
    t_car.backward(50)


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

    # while not done:
    #     print('Driving...')
    #     time.sleep(0.5)

    # screen.bye()
    turtle.done()


if __name__ == '__main__':
    main()
