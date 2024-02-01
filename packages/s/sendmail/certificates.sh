#!/bin/bash

#
# Change values at your own need
#
# Two letter Country Code
C="DE"
# State
ST="Bayern"
# Organization
O="OpenSUSE"
# Firstname Lastname ... or Server Name
CN="$(hostname -f)"

test -s serial || echo '01' > serial
touch index.txt

export SSLDIR=${PWD}
ln -sf ${PWD} ./demoCA

  openssl req -new -newkey rsa:4096 -nodes -x509 -days 7300 -keyout private/key.pem -out careq.pem \
     -utf8 -subj "/C=${C}/ST=${ST}/O=${O}/CN=${CN}"

  openssl x509 -x509toreq -in careq.pem -signkey private/key.pem -out csr.pem

  yes | openssl ca -outdir $PWD -policy policy_anything --cert careq.pem -keyfile private/key.pem \
     -days 7300 -out cert.pem -infiles csr.pem

rm -vf ./demoCA
