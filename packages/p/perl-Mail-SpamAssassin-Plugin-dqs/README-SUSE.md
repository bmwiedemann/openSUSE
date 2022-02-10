Usage of spamhaus/spamassassin-dqs
==================================

Check, if HBL is enabled for your query-key, execute `hbltest.sh` and
enter your query key.
If HBL is disabled, replace sh_hbl.cf and sh_hbl_scores.cf by empty content:
```
echo '' > /etc/mail/spamassassin/sh_hbl.cf
echo '' > /etc/mail/spamassassin/sh_hbl_scores.cf
```

To allow network queries via the DQS plugin, the local-only configuration from 
/etc/sysconfig/spamd must be removed by removing the '-L' parameter:
```
sed -e 's/^\(SPAMD_ARGS="-d -c\) -L"/\1"/' -i /etc/sysconfig/spamd
```


Add your query key into the configuration files.
Use you personal key instead of the example's key!:
```
for FILE in /etc/mail/spamassassin/sh*.cf 
do sed -e 's/your_DQS_key/aip7yig6sahg6ehsohn5shco3z/g' -i $FILE ; done
```


After restarting spamd by executing `systemctl restart spamd.service`, your 
Spamaccassin daemon will query Spamhaus Servers.
It's highlly recommended to run the "Spamhaus Blocklist Tester" to check if
your configuration works as expected. Be aware, that some mails will blocked 
on SMTP level, others are tagged as spam and others will only have spam headers
set depending on your configuration.
