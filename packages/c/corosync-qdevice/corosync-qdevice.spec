#
# spec file for package corosync-qdevice
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT license). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# Conditionals
# Invoke "rpmbuild --without <feature>" or "rpmbuild --with <feature>"
# to disable or enable specific features

%bcond_without runautogen
%bcond_without systemd

%global gitver %{?numcomm:.%{numcomm}}%{?alphatag:.%{alphatag}}%{?dirty:.%{dirty}}
%global gittarver %{?numcomm:.%{numcomm}}%{?alphatag:-%{alphatag}}%{?dirty:-%{dirty}}
%define _unpackaged_files_terminate_build 0

Name:    corosync-qdevice
Summary: The Corosync Cluster Engine Qdevice
Version: 3.0.3
Release: 0%{?gitver}%{?dist}
License: BSD-3-Clause
URL:     https://github.com/corosync/corosync-qdevice
Source0: https://github.com/corosync/corosync-qdevice/releases/download/v%{version}%{?gittarver}/%{name}-%{version}%{?gittarver}.tar.gz

# Runtime bits
Requires: corosync > 2.4.6
Requires: corosync-libs > 2.4.6
Requires: mozilla-nss-tools

%if %{with systemd}
BuildRequires: pkgconfig(systemd)
BuildRequires:  systemd-devel
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%else
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
%endif

# Build bits
BuildRequires: gcc
BuildRequires: corosync-devel > 2.4.6
BuildRequires: libqb-devel
BuildRequires: sed

%if 0%{?suse_version}
BuildRequires: groff-full
%else
BuildRequires: groff
%endif

%if 0%{?suse_version}
BuildRequires: mozilla-nss-devel
%else
BuildRequires: nss-devel
%endif

%if %{with runautogen}
BuildRequires: autoconf automake libtool
%endif

%prep
%setup -q -n %{name}-%{version}%{?gittarver}

echo %{version} > .tarball-version
echo %{version} > .version

%build
%if %{with runautogen}
./autogen.sh
%endif

%{configure} \
%if %{with systemd}
	--enable-systemd \
%endif
	--enable-qdevices \
	--enable-qnetd \
	--with-initddir=%{_initrddir} \
	--with-systemddir=%{_unitdir} \
	--docdir=%{_docdir}

make %{_smp_mflags}

%install

%make_install
%if %{with systemd}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rccorosync-qnetd
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rccorosync-qdevice
%endif

## tree fixup
# drop docs and html docs for now
rm -rf %{buildroot}%{_docdir}/*
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p  %{buildroot}%{_fillupdir}/
# /etc/sysconfig/corosync-qdevice
install -p -m 644 init/corosync-qdevice.sysconfig.example \
   %{buildroot}%{_fillupdir}/sysconfig.corosync-qdevice
# /etc/sysconfig/corosync-qnetd
install -p -m 644 init/corosync-qnetd.sysconfig.example \
   %{buildroot}%{_fillupdir}/sysconfig.corosync-qnetd

%if %{with systemd}
sed -i -e 's/^#User=/User=/' \
   %{buildroot}%{_unitdir}/corosync-qnetd.service
%else
sed -i -e 's/^COROSYNC_QNETD_RUNAS=""$/COROSYNC_QNETD_RUNAS="coroqnetd"/' \
   %{buildroot}%{_sysconfdir}/sysconfig/corosync-qnetd
%endif

%description
This package contains the Corosync Cluster Engine Qdevice, script for creating
NSS certificates and an init script.

%pre -n corosync-qdevice
%service_add_pre corosync-qdevice.service

%post -n corosync-qdevice
%{fillup_and_insserv -n corosync-qdevice}
%if %{sles_version} > 0
ln -s /run/corosync-qdevice /var/run/
%endif
%service_add_post corosync-qdevice.service

%preun -n corosync-qdevice
%service_del_preun corosync-qdevice.service

%if %{sles_version}
unlink /var/run/corosync-qdevice
%endif

%postun -n corosync-qdevice
if [ -f /etc/sysconfig/corosync-qdevice ]; then
    rm /etc/sysconfig/corosync-qdevice
fi
%service_del_postun corosync-qdevice.service

%files
%defattr(-,root,root,-)
%dir %{_sysconfdir}/corosync/qdevice
%dir %config(noreplace) %{_sysconfdir}/corosync/qdevice/net
#change corosync-qdevice to /run as /var/run is symlink nowdays
%ghost /run/corosync-qdevice
%{_sbindir}/corosync-qdevice
%{_sbindir}/corosync-qdevice-net-certutil
%{_sbindir}/corosync-qdevice-tool
%config(noreplace) %{_fillupdir}/sysconfig.corosync-qdevice
%if %{with systemd}
%{_unitdir}/corosync-qdevice.service
%{_sbindir}/rccorosync-qdevice
%dir %{_sysconfdir}/corosync
%else
%{_initrddir}/corosync-qdevice
%endif
%{_mandir}/man8/corosync-qdevice-tool.8*
%{_mandir}/man8/corosync-qdevice-net-certutil.8*
%{_mandir}/man8/corosync-qdevice.8*

%package -n corosync-qnetd
Summary: The Corosync Cluster Engine Qdevice Network Daemon
Group:          System/Base
Requires: mozilla-nss-tools
Requires(pre): shadow
Requires(pre):  /usr/sbin/useradd
Provides:       group(coroqnetd)
Provides:       user(coroqnetd)

%if %{with systemd}
%{?systemd_requires}
%endif

%description -n corosync-qnetd
This package contains the Corosync Cluster Engine Qdevice Network Daemon,
script for creating NSS certificates and an init script.

%pre -n corosync-qnetd
getent group coroqnetd >/dev/null || groupadd -r coroqnetd -g 701
getent passwd coroqnetd >/dev/null || useradd -r -g coroqnetd -u 701 -s /sbin/nologin -c "User for corosync-qnetd" coroqnetd

%service_add_pre corosync-qnetd.service

exit 0

%post -n corosync-qnetd
%if %{sles_version} > 0
ln -s /run/corosync-qnetd /var/run/
%endif
%{fillup_and_insserv -n corosync-qnetd}

%service_add_post corosync-qnetd.service

%preun -n corosync-qnetd
%service_del_preun corosync-qnetd.service

%if %{sles_version} > 0
unlink /var/run/corosync-qnetd
%endif

%postun -n corosync-qnetd
if [ -f /etc/sysconfig/corosync-qnetd ];then
    rm /etc/sysconfig/corosync-qnetd
fi
%service_del_postun corosync-qnetd.service

%files -n corosync-qnetd
%defattr(-,root,root,-)
%license LICENSE
%dir %config(noreplace) %attr(770, coroqnetd, coroqnetd) %{_sysconfdir}/corosync/qnetd
#change corosync-qnetd to /run as /var/run is just symlink nowadays
%ghost %attr (750, coroqnetd, coroqnetd) /run/corosync-qnetd
%{_bindir}/corosync-qnetd
%{_bindir}/corosync-qnetd-certutil
%{_bindir}/corosync-qnetd-tool
%config(noreplace) %{_fillupdir}/sysconfig.corosync-qnetd
%if %{with systemd}
%{_unitdir}/corosync-qnetd.service
%{_sbindir}/rccorosync-qnetd
%else
%{_initrddir}/corosync-qnetd
%endif
%{_mandir}/man8/corosync-qnetd-tool.8*
%{_mandir}/man8/corosync-qnetd-certutil.8*
%{_mandir}/man8/corosync-qnetd.8*

%changelog
