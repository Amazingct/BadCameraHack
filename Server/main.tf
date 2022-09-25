resource "digitalocean_droplet" "mosquitto-mqtt" {
  image = "ubuntu-20-04-x64"
  name = "mosquitto-mqtt"
  region = "nyc3"
  size = "s-1vcpu-1gb"

  ssh_keys = [
      data.digitalocean_ssh_key.dell.id
  ]
  
  connection {
    host = self.ipv4_address
    user = "root"
    type = "ssh"
    private_key = file(var.my_private_key_file_path)
    timeout = "2m"
  }
  
  provisioner "remote-exec" {
    inline = [
      "export PATH=$PATH:/usr/bin",
      # install mosquitto and set it up
      "sudo apt install -y mosquitto",
      "touch /etc/mosquitto/conf.d/default.conf",
      "echo 'listener 30100' >> /etc/mosquitto/conf.d/default.conf",
      "echo 'allow_anonymous true' >> /etc/mosquitto/conf.d/default.conf",
      "sudo systemctl restart mosquitto"
    ]
  }
}



