#
# spec file for package fcgiwrap
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


%if ! %{defined _fillupdir}
%define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%if ! %{defined make_build}
%define make_build make %{?_smp_mflags}
%endif
Name:           fcgiwrap
Version:        1.1.0+18+g99c942c
Release:        0
Summary:        FastCGI wrapper for CGI scripts
License:        MIT
Group:          Productivity/Networking/Web/Servers
URL:            https://github.com/gnosek/fcgiwrap
Source0:        fcgiwrap-%{version}.tar.xz
Patch0:         fix-configure.ac-test-for-libsytemd.patch
Patch1:         adapt-user-and-group-for-nginx.patch
Patch2:         add-environment-variable-for-number-of-workers.patch
Patch3:         Declare-cgi_error-noreturn.patch
Patch4:         support-p-flag-in-sysconfig.patch
Patch5:         fix-kill-parameter-sequence.patch
Patch6:         fix-run-fcgiwrap-script.patch
Patch7:         fcgiwrap.service-depend-on-fcgiwrap.socket.patch
BuildRequires:  FastCGI-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsystemd)
Requires(post): %fillup_prereq
Suggests:       spawn-fcgi
%systemd_requires
%{?systemd_requires}

%description
fcgiwrap is a server for running CGI applications over FastCGI.
It provides CGI support to Nginx (and other web servers
that may need it). Apache and lighthttpd don't need it, as they spawn
FastCGI workers on demand.

%package nginx
Summary:        System services for using fcgiwrap with nginx
Group:          Productivity/Networking/Web/Servers
Requires:       %{name}
# Because of nginx user/group
Requires:       nginx
# fcgiwrap is useful if nginx is to be used with FastCGI scripts
Supplements:    packageand(nginx:%(rpm --qf "%%{name}" -qf $(readlink -f %{_libdir}/libfcgi.so)))

%description nginx
This package provides systemd unit files to run a set of fcgiwrap
processes ready for use with nginx or other web servers.

%prep
%setup -q
%autopatch -p1

%build
autoreconf -v -i
%configure --with-systemd --prefix='' CFLAGS="-I/usr/include/fastcgi"
%make_build

%install
%make_install
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0755 -t %{buildroot}%{_sbindir} systemd/run-fcgiwrap
install -m 0644 -t %{buildroot}%{_unitdir} systemd/fcgiwrap.{socket,service}
install -d %{buildroot}%{_fillupdir}
install -m 644 -t %{buildroot}%{_fillupdir} systemd/sysconfig.fcgiwrap

%pre nginx
%service_add_pre fcgiwrap.socket fcgiwrap.service

%post nginx
%fillup_only
%service_add_post fcgiwrap.socket fcgiwrap.service

%preun nginx
%service_del_preun fcgiwrap.service fcgiwrap.socket

%postun nginx
%service_del_postun fcgiwrap.service
# restarting the socket fails if service is active
if [ -x /usr/bin/systemctl ] && ! systemctl is-active fcgiwrap.service >/dev/null 2>&1; then
    %service_del_postun fcgiwrap.socket
fi

%files
%doc README.rst
%license COPYING
%{_sbindir}/fcgiwrap
%{_mandir}/man8/fcgiwrap.8%{?ext_man}

%files nginx
%{_sbindir}/run-fcgiwrap
%{_unitdir}/*
%{_fillupdir}/sysconfig.fcgiwrap

%changelog
