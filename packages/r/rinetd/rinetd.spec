#
# spec file for package rinetd
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%if 0%{?suse_version} > 1220
%define with_systemd 1
%else
%define with_systemd 0
%endif

Name:           rinetd
License:        GPL-2.0+
Group:          Productivity/Networking/System
Version:        0.62
Release:        0
Summary:        TCP Redirection Server
Url:            http://www.boutell.com/rinetd/
Source0:        %{name}-%{version}.tar.bz2
Source1:        rc.rinetd
Source2:        logrotate.rinetd
Source3:        rinetd.service
Patch0:         rinetd-doc.patch
Patch1:         rinetd-syslog.patch
Patch2:         rinetd-conf.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{with_systemd}
BuildRequires:  systemd
%{?systemd_requires}
%else
PreReq:         %fillup_prereq %insserv_prereq
%endif

%description
rinetd redirects TCP connections from one IP address and port to
another address and port. rinetd is a single-process server which
handles any number of connections to the address or port pairs
specified in the file /etc/rinetd.conf. Because rinetd runs as a single
process using nonblocking I/O, it is able to redirect a large number of
connections without a severe impact on the machine. This makes it
practical to run TCP services on machines inside an IP masquerading
firewall.

Note: rinetd can not redirect FTP because FTP requires more than one
socket.


%prep
%setup
%patch0
%patch1
%patch2

%build
make CFLAGS="$CFLAGS $RPM_OPT_FLAGS -DLINUX -fno-strict-aliasing"

%install
mkdir -p %{buildroot}/%_mandir/man8
mkdir -p %{buildroot}/%{_sbindir}
%if %{with_systemd}
mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}
%else
mkdir -p %{buildroot}/etc/init.d
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/etc/init.d/rinetd
ln -s ../../etc/init.d/rinetd $RPM_BUILD_ROOT/usr/sbin/rcrinetd
%endif
mkdir -p %{buildroot}/etc/logrotate.d
touch $RPM_BUILD_ROOT/etc/rinetd.conf
install -m 700 rinetd %{buildroot}/usr/sbin
install -m 644 rinetd.8 %{buildroot}%_mandir/man8
install -m 644 %SOURCE2 %{buildroot}/etc/logrotate.d/rinetd

%post
%if %{with_systemd}
%service_add_post %{name}.service
%else
%{fillup_and_insserv rinetd}
%endif

%postun
%if %{with_systemd}
%service_del_postun %{name}.service
%else
%{insserv_cleanup}
%endif

%if %{with_systemd}
%pre 
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service
%endif

%files
%defattr(-, root, root)
%doc CHANGES README index.html rinetd.conf.sample
%config(missingok,noreplace) %ghost /etc/rinetd.conf
%config(noreplace) /etc/logrotate.d/rinetd
%if %{with_systemd}
%{_unitdir}/%{name}.service
%else
%config /etc/init.d/rinetd
%endif
%_mandir/man8/rinetd.8.gz
/usr/sbin/rcrinetd
/usr/sbin/rinetd

%changelog
