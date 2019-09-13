#
# spec file for package gssproxy
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


Name:           gssproxy
Version:        0.8.2
Release:        0
Summary:        Daemon for managing gss-api requests
License:        MIT
Group:          Productivity/Networking/System
URL:            https://pagure.io/gssproxy
Source0:        https://releases.pagure.org/gssproxy/%{name}-%{version}.tar.gz
# PATCH-FIX-SUSE tchvatal@suse.com disable test that fails only on OBS builds
Patch0:         0001-Fix-runtests.py.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  doxygen
BuildRequires:  krb5-client
BuildRequires:  krb5-plugin-kdb-ldap
BuildRequires:  libtool
BuildRequires:  openldap2
BuildRequires:  openldap2-client
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  system-user-nobody
BuildRequires:  systemd-rpm-macros
BuildRequires:  valgrind
BuildRequires:  pkgconfig(ini_config) >= 1.2.0
BuildRequires:  pkgconfig(krb5-gssapi) >= 1.12.0
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(nss_wrapper)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(socket_wrapper)
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%if 0%{?suse_version} > 1315
# in earlier versions, libverto is in krb5-devel
BuildRequires:  pkgconfig(libverto) >= 0.2.2
%endif

%description
gssproxy allows the complexity of GSS security negotiation
to be centrallized.  It is particularly useful to keep this out
of kernel space, so that CIPFS, NFS, AFS etc can use GSS-API without
complexity in the kernel.

Using it also improves isolation and privilege separation, so that
HTTP servers, for example, can use GSS-API without needing to access
keys directly.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fvi
%configure
make %{?_smp_mflags}
make -j1 test_proxymech

%install
%make_install
rm -f %{buildroot}%{_libdir}/gssproxy/proxymech.la
ln -s service %{buildroot}%{_sbindir}/rcgssproxy
install -D -m 644 examples/gssproxy.conf %{buildroot}%{_sysconfdir}/gssproxy/gssproxy.conf
install -d -m 700 %{buildroot}%{_localstatedir}/lib/gssproxy/rcache
install -D -m 644 examples/24-nfs-server.conf %{buildroot}%{_sysconfdir}/gssproxy/24-nfs-server.conf

%check
make %{?_smp_mflags} check

%pre
%service_add_pre gssproxy.service

%post
%service_add_post gssproxy.service

%preun
%service_del_preun gssproxy.service

%postun
%service_del_postun gssproxy.service

%files
%license COPYING
%{_sbindir}/gssproxy
%{_sbindir}/rcgssproxy
%dir %{_libdir}/gssproxy
%{_libdir}/gssproxy/proxymech.so
%dir %{_localstatedir}/lib/gssproxy
%dir %{_localstatedir}/lib/gssproxy/rcache
%{_unitdir}/gssproxy.service
%{_mandir}/man5/gssproxy.conf.5%{?ext_man}
%{_mandir}/man8/gssproxy-mech.8%{?ext_man}
%{_mandir}/man8/gssproxy.8%{?ext_man}
%dir %{_sysconfdir}/gssproxy
%config %{_sysconfdir}/gssproxy/gssproxy.conf
%config %{_sysconfdir}/gssproxy/24-nfs-server.conf

%changelog
