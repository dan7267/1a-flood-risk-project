from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Tasl_1F"""
    print(sorted(inconsistent_typical_range_stations(MonitoringStation)))
    
if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()

