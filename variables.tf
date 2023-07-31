variable "prefix" {
  description = "The prefix used for all resources in this environment"
  default = "JP"
}

variable "docker_url" {
  default = "https://index.docker.io/v1"
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
}

variable "website_service_storage_enabled" {
  type = bool
}

variable "websites_port" {
}
