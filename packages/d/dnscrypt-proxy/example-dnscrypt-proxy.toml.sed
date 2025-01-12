# the socket unit should listen
s/listen_addresses = \['127.0.0.1:53']/#listen_addresses = ['127.0.0.1:53']\nlisten_addresses = []/

# point to shipped distro specific documentation
12c\\n##********************************************************************##\n##                                                                    ##
13c\##                    README.openSUSE in directory                    ##\n##              \/usr\/share\/doc\/packages\/dnscrypt-proxy                ##\n##                       might be useful to read.                     ##\n##                                                                    ##\n##********************************************************************##

# absolute paths by default
s/# log_file = 'dnscrypt-proxy.log'/# log_file = '\/var\/log\/dnscrypt-proxy\/dnscrypt-proxy.log'/
s/# forwarding_rules = 'forwarding-rules.txt'/# forwarding_rules = '\/etc\/dnscrypt-proxy\/forwarding-rules.txt'/
s/# cloaking_rules = 'cloaking-rules.txt'/# cloaking_rules = '\/etc\/dnscrypt-proxy\/cloaking-rules.txt'/
s/# map_file = 'example-captive-portals.txt'/# map_file = '\/etc\/dnscrypt-proxy\/captive-portals.txt'/
s/# cert_file = 'localhost.pem'/# cert_file = '\/etc\/dnscrypt-proxy\/localhost.pem'/
s/# cert_key_file = 'localhost.pem'/# cert_key_file = '\/etc\/dnscrypt-proxy\/localhost.pem'/
s/# file = 'query.log'/# file = '\/var\/log\/dnscrypt-proxy\/query.log'/
s/# file = 'nx.log'/# file = '\/var\/log\/dnscrypt-proxy\/nx.log'/
s/# blocked_names_file = 'blocked-names.txt'/# blocked_names_file = '\/etc\/dnscrypt-proxy\/blocked-names.txt'/
s/# log_file = 'blocked-names.log'/# log_file = '\/var\/log\/dnscrypt-proxy\/blocked-names.log'/
s/# blocked_ips_file = 'blocked-ips.txt'/# blocked_ips_file = '\/etc\/dnscrypt-proxy\/blocked-ips.txt'/
s/# log_file = 'blocked-ips.log'/# log_file = '\/var\/log\/dnscrypt-proxy\/blocked-ips.log'/
s/# allowed_names_file = 'allowed-names.txt'/# allowed_names_file = '\/etc\/dnscrypt-proxy\/allowed-names.txt'/
s/# log_file = 'allowed-names.log'/# log_file = '\/var\/log\/dnscrypt-proxy\/allowed-names.log'/
s/# allowed_ips_file = 'allowed-ips.txt'/# allowed_ips_file = '\/etc\/dnscrypt-proxy\/allowed-ips.txt'/
s/# log_file = 'allowed-ips.log'/# log_file = '\/var\/log\/dnscrypt-proxy\/allowed-ips.log'/
s/    cache_file = 'public-resolvers.md'/    cache_file = '\/var\/lib\/dnscrypt-proxy\/public-resolvers.md'/
s/    cache_file = 'relays.md'/    cache_file = '\/var\/lib\/dnscrypt-proxy\/relays.md'/
s/  #   cache_file = 'odoh-servers.md'/  #   cache_file = '\/var\/lib\/dnscrypt-proxy\/odoh-servers.md'/
s/  #   cache_file = 'odoh-relays.md'/  #   cache_file = '\/var\/lib\/dnscrypt-proxy\/odoh-relays.md'/
s/  #   cache_file = 'quad9-resolvers.md'/  #   cache_file = '\/var\/lib\/dnscrypt-proxy\/quad9-resolvers.md'/
s/  #   cache_file = 'parental-control.md'/  #   cache_file = '\/var\/lib\/dnscrypt-proxy\/parental-control.md'/
s/  #    cache_file = "dnscry.pt-resolvers.md"/  #    cache_file = '\/var\/lib\/dnscrypt-proxy\/dnscry.pt-resolvers.md'/

# package directory instead of source code directory
s/## `utils\/generate-domains-blocklists` directory of the dnscrypt-proxy source code./## '\/usr\/share\/dnscrypt-proxy\/generate-domains-blocklists' directory./
