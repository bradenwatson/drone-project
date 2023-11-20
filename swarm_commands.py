from DJITelloPy.djitellopy import TelloSwarm, TelloException


drone_ips = []
connected_drone_ips = []
drone_battery_percentages = []


def add_drone(ip: str) -> None:
    drone_ips.append(ip)


def filter_drone_data() -> dict:
    average_battery_percentage = sum(drone_battery_percentages) / len(drone_battery_percentages)

    drone_averages = {
        'battery_percentage': average_battery_percentage,
    }

    return drone_averages


def connect_swarm() -> None:
    try:
        if connected_drone_ips == drone_ips:
            print("ERROR: Swarm is already connected.")
            return

        swarm = TelloSwarm.fromIps(drone_ips)
        swarm.connect()

        connected_drone_ips.clear()
        for ips in drone_ips:
            connected_drone_ips.append(ips)
    except Exception as exception:
        print(f"ERROR: {exception.args[0]}")


# Check if drone_ips is same as connect one
def launch() -> None:
    swarm = TelloSwarm.fromIps(drone_ips)
    drone_battery_percentages.clear()

    try:
        swarm.connect()
        swarm.takeoff()

        for index, tello in enumerate(swarm.tellos):
            try:
                drone_data = tello.get_current_state()

                print(drone_data)
                for key, value in drone_data.items():
                    if key.strip() == 'bat':
                        drone_battery_percentages.append(int(value))
            except TelloException:
                print(f"ERROR: {TelloException}")

        drone_dict = filter_drone_data()

        print(drone_battery_percentages)

        # run in parallel on all tellos
        swarm.move_up(50)

        # run by one tello after the other
        # swarm.sequential(lambda i, tello: tello.move_forward(i * 20 + 20))
        #
        # making each tello do something unique in parallel
        # swarm.parallel(lambda i, tello: tello.move_left(i * 20 + 20))
    finally:
        swarm.land()
        swarm.end()
