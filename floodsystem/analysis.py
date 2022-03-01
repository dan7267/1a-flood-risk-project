import matplotlib.pyplot as plt
import matplotlib
import datetime
from floodsystem.station import MonitoringStation
from .stationdata import build_station_list
import numpy as np
from .stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level

def polyfit(dates, levels, p):
    stations = build_station_list()
    """for station in stations:
        update_water_levels(stations)"""
    x = np.array(matplotlib.dates.date2num(dates))
    p_coeff = np.polyfit(x-x[0], levels, p)
    poly = np.poly1d(p_coeff)

    
    return (poly, x[0])