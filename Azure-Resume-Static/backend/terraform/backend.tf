terraform {
  backend "azurerm" {
    resource_group_name  = "standard"
    storage_account_name = "chikstandard"
    container_name       = "tfstate"
    key                  = "azure-resume-static.terraform.tfstate"
  }
}
