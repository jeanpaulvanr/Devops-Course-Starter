terraform {

  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = ">= 3.8"
    }
  }

  backend "azurerm" {
      resource_group_name  = "Cohort26_JeaRys_ProjectExercise"
      storage_account_name = "jpdoapptfstate"
      container_name       = "jptodoappcontainer"
      key                  = "terraform.tfstate"
  }

}

provider "azurerm" {
  features {}
}

data "azurerm_resource_group" "main" {
  name     = "Cohort26_JeaRys_ProjectExercise"
}

resource "azurerm_service_plan" "main" {
  name                = "${var.prefix}-terraformed-asp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = "B1"
}

#Cosmos DB Account

resource "random_integer" "ri" {
  min = 10000
  max = 99999
}

resource "azurerm_cosmosdb_account" "acc" {
  name                = "jp-todoapp-cosmos-db-${random_integer.ri.result}"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  offer_type          = "Standard"
  kind                = "MongoDB"

  enable_automatic_failover = true

  capabilities {
    name = "EnableAggregationPipeline"
  }

  capabilities {
    name = "mongoEnableDocLevelTTL"
  }

  capabilities {
    name = "MongoDBv3.4"
  }

  capabilities {
    name = "EnableMongo"
  }

  capabilities {
      name = "EnableServerless"
  }

  consistency_policy {
    consistency_level       = "BoundedStaleness"
    max_interval_in_seconds = 300
    max_staleness_prefix    = 100000
  }

  geo_location {
    location          = "eastus"
    failover_priority = 0
  }
}

#Cosmos DB

resource "azurerm_cosmosdb_mongo_database" "db" {
  name                = "jp-todoapp-cosmos-mongo-db"
  resource_group_name = azurerm_cosmosdb_account.acc.resource_group_name
  account_name        = azurerm_cosmosdb_account.acc.name

lifecycle { 
    prevent_destroy = false 
  }
}

#App

resource "azurerm_linux_web_app" "main" {
  name                = "JP-ToDo-App"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id

  site_config {
    application_stack {
      docker_image     = "jeanpaulvanr/todoapp"
      docker_image_tag = "latest"
    }
  }

  app_settings = {
    "CONNECTION_STRING" = azurerm_cosmosdb_account.acc.connection_strings[0]
    "CONTAINER_REPOSITORY_SERVER_URL" = var.container_repository_server_url
    "FLASK_APP" = var.flask_app
    "FLASK_ENV" = var.flask_env
    "SECRET_KEY" = var.secret_key
    "WEBSITE_USE_DIAGNOSTIC_SERVER" = var.website_diagnostics_enabled
    "WEBSITES_ENABLE_APP_SERVICE_STORAGE" = var.website_service_storage_enabled
    "WEBSITES_PORT" = var.websites_port
    "LOG_LEVEL" = var.log_level
    "LOGGING_SERVICE_TOKEN" = var.logging_service_token
    "GH_CLIENT_ID" = var.gh_client_id
    "GH_CLIENT_SECRET" = var.gh_client_secret
  }
}