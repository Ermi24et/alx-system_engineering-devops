# fix a line of for typo error
exec { 'fix-wp-error':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
}
