import os.path
from src.Company import Company

my_path = os.path.abspath(os.path.dirname(_file_))
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

count = 0

for client in clientsList:
    clientPoint = (float(client.latitude), float(client.longitude))

    provider = providersList[0]
    euclideanDistance = provider.euclidean_distance(clientPoint)

    smallerProvider = {
      "company": providersList[0],
      "euclidean_distance": euclideanDistance,
    }

    for i in range(1, len(providersList)):
        provider = providersList[i]
        euclideanDistance = provider.euclidean_distance(clientPoint)

        if smallerProvider['euclidean_distance'] > euclideanDistance:
            smallerProvider['company'] = provider
            smallerProvider['euclidean_distance'] = euclideanDistance

    client.set_current_company([smallerProvider])