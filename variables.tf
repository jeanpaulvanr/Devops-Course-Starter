variable "prefix" {
  description = "The prefix used for all resources in this environment"
  default = "JP"
}

variable "docker_url" {
  default = "https://index.docker.io/v1"
}

variable "flask_app" {
  default = "todo_app/app"
}

variable "flask_env" {
  default = "development"
}

variable "secret_key" {
  sensitive = true
}

variable "website_diagnostics_enabled" {
  type = bool
  default = "true"
}

variable "website_service_storage_enabled" {
  type = bool
  default = "false"
}

variable "websites_port" {
  default = 5000
}
