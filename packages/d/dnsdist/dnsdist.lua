-- for more see https://github.com/PowerDNS/pdns/blob/master/pdns/dnsdistconf.lua
-- controlSocket("127.0.0.1")
-- setKey(please generate a fresh private key with makeKey())

addLocal("127.0.0.1:53")
newServer{address="8.8.8.8:53"}
newServer{address="8.8.4.4:53"}

-- vim: set filetype=lua
