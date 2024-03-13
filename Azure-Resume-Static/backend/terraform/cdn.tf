
resource "azurerm_cdn_profile" "profile" {
  name                = "ck-cloud-resume-cdn-profile"
  location            = "westeurope"
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "Standard_Microsoft"
}

resource "azurerm_cdn_endpoint" "endpoint" {
  name                = "ck-cloud-resume-endpoint"
  profile_name        = azurerm_cdn_profile.profile.name
  location            = "westeurope"
  resource_group_name = azurerm_resource_group.rg.name

  origin_host_header = azurerm_storage_account.storage_acct.primary_web_host
  origin {
    name      = "ck-cloud-resume-origin"
    host_name = azurerm_storage_account.storage_acct.primary_web_host
  }
}