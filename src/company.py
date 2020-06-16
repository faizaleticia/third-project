from scipy.spatial import distance


class Company:
    current_company = []

    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        message = ''

        for company in self.current_company:
            message += company['company'].name + ' - Distância: ' + str(company['euclidean_distance']) + ' | '

        return self.name + " - Latitude: " + self.latitude + " Longitude: " + self.longitude + '\n [' + message + ']\n'

    def euclidean_distance(self, client_point):
        company_point = (float(self.latitude), float(self.longitude))
        total_euclidean_distance = distance.euclidean(client_point, company_point)
        return total_euclidean_distance

    def set_current_company(self, company):
        self.current_company = company
