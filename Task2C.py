from floodsystem.station import MonitoringStation

from floodsystem.flood import stations_highest_rel_level


def run():
    print(stations_highest_rel_level(MonitoringStation, 10))

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()