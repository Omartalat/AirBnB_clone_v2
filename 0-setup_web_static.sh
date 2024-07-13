#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install -y nginx

# Create some folders if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file /data/web_static/releases/test/index.html
echo 'Hello Alx!' | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# restart Nginx after updating the configuration
sudo nginx -t
sudo service nginx restart
