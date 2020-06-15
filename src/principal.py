import os.path
from src.Company import Company
from operator import attrgetter

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

providersList.sort(key=attrgetter('name'))

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

    for i in range(1, len(providersList)):
        provider = providersList[i]
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

providersList = []

for provider in newProvidersList:
    provider['company'].set_current_company(provider['client_list'])
    providersList.append(provider['company'])

for provider in providersList:
    print(provider)
