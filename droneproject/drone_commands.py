from DJITelloPy.djitellopy import Tello

tello = Tello("127.0.0.1")


def launch():
    tello.connect()
    tello.takeoff()

    tello.move_left(50)
    tello.rotate_clockwise(90)
    tello.move_forward(50)

    tello.land()
