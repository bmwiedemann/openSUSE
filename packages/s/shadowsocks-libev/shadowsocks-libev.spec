#
# spec file for package shadowsocks-libev
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%global selinuxtype targeted
%if 0%{?suse_version} >= 1600
%bcond_without selinux
%bcond_without apparmor
%else
%bcond_with selinux
%bcond_without apparmor
%endif

%define libver 2
Name:           shadowsocks-libev
Version:        3.3.6
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
Source13:       %{name}.apparmor
Source14:       %{name}.te
Source15:       %{name}.fc
Source99:       https://github.com/shadowsocks/libbloom/archive/437e1add5a2b9a87797d8c648df7cf5f3ee155a8/libbloom-437e1ad.tar.gz
Source100:      https://github.com/shadowsocks/libcork/archive/074e074b26e9e372e90e6ade215217763c8644aa/libcork-074e074.tar.gz
Source101:      https://github.com/shadowsocks/ipset/archive/3ea7fe30adf4b39b27d932e5a70a2ddce4adb508/ipset-3ea7fe3.tar.gz
# PATCH-FIX-UPSTREAM shadowsocks-libev-gcc13-compat.patch hillwood@opensuse.org - Fix build with gcc 13
Patch0:         shadowsocks-libev-gcc13-compat.patch
BuildRequires:  apparmor-abstractions
BuildRequires:  apparmor-rpm-macros
BuildRequires:  asciidoc
BuildRequires:  checkpolicy
BuildRequires:  checkpolicy
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libapparmor-devel
BuildRequires:  mbedtls-3-devel
BuildRequires:  pkgconfig
BuildRequires:  selinux-policy-devel
BuildRequires:  shadowsocks-common-selinux
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  xmlto
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libev)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libsodium) >= 1.0.4
BuildRequires:  pkgconfig(openssl)
Requires(pre):  shadowsocks-sysuser
Requires(pre):  shadow
Recommends:     shadowsocks-v2ray-plugin
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

%package apparmor
Summary:        Apparmor profile for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Supplements:    (shadowsocks-libev and apparmor-abstractions)

%description apparmor
This package adds the Apparmor profile to %{name}

%package selinux
Summary:        Selinux support for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       selinux-policy-targeted
Requires:       shadowsocks-common-selinux
Supplements:    (shadowsocks-libev and selinux-policy-targeted)

%description selinux
This package adds SELinux enforcement to %{name}.

%package devel
Summary:        Development headers for shadowsocks-libev
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{libver} = %{version}

%description devel
shadowsocks-libev is a lightweight secured SOCKS5 proxy for embedded devices and
low-end boxes.

This package provides development headers for it.

%prep
%autosetup -p1
rmdir libbloom libcork libipset
tar -zxf %{SOURCE99}
tar -zxf %{SOURCE100}
tar -zxf %{SOURCE101}
mv libbloom-437e1add5a2b9a87797d8c648df7cf5f3ee155a8 libbloom
mv libcork-074e074b26e9e372e90e6ade215217763c8644aa libcork
mv ipset-3ea7fe30adf4b39b27d932e5a70a2ddce4adb508 libipset
cp %{SOURCE14} shadowsocks_libev.te
cp %{SOURCE15} shadowsocks_libev.fc

%build
make -f %{_datadir}/selinux/devel/Makefile shadowsocks_libev.pp

%cmake -DWITH_STATIC=OFF
%cmake_build

%install
install -d %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}
install -m 0644 shadowsocks_libev.pp %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/shadowsocks_libev.pp

%cmake_install

find %{buildroot} -type f -name "*.la" -delete -print

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

install -d %{buildroot}%{_sysconfdir}/apparmor.d
install -m 0644 %{SOURCE13} %{buildroot}%{_sysconfdir}/apparmor.d/%{name}

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

%post apparmor
%apparmor_reload %{_sysconfdir}/apparmor.d/%{name}

%preun apparmor
if [ -d %{_sysconfdir}/apparmor.d ] && [ -d /sys/kernel/security/apparmor ]; then
        %apparmor_reload %{_sysconfdir}/apparmor.d/%{name}
fi

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/shadowsocks_libev.pp
%selinux_relabel_post -s %{selinuxtype}

%preun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} shadowsocks_libev
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%ldconfig_scriptlets -n lib%{name}2

%files
%doc Changes README.md AUTHORS
%license COPYING
%attr(750,root,shadowsocks) %dir %{_sysconfdir}/shadowsocks
%attr(640,root,shadowsocks) %config(noreplace) %{_sysconfdir}/shadowsocks/%{name}-config.json
%{_bindir}/ss-local
%{_bindir}/ss-redir
%{_bindir}/ss-server
%{_bindir}/ss-tunnel
%{_bindir}/ss-manager
%{_bindir}/ss-nat
%{_bindir}/ss-setup
%{_mandir}/man8/%{name}.8%{?ext_man}
%{_mandir}/man1/ss-*.1%{?ext_man}
%{_sbindir}/rcshadowsocks-libev-*
%{_unitdir}/%{name}-*.service

%files -n lib%{name}%{libver}
%license COPYING
%{_libdir}/lib%{name}.so.*

%files apparmor
%license COPYING
%config %{_sysconfdir}/apparmor.d/%{name}

%files selinux
%license COPYING
%{_datadir}/selinux/packages/targeted/shadowsocks_libev.pp

%files devel

%files doc
%license COPYING
%dir %{_datadir}/doc/%{name}
%doc %{_datadir}/doc/%{name}/*.html

%files devel
%license COPYING
%{_includedir}/shadowsocks.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so

%changelog
