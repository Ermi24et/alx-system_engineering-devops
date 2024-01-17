# fix a line of code for typo error
exec { 'fix-error':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path => '/bin'
}
