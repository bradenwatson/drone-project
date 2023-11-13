from DJITelloPy.djitellopy import TelloSwarm


def launch():
    swarm = TelloSwarm.fromIps([
        "127.0.0.1"
    ])

    swarm.connect()
    swarm.takeoff()

    swarm.move_up(50)

    # run by one tello after the other
    swarm.sequential(lambda i, tello: tello.move_forward(i * 20 + 20))

    # making each tello do something unique in parallel
    swarm.parallel(lambda i, tello: tello.move_left(i * 20 + 20))

    swarm.land()
    swarm.end()
