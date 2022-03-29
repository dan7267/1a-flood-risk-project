from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.station import MonitoringStation
import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
import datetime

from floodsystem.stationdata import build_station_list, update_water_levels

def test_polyfit():
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        if station.name == "Cambridge Jesus Lock":
            dt = 10
            dates, levels = fetch_measure_levels(
                station.measure_id, dt = datetime.timedelta(days=dt))
            a = polyfit(dates, levels, 4)
    assert type(a[0]) == np.poly1d
