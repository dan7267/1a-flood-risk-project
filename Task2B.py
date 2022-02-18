from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


'''def run():
    Requirements for Task_2B
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        if station.typical_range_consistent() == True and station.relative_water_level() > 0.8:
            print(station.name, station.relative_water_level())'''


def run():
    print(stations_level_over_threshold(MonitoringStation, 0.8))


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()