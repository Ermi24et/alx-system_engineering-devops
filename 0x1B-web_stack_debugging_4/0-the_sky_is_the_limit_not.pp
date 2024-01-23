# fix the U-LIMIT inorder to get rid of the failed requests
exec { 'fix-config_nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}
-> exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
