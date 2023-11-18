from DJITelloPy.djitellopy import TelloSwarm


drone_ips = []
drone_ports = []


def add_drone(ip: str, port: int) -> None:
    drone_ips.append(ip)
    drone_ports.append(port)


def launch() -> None:
    swarm = TelloSwarm.fromIps(drone_ips, drone_ports)

    swarm.connect()
    swarm.takeoff()

    # run in parallel on all tellos
    swarm.move_up(50)

    # run by one tello after the other
    swarm.sequential(lambda i, tello: tello.move_forward(i * 20 + 20))

    # making each tello do something unique in parallel
    swarm.parallel(lambda i, tello: tello.move_left(i * 20 + 20))

    swarm.land()
    swarm.end()
