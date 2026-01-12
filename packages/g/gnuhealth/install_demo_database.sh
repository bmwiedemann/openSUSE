#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2008-2022 Luis Falcón <falcon@gnuhealth.org>
# SPDX-FileCopyrightText: 2011-2022 GNU Solidario <health@gnusolidario.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

#########################################################################
#   Hospital Management Information System (HMIS) component of the      #
#                       GNU Health project                              #
#                   https://www.gnuhealth.org                           #
#########################################################################
#                      install_demo_database.sh                         #
#        Downloads and installs the GNU Health demo database            #
#########################################################################



URL="https://www.gnuhealth.org/downloads/postgres_dumps/gnuhealth-$1-demo.sql.gz"
DB="ghdemo$1"

help()
{
    cat << EOF

GNU Health HMIS demo database installer

usage: `basename $0` <db_version>

    Example:
    $ bash ./install_demo_dabase.sh 40

    will install the latest demo db for version 4.0.x
EOF
    exit 0
}

bailout () {
    echo "Error"
    echo "Cleaning up..."
    cleanup
    exit 1
    }


if [ $# -eq 0 ]; then
    help
fi

cleanup () {
    rm -f gnuhealth_demo_database-$1.sql.gz
    rm -f gnuhealth_demo_database-$1.sql
    }


if psql -l | grep -wq "$DB"; then
    echo "$DB database already exists"
    echo "    delete it/change target database before proceeding"
    bailout
fi



echo -n "Downloading the demo database..."
wget "$URL" -O gnuhealth_demo_database-$1.sql.gz || bailout
echo 'SUCCESS...'

echo -n "Unpacking the database..."
gunzip -q gnuhealth_demo_database-$1.sql.gz || bailout
echo 'SUCCESS...'

echo -n "Initializing empty database..."
createdb $DB
echo 'SUCCESS...'

echo "Importing demo database..."
psql -q "$DB" < gnuhealth_demo_database-$1.sql > /dev/null 2>&1 || bailout
echo "IMPORT OF DEMO DATABASE $DB COMPLETED SUCCESFULLY !"

echo "Login Info:"
echo "    Database: $DB"
echo "    Username: admin"
echo "    Password: gnusolidario"
echo "**  IMPORTANT: Check that the GNUHealth kernel matches this demo DB"
exit 0


