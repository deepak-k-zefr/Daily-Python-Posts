
import pandas as pd 
import googlemaps
 
class BubbleTea(object):
 
    # authentication initialized
    gmaps = googlemaps.Client(key='[your-own-key]')
 
    def __init__(self, filename):
        self.boba = pd.read_csv(filename)

