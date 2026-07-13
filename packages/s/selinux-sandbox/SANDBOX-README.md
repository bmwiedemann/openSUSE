# policycoreutils-sandbox

Package for additional sandboxing of binaries.

## Setup

To get the 'sandbox' binary to work properly setting a setuid bit on 'seunshare'
is needed. Different variants of these permissions are handled via the
'permissions' package and the permctl tool.

Manually adding a setuid bit is also a possibility:

  chmod u+s /usr/bin/seunshare

## Hints

The selinux-policy-sandbox package ships with multiple types:

- sandbox_x_t
- sandbox_web_t
- sandbox_net_t

To be used with the '-t' flag:

  sandbox -t sandbox_x_t <binary>

