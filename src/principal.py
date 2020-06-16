import os.path
import matplotlib
import matplotlib.pyplot as plt
from src.Company import Company

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

for index, provider in enumerate(newProvidersList, 0):
    provider['company'].set_current_company(provider['client_list'])
    newProvidersList[index] = provider['company']

matplotlib.style.use('dark_background')

ax = plt.axes()

ny_lon, ny_lat = 0.5154, 0.8832
client_lon, client_lat = 0.3228, 0.6503

delhi_lon, delhi_lat = 0.5984, 0.0715

plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
         color='gray', linestyle='--', linewidth=0.8)

plt.plot([client_lon, delhi_lon], [client_lat, delhi_lat],
         color='gray', linestyle='--', linewidth=0.8)

plt.scatter(0.3228, 0.6503, s=50)

plt.scatter(0.5154, 0.8832, s=50)

plt.scatter(0.5984, 0.0715, s=50)

plt.text(client_lon, client_lat + 0.01, 'Cliente ID0001',
         horizontalalignment='left')

plt.text(ny_lon, ny_lat + 0.01, 'Cliente ID0000',
         horizontalalignment='left')

plt.text(delhi_lon, delhi_lat + 0.01, 'Fornecedor A',
         horizontalalignment='left')

plt.show()