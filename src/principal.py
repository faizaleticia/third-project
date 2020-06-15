import os.path
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
    providersList.append(Company(objectClient[0], objectClient[1], objectClient[2]))

print(len(clientsList))
print(len(providersList))

