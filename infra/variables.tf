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

variable "docker_image_name" {
  description = "Nome da imagem Docker publicada no Docker Hub"
  type        = string
}

variable "docker_regitry_username" {
  description = "Nome de usuário do Docker Registry"
  type        = string  
  
}

variable "docker_regitry_password" {
  description = "Senha do Docker Registry"
  type        = string  
  sensitive   = true
}