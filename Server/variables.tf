variable "digitalocean_token" {
  
    description = "DigitalOcean API token"
    type        = string
    default     = "***"
}

variable "my_private_key_file_path" {
  
    description = "Private Key File Path"
    type        = string
    default     = "/home/amazing/.ssh/id_rsa"

}
