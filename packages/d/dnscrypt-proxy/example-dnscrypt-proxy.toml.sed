# the socket unit should listen
s/listen_addresses = \['127.0.0.1:53']/#listen_addresses = ['127.0.0.1:53']\nlisten_addresses = []/

# absolute paths by default
s/# log_file = 'dnscrypt-proxy.log'/# log_file = '\/var\/log\/dnscrypt-proxy\/dnscrypt-proxy.log'/
s/# forwarding_rules = 'forwarding-rules.txt'/# forwarding_rules = '\/etc\/dnscrypt-proxy\/forwarding-rules.txt'/
s/# cloaking_rules = 'cloaking-rules.txt'/# cloaking_rules = '\/etc\/dnscrypt-proxy\/cloaking-rules.txt'/
s/# cert_file = "localhost.pem"/# cert_file = '\/etc\/dnscrypt-proxy\/localhost.pem'/
s/# cert_key_file = "localhost.pem"/# cert_key_file = '\/etc\/dnscrypt-proxy\/localhost.pem'/
s/  # file = 'query.log'/  # file = '\/var\/log\/dnscrypt-proxy\/query.log'/
s/  # file = 'nx.log'/  # file = '\/var\/log\/dnscrypt-proxy\/nx.log'/
s/  # blacklist_file = 'blacklist.txt'/  # blacklist_file = '\/etc\/dnscrypt-proxy\/blacklist.txt'/
s/  # log_file = 'blocked.log'/  # log_file = '\/var\/log\/dnscrypt-proxy\/blocked.log'/
s/  # blacklist_file = 'ip-blacklist.txt'/# blacklist_file = '\/etc\/dnscrypt-proxy\/ip-blacklist.txt'/
s/  # log_file = 'ip-blocked.log'/  # log_file = '\/var\/log\/dnscrypt-proxy\/ip-blocked.log'/
s/  # whitelist_file = 'whitelist.txt'/# blacklist_file = '\/etc\/dnscrypt-proxy\/whitelist.txt'/
s/  # log_file = 'whitelisted.log'/  # log_file = '\/var\/log\/dnscrypt-proxy\/whitelisted.log'/
s/  cache_file = 'public-resolvers.md'/  cache_file = '\/var\/lib\/dnscrypt-proxy\/public-resolvers.md'/
s/  cache_file = 'relays.md'/  cache_file = '\/var\/lib\/dnscrypt-proxy\/relays.md'/
s/  #  cache_file = "quad9-resolvers.md"/  #  cache_file = '\/var\/lib\/dnscrypt-proxy\/quad9-resolvers.md'/
s/  #  cache_file = 'parental-control.md'/  #  cache_file = '\/var\/lib\/dnscrypt-proxy\/parental-control.md'/
