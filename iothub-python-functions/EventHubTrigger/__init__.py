import logging
import azure.functions as func
from azure.cosmosdb.table.tableservice import TableService
import requests
import json
import os


imageScannerTable = "Classified"

storageConnectionString = os.environ['StorageConnectionString']
partitionKey = os.environ['PartitionKey']
signalrUrl = os.environ['SignalrUrl']


table_service = TableService(connection_string=storageConnectionString)
if not table_service.exists(imageScannerTable):
    table_service.create_table(imageScannerTable)

def main(event: func.EventHubEvent):

    messages = json.loads(event.get_body().decode('utf-8'))

    for msg in messages:

        sortResponse = sorted(
            msg, key=lambda k: k['Probability'], reverse=True)[0]

        sortResponse['PartitionKey'] = partitionKey
        sortResponse['RowKey'] = sortResponse['Tag']

        # Note, Count read and update is not transactional
        try:
            entity = table_service.get_entity(
                imageScannerTable, partitionKey, sortResponse['Tag'])
            if 'Count' not in entity:
                count = 0
            else:
                count = entity['Count']
        except:
            count = 0

        sortResponse['Count'] = count + 1

        table_service.insert_or_replace_entity(imageScannerTable, sortResponse)

        notifyClients(signalrUrl, sortResponse)

        # scannedImages.set(json.dumps(sortResponse))

def notifyClients(signalrUrl, telemetry):
    headers = {'Content-type': 'application/json'}
    r = requests.post(signalrUrl, data=json.dumps(telemetry), headers=headers)
    logging.info(r)
