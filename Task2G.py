from floodsystem.analysis import poly_deriv
from floodsystem.station import MonitoringStation
from floodsystem.flood import Towns_risk_level

def run():
    """Requirements for Task2G"""
    Towns_risk_level(MonitoringStation)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()