# Configures the nginx web server to listen port 80,
# return a page that contains the string "Hello World!" when queried
# at its root (/) and sets /redirect_me to a 301 moved permanently

exec {'configure_nginx':
  command  => '
  ./1-install_nginx_web_server 
  ./3-redirection
  ./4-not_found_page_404
  ',
  provider => 'shell'
}
