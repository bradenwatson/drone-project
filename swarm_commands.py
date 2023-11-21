from DJITelloPy.djitellopy import TelloSwarm, TelloException


drone_ips = []
connected_drone_ips = []


def clear_drones() -> None:
    drone_ips.clear()


def add_drone(ip: str) -> None:
    drone_ips.append(ip)


def filter_drone_data() -> dict:
    average_battery_percentage = sum(drone_battery_percentages) / len(drone_battery_percentages)

    drone_averages = {
        'battery_percentage': average_battery_percentage,
    }

    return drone_averages


def return_battery_percentages(drones: list) -> list:
    drone_battery_percentages = []
    for i, tello in enumerate(drones):
        try:
            drone_data = tello.get_current_state()

            battery_percentage = None
            for key, value in drone_data.items():
                if key.strip() == 'bat':
                    battery_percentage = int(value)

            drone_info = {
                "drone_number": i + 1,
                "battery_percentage": battery_percentage
            }

            drone_battery_percentages.append(drone_info)
        except Exception as exception:
            print(f"ERROR: {exception}")

    return drone_battery_percentages


def connect_swarm() -> list:
    try:
        if connected_drone_ips == drone_ips:
            print("ERROR: Swarm is already connected.")
            return []

        swarm = TelloSwarm.fromIps(drone_ips)
        swarm.connect()

        battery_percentages = return_battery_percentages(swarm.tellos)

        connected_drone_ips.clear()
        for ips in drone_ips:
            connected_drone_ips.append(ips)

        return battery_percentages
    except Exception as exception:
        print(f"ERROR: {exception.args[0]}")
        return []


def launch() -> None:
    # Remove later
    connected_drone_ips.clear()
    for ips in drone_ips:
        connected_drone_ips.append(ips)
    # -

    if drone_ips == connected_drone_ips:
        swarm = TelloSwarm.fromIps(drone_ips)
        # drone_battery_percentages.clear()

        try:
            swarm.takeoff()

            # for index, tello in enumerate(swarm.tellos):
            #     try:
            #         drone_data = tello.get_current_state()
            #
            #         print(drone_data)
            #         for key, value in drone_data.items():
            #             if key.strip() == 'bat':
            #                 drone_battery_percentages.append(int(value))
            #     except TelloException:
            #         print(f"ERROR: {TelloException}")
            #
            # drone_dict = filter_drone_data()
            #
            # print(drone_battery_percentages)

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
    else:
        print("ERROR: Swarm is not connected.")
