import matplotlib
import matplotlib.pyplot as plt
import datetime
from floodsystem.station import MonitoringStation
from .stationdata import build_station_list
import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import polyfit


def plot_water_levels(station, dates, levels):
    """A function which displays a plot of the water level data against time for a station,
    including the typical low and high values"""

    Highest_risk_stations = stations_highest_rel_level(MonitoringStation, levels)
    stations = build_station_list()

    for x in Highest_risk_stations:
        Station_names = [x[0] for x in Highest_risk_stations]
    for x in Station_names:
        station_name = x

        station_input = None
        for station in stations:
            if station.name == station_name:
                station_input = station
                break

        print(dates)
        dt = 10
        dates, levels = fetch_measure_levels(
            station_input.measure_id, dt = datetime.timedelta(days=dt))
        time =[]
        water_levels =[]
        for dates, levels in zip(dates, levels):
            time.append(dates)
            water_levels.append(levels)

        plt.plot(time, water_levels)
        plt.axhline(y=station_input.typical_range[0], color='b', linestyle='-')
        plt.axhline(y=station_input.typical_range[1], color='r', linestyle='-')
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45);
        plt.title(x)
        plt.tight_layout()
        plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the water level against time along with the polynomial which fits the data of order 4 and the #
typical high and low range"""

    print(station)
    x = np.array(matplotlib.dates.date2num(dates))
    plt.plot(x, levels)
    x1 = np.linspace(x[0], x[-1], len(levels))
    tup = polyfit(dates, levels, p)[0]
    plt.plot(x1, tup(x1-x[0]))
    plt.axhline(y=station.typical_range[0], color='b', linestyle='-')
    plt.axhline(y=station.typical_range[1], color='r', linestyle='-')
    plt.title(station)
    plt.tight_layout()
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.show()