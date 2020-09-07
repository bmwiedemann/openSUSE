#
# spec file for package shadowsocks-libev
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


%define libver 2

Name:           shadowsocks-libev
Version:        3.3.4
Release:        0
Summary:        Libev port of Shadowsocks
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Proxy
URL:            https://github.com/shadowsocks/shadowsocks-libev
Source0:        https://github.com/shadowsocks/shadowsocks-libev/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-config.json
Source2:        %{name}-client.service
Source3:        %{name}-server.service
Source4:        %{name}-tunnel.service
Source5:        %{name}-nat.service
Source6:        %{name}-manager.service
Source7:        %{name}-redir.service
Source8:        %{name}-client@.service
Source9:        %{name}-server@.service
Source10:       %{name}-tunnel@.service
Source11:       %{name}-nat@.service
Source12:       %{name}-redir@.service
BuildRequires:  libtool
BuildRequires:  mbedtls-devel
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libev)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libsodium) >= 1.0.4
BuildRequires:  pkgconfig(openssl)
%if 0%{?fedora} >= 24
BuildRequires:  pkgconfig
%else
BuildRequires:  pkg-config
%endif
%if 0%{?fedora} == 24
BuildRequires:  ghostscript-core
%endif
BuildRequires:  asciidoc
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmlto
BuildRequires:  pkgconfig(systemd)
Recommends:     shadowsocks-v2ray-plugin
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_ordering}

%description
shadowsocks-libev is a lightweight secured SOCKS5 proxy for embedded devices and
low-end boxes.

%package -n lib%{name}%{libver}
Summary:        Libev port of Shadowsocks
Group:          System/Libraries

%description -n lib%{name}%{libver}
shadowsocks-libev is a lightweight secured SOCKS5 proxy for embedded devices and
low-end boxes.

This package provides libraries for it.

%package doc
Summary:        Documents for shadowsocks-libev
Group:          Documentation/HTML
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
shadowsocks-libev is a lightweight secured SOCKS5 proxy for embedded devices and
low-end boxes.

This package provides Documents for it.

%package devel
Summary:        Development headers for shadowsocks-libev
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{libver} = %{version}

%description devel
shadowsocks-libev is a lightweight secured SOCKS5 proxy for embedded devices and
low-end boxes.

This package provides development headers for it.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fcommon"
%configure \
           --enable-shared 

%make_build

%install
%make_install

rm -rf %{buildroot}/%{_libdir}/*.la

install -d %{buildroot}%{_sysconfdir}/shadowsocks/
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/shadowsocks/

install -d %{buildroot}%{_unitdir}
install -m 644 %{SOURCE2} %{buildroot}%{_unitdir}
install -m 644 %{SOURCE3} %{buildroot}%{_unitdir}
install -m 644 %{SOURCE4} %{buildroot}%{_unitdir}
install -m 644 %{SOURCE5} %{buildroot}%{_unitdir}
install -m 644 %{SOURCE6} %{buildroot}%{_unitdir}
install -m 644 %{SOURCE7} %{buildroot}%{_unitdir}
install -m 644 %{SOURCE8} %{buildroot}%{_unitdir}
install -m 644 %{SOURCE9} %{buildroot}%{_unitdir}
install -m 644 %{SOURCE10} %{buildroot}%{_unitdir}
install -m 644 %{SOURCE11} %{buildroot}%{_unitdir}
install -m 644 %{SOURCE12} %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcshadowsocks-libev-client
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcshadowsocks-libev-server
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcshadowsocks-libev-manager
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcshadowsocks-libev-nat
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcshadowsocks-libev-redir
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcshadowsocks-libev-tunnel
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcshadowsocks-libev-client@
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcshadowsocks-libev-server@
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcshadowsocks-libev-nat@
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcshadowsocks-libev-redir@
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcshadowsocks-libev-tunnel@

%pre
%service_add_pre %{name}-server.service
%service_add_pre %{name}-client.service
%service_add_pre %{name}-manager.service 
%service_add_pre %{name}-nat.service 
%service_add_pre %{name}-redir.service
%service_add_pre %{name}-tunnel.service
%service_add_pre %{name}-server@.service
%service_add_pre %{name}-client@.service
%service_add_pre %{name}-nat@.service 
%service_add_pre %{name}-redir@.service
%service_add_pre %{name}-tunnel@.service

%post
%service_add_post %{name}-server.service
%service_add_post %{name}-client.service
%service_add_post %{name}-manager.service
%service_add_post %{name}-nat.service
%service_add_post %{name}-redir.service
%service_add_post %{name}-tunnel.service
%service_add_post %{name}-server@.service
%service_add_post %{name}-client@.service
%service_add_post %{name}-nat@.service
%service_add_post %{name}-redir@.service
%service_add_post %{name}-tunnel@.service

%preun
%service_del_preun %{name}-server.service
%service_del_preun %{name}-client.service
%service_del_preun %{name}-manager.service
%service_del_preun %{name}-nat.service
%service_del_preun %{name}-redir.service
%service_del_preun %{name}-tunnel.service
%service_del_preun %{name}-server@.service
%service_del_preun %{name}-client@.service
%service_del_preun %{name}-nat@.service
%service_del_preun %{name}-redir@.service
%service_del_preun %{name}-tunnel@.service

%postun
%service_del_postun %{name}-server.service 
%service_del_postun %{name}-client.service
%service_del_postun %{name}-manager.service 
%service_del_postun %{name}-nat.service 
%service_del_postun %{name}-redir.service
%service_del_postun %{name}-tunnel.service
%service_del_postun %{name}-server@.service 
%service_del_postun %{name}-client@.service
%service_del_postun %{name}-nat@.service 
%service_del_postun %{name}-redir@.service
%service_del_postun %{name}-tunnel@.service

%post -n lib%{name}2 -p /sbin/ldconfig

%postun -n lib%{name}2 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc Changes README.md AUTHORS
%dir %{_sysconfdir}/shadowsocks
%config(noreplace) %{_sysconfdir}/shadowsocks/%{name}-config.json
%license COPYING
%{_bindir}/ss-local
%{_bindir}/ss-redir
%{_bindir}/ss-server
%{_bindir}/ss-tunnel
%{_bindir}/ss-manager
%{_bindir}/ss-nat
%{_mandir}/man8/%{name}.8.gz
%{_mandir}/man1/ss-*.1.gz
%{_sbindir}/rcshadowsocks-libev-*
%{_unitdir}/%{name}-*.service

%files -n lib%{name}%{libver}
%defattr(-,root,root)
%{_libdir}/lib%{name}.so.*

%files doc
%defattr(-,root,root)
%dir %{_datadir}/doc/%{name}
%doc %{_datadir}/doc/%{name}/*.html

%files devel
%defattr(-,root,root)
%{_includedir}/shadowsocks.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so

%changelog
