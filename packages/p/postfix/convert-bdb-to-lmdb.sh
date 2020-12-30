#!/bin/bash
if grep -q "hash:" /etc/postfix/{main.cf,master.cf}; then
	sed -i 's/hash:/lmdb:/g' /etc/postfix/{main.cf,master.cf}
fi
for i in $( find /etc/postfix/  -name "*.db"  )
do
	mv $i $i-back
	postmap ${i%.db}
done
for i in $( find /etc/aliases.d/  -name "*.db" )
do
	mv $i $i-back
	postalias ${i%.db}
done
if [ -e /etc/aliases.db ]; then
	mv /etc/aliases.db /etc/aliases.db-back
	postalias /etc/aliases
fi
