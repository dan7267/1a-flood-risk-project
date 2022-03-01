from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels
import datetime
def run():
    """Requirements for Task2E"""
    plot_water_levels(MonitoringStation, 10, 5)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()