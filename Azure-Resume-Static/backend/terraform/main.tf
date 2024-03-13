terraform {
  required_providers {

    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.91.0"
    }

    random = {
      source  = "hashicorp/random"
      version = "3.6.0"
    }

    azuread = {
      source  = "hashicorp/azuread"
      version = "2.47.0"
    }

  }
  required_version = ">= 1.1.0"
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "azure-resume"
  location = "uksouth"
}