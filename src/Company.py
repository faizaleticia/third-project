class Company:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return self.name + " - Latitude: " + self.latitude + " Longitude: " + self.longitude