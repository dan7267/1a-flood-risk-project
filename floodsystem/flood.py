from .stationdata import build_station_list
from .stationdata import update_water_levels
from .analysis import poly_deriv
from .analysis import polyfit
import datetime
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
import matplotlib
from .station import MonitoringStation



def stations_level_over_threshold(stations, tol):
    """A function which returns a list of tuples where each tuple holds a station at which the latest relative
    water level is over a given tol value and also the relative water level at that station"""
    floods =[]
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        if station.typical_range_consistent() == True and station.relative_water_level() > tol:
            floods.append((station.name,station.relative_water_level()))
    floods = sorted(floods, key=lambda tup: tup[1], reverse = True)
    return floods

def stations_highest_rel_level(stations, N):
    """A function which returns a list of the N stations at which the water level relative to the typical range
    is highest"""
    Stations_at_risk = []
    Most_at_risk = []
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        if station.typical_range_consistent() == True:
            Stations_at_risk.append((station.name,station.relative_water_level()))
    Stations_at_risk = sorted(Stations_at_risk, key=lambda tup: tup[1], reverse = True)
    Most_at_risk = Stations_at_risk[0:N]
    return Most_at_risk


def Towns_risk_level(station):
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        if station.typical_range_consistent() == True:
            dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days=2))
            hi = polyfit(dates, levels, 4)
            print(hi)
            deriv = poly_deriv(hi[0])
            x = np.array(matplotlib.dates.date2num(dates))
            current_der = np.polyval(deriv, x[-1]-x[0])
            if current_der > 0.5:
                print(current_der)


