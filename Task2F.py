from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit

from floodsystem.station import MonitoringStation
def run():
    """Requirements for Task2F"""
    Highest_risk_stations = stations_highest_rel_level(MonitoringStation, 5)
    stations = build_station_list()
    print(Highest_risk_stations)
    # Build list of stations
    for x in Highest_risk_stations:
        Station_names = [x[0] for x in Highest_risk_stations]
        #Station_names = Highest_risk_stations[x][0]
    for x in Station_names:
        station_name = x

    # Find station
        station_input = None
        for station in stations:
            if station.name == station_name:
                station_input = station
                break

        dates, levels = fetch_measure_levels(station_input.measure_id, datetime.timedelta(days=2))
        if len(levels) != 0:
            plot_water_level_with_fit(station_input, dates, levels, 4)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
