import azure.functions as func
from azure.cosmos import CosmosClient
import os
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="counter")
def counter(req: func.HttpRequest) -> func.HttpResponse:
    try:
        ## Gets variables specified from local.setting.json file 
        conn = os.environ["conn_str"]
        database_name = "azure-resume-db"
        container_name = "azure-resume-container"

        client = CosmosClient.from_connection_string(conn_str=conn) # Connection to Azure CosmosDB API
        database = client.get_database_client(database_name) # Gets database we want to query from
        container = database.get_container_client(container_name) # Gets container inside the database we want to work with
        item = container.read_item("1", partition_key="1") # finds item ID 1 in container
        updated_item = updatecount(item) #increments count value
        updated_item = container.upsert_item(item) # Uploads dictionary back to the Cosmos DB with updated count value
    
        return func.HttpResponse(json.dumps(updated_item["count"]))
    except:
        return func.HttpResponse(status_code=400)
    
def updatecount(item):
    count = item["count"] # Gets the value for count
    count = int(count) + 1 # Increments count value by 1
    item["count"] = str(count) # Passes incremented count value back to dictionary
    return item