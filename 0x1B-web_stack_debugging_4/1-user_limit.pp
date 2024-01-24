# increasing the number of files a process can run at a time

exec { 'increasing-hard-limit':
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 5000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin'
}

exec { 'increasing-soft-limit':
  command => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 4000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin'
}
