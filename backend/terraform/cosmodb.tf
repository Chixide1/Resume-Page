resource "azurerm_cosmosdb_account" "dbaccount" {
  name                = "ck-cloud-resume-cosmos"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"

  capabilities {
    name = "EnableServerless"
  }

  consistency_policy {
    consistency_level = "Session"
  }

  geo_location {
    location          = azurerm_resource_group.rg.location
    failover_priority = 0
    zone_redundant    = false
  }
}

resource "azurerm_cosmosdb_sql_database" "cosmosdb" {
  name                = "azure-resume-db"
  resource_group_name = azurerm_resource_group.rg.name
  account_name        = azurerm_cosmosdb_account.dbaccount.name
}

resource "azurerm_cosmosdb_sql_container" "container" {
  name                = "azure-resume-container"
  resource_group_name = azurerm_resource_group.rg.name
  account_name        = azurerm_cosmosdb_account.dbaccount.name
  database_name       = azurerm_cosmosdb_sql_database.cosmosdb.name
  partition_key_path  = "/id"

    provisioner "local-exec" {
    command = "az cosmosdb item create --resource-group ${azurerm_resource_group.rg.name} --name ${azurerm_cosmosdb_account.dbaccount.name} --database-name ${azurerm_cosmosdb_sql_database.cosmosdb.name} --container-name ${azurerm_cosmosdb_sql_container.container.name} --api-version 2021-05-15 --content '{ 'id': 1, 'count': 0 }'"
  }
}