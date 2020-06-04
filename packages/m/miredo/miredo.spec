#
# spec file for package miredo
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


Name:           miredo
Version:        1.2.6
Release:        0
Summary:        IPv6-over-UDP tunnel implementation
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            http://www.remlab.net/miredo/
Source0:        http://www.remlab.net/files/miredo/miredo-%{version}.tar.xz
Source4:        miredo-client.service
Source5:        miredo-server.service
Patch0:         reread-resolv-before-resolv-ipv4.patch
## PATCH-FIX-UPSTREAM marguerite@opensuse.org -- remove __DATE__ from main.c
Patch1:         miredo-no-build-date.patch
BuildRequires:  judy-devel
BuildRequires:  libcap-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz

%description
Miredo is an implementation of the "Teredo: Tunneling IPv6 over UDP
through NATs" proposed Internet standard (RFC4380). It can serve
either as a Teredo client, a stand-alone Teredo relay, or a Teredo
server, please install the miredo-server or miredo-client appropriately.
It is meant to provide IPv6 connectivity to hosts behind NAT
devices, most of which do not support IPv6, and not even
IPv6-over-IPv4 (including 6to4).

%package -n libteredo5
Summary:        Teredo implementation library used by miredo
Group:          System/Libraries

%description -n libteredo5
Miredo is an implementation of the "Teredo: Tunneling IPv6 over UDP
through NATs" proposed Internet standard (RFC4380).
This package contains a Teredo implementation.

%package -n libtun6-0
Summary:        Linux tunnel configuration library used by miredo
Group:          System/Libraries

%description -n libtun6-0
Miredo is an implementation of the "Teredo: Tunneling IPv6 over UDP
through NATs" proposed Internet standard (RFC4380).
This package contains a library that takes care of configuring
Linux tunnel interfaces.

%package common
Summary:        Runtime libraries for %{name}
Group:          System/Libraries
Requires(pre):  shadow
Obsoletes:      miredo-libs
Provides:       miredo-libs

%description common
Miredo is an implementation of the "Teredo: Tunneling IPv6 over UDP
through NATs" proposed Internet standard (RFC4380). It can serve
either as a Teredo client, a stand-alone Teredo relay, or a Teredo
server, please install the miredo-server or miredo-client appropriately.
It is meant to provide IPv6 connectivity to hosts behind NAT
devices, most of which do not support IPv6, and not even
IPv6-over-IPv4 (including 6to4).
This common package provides the files necessary for both server and client.

%package devel
Summary:        Header files, libraries and development documentation for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}-common = %{version}

%description devel
This package contains the header files, development libraries and development
documentation for %{name}. If you would like to develop programs using %{name},
you will need to install %{name}-devel.

%package server
Summary:        Tunneling server for IPv6 over UDP through NATs
Group:          Productivity/Networking/System
Requires:       %{name}-common = %{version}
%{?systemd_requires}

%description server
Miredo is an implementation of the "Teredo: Tunneling IPv6 over UDP
through NATs" proposed Internet standard (RFC4380). This offers the server
part of miredo. Most people will need only the client part.

%package client
Summary:        Tunneling client for IPv6 over UDP through NATs
Group:          Productivity/Networking/System
Requires:       %{name}-common = %{version}
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
%{?systemd_requires}

%description client
Miredo is an implementation of the "Teredo: Tunneling IPv6 over UDP
through NATs" proposed Internet standard (RFC4380). This offers the client
part of miredo. Most people only need the client part.

%prep
%autosetup -p1
## non exec for config
sed -i "1d" misc/miredo.conf-in

%build
# fix /usr/lib/miredo/miredo-privproc
%configure --libexecdir=%{_libdir} \
	   --disable-static \
           --disable-rpath \
	   --enable-miredo-user

## rpath does not really work
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
%make_install

# locale
%find_lang %{name}

rm -rf %{buildroot}%{_libdir}/systemd
install -D -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/miredo-client.service
install -D -m 644 %{SOURCE5} %{buildroot}%{_unitdir}/miredo-server.service

# clean
find %{buildroot} -type f -name "*.la" -delete -print

# config
touch %{buildroot}%{_sysconfdir}/miredo/miredo-server.conf

# documentation
mkdir -p %{buildroot}/%{_docdir}
mv %{buildroot}%{_datadir}/doc/miredo %{buildroot}/%{_docdir}/

%pre common
getent group miredo >/dev/null || groupadd -r miredo
getent passwd miredo >/dev/null || useradd -r -g miredo -d %{_sysconfdir}/miredo \
         -s /sbin/nologin -c "Miredo Daemon" miredo

%post   -n libteredo5 -p /sbin/ldconfig
%postun -n libteredo5 -p /sbin/ldconfig
%post   -n libtun6-0 -p /sbin/ldconfig
%postun -n libtun6-0 -p /sbin/ldconfig

%pre client
%service_add_pre miredo-client.service

%post client
%service_add_post miredo-client.service

%preun client
%service_del_preun miredo-client.service

%postun client
%service_del_postun miredo-client.service

%pre server
%service_add_pre miredo-server.service

%post server
%service_add_post miredo-server.service

%preun server
%service_del_preun miredo-server.service

%postun server
%service_del_postun miredo-server.service

%files -n libteredo5
%{_libdir}/libteredo.so.*

%files -n libtun6-0
%{_libdir}/libtun6.so.*

%files common -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%dir %{_sysconfdir}/miredo
%{_libdir}/miredo/

%files devel
%{_includedir}/libteredo/
%{_includedir}/libtun6/
%{_libdir}/libteredo.so
%{_libdir}/libtun6.so

%files server
%ghost %config(noreplace,missingok) %{_sysconfdir}/miredo/miredo-server.conf
%{_bindir}/teredo-mire
%{_sbindir}/miredo-server
%{_sbindir}/miredo-checkconf
%{_unitdir}/miredo-server.service
%{_mandir}/man1/teredo-mire*
%{_mandir}/man?/miredo-server*
%{_mandir}/man?/miredo-checkconf*

%files client
%config(noreplace) %{_sysconfdir}/miredo/miredo.conf
%config(noreplace) %{_sysconfdir}/miredo/client-hook
%{_sbindir}/miredo
%{_unitdir}/miredo-client.service
%{_mandir}/man?/miredo.*
%doc %{_docdir}/%{name}

%changelog
