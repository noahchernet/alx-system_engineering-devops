# Configures the nginx web server to listen port 80,
# return a page that contains the string "Hello World!" when queried
# at its root (/) and sets /redirect_me to a 301 moved permanently

exec {'configure_nginx':
  command  => '
  sudo apt install nginx -y
  sudo rm /var/www/html/index.nginx-debian.html;
  sudo echo "Hello World!" | sudo tee -a /var/www/html/index.nginx-debian.html;
  sudo sed -i "s/\tlisten [0-9].* default_server;*/\tlisten 80 default_server;/" /etc/nginx/sites-available/default;
  sudo sed -i "s/\tlisten \[::\]:[0-9].* default_server;*/\tlisten [::]:80 default_server;/" /etc/nginx/sites-available/default;
  new_url="\troot \/var\/www\/html;\n\trewrite ^\/redirect_me$ https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent;";
  sudo sed -i "s/\troot \/var\/www\/html;/$new_url/" /etc/nginx/sites-available/default;
  sudo service nginx reload;
  ',
  provider => 'shell'
}
