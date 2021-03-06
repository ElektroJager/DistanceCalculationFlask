## Yandex Geocoder_API
import yandex_geocoder
from yandex_geocoder import Client

## Library To Calculate Distance
from haversine import haversine

## Library To Check If Adress Is In MKAD_ZONE
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

client = Client("bc77a24e-3a2a-4a05-83e9-abbe885323f3")

def input_data(input_data):
    try:
        coordinates = client.coordinates(input_data)
        return True

    except yandex_geocoder.YandexGeocoderException:
        return False

def distance(location):
    MOSCOW_RING_ROAD = (55.75249, 37.62320)

    coordinates = client.coordinates(location) 

    location_long= round(coordinates[0],5)
    location_lat = round(coordinates[1],5)
    location_coords = location_lat,location_long  

    return round(haversine(MOSCOW_RING_ROAD,location_coords), 2) 

def inside_mkad(location):
    ## Creating a Polygon With The Coordinates of MKAD
    mkad_zone = Polygon(MKAD_KM)

    coordinates = client.coordinates(location) 

    location_long= round(coordinates[0],5)
    location_lat = round(coordinates[1],5) 

    location_point = Point(location_lat,location_long)

    if(location_point.within(mkad_zone)):
        return True
    else:
        return False

def test_distance():
    # Lyon Distance 2528.26
    assert distance("Lyon") == 2528.26
    # İstanbul Distance 1755.9
    assert distance("İstanbul") == 1755.9 

def test_zone():
    # Inside
    assert inside_mkad("Lyon") == False
    # Outside
    assert inside_mkad("Russia, Moscow, Arbatsko-Pokrovskaya Line, metro Arbatskaya") == True

def test_input():
    # Valid Input
    assert input_data("İstanbul") == True
    # Invalid Inputs
    assert input_data("1423128745128491slşfqlşfk124o1ı249012wd12qw45fas56f4q5wfasjmfjkqf^%") == False
    assert input_data("123465892315675646789") == False
    assert input_data("='^+('+(='^+!='^)'^=%()'^+!'(+'^(+('^%('") == False


MKAD_KM =  [
[55.77455,37.84276],
[55.76522,37.84278],
[55.75572,37.84262],
[55.747399,37.841828],
[55.739103,37.841217],
[55.730482,37.840175],
[55.721939,37.83916],
[55.712203,37.837121],
[55.703048,37.83262],
[55.694287,37.829512],
[55.68529,37.831353],
[55.675945,37.834605],
[55.667752,37.837597],
[55.658667,37.839348],
[55.650053,37.833842],
[55.643713,37.824787],
[55.637347,37.814564],
[55.62913,37.802473],
[55.623758,37.794235],
[55.617713,37.781928],
[55.611755,37.771139],
[55.604956,37.758725],
[55.599677,37.747945],
[55.594143,37.734785],
[55.589234,37.723062],
[55.583983,37.709425],
[55.578834,37.696256],
[55.574019,37.683167],
[55.571999,37.668911],
[55.573093,37.647765],
[55.573928,37.633419],
[55.574732,37.616719],
[55.575816,37.60107],
[55.5778,37.586536],
[55.581271,37.571938],
[55.585143,37.555732],
[55.587509,37.545132],
[55.5922,37.526366],
[55.594728,37.516108],
[55.60249,37.502274],
[55.609685,37.49391],
[55.617424,37.484846],
[55.625801,37.474668],
[55.630207,37.469925],
[55.641041,37.456864],
[55.648794,37.448195],
[55.654675,37.441125],
[55.660424,37.434424],
[55.670701,37.42598],
[55.67994,37.418712],
[55.686873,37.414868],
[55.695697,37.407528],
[55.702805,37.397952],
[55.709657,37.388969],
[55.718273,37.383283],
[55.728581,37.378369],
[55.735201,37.374991],
[55.744789,37.370248],
[55.75435,37.369188],
[55.762936,37.369053],
[55.771444,37.369619],
[55.779722,37.369853],
[55.789542,37.372943],
[55.79723,37.379824],
[55.805796,37.386876],
[55.814629,37.390397],
[55.823606,37.393236],
[55.83251,37.395275],
[55.840376,37.394709],
[55.850141,37.393056],
[55.858801,37.397314],
[55.867051,37.405588],
[55.872703,37.416601],
[55.877041,37.429429],
[55.881091,37.443596],
[55.882828,37.459065],
[55.884625,37.473096],
[55.888897,37.48861],
[55.894232,37.5016],
[55.899578,37.513206],
[55.90526,37.527597],
[55.907687,37.543443],
[55.909388,37.559577],
[55.910907,37.575531],
[55.909257,37.590344],
[55.905472,37.604637],
[55.901637,37.619603],
[55.898533,37.635961],
[55.896973,37.647648],
[55.895449,37.667878],
[55.894868,37.681721],
[55.893884,37.698807],
[55.889094,37.712363],
[55.883555,37.723636],
[55.877501,37.735791],
[55.874698,37.741261],
[55.862464,37.764519],
[55.861979,37.765992],
[55.850257,37.788216],
[55.850383,37.788522],
[55.844167,37.800586],
[55.832707,37.822819],
[55.828789,37.829754],
[55.821072,37.837148],
[55.811599,37.838926],
[55.802781,37.840004],
[55.793991,37.840965],
[55.785017,37.841576],
]