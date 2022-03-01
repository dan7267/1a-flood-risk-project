from floodsystem.plot import plot_water_levels
import datetime
from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels

def test_plot_water_levels():
    plot_water_levels(MonitoringStation, 10, 5)