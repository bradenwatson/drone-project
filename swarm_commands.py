from DJITelloPy.djitellopy import TelloSwarm


drone_ips = []
connected_drone_ips = []


def clear_drones() -> None:
    """Clears the list of drone ips."""
    drone_ips.clear()


def add_drone(ip: str) -> None:
    """Appends a new drone ip to the list of drone ips.

    Args:
        ip: The ip of the drone to add.
    """
    drone_ips.append(ip)


def return_battery_percentages(drones: list) -> list:
    """Returns a list of battery percentages for all the drones in the list.

    Args:
        drones: The list of drones to check battery percentages.

    Returns:
        list: A list of battery percentages with the number of the drone.
    """
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
    """Connects the swarm of drones.

    Returns:
        list: A list of battery percentages with the number of the drone.
    """
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
    """Launches the swarm of drones and moves them up, forward, back, and then lands them."""
    if drone_ips == connected_drone_ips and connected_drone_ips:
        swarm = TelloSwarm.fromIps(drone_ips)

        try:
            swarm.takeoff()
            swarm.move_up(60)
            swarm.move_forward(30)
            swarm.move_back(30)
        except Exception as exception:
            print(f"ERROR: {exception.args[0]}")
        finally:
            swarm.land()
            swarm.end()
    else:
        print("ERROR: Swarm is not connected.")
