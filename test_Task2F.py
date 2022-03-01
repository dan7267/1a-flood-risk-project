from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.station import MonitoringStation
import numpy as np

def test_polyfit():
    assert type(polyfit(10, 5, 4)) == np.poly1d


def test_plot_water_level_with_fit():
    plot_water_level_with_fit(MonitoringStation, 10, 5, 4)