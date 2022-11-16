#
# spec file for package rkhunter
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2009-2010 by Sascha Manns <saigkill@opensuse.org>
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           rkhunter
Version:        1.4.6
Release:        0
Summary:        A scanner for Rootkits, Backdoors, and Local Exploits
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            http://rkhunter.sourceforge.net/
Source0:        https://sourceforge.net/projects/rkhunter/files/%{name}-%{version}.tar.gz
Source1:        https://sourceforge.net/projects/rkhunter/files/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.sysconfig
Source3:        %{name}.cron
Source5:        %{name}-README.SUSE
Source6:        %{name}.logrotate
Source7:        %{name}.keyring
Source8:        %{name}.timer
Source9:        %{name}.service
# PATCH-FIX-OPENSUSE -- saigkill@opensuse.org - Fix Pathes2
Patch0:         %{name}-installer-fix.patch
# PATCH-FIX-UPSTREAM -- bmwiedemann - boo#968578
Patch1:         rkhunter-grep-fix.patch
BuildRequires:  wget
PreReq:         %fillup_prereq
Requires:       bash
Requires:       findutils
Recommends:     cron
Recommends:     logrotate
Recommends:     netcfg
Recommends:     wget
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Rootkit Hunter scans files and systems for known and unknown rootkits,
backdoors, and sniffers.  The package contains one shell script, a few
text-based databases, and optional Perl modules. This tool scans for
rootkits, backdoors, and local exploits by running tests like:

* Comparing MD5 hashes

* Looking for default files used by rootkits

* Checking for wrong file permissions for binaries

* Looking for suspected strings in LKM and KLD modules

* Looking for hidden files

* Optionally scanning within plain text and binary files

* Checking software versions

* Testing applications

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
sed -e 's/\${MYDIR}\/lib/\%{_prefix}\/share/;' files/rkhunter >files/rkhunter.new
mv files/rkhunter.new files/rkhunter

%install
LIBDIR=%{buildroot}%{_libdir} sh ./installer.sh --layout RPM --install
install -D -m640 %{SOURCE2} %{buildroot}/%{_fillupdir}/sysconfig.%{name}
install -d %{buildroot}/%{_docdir}/%{name}-%{version}
install -m644 %{SOURCE5} %{buildroot}/%{_docdir}/%{name}-%{version}/README.SUSE
install -D -m640 %{SOURCE6} %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}
install -m644 %{SOURCE3} %{buildroot}/%{_docdir}/%{name}-%{version}/%{name}.cron
install -m644 %{SOURCE8} %{buildroot}/%{_docdir}/%{name}-%{version}/%{name}.timer
install -m644 %{SOURCE9} %{buildroot}/%{_docdir}/%{name}-%{version}/%{name}.service
# adapt the default config for using in openSUSE
sed "s|^PREFIX*|PREFIX="%{_prefix}"|g; \
     s|^#SCRIPTDIR=.*|SCRIPTDIR=%{_libdir}/%{name}/scripts|g; \
     s|^#TMPDIR=.*|TMPDIR=%{_var}/lib/rkhunter/tmp|g; \
     s|^#DBDIR=.*|DBDIR=%{_var}/lib/rkhunter/db|g; \
     s|^APPEND_LOG=0|APPEND_LOG=1|g; \
     s|ALLOW_SSH_ROOT_USER=no|ALLOW_SSH_ROOT_USER=yes|g; \
     s|^#PKGMGR=.*|PKGMGR=RPM|g; \
     s|^#OS_VERSION_FILE="/etc/release"|OS_VERSION_FILE="/etc/os-release"|g; \
     s|^#ALLOWHIDDENDIR=%{_sysconfdir}/.java.*|ALLOWHIDDENDIR=%{_sysconfdir}/.java|g; \
     s|^#ALLOWHIDDENDIR=/dev/.udev.*|ALLOWHIDDENDIR=/dev/.udev|g; \
     s|^#ALLOWHIDDENFILE=%{_sysconfdir}/.pwd.lock.*|ALLOWHIDDENFILE=%{_sysconfdir}/.pwd.lock|g; \
     s|^#ALLOWDEVFILE=/dev/shm/pulse-shm-.*|ALLOWDEVFILE=/dev/shm/sysconfig/new-stamp-\*|g" \
     %{buildroot}%{_sysconfdir}/%{name}.conf > %{buildroot}%{_sysconfdir}/%{name}.conf.new
mv %{buildroot}%{_sysconfdir}/%{name}.conf.new %{buildroot}%{_sysconfdir}/%{name}.conf.local
# Create a new config file for settings that don't have to be in main config.
mkdir %{buildroot}%{_sysconfdir}/%{name}.d
chmod 700 %{buildroot}%{_sysconfdir}/%{name}.d
cat >> %{buildroot}%{_sysconfdir}/%{name}.d/00-opensuse.conf <<EOF
# /etc/rkhunter.d/00-opensuse.conf
#
# Additional configuration for openSUSE.
#

# Get ourselves checked.
USER_FILEPROP_FILES_DIRS=/etc/rkhunter.d/00-opensuse.conf

APPEND_LOG=1

ALLOWDEVFILE=/dev/shm/sysconfig/config-lo
ALLOWDEVFILE=/dev/shm/sysconfig/if-lo
ALLOWDEVFILE=/dev/shm/sysconfig/ifup-lo
ALLOWDEVFILE=/dev/shm/sysconfig/network
ALLOWDEVFILE=/dev/shm/sysconfig/new-stamp-2
ALLOWDEVFILE=/dev/shm/sysconfig/ifup-eth[0-9]
ALLOWDEVFILE=/dev/shm/sysconfig/if-eth[0-9]
ALLOWDEVFILE=/dev/shm/sysconfig/config-eth[0-9]

# fix for bnc#826276
ALLOWDEVFILE=/dev/.sysconfig/network/config-lo
ALLOWDEVFILE=/dev/.sysconfig/network/if-lo
ALLOWDEVFILE=/dev/.sysconfig/network/ifup-lo
ALLOWDEVFILE=/dev/.sysconfig/network/network
ALLOWDEVFILE=/dev/.sysconfig/network/new-stamp-2
ALLOWDEVFILE=/dev/.sysconfig/network/ifup-eth[0-9]
ALLOWDEVFILE=/dev/.sysconfig/network/if-eth[0-9]
ALLOWDEVFILE=/dev/.sysconfig/network/config-eth[0-9]
ALLOWDEVFILE=/dev/.sysconfig/network/started

ALLOWDEVFILE=/dev/shm/pulse-shm-*
ALLOWHIDDENFILE=/dev/.blkid.tab
ALLOWHIDDENFILE=/dev/.blkid.tab.old
ALLOWHIDDENFILE=/etc/.updated

# fix for boo#1030378
ALLOWDEVFILE=/dev/shm/CAPI20*
ALLOWDEVFILE=/dev/shm/sem.CAPI20*
# from https://lists.opensuse.org/opensuse-factory/2014-10/msg00044.html
# its a checksum for a binary file
ALLOWHIDDENFILE=/usr/bin/.fipscheck.hmac

# fix for bnc#826276
ALLOWHIDDENDIR=/dev/.sysconfig
EOF

# install ghost file
mkdir -p %{buildroot}%{_localstatedir}/log
touch %{buildroot}%{_localstatedir}/log/%{name}.log

# strip %%#{_libdir}/%%{name}/%%{name}/plugins/*.so

%post
%{fillup_only}

%files
%defattr(644,root,root,755)
%doc %{_mandir}/man8/%{name}.8*
%doc %{_docdir}/%{name}-%{version}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/scripts
%dir %{_var}/lib/%{name}
%dir %{_var}/lib/%{name}/db
%dir %{_var}/lib/%{name}/db/i18n
%dir %{_var}/lib/%{name}/db/signatures
%dir %{_var}/lib/%{name}/tmp
%defattr(640,root,root,-)
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}.conf.local
%dir %{_sysconfdir}/%{name}.d
%config(noreplace) %{_sysconfdir}/%{name}.d/00-opensuse.conf
%verify(not md5 size mtime) %{_var}/lib/%{name}/db/*.dat
%{_var}/lib/%{name}/db/i18n/*
%{_var}/lib/%{name}/db/signatures/*
%config(noreplace) %{_sysconfdir}/logrotate.d/rkhunter
%{_fillupdir}/sysconfig.%{name}
%ghost %verify(not md5 size mtime) %config(noreplace)%{_localstatedir}/log/%{name}.log
%defattr(750,root,root,-)
%{_bindir}/%{name}
%{_libdir}/%{name}/scripts/*.pl
%{_libdir}/%{name}/scripts/*.sh

%changelog
