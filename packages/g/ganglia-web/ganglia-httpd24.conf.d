#
# Ganglia monitoring system php web frontend
#
# Make sure to enable PHP. Depending on the version used.
# For php5 execute "a2enmod php5",
# for php7 execute "a2enmod php7".
Alias /ganglia WEBPATH

<Location /ganglia>
  Require all granted
  # Require host example.org
</Location>
