#!/bin/bash

# Identify whether any config files exist
configfiles=($(find /etc/redis -maxdepth 1 -name "*.conf"))
redisunits=($(find /etc/systemd/system -maxdepth 1 -name "redis@*.service" -execdir basename {} \;))
sentinelunits=($(find /etc/systemd/system -maxdepth 1 -name "redis-sentinel@*.service" -execdir basename {} \;))

if [ ${#configfiles[@]} -gt 0 ]; then
  for configfile in ${configfiles[@]}
  do
      configfilename=$(basename "$configfile")
      cp $configfile /etc/valkey/$configfilename
      mv $configfile ${configfile}.bak
  done
  sed -e 's|^dir\s.*|dir /var/lib/valkey|g' -i /etc/valkey/*.conf
  echo "/etc/redis/*.conf has been copied to /etc/valkey.  Manual review of adjusted configs is strongly suggested."
fi
if [ ${#redisunits[@]} -gt 0 ]; then
  for redisunit in ${redisunits[@]}
  do
      systemctl disable "${redisunit}"
      systemctl enable "valkey@${redisunit##*@}"
  done
fi
if [ ${#sentinelunits[@]} -gt 0 ]; then
  for sentinelunit in ${sentinelunits[@]}
  do
      systemctl disable "${sentinelunit}"
      systemctl enable "valkey-sentinel@${sentinelunit##*@}"
  done
fi
if [ -d /var/lib/redis ]; then
  cp -r /var/lib/redis/* /var/lib/valkey/
  chown -R valkey. /var/lib/valkey
  mv /var/lib/redis /var/lib/redis.bak
  echo "On-disk redis dumps copied from /var/lib/redis/ to /var/lib/valkey"
fi
