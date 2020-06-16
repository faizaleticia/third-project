import os.path
import matplotlib
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import numpy as np
from shapely.geometry import LineString, MultiPoint, Point, MultiPolygon
from shapely.ops import polygonize, unary_union
from src.company import Company
from src.pdf_generate import get_data_from_prettytable, export_to_pdf
from scipy.spatial import Voronoi

my_path = os.path.abspath(os.path.dirname(__file__))
clientPath = os.path.join(my_path, '../files/clients.txt')

clientsFile = open(clientPath, 'r')
clients = clientsFile.readlines()

clientsList = []
providersList = []

for client in clients:
    objectClient = client.split(' ')
    clientsList.append(Company(objectClient[0], objectClient[1], objectClient[2]))

providersPath = os.path.join(my_path, '../files/providers.txt')

providersFile = open(providersPath, 'r')
providers = providersFile.readlines()

for provider in providers:
    objectProvider = provider.split(' ')
    providersList.append(Company(objectProvider[0], objectProvider[1], objectProvider[2]))

newProvidersList = []

for client in clientsList:
    clientPoint = (float(client.latitude), float(client.longitude))

    provider = providersList[0]
    euclideanDistance = provider.euclidean_distance(clientPoint)

    smallerProvider = {
        "company": provider,
        "euclidean_distance": euclideanDistance,
    }

    equalsProvider = []

    for index, provider in enumerate(providersList, 1):
        euclideanDistance = provider.euclidean_distance(clientPoint)

        if smallerProvider['euclidean_distance'] > euclideanDistance:
            smallerProvider['company'] = provider
            smallerProvider['euclidean_distance'] = euclideanDistance
            equalsProvider = []
        elif smallerProvider['euclidean_distance'] == euclideanDistance:
            equalsProvider.append({
                "company": provider,
                "euclidean_distance": euclideanDistance,
            })

    equalsProvider.append(smallerProvider)
    client.set_current_company(equalsProvider)

    providerFound = False

    for provider in equalsProvider:
        for newProvider in newProvidersList:
            if newProvider['company'] == provider['company']:
                newProvider['client_list'].append(
                    {'company': client, 'euclidean_distance': provider['euclidean_distance']})
                providerFound = True
                break

        if providerFound is not True:
            newProvider = {
                'company': provider['company'],
                'client_list': [{'company': client, 'euclidean_distance': provider['euclidean_distance']}]
            }
            newProvidersList.append(newProvider)

matplotlib.style.use('dark_background')
plt.rcParams['figure.figsize'] = (11, 7)

for index, provider in enumerate(newProvidersList, 0):
    provider['company'].set_current_company(provider['client_list'])
    newProvidersList[index] = provider['company']
    currentProvider = provider['company']

    axes = plt.axes()
    axes.margins(x=0.01, y=0.01)

    plt.title('Fornecedor ' + currentProvider.name)

    points = [[float(currentProvider.longitude), float(currentProvider.latitude)]]

    x = PrettyTable(["Cliente", "Latitude", "Longitude", "Distância Euclidiana"])
    x.align["Cliente"] = "l"
    x.align["Latitude"] = "r"
    x.align["Longitude"] = "r"
    x.align["Distância Euclidiana"] = "r"
    x.padding_width = 1

    for client in currentProvider.current_company:
        currentClient = client['company']
        points.append([float(currentClient.longitude), float(currentClient.latitude)])
        x.add_row([currentClient.name, currentClient.latitude, currentClient.longitude, client['euclidean_distance']])

    header, data = get_data_from_prettytable(x.get_string(sortby="Distância Euclidiana", reversesort=True))
    export_to_pdf(header, data, currentProvider.name)

    vor = Voronoi(np.array(points))

    lines = [
        LineString(vor.vertices[line])
        for line in vor.ridge_vertices if -1 not in line
    ]

    convex_hull = MultiPoint([Point(i) for i in points]).convex_hull.buffer(2)
    result = MultiPolygon([poly.intersection(convex_hull) for poly in polygonize(lines)])
    result = MultiPolygon([p for p in result] + [p for p in convex_hull.difference(unary_union(result))])

    plt.plot(float(currentProvider.longitude), float(currentProvider.latitude), 'ko')
    plt.text(float(currentProvider.longitude), float(currentProvider.latitude) + 0.01,
             'Fornecedor ' + currentProvider.name, horizontalalignment='left',
             color='black')
    plt.axis('equal')
    plt.xlim(vor.min_bound[0] + 0.01, vor.max_bound[0] + 0.01)
    plt.ylim(vor.min_bound[1] + 0.01, vor.max_bound[1] + 0.01)

    for r in result:
        plt.fill(*zip(*np.array(list(
            zip(r.boundary.coords.xy[0][:-1], r.boundary.coords.xy[1][:-1])))),
                 alpha=1)

    plt.savefig(os.path.join(my_path, '../assets/img/' + currentProvider.name + '.png'), transparent=True)
    plt.show()
