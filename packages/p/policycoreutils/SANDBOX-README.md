# policycoreutils-sandbox

Package for additional sandboxing of binaries.

## Setup

To get the 'sandbox' binary to work setting a setuid bit manually is currently
needed:

  chmod u+s /usr/sbin/seunshare

## Hints

The selinux-policy-sandbox package ships with multiple types:

- sandbox_x_t
- sandbox_web_t
- sandbox_net_t

To be used with the '-t' flag:

  sandbox -t sandbox_x_t <binary>

