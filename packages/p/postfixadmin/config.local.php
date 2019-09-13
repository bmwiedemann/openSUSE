<?php
################################################################################
#                                                                              #
#    PostfixAdmin local configuration                                          #
#                                                                              #
#    Use this file for your own configuration settings.                        #
#                                                                              #
#    See config.inc.php for all available config options, but please do not    #
#    change that file. Instead, add the options you want to change/override    #
#    to config.local.php (= this file).                                        #
#                                                                              #
################################################################################


# You have to set $CONF['configured'] = true; before the application will run!
# Doing this implies you have changed your config as required.
# i.e. configuring database etc; specifying setup.php password etc.
$CONF['configured'] = false;

# In order to setup Postfixadmin, you MUST specify a hashed password here.
# To create the hash, visit setup.php in a browser and type a password into the field,
# on submission it will be echoed out to you as a hashed value.
$CONF['setup_password'] = 'changeme';

# Database Config
# mysqli = MySQL 4.1+ or MariaDB
# pgsql = PostgreSQL
# sqlite = SQLite 3
$CONF['database_type'] = 'mysqli';
$CONF['database_host'] = 'localhost';
$CONF['database_user'] = 'postfix';
$CONF['database_password'] = 'postfixadmin';
$CONF['database_name'] = 'postfix';
