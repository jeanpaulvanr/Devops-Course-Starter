variable "prefix" {
  description = "The prefix used for all resources in this environment"
  default = "JP"
}

variable "container_repository_url" {
}

variable "flask_app" {
}

variable "flask_env" {
}

variable "secret_key" {
  sensitive = true
}

variable "website_diagnostics_enabled" {
  type = bool
  default = true
}

variable "website_service_storage_enabled" {
  type = bool
  default = false
}

variable "websites_port" {
}