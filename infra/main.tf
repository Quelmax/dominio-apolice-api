terraform {
    required_providers {
        azurerm = {
            source  = "hashicorp/azurerm"
            version = "~> 3.0"
        }
    }
    required_version = ">= 1.0.0"
}

provider "azurerm" {
    features {}
  
}

resource "azurerm_resource_group" "rg" {
    name     = var.resource_group_name
    location = var.location
}

resource "azurerm_app_service_plan" "asp" {
    name                = var.app_service_plan_name
    location            = azurerm_resource_group.rg.location
    resource_group_name = azurerm_resource_group.rg.name
    kind = "Linux"
    reserved = true
    sku {
        tier     = "Basic"
        size     = "B1"
    }
  
}

resource "azurerm_app_service" "app" {
    name                = var.app_service_name
    location            = azurerm_resource_group.rg.location
    resource_group_name = azurerm_resource_group.rg.name
    app_service_plan_id = azurerm_app_service_plan.asp.id

    site_config {
      linux_fx_version = "DOCKER|${var.docker_image_name}"
    }

    app_settings = {
        website_port = 80
        DOCKER_REGISTRY_SERVER_USERNAME = var.docker_regitry_username
        DOCKER_REGISTRY_SERVER_PASSWORD = var.docker_regitry_password
    }
 
    identity {
        type = "SystemAssigned"
    }
  
}