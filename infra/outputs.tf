output "app_service_url" {
  description = "URL pública da API no Azure App Service"
  value       = "https://${azurerm_app_service.app.default_site_hostname}"
}
