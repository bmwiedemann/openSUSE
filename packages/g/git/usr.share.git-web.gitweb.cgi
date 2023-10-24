#include <tunables/global>

profile gitweb.cgi /usr/share/gitweb/gitweb.cgi {
  #include <abstractions/base>
  #include <abstractions/bash>
  #include <abstractions/nameservice>
  #include <abstractions/perl>
  #include <abstractions/private-files-strict>

  /etc/gitconfig r,
  /{usr/,}bin/bash rix,
  /{usr/,}bin/tar rix,
  /usr/bin/gzip rix,
  /usr/bin/bzip2 rix,
  /usr/bin/zip rix,
  /dev/tty rw,
  /etc/gitweb.conf r,
  /etc/mime.types r,
  /proc/loadavg r,
  /proc/meminfo r,
  /proc/sys/kernel/ngroups_max r,
  /srv/git/ r,
  /srv/git/** r,
  /usr/bin/perl ix,
  /usr/lib/git/git rix,
  /usr/bin/git-receive-pack rix,
  /usr/share/gitweb/* r,
  /usr/share/gitweb/static/* r,
  owner /**/ r,
  owner /**/.git/** r,
  owner @{HOME}/.gitconfig r,

  # Site-specific additions and overrides. See local/README for details.
  include if exists <local/usr.share.git-web.gitweb.cgi>
}
