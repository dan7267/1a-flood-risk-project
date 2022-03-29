from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold


def run():
    """Requirements for Task2B"""
    print(stations_level_over_threshold(MonitoringStation, 0.8))

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()