#
# spec file for package aaa_base
#
# Copyright (c) 2025 SUSE LLC
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

%if 0%{?_build_in_place}
%define git_version %(git log '-n1' '--date=format:%Y%m%d' '--no-show-signature' "--pretty=format:+git%cd.%h")
BuildRequires:  git-core
%else
# this is required for obs' source validator. It's
# 20-files-present-and-referenced ignores all conditionals. So the
# definition of git_version actually happens always.
%define git_version %{nil}
%endif

Name:           aaa_base
Version:        84.87+git20250410.71df276%{git_version}
Release:        0
Summary:        openSUSE Base Package
License:        GPL-2.0-or-later
Group:          System/Fhs
URL:            https://github.com/openSUSE/aaa_base
Source:         aaa_base-%{version}.tar
Source1:        README.packaging.txt
Source99:       aaa_base-rpmlintrc
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
# required for nsswitch.conf usrfiles fixes in post script
Requires(post): (glibc >= 2.30 if glibc)
Requires(post): fillup
Recommends:     aaa_base-extras
Recommends:     iproute2
Recommends:     iputils
Recommends:     logrotate
Recommends:     netcfg
Recommends:     udev
# do not require systemd - aaa_base is in the build environment and we don't
# want to pull in tons of dependencies
Conflicts:      sysvinit-init

# run osc service mr to recreate

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
strictly required to run a system. (bash completions and convenience hacks).

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

%package yama-enable-ptrace
Summary:        sysctl setting to allow ptrace with the YAMA LSM enabled
Group:          System/Fhs
Requires:       %{name} = %{version}

%description yama-enable-ptrace
When the YAMA LSM is enabled, ptrace is restriced by default. On
developer systems this has an impact on e.g. strace and gdb. So
this package contains a setting that allows ptrace again.

See https://docs.kernel.org/admin-guide/LSM/Yama.html

%prep
%autosetup -p1

%build
%make_build CFLAGS="%{optflags}" CC="%{__cc}"

%install
%make_install
mkdir -p %{buildroot}/etc/sysctl.d
#
# make sure it does not creep in again
test -d %{buildroot}/root/.gnupg && exit 1
# TODO: get rid of that at some point in the future
mkdir -p %{buildroot}/etc/init.d
for i in boot.local after.local ; do
  install -m 755 /dev/null %{buildroot}/etc/init.d/$i
done
# keep as ghost for migration
touch %buildroot/etc/inittab

# Backup directories
install -d -m 755 %{buildroot}/var/adm/backup/rpmdb %{buildroot}/var/adm/backup/sysconfig

mkdir -p %{buildroot}%{_fillupdir}
%if "%{_fillupdir}" != "/var/adm/fillup-templates"
  for f in %{buildroot}/var/adm/fillup-templates/* ; do
    test -e "$f" || continue
    mv "$f" "%{buildroot}/%{_fillupdir}/"
  done
  rm -vrf %{buildroot}/var/adm/fillup-templates
%endif
%if "%{_fillupdir}" != "/usr/share/fillup-templates"
  for f in %{buildroot}/usr/share/fillup-templates/* ; do
    test -e "$f" || continue
    mv "$f" "%{buildroot}/%{_fillupdir}/"
  done
  rm -vrf %{buildroot}/usr/share/fillup-templates
%endif

%pre
%service_add_pre soft-reboot-cleanup.service

%preun
%service_del_preun soft-reboot-cleanup.service

%post
export LC_ALL=C

#XXX Fix /etc/nsswitch.conf to include usrfiles [bsc#1162916]
if [ -e /etc/nsswitch.conf ]; then
    for key in services protocols rpc ; do
	if ! grep -q "^${key}.*usrfiles" /etc/nsswitch.conf ; then
	    cp /etc/nsswitch.conf "/etc/nsswitch.conf.pre-usrfiles.${key}"
	    sed -i -e "s|^\(${key}:.*[[:space:]]\)files\([[:space:]].*\)*\$|\1files usrfiles\2|" /etc/nsswitch.conf
	fi
    done
fi

%{fillup_only -n language}
%{fillup_only -n proxy}
%service_add_post soft-reboot-cleanup.service

%postun
%service_del_postun_without_restart soft-reboot-cleanup.service

%pre extras
%service_add_pre backup-rpmdb.service backup-rpmdb.timer backup-sysconfig.service backup-sysconfig.timer check-battery.service check-battery.timer setup-systemd-proxy-env.path setup-systemd-proxy-env.service

%post extras
%fillup_only -n backup
%service_add_post backup-rpmdb.service backup-rpmdb.timer backup-sysconfig.service backup-sysconfig.timer check-battery.service check-battery.timer setup-systemd-proxy-env.path setup-systemd-proxy-env.service

%preun extras
%service_del_preun backup-rpmdb.service backup-rpmdb.timer backup-sysconfig.service backup-sysconfig.timer check-battery.service check-battery.timer setup-systemd-proxy-env.path setup-systemd-proxy-env.service

%postun extras
%service_del_postun backup-rpmdb.service backup-rpmdb.timer backup-sysconfig.service backup-sysconfig.timer check-battery.service check-battery.timer setup-systemd-proxy-env.path setup-systemd-proxy-env.service

%post yama-enable-ptrace
# check if yama is active
if [ -f /proc/sys/kernel/yama/ptrace_scope ]; then
  # automatically disable ptrace protection upon install if systemd is not
  # available. Usually system will automatically apply the setting
  if ! type -p systemd-notify > /dev/null || ! systemd-notify --booted; then
    # don't do it on transactional systems to avoid altering the state of the
    # system before reboot
    if [ -z "${TRANSACTIONAL_UPDATE}" ]; then
      # can't use sysctl since that would cause us to require procps, which is
      # bad for container size
      echo 0 > /proc/sys/kernel/yama/ptrace_scope || :
    fi
  fi
fi

%files
%license COPYING
%ghost %config(noreplace) /etc/sysctl.conf
%config /etc/bash.bashrc
%config /etc/csh.cshrc
%config /etc/csh.login
%config /etc/inputrc
%config /etc/mime.types
%config /etc/profile
/usr/etc/DIR_COLORS
/usr/etc/csh.cshrc
/usr/etc/csh.login
/usr/etc/bash.bashrc
/usr/etc/profile
/usr/etc/inputrc
/usr/etc/inputrc.keys
/usr/etc/profile.d/alljava.csh
/usr/etc/profile.d/alljava.sh
/usr/etc/profile.d/lang.csh
/usr/etc/profile.d/lang.sh
/usr/etc/profile.d/profile.csh
/usr/etc/profile.d/profile.sh
/usr/etc/profile.d/xdg-environment.csh
/usr/etc/profile.d/xdg-environment.sh
/usr/etc/profile.d/alias.ash
/usr/etc/profile.d/alias.bash
/usr/etc/profile.d/alias.tcsh
/usr/etc/profile.d/ls.tcsh
/usr/etc/profile.d/ls.bash
/usr/etc/profile.d/ls.zsh
/usr/etc/profile.d/terminal.sh
/usr/etc/profile.d/terminal.csh
%dir /usr/lib/environment.d
/usr/lib/environment.d/50-xdg.conf
/usr/lib/systemd/system/soft-reboot-cleanup.service
/usr/libexec/soft-reboot-cleanup
%{_tmpfilesdir}/soft-reboot-cleanup.conf
%config /etc/shells
%ghost %dir /etc/init.d
%ghost %config(noreplace) /etc/init.d/boot.local
%ghost %config(noreplace) /etc/init.d/after.local
%ghost %config /etc/inittab
/usr/bin/get_kernel_version
/usr/sbin/service
/usr/sbin/smart_agetty
/usr/bin/filesize
/usr/bin/old
/usr/bin/rpmlocate
/usr/sbin/sysconf_addword
/usr/share/man/man1/smart_agetty.1*
/usr/share/man/man8/service.8*
/usr/lib/sysctl.d/50-default.conf
%ifnarch %ix86 %arm
/usr/lib/sysctl.d/50-pid-max.conf
%endif
/usr/lib/sysctl.d/51-network.conf
%{_fillupdir}/sysconfig.language
%{_fillupdir}/sysconfig.proxy

%files extras
/usr/bin/setup-systemd-proxy-env
/usr/etc/skel/.emacs
/usr/etc/skel/.inputrc
%dir /usr/lib/base-scripts
/usr/lib/base-scripts/backup-rpmdb
/usr/lib/base-scripts/backup-sysconfig
/usr/lib/base-scripts/check-battery
/usr/lib/systemd/system/[bc]*
/usr/lib/systemd/system/setup-systemd-proxy-env.*
/var/adm/backup/rpmdb
/var/adm/backup/sysconfig
%{_fillupdir}/sysconfig.backup

%files malloccheck
/usr/etc/profile.d/malloc-debug.sh
/usr/etc/profile.d/malloc-debug.csh

%files wsl
/usr/etc/profile.d/wsl.csh
/usr/etc/profile.d/wsl.sh

%files yama-enable-ptrace
/usr/lib/sysctl.d/52-yama.conf

%changelog
