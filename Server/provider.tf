terraform {
  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}

# variable "do_token" {}
# variable "pvt_key" {}

# Configure the DigitalOcean Provider
provider "digitalocean" {
  token = var.digitalocean_token
}

data "digitalocean_ssh_key" "dell" {
  name = "dell"
}