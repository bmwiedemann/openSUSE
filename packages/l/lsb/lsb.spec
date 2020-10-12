#
# spec file for package lsb
#
# Copyright (c) 2020 SUSE LLC
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
Version:        4.0.fake
Release:        0
Summary:        LSB Fake Package
License:        GPL-2.0-or-later
Group:          System/Fhs
URL:            https://www.linuxbase.org/
BuildRequires:  glibc-devel-32bit
BuildRequires:  openSUSE-release
Requires:       %{_bindir}/ar
Requires:       %{_bindir}/at
Requires:       %{_bindir}/awk
Requires:       %{_bindir}/basename
Requires:       %{_bindir}/batch
Requires:       %{_bindir}/bc
Requires:       %{_bindir}/chfn
Requires:       %{_bindir}/chsh
Requires:       %{_bindir}/cksum
Requires:       %{_bindir}/cmp
Requires:       %{_bindir}/col
Requires:       %{_bindir}/comm
Requires:       %{_bindir}/crontab
Requires:       %{_bindir}/csplit
Requires:       %{_bindir}/cut
Requires:       %{_bindir}/diff
Requires:       %{_bindir}/dirname
Requires:       %{_bindir}/du
Requires:       %{_bindir}/ed
Requires:       %{_bindir}/env
Requires:       %{_bindir}/expand
Requires:       %{_bindir}/expr
Requires:       %{_bindir}/file
Requires:       %{_bindir}/find
Requires:       %{_bindir}/fold
Requires:       %{_bindir}/foomatic-rip
Requires:       %{_bindir}/gencat
Requires:       %{_bindir}/getconf
Requires:       %{_bindir}/gettext
Requires:       %{_bindir}/groups
Requires:       %{_bindir}/gs
Requires:       %{_bindir}/head
Requires:       %{_bindir}/iconv
Requires:       %{_bindir}/id
Requires:       %{_bindir}/install
Requires:       %{_bindir}/ipcrm
Requires:       %{_bindir}/ipcs
Requires:       %{_bindir}/join
Requires:       %{_bindir}/killall
Requires:       %{_bindir}/locale
Requires:       %{_bindir}/localedef
Requires:       %{_bindir}/logname
Requires:       %{_bindir}/lp
Requires:       %{_bindir}/lpr
Requires:       %{_bindir}/m4
Requires:       %{_bindir}/mailx
Requires:       %{_bindir}/make
Requires:       %{_bindir}/man
Requires:       %{_bindir}/md5sum
Requires:       %{_bindir}/mkfifo
Requires:       %{_bindir}/msgfmt
Requires:       %{_bindir}/newgrp
Requires:       %{_bindir}/nice
Requires:       %{_bindir}/nl
Requires:       %{_bindir}/nohup
Requires:       %{_bindir}/od
Requires:       %{_bindir}/passwd
Requires:       %{_bindir}/paste
Requires:       %{_bindir}/patch
Requires:       %{_bindir}/pathchk
Requires:       %{_bindir}/pidof
Requires:       %{_bindir}/pr
Requires:       %{_bindir}/printf
Requires:       %{_bindir}/renice
Requires:       %{_bindir}/rsync
Requires:       %{_bindir}/split
Requires:       %{_bindir}/strip
Requires:       %{_bindir}/sum
Requires:       %{_bindir}/tail
Requires:       %{_bindir}/tee
Requires:       %{_bindir}/test
Requires:       %{_bindir}/time
Requires:       %{_bindir}/tr
Requires:       %{_bindir}/tsort
Requires:       %{_bindir}/tty
Requires:       %{_bindir}/unexpand
Requires:       %{_bindir}/uniq
Requires:       %{_bindir}/wc
Requires:       %{_bindir}/xargs
Requires:       %{_bindir}/xdg-desktop-icon
Requires:       %{_bindir}/xdg-desktop-menu
Requires:       %{_bindir}/xdg-email
Requires:       %{_bindir}/xdg-icon-resource
Requires:       %{_bindir}/xdg-mime
Requires:       %{_bindir}/xdg-open
Requires:       %{_bindir}/xdg-screensaver
Requires:       %{_sbindir}/groupadd
Requires:       %{_sbindir}/groupdel
Requires:       %{_sbindir}/groupmod
Requires:       %{_sbindir}/sendmail
Requires:       %{_sbindir}/useradd
Requires:       %{_sbindir}/userdel
Requires:       %{_sbindir}/usermod
Requires:       /bin/cat
Requires:       /bin/chgrp
Requires:       /bin/chmod
Requires:       /bin/chown
Requires:       /bin/cp
Requires:       /bin/dd
Requires:       /bin/df
Requires:       /bin/echo
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
Requires:       /sbin/shutdown
Requires:       Mesa
Requires:       cpio
Requires:       grep
Requires:       gzip
Requires:       lsb-release
Requires:       pax
Requires:       perl-base >= 5.8.8
Requires:       python >= 2.7.3
Obsoletes:      lsb-desktop
Obsoletes:      lsb-runtime
Provides:       lsb = 2.0
Provides:       lsb-core-noarch = 2.0
Provides:       lsb-core-noarch = 3.2
Provides:       lsb-core-noarch = 4.0
Provides:       lsb-graphics-noarch = 2.0
Provides:       lsb-graphics-noarch = 3.2
Provides:       lsb-graphics-noarch = 4.0
%ifarch %{ix86}
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
%ifarch %{ix86}
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

%description
Necessary files and dependencies for the Linux Standard Base (LSB)
Core.

%prep

%build

%install
mkdir -p %{buildroot}/%{_lib}
mkdir -p %{buildroot}%{_sysconfdir}/lsb-release.d
echo -n "LSB_VERSION=\"core-2.0-noarch:core-3.2-noarch:core-4.0-noarch:" > %{buildroot}%{_sysconfdir}/lsb-release
%ifarch %{ix86}
echo -n "core-2.0-ia32:core-3.2-ia32:core-4.0-ia32" >>  %{buildroot}%{_sysconfdir}/lsb-release
%else
echo -n "core-2.0-%{_target_cpu}:core-3.2-%{_target_cpu}:core-4.0-%{_target_cpu}" >>  %{buildroot}%{_sysconfdir}/lsb-release
%endif
echo "\"" >> %{buildroot}%{_sysconfdir}/lsb-release
%ifarch x86_64
mkdir -p %{buildroot}/lib
ln -sf /lib64/ld-linux-x86-64.so.2 %{buildroot}/lib64/ld-lsb-x86-64.so.2
ln -sf /lib64/ld-linux-x86-64.so.2 %{buildroot}/lib64/ld-lsb-x86-64.so.3
%endif
%ifarch %{ix86} x86_64
ln -sf /lib/ld-linux.so.2 %{buildroot}/lib/ld-lsb.so.2
ln -sf /lib/ld-linux.so.2 %{buildroot}/lib/ld-lsb.so.3
%endif
%ifarch ppc64
mkdir -p %{buildroot}/lib
ln -s /lib64/ld64.so.1 %{buildroot}/lib64/ld-lsb-ppc64.so.2
ln -s /lib64/ld64.so.1 %{buildroot}/lib64/ld-lsb-ppc64.so.3
%endif
%ifarch ppc ppc64
ln -s /lib/ld.so.1            %{buildroot}/lib/ld-lsb-ppc32.so.2
ln -s /lib/ld.so.1            %{buildroot}/lib/ld-lsb-ppc32.so.3
%endif
%ifarch ia64
ln -s /lib/ld-linux-ia64.so.2 %{buildroot}/lib/ld-lsb-ia64.so.2
ln -s /lib/ld-linux-ia64.so.2 %{buildroot}/lib/ld-lsb-ia64.so.3
%endif
%ifarch s390x
mkdir -p %{buildroot}/lib
ln -sf /lib64/ld64.so.1         %{buildroot}/lib64/ld-lsb-s390x.so.2
ln -sf /lib64/ld64.so.1         %{buildroot}/lib64/ld-lsb-s390x.so.3
%endif
%ifarch s390
ln -sf /lib/ld.so.1	      %{buildroot}/lib/ld-lsb-s390.so.2
ln -sf /lib/ld.so.1           %{buildroot}/lib/ld-lsb-s390.so.3
%endif
%ifarch sparc
ln -sf /lib/ld-linux.so.2      %{buildroot}/lib/ld-lsb-sparc.so.2
ln -sf /lib/ld-linux.so.2      %{buildroot}/lib/ld-lsb-sparc.so.3
%endif
# These platforms do not have a LSB, just add something to make it compile
%ifarch axp mips
ln -sf /lib/ld-linux.so.2      %{buildroot}/lib/ld-lsb-%{_target_cpu}.so.2
ln -sf /lib/ld-linux.so.2      %{buildroot}/lib/ld-lsb-%{_target_cpu}.so.3
%endif
mkdir -p %{buildroot}%{_sysconfdir}/lsb-release.d
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-2.0-noarch
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-3.2-noarch
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-%{version}-noarch
touch %{buildroot}%{_sysconfdir}/lsb-release.d/desktop-%{version}-noarch
%ifarch %{ix86}
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-2.0-ia32
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-3.2-ia32
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-%{version}-ia32
touch %{buildroot}%{_sysconfdir}/lsb-release.d/desktop-%{version}-ia32
%else
%ifarch x86_64
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-2.0-amd64
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-3.2-amd64
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-%{version}-amd64
touch %{buildroot}%{_sysconfdir}/lsb-release.d/desktop-%{version}-amd64
%else
%ifarch s390x
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-2.0-s390
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-3.2-s390
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-%{version}-s390
touch %{buildroot}%{_sysconfdir}/lsb-release.d/desktop-%{version}-s390
%endif
%ifarch ppc64 ppc
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-2.0-ppc32
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-3.2-ppc32
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-%{version}-ppc32
touch %{buildroot}%{_sysconfdir}/lsb-release.d/desktop-%{version}-ppc32
%ifarch ppc64
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-2.0-ppc64
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-3.2-ppc64
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-%{version}-ppc64
touch %{buildroot}%{_sysconfdir}/lsb-release.d/desktop-%{version}-ppc64
%endif
%else
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-2.0-%{_target_cpu}
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-3.2-%{_target_cpu}
touch %{buildroot}%{_sysconfdir}/lsb-release.d/graphics-%{version}-%{_target_cpu}
touch %{buildroot}%{_sysconfdir}/lsb-release.d/desktop-%{version}-%{_target_cpu}
%endif
%endif
%endif

%files
%dir %{_sysconfdir}/lsb-release.d
%{_sysconfdir}/lsb-release.d/*
%{_sysconfdir}/lsb-release
%ifarch %{ix86} x86_64
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
