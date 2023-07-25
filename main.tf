terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = ">= 3.8"
    }
  }
}

provider "azurerm" {
  features {}
}

data "azurerm_resource_group" "main" {
  name     = "Cohort26_JeaRys_ProjectExercise"
}

resource "azurerm_service_plan" "main" {
  name                = "terraformed-asp"
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
    failover_priority = 1
  }

  geo_location {
    location          = "westus"
    failover_priority = 0
  }
}

#Cosmos DB

resource "azurerm_cosmosdb_mongo_database" "db" {
  name                = "jp-todoapp-cosmos-mongo-db"
  resource_group_name = data.azurerm_cosmosdb_account.acc.resource_group_name
  account_name        = data.azurerm_cosmosdb_account.acc.name
  throughput          = 400
}

#App

resource "azurerm_linux_web_app" "main" {
  name                = "JP-Hello-World"
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
    "MONGODB_CONNECTION_STRING" = azurerm_cosmosdb_account.acc.connection_strings[0]
    "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io"
    "FLASK_APP" = "todo_app/app"
    "FLASK_ENV" = "development2
    "SECRET_KEY" = "secret-key"
    "WEBSITE_USE_DIAGNOSTIC_SERVER" = "true"
    "WEBSITES_ENABLE_APP_SERVICE_STORAGE" = "false"
    "WEBSITES_PORT" = "5000"
    
  }
}