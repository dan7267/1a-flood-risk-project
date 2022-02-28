import matplotlib.pyplot as plt
import datetime
from floodsystem.station import MonitoringStation
from .stationdata import build_station_list

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level


def plot_water_levels(station, dates, levels):

    Highest_risk_stations = stations_highest_rel_level(MonitoringStation, levels)
    stations = build_station_list()
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


    # Alternative find station 'Cam' using the Python 'next' function
    # (https://docs.python.org/3/library/functions.html#next). Raises
    # an exception if station is not found.
    # try:
    #     station_cam = next(s for s in stations if s.name == station_name)
    # except StopIteration:
    #     print("Station {} could not be found".format(station_name))
    #     return
        print(dates)
    # Fetch data over past 2 days
        dt = 10
        dates, levels = fetch_measure_levels(
            station_input.measure_id, dt = datetime.timedelta(days=dt))
        time =[]
        water_levels =[]
    # Print level history
        for dates, levels in zip(dates, levels):
            time.append(dates)
            water_levels.append(levels)


# Plot
        plt.plot(time, water_levels)
        plt.axhline(y=station_input.typical_range[0], color='b', linestyle='-')
        plt.axhline(y=station_input.typical_range[1], color='r', linestyle='-')

# Add axis labels, rotate date labels and add plot title
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45);
        plt.title(x)

# Display plot
        plt.tight_layout()  # This makes sure plot does not cut off date labels

        plt.show()