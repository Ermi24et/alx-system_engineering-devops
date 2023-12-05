# a manifest to install nginx

class { 'nginx':
  ensure => 'installed',
}

file { 'etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
    	listen 80 default_server;
    	listen [::]:80 default_server;
    	add_header X-Served-By ${hostname};
    	root /etc/nginx/html;
    	index index.html index.htm;

    	location /redirect_me {
    	    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    	}

    	error_page 404 /404_error.html;
    	location /404 {
    	    root /etc/nginx/html;
    	    internal;
    	}
    }
  ",
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
