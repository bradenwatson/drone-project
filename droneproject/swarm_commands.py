from DJITelloPy.djitellopy import TelloSwarm, TelloException


drone_ips = []
drone_heights = []
drone_battery_percentages = []
drone_time_of_flights = []


def add_drone(ip: str) -> None:
    drone_ips.append(ip)


def filter_drone_data(drone_data: dict) -> dict:
    print(drone_data)
    for key, value in drone_data.items():
        if key.strip() == 'h':
            drone_heights.append(int(value))
        elif key.strip() == 'bat':
            drone_battery_percentages.append(int(value))
        elif key.strip() == 'tof':
            drone_time_of_flights.append(int(value))

    average_height = sum(drone_heights) / len(drone_heights)
    average_battery_percentage = sum(drone_battery_percentages) / len(drone_battery_percentages)
    average_time_of_flight = sum(drone_time_of_flights) / len(drone_battery_percentages)

    drone_averages = {
        'height': average_height,
        'battery_percentage': average_battery_percentage,
        'time_of_flight': average_time_of_flight
    }

    return drone_averages


def launch() -> None:
    swarm = TelloSwarm.fromIps(drone_ips)
    drone_heights.clear()
    drone_battery_percentages.clear()
    drone_time_of_flights.clear()

    try:
        swarm.connect()
        swarm.takeoff()

        for index, tello in enumerate(swarm.tellos):
            try:
                drone_data = tello.get_current_state()
                drone_dict = filter_drone_data(drone_data)
            except TelloException:
                print(f"ERROR: {TelloException}")

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
