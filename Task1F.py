from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Task_1F"""
    print(sorted(inconsistent_typical_range_stations(MonitoringStation)))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()

