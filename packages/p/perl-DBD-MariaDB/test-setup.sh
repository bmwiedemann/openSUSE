#!/bin/bash

# MySQL setup
export MYSQL_DIR=${PWD}/t/testdb
export MYSQL_UNIX_PORT=${MYSQL_DIR}/mysql.sock
export MYSQL_PIDFILE=${MYSQL_DIR}/mysql.pid
export MYSQL_USER=$(whoami)

# DBD::MariaDB test setup
export DBD_MARIADB_TESTDB=testdb
export DBD_MARIADB_TESTHOST=localhost
export DBD_MARIADB_TESTSOCKET=${MYSQL_UNIX_PORT}
export DBD_MARIADB_TESTUSER=testuser
export DBD_MARIADB_TESTPASSWORD=testpassword

#export EXTENDED_TESTING=1

if mysql --version | grep -q MariaDB; then
    mysql_install_db --no-defaults --datadir=${MYSQL_DIR} --force --skip-name-resolve --explicit_defaults_for_timestamp --user=${MYSQL_USER} 2>&1
else
    /usr/sbin/mysqld --no-defaults --initialize-insecure --datadir=${MYSQL_DIR} --explicit_defaults_for_timestamp --user=${MYSQL_USER} 2>&1
fi

/usr/sbin/mysqld --no-defaults --user=${MYSQL_USER} --socket=${MYSQL_UNIX_PORT} --datadir=${MYSQL_DIR} --pid-file=${MYSQL_PIDFILE} --explicit_defaults_for_timestamp --skip-networking 2>&1 &
attempts=0
while ! /usr/bin/mysqladmin --user=root --socket=${MYSQL_UNIX_PORT} ping 2>&1 ; do
    sleep 3
    attempts=$((attempts+1))
    if [ ${attempts} -gt 10 ] ; then
        echo "skipping test, mariadb/mysql server could not be contacted after 30 seconds"
        exit 1
    fi
done

mysql --user=root --socket=${MYSQL_UNIX_PORT} --execute "CREATE USER '${DBD_MARIADB_TESTUSER}'@'localhost';" 2>&1
mysql --user=root --socket=${MYSQL_UNIX_PORT} --execute "CREATE DATABASE IF NOT EXISTS ${DBD_MARIADB_TESTDB} CHARACTER SET='utf8mb4';" 2>&1
mysql --user=root --socket=${MYSQL_UNIX_PORT} --execute "GRANT ALL PRIVILEGES ON ${DBD_MARIADB_TESTDB}.* TO '${DBD_MARIADB_TESTUSER}'@'localhost' IDENTIFIED BY '${DBD_MARIADB_TESTPASSWORD}';" 2>&1

if ! /usr/bin/mysqladmin --user=${DBD_MARIADB_TESTUSER} --password=${DBD_MARIADB_TESTPASSWORD} --socket=${DBD_MARIADB_TESTSOCKET} ping 2>&1; then
    echo "skipping test, cannot connect to server with test user"
    exit 1
fi
