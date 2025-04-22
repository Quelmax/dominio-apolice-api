variable "resource_group_name" {
  description = "Nome do Resource Group no Azure"
  type        = string
}

variable "location" {
  description = "Região do Azure onde os recursos serão criados"
  type        = string
  default     = "eastus"  
}

variable "app_service_plan_name" {
  description = "Nome do App Service Plan"
  type        = string
}

variable "app_service_name" {
  description = "Nome da aplicação (App Service)"
  type        = string
}

