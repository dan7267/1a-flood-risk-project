from floodsystem.stationdata import build_station_list

def stations_by_distance(stations, p):
    stations_coordinates = []
    stations = build_station_list()
    for station in stations:
        stations_coordinates.append(station.coord)
        
    print(stations_coordinates)

stations_by_distance('Bourton Dickler', (0, 0))
