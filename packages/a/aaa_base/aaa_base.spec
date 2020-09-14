#
# spec file for package aaa_base
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
# icecream 0


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           aaa_base
Version:        84.87+git20200909.ee4a72c
Release:        0
URL:            https://github.com/openSUSE/aaa_base
# do not require systemd - aaa_base is in the build environment and we don't
# want to pull in tons of dependencies
Conflicts:      sysvinit-init
Requires:       /bin/mktemp
Requires:       /usr/bin/cat
Requires:       /usr/bin/date
Requires:       /usr/bin/grep
Requires:       /usr/bin/mv
Requires:       /usr/bin/sed
Requires:       /usr/bin/tput
Requires:       /usr/bin/xz
Requires:       distribution-release
Requires:       filesystem
Recommends:     logrotate netcfg udev iputils iproute2 aaa_base-extras
Requires(pre):  /usr/bin/rm
Requires(pre):  glibc >= 2.30
Requires(post): fillup /usr/bin/chmod /usr/bin/chown

Summary:        openSUSE Base Package
License:        GPL-2.0-or-later
Group:          System/Fhs
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# run osc service dr to recreate
Source:         aaa_base-%{version}.tar.xz
#
# Read README.packaging.txt before making any changes to this
# package
#
Source1:        README.packaging.txt
Source99:       aaa_base-rpmlintrc

%description
This package installs several important configuration files and central scripts.

%package extras
Summary:        SUSE Linux Base Package (recommended part)
Group:          System/Fhs
Requires:       %{name} = %{version}
Requires:       /usr/bin/find
Requires:       cpio
Requires(post): fillup
Provides:       aaa_base:/etc/DIR_COLORS

%description extras
The parts of aaa_base that should be installed by default but are not
strictly required to run a system. (Shell aliases, bash completions
and convenience hacks).

%package malloccheck
Summary:        SUSE Linux Base Package (malloc checking)
Group:          System/Fhs
Requires:       %{name} = %{version}

%description malloccheck
This package sets environment variables that enable stricter
malloc checks to catch potential heap corruptions. It's not
installed by default as it may degrade performance.

%package wsl
Summary:        SUSE Linux Base Package (Windows Subsystem for Linux)
Group:          System/Fhs
Requires:       %{name} = %{version}

%description wsl
This package includes some special settings needed on Windows Subsystem
for Linux. It should only be installed on WSL and not on regular Linux
systems.

%prep
%setup -q
sed -i 's|actiondir="/usr/lib/initscripts/legacy-actions"|actiondir="%{_libexecdir}/initscripts/legacy-actions"|' \
    files/usr/sbin/service

%build
make CFLAGS="$RPM_OPT_FLAGS" CC="%{__cc}" %{?_smp_mflags}
if test -d patches/$RPM_ARCH; then
	pushd files
	for file in ../patches/$RPM_ARCH/*; do
		patch -p0 --input=$file
	done
	find -name "*.orig" | xargs -r rm
	popd
fi

%install
#
make DESTDIR=$RPM_BUILD_ROOT install
#
mkdir -p %{buildroot}/etc/sysctl.d
case "$RPM_ARCH" in
	s390*) ;;
	*) rm -f %{buildroot}/usr/lib/sysctl.d/50-default-s390.conf ;;
esac
#
# make sure it does not creep in again
test -d $RPM_BUILD_ROOT/root/.gnupg && exit 1
mkdir -p $RPM_BUILD_ROOT/etc/init.d
for i in boot.local after.local ; do
  touch $RPM_BUILD_ROOT/etc/init.d/$i
done
#
install -d -m 755 %buildroot%{_libexecdir}/initscripts/legacy-actions
# keep as ghost for migration
touch %buildroot/etc/inittab

# Backup directories
install -d -m 755 %{buildroot}/var/adm/backup/{rpmdb,sysconfig}

mkdir -p %{buildroot}%{_fillupdir}
%if "%{_fillupdir}" != "/var/adm/fillup-templates"
  for f in %{buildroot}/var/adm/fillup-templates/* ; do
    test -e "$f" || continue
    mv $f %{buildroot}%{_fillupdir}/
  done
  rm -vrf %{buildroot}/var/adm/fillup-templates
%endif
%if "%{_fillupdir}" != "/usr/share/fillup-templates"
  for f in %{buildroot}/usr/share/fillup-templates/* ; do
    test -e "$f" || continue
    mv $f %{buildroot}%{_fillupdir}/
  done
  rm -vrf %{buildroot}/usr/share/fillup-templates
%endif

%pre -f aaa_base.pre

%post -f aaa_base.post

%pre extras
%service_add_pre backup-rpmdb.service backup-rpmdb.timer backup-sysconfig.service backup-sysconfig.timer check-battery.service check-battery.timer

%post extras
%fillup_only -n backup
%service_add_post backup-rpmdb.service backup-rpmdb.timer backup-sysconfig.service backup-sysconfig.timer check-battery.service check-battery.timer

%preun extras
%service_del_preun backup-rpmdb.service backup-rpmdb.timer backup-sysconfig.service backup-sysconfig.timer check-battery.service check-battery.timer

%postun extras
%service_del_postun backup-rpmdb.service backup-rpmdb.timer backup-sysconfig.service backup-sysconfig.timer check-battery.service check-battery.timer

%files
%defattr(-,root,root)
%license COPYING
%config(noreplace) /etc/sysctl.conf
%config /etc/bash.bashrc
%config /etc/csh.cshrc
%config /etc/csh.login
%config /etc/inputrc
%config /etc/inputrc.keys
%config /etc/mime.types
%config /etc/profile
%config /etc/profile.d/alljava.csh
%config /etc/profile.d/alljava.sh
%config /etc/profile.d/csh.ssh
%config /etc/profile.d/lang.csh
%config /etc/profile.d/lang.sh
%config /etc/profile.d/profile.csh
%config /etc/profile.d/profile.sh
%config /etc/profile.d/sh.ssh
%config /etc/profile.d/xdg-environment.csh
%config /etc/profile.d/xdg-environment.sh
%config /etc/profile.d/complete.bash
%config /etc/profile.d/alias.ash
/etc/profile.d/alias.bash
/etc/profile.d/alias.tcsh
/etc/profile.d/ls.tcsh
/etc/profile.d/ls.bash
/etc/profile.d/ls.zsh
%config /etc/shells
%config /etc/ttytype
%dir /etc/init.d/
%ghost /etc/init.d/boot.local
%ghost /etc/init.d/after.local
%ghost %config /etc/inittab
# don't forget to also change aaa_base.post, boot.cleanup
# and /etc/permissions!
%ghost %attr(0644,root,root) %verify(not md5 size mtime) /var/log/lastlog
/etc/hushlogins
/usr/bin/get_kernel_version
/sbin/refresh_initrd
/usr/sbin/refresh_initrd
/sbin/service
/usr/sbin/service
/sbin/smart_agetty
/usr/sbin/smart_agetty
/usr/bin/filesize
/usr/bin/old
/usr/bin/rpmlocate
/usr/bin/safe-rm
/usr/bin/safe-rmdir
/usr/lib/restricted/bin/hostname
/usr/sbin/sysconf_addword
/usr/share/man/man1/smart_agetty.1*
/usr/share/man/man5/defaultdomain.5*
/usr/share/man/man8/safe-rm.8*
/usr/share/man/man8/safe-rmdir.8*
/usr/share/man/man8/service.8*
/usr/lib/sysctl.d/*.conf
%dir %{_libexecdir}/initscripts
%dir %{_libexecdir}/initscripts/legacy-actions
%{_fillupdir}/sysconfig.language
%{_fillupdir}/sysconfig.proxy
%{_fillupdir}/sysconfig.windowmanager

%files extras
%defattr(-,root,root)
%config(noreplace) /etc/DIR_COLORS
/etc/skel/.emacs
/etc/skel/.inputrc
%dir /usr/lib/base-scripts
/usr/lib/base-scripts/backup-rpmdb
/usr/lib/base-scripts/backup-sysconfig
/usr/lib/base-scripts/check-battery
/usr/lib/systemd/system/*
/usr/share/man/man8/resolv+.8*
/var/adm/backup/rpmdb
/var/adm/backup/sysconfig
%{_fillupdir}/sysconfig.backup

%files malloccheck
%defattr(-,root,root)
%config /etc/profile.d/malloc-debug.sh
%config /etc/profile.d/malloc-debug.csh

%files wsl
%defattr(-,root,root)
%config /etc/profile.d/wsl.csh
%config /etc/profile.d/wsl.sh

%changelog
