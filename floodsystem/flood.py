from .stationdata import build_station_list
from .stationdata import update_water_levels
from .analysis import poly_deriv
from .analysis import polyfit
import datetime
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
import matplotlib

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
    '''Function which assesses the current risk level of each town using the rate of 
    change of nearby river levels and the current river level relative to the typical range'''
    stations = build_station_list()
    update_water_levels(stations)
    floods = []
    lowfloods = []
    midfloods = []
    severe = []
    high = []
    moderate = []
    low = []
    for station in stations:
        try:
            if station.typical_range_consistent() == True:
                if station.measure_id != None:
                    try:
                        dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days=2))
                    except KeyError:
                        continue
                    if len(levels) == 0 or len(dates) == 0:
                        continue
                    hi = polyfit(dates, levels, 4)
                    deriv = poly_deriv(hi[0])
                    x = np.array(matplotlib.dates.date2num(dates))
                    current_der = np.polyval(deriv, x[-1]-x[0])
                    if station.typical_range_consistent() == True and station.relative_water_level() > 1.15:
                        floods.append(station.name)
                    if station.typical_range_consistent() == True and station.relative_water_level() > 1.4:
                        midfloods.append(station.name)
                    if station.typical_range_consistent() == True and station.relative_water_level() > 1:
                        lowfloods.append(station.name)

                    if current_der > 0.6 and station.name in floods:
                        if station.town in severe:
                            pass
                        else:
                            severe.append(station.town) 
                    elif current_der > 0.6 or station.name in midfloods:
                        if station.town in high:
                            pass
                        else:
                            high.append(station.town) 
                    elif current_der > 0.4 or station.name in lowfloods:
                        if station.town in moderate:
                            pass
                        else:
                            moderate.append(station.town) 
                    else:
                        if station.town in low:
                            pass
                        else:   
                            low.append(station.town)
        except:
            continue
    '''print("Severe: ", severe)
    print("\n")
    print("High: ", high)
    print("\n")
    print("Moderate: ", moderate)
    print("\n")
    print("Low: ", low)'''
    return severe
                    


