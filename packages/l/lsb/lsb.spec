#
# spec file for package lsb
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           lsb
Summary:        LSB Fake Package
License:        GPL-2.0-or-later
Group:          System/Fhs
Version:        4.0.fake
Release:        0
Obsoletes:      lsb-desktop
BuildRequires:  glibc-devel-32bit
BuildRequires:  openSUSE-release
Requires:       /bin/cat
Requires:       /bin/chgrp
Requires:       /bin/chmod
Requires:       /bin/chown
Requires:       /bin/cp
Requires:       /bin/dd
Requires:       /bin/df
Requires:       /bin/echo
Requires:       /bin/ed
Requires:       /bin/false
Requires:       /bin/fuser
Requires:       /bin/hostname
Requires:       /bin/kill
Requires:       /bin/ln
Requires:       /bin/logger
Requires:       /bin/ls
Requires:       /bin/mkdir
Requires:       /bin/mknod
Requires:       /bin/more
Requires:       /bin/mount
Requires:       /bin/mv
Requires:       /bin/ps
Requires:       /bin/pwd
Requires:       /bin/rm
Requires:       /bin/rmdir
Requires:       /bin/sed
Requires:       /bin/sh
Requires:       /bin/sleep
Requires:       /bin/sort
Requires:       /bin/stty
Requires:       /bin/su
Requires:       /bin/sync
Requires:       /bin/tar
Requires:       /bin/touch
Requires:       /bin/true
Requires:       /bin/umount
Requires:       /bin/uname
Requires:       /sbin/pidof
Requires:       /sbin/shutdown
Requires:       /usr/bin/ar
Requires:       /usr/bin/at
Requires:       /usr/bin/awk
Requires:       /usr/bin/basename
Requires:       /usr/bin/batch
Requires:       /usr/bin/bc
Requires:       /usr/bin/chfn
Requires:       /usr/bin/chsh
Requires:       /usr/bin/cksum
Requires:       /usr/bin/cmp
Requires:       /usr/bin/col
Requires:       /usr/bin/comm
Requires:       /usr/bin/crontab
Requires:       /usr/bin/csplit
Requires:       /usr/bin/cut
Requires:       /usr/bin/diff
Requires:       /usr/bin/dirname
Requires:       /usr/bin/du
Requires:       /usr/bin/env
Requires:       /usr/bin/expand
Requires:       /usr/bin/expr
Requires:       /usr/bin/file
Requires:       /usr/bin/find
Requires:       /usr/bin/fold
Requires:       /usr/bin/foomatic-rip
Requires:       /usr/bin/gencat
Requires:       /usr/bin/getconf
Requires:       /usr/bin/gettext
Requires:       /usr/bin/groups
Requires:       /usr/bin/gs
Requires:       /usr/bin/head
Requires:       /usr/bin/iconv
Requires:       /usr/bin/id
Requires:       /usr/bin/install
Requires:       /usr/bin/ipcrm
Requires:       /usr/bin/ipcs
Requires:       /usr/bin/join
Requires:       /usr/bin/killall
Requires:       /usr/bin/locale
Requires:       /usr/bin/localedef
Requires:       /usr/bin/logname
Requires:       /usr/bin/lp
Requires:       /usr/bin/lpr
Requires:       /usr/bin/m4
Requires:       /usr/bin/mailx
Requires:       /usr/bin/make
Requires:       /usr/bin/man
Requires:       /usr/bin/md5sum
Requires:       /usr/bin/mkfifo
Requires:       /usr/bin/msgfmt
Requires:       /usr/bin/newgrp
Requires:       /usr/bin/nice
Requires:       /usr/bin/nl
Requires:       /usr/bin/nohup
Requires:       /usr/bin/od
Requires:       /usr/bin/passwd
Requires:       /usr/bin/paste
Requires:       /usr/bin/patch
Requires:       /usr/bin/pathchk
Requires:       /usr/bin/pr
Requires:       /usr/bin/printf
Requires:       /usr/bin/renice
Requires:       /usr/bin/rsync
Requires:       /usr/bin/split
Requires:       /usr/bin/strip
Requires:       /usr/bin/sum
Requires:       /usr/bin/tail
Requires:       /usr/bin/tee
Requires:       /usr/bin/test
Requires:       /usr/bin/time
Requires:       /usr/bin/tr
Requires:       /usr/bin/tsort
Requires:       /usr/bin/tty
Requires:       /usr/bin/unexpand
Requires:       /usr/bin/uniq
Requires:       /usr/bin/wc
Requires:       /usr/bin/xargs
Requires:       /usr/bin/xdg-desktop-icon
Requires:       /usr/bin/xdg-desktop-menu
Requires:       /usr/bin/xdg-email
Requires:       /usr/bin/xdg-icon-resource
Requires:       /usr/bin/xdg-mime
Requires:       /usr/bin/xdg-open
Requires:       /usr/bin/xdg-screensaver
Requires:       /usr/sbin/groupadd
Requires:       /usr/sbin/groupdel
Requires:       /usr/sbin/groupmod
Requires:       /usr/sbin/sendmail
Requires:       /usr/sbin/useradd
Requires:       /usr/sbin/userdel
Requires:       /usr/sbin/usermod
Requires:       cpio
Requires:       grep
Requires:       gzip
Requires:       lsb-release
Requires:       pax
Obsoletes:      lsb-runtime
Provides:       lsb = 2.0
Provides:       lsb-core-noarch = 2.0
Provides:       lsb-core-noarch = 3.2
Provides:       lsb-core-noarch = 4.0
%ifarch %ix86
Provides:       lsb-core-ia32 = 2.0
Provides:       lsb-core-ia32 = 3.2
Provides:       lsb-core-ia32 = 4.0
%else
%ifarch x86_64
Provides:       lsb-core-amd64 = 2.0
Provides:       lsb-core-amd64 = 3.2
Provides:       lsb-core-amd64 = 4.0
Provides:       lsb-core-ia32 = 2.0
Provides:       lsb-core-ia32 = 3.2
Provides:       lsb-core-ia32 = 4.0
%else
%ifarch s390x
Provides:       lsb-core-s390 = 2.0
Provides:       lsb-core-s390 = 3.2
Provides:       lsb-core-s390 = 4.0
%endif
%ifarch ppc64 ppc
Provides:       lsb-core-ppc32 = 2.0
Provides:       lsb-core-ppc32 = 3.2
Provides:       lsb-core-ppc32 = 4.0
%ifarch ppc64
Provides:       lsb-core-ppc64 = 2.0
Provides:       lsb-core-ppc64 = 3.2
Provides:       lsb-core-ppc64 = 4.0
%endif
%else
Provides:       lsb-core-%{_target_cpu} = 2.0
Provides:       lsb-core-%{_target_cpu} = 3.2
Provides:       lsb-core-%{_target_cpu} = 4.0
%endif
%endif
%endif
Provides:       lsb-graphics-noarch = 2.0
Provides:       lsb-graphics-noarch = 3.2
Provides:       lsb-graphics-noarch = 4.0
%ifarch %ix86
Provides:       lsb-graphics-ia32 = 2.0
Provides:       lsb-graphics-ia32 = 3.2
Provides:       lsb-graphics-ia32 = 4.0
%else
%ifarch x86_64
Provides:       lsb-graphics-amd64 = 2.0
Provides:       lsb-graphics-amd64 = 3.2
Provides:       lsb-graphics-amd64 = 4.0
Provides:       lsb-graphics-ia32 = 2.0
Provides:       lsb-graphics-ia32 = 3.2
Provides:       lsb-graphics-ia32 = 4.0
%else
%ifarch s390x
Provides:       lsb-graphics-s390 = 2.0
Provides:       lsb-graphics-s390 = 3.2
Provides:       lsb-graphics-s390 = 4.0
%endif
%ifarch ppc64 ppc
Provides:       lsb-graphics-ppc32 = 2.0
Provides:       lsb-graphics-ppc32 = 3.2
Provides:       lsb-graphics-ppc32 = 4.0
%ifarch ppc64
Provides:       lsb-graphics-ppc64 = 2.0
Provides:       lsb-graphics-ppc64 = 3.2
Provides:       lsb-graphics-ppc64 = 4.0
%endif
%else
Provides:       lsb-graphics-%{_target_cpu} = 2.0
Provides:       lsb-graphics-%{_target_cpu} = 3.2
Provides:       lsb-graphics-%{_target_cpu} = 4.0
%endif
%endif
%endif
Requires:       Mesa
Requires:       perl-base >= 5.8.8
Requires:       python >= 2.7.3
Prefix:         /usr
Url:            http://www.linuxbase.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Necessary files and dependencies for the Linux Standard Base (LSB)
Core.



%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_lib}
mkdir -p $RPM_BUILD_ROOT/etc/lsb-release.d
echo -n "LSB_VERSION=\"core-2.0-noarch:core-3.2-noarch:core-4.0-noarch:" > $RPM_BUILD_ROOT/etc/lsb-release
%ifarch %ix86
echo -n "core-2.0-ia32:core-3.2-ia32:core-4.0-ia32" >>  $RPM_BUILD_ROOT/etc/lsb-release
%else
echo -n "core-2.0-%{_target_cpu}:core-3.2-%{_target_cpu}:core-4.0-%{_target_cpu}" >>  $RPM_BUILD_ROOT/etc/lsb-release
%endif
echo "\"" >> $RPM_BUILD_ROOT/etc/lsb-release
%ifarch x86_64
mkdir -p $RPM_BUILD_ROOT/lib
ln -sf /lib64/ld-linux-x86-64.so.2 $RPM_BUILD_ROOT/lib64/ld-lsb-x86-64.so.2
ln -sf /lib64/ld-linux-x86-64.so.2 $RPM_BUILD_ROOT/lib64/ld-lsb-x86-64.so.3
%endif
%ifarch %ix86 x86_64
ln -sf /lib/ld-linux.so.2 $RPM_BUILD_ROOT/lib/ld-lsb.so.2
ln -sf /lib/ld-linux.so.2 $RPM_BUILD_ROOT/lib/ld-lsb.so.3
%endif
%ifarch ppc64
mkdir -p $RPM_BUILD_ROOT/lib
ln -s /lib64/ld64.so.1 $RPM_BUILD_ROOT/lib64/ld-lsb-ppc64.so.2
ln -s /lib64/ld64.so.1 $RPM_BUILD_ROOT/lib64/ld-lsb-ppc64.so.3
%endif
%ifarch ppc ppc64
ln -s /lib/ld.so.1            $RPM_BUILD_ROOT/lib/ld-lsb-ppc32.so.2
ln -s /lib/ld.so.1            $RPM_BUILD_ROOT/lib/ld-lsb-ppc32.so.3
%endif
%ifarch ia64
ln -s /lib/ld-linux-ia64.so.2 $RPM_BUILD_ROOT/lib/ld-lsb-ia64.so.2
ln -s /lib/ld-linux-ia64.so.2 $RPM_BUILD_ROOT/lib/ld-lsb-ia64.so.3
%endif
%ifarch s390x
mkdir -p $RPM_BUILD_ROOT/lib
ln -sf /lib64/ld64.so.1         $RPM_BUILD_ROOT/lib64/ld-lsb-s390x.so.2
ln -sf /lib64/ld64.so.1         $RPM_BUILD_ROOT/lib64/ld-lsb-s390x.so.3
%endif
%ifarch s390
ln -sf /lib/ld.so.1	      $RPM_BUILD_ROOT/lib/ld-lsb-s390.so.2
ln -sf /lib/ld.so.1           $RPM_BUILD_ROOT/lib/ld-lsb-s390.so.3
%endif
%ifarch sparc
ln -sf /lib/ld-linux.so.2      $RPM_BUILD_ROOT/lib/ld-lsb-sparc.so.2
ln -sf /lib/ld-linux.so.2      $RPM_BUILD_ROOT/lib/ld-lsb-sparc.so.3
%endif
# These platforms do not have a LSB, just add something to make it compile
%ifarch axp mips
ln -sf /lib/ld-linux.so.2      $RPM_BUILD_ROOT/lib/ld-lsb-%{_target_cpu}.so.2
ln -sf /lib/ld-linux.so.2      $RPM_BUILD_ROOT/lib/ld-lsb-%{_target_cpu}.so.3
%endif
mkdir -p $RPM_BUILD_ROOT/etc/lsb-release.d
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-2.0-noarch
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-3.2-noarch
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-%{version}-noarch
touch $RPM_BUILD_ROOT/etc/lsb-release.d/desktop-%{version}-noarch
%ifarch %ix86
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-2.0-ia32
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-3.2-ia32
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-%{version}-ia32
touch $RPM_BUILD_ROOT/etc/lsb-release.d/desktop-%{version}-ia32
%else
%ifarch x86_64
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-2.0-amd64
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-3.2-amd64
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-%{version}-amd64
touch $RPM_BUILD_ROOT/etc/lsb-release.d/desktop-%{version}-amd64
%else
%ifarch s390x
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-2.0-s390
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-3.2-s390
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-%{version}-s390
touch $RPM_BUILD_ROOT/etc/lsb-release.d/desktop-%{version}-s390
%endif
%ifarch ppc64 ppc
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-2.0-ppc32
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-3.2-ppc32
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-%{version}-ppc32
touch $RPM_BUILD_ROOT/etc/lsb-release.d/desktop-%{version}-ppc32
%ifarch ppc64
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-2.0-ppc64
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-3.2-ppc64
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-%{version}-ppc64
touch $RPM_BUILD_ROOT/etc/lsb-release.d/desktop-%{version}-ppc64
%endif
%else
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-2.0-%{_target_cpu}
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-3.2-%{_target_cpu}
touch $RPM_BUILD_ROOT/etc/lsb-release.d/graphics-%{version}-%{_target_cpu}
touch $RPM_BUILD_ROOT/etc/lsb-release.d/desktop-%{version}-%{_target_cpu}
%endif
%endif
%endif

%files
%defattr(-,root,root)
%dir /etc/lsb-release.d
/etc/lsb-release.d/*
/etc/lsb-release
%ifarch %ix86 x86_64
/lib/ld-lsb.so.2
/lib/ld-lsb.so.3
%endif
%ifarch ppc ppc64
/lib/ld-lsb-ppc32.so.2
/lib/ld-lsb-ppc32.so.3
%endif
%ifarch x86_64
/lib64/ld-lsb-x86-64.so.2
/lib64/ld-lsb-x86-64.so.3
%endif
%ifarch s390
/lib/ld-lsb-s390.so.2
/lib/ld-lsb-s390.so.3
%endif
%ifarch ppc64 s390x ia64
/%{_lib}/ld-lsb-%{_target_cpu}.so.2
/%{_lib}/ld-lsb-%{_target_cpu}.so.3
%endif

%changelog
