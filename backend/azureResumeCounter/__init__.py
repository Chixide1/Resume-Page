import os
import json
import azure.functions as func
from azure.cosmos import CosmosClient


def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        ## Gets variables specified from local.setting.json file 
        conn = os.environ["CosmosDbConnectionString"]
        database_name = "azure-resume"
        container_name = "counter"

        client = CosmosClient.from_connection_string(conn_str=conn) # Connection to Azure CosmosDB API
        database = client.get_database_client(database_name) # Gets database we want to query from
        container = database.get_container_client(container_name) # Gets container inside the database we want to work with
        item = container.read_item("1", partition_key="1") # Finds item ID 1 in container
        GetCountValue = item["count"] # Gets the value for count
        IncrementValue = int(GetCountValue) + 1 # Increments count value by 1
        item["count"] = str(IncrementValue) # Passes incremented count value back to dictionary
        updated_item = container.upsert_item(item) # Uploads dictionary back to the Cosmos DB with updated count value
    
        return func.HttpResponse(json.dumps(updated_item["count"]))
    except:
        return func.HttpResponse(status_code=400)
