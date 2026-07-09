#
# spec file for package bitcoin
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2011-2014  P Rusnak <prusnak@opensuse.org>
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


# typical altcoin changes: name, name_pretty, consensus 0, is_base 0
%define base bitcoin
%define base_pretty Bitcoin
%define name_pretty %{base_pretty}
%define consensus 0
%define is_base 1
Name:           bitcoin
Version:        31.1
Release:        0
Summary:        P2P Digital Currency
License:        MIT
URL:            https://%{name}.org
Source0:        %{name}-%{version}.tar.gz
Source1:        %{base}d.service
Source2:        %{base}-qt.desktop
Source3:        %{base}d.conf
Source4:        %{base}.conf
Patch0:         harden_bitcoind.service.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel >= 1.74.0
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  qt6-linguist-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(Qt6Core) >= 6.2
BuildRequires:  pkgconfig(Qt6DBus) >= 6.2
BuildRequires:  pkgconfig(Qt6Gui) >= 6.2
BuildRequires:  pkgconfig(Qt6Network) >= 6.2
BuildRequires:  pkgconfig(Qt6Test) >= 6.2
BuildRequires:  pkgconfig(Qt6Widgets) >= 6.2
BuildRequires:  pkgconfig(libevent) >= 2.1.8
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  pkgconfig(sqlite3) >= 3.7.17

%description
%{name_pretty} is a peer-to-peer electronic cash system
that is completely decentralized, without the need for a central server or
trusted parties. Users hold the crypto keys to their own money and
transact directly with each other, with the help of a P2P network to check
for double-spending.

Full transaction history is stored locally at each client. This requires
several GB of space, slowly growing.

%package qt6
Summary:        An end-user Qt6 GUI for the %{name_pretty} crypto-currency
Obsoletes:      %{name}-qt5 < %{version}-%{release}

%description qt6
%{name_pretty} is a peer-to-peer electronic cash system
that is completely decentralized, without the need for a central server or
trusted parties. Users hold the crypto keys to their own money and
transact directly with each other, with the help of a P2P network to check
for double-spending.

Full transaction history is stored locally at each client. This requires
several GB of space, slowly growing.

This package provides %{name_pretty}-Qt, a GUI for %{name_pretty} based on
Qt.

%package utils
Summary:        An end-user CLI for the %{name_pretty} crypto-currency

%description utils
%{name_pretty} is a peer-to-peer electronic cash system
that is completely decentralized, without the need for a central server or
trusted parties. Users hold the crypto keys to their own money and
transact directly with each other, with the help of a P2P network to check
for double-spending.

Full transaction history is stored locally at each client. This requires
several GB of space, slowly growing.

This package provides %{name}-cli — a CLI tool to interact with the daemon.

%if %{consensus} == 1
%package -n lib%{name}consensus0
Summary:        %{name_pretty} consensus library

%description -n lib%{name}consensus0
The purpose of this library is to make the verification functionality that
is critical to %{name_pretty}’s consensus available to other applications,
e.g. to language bindings such as python-%{name}lib or alternative node
implementations.

%package -n lib%{name}consensus-devel
Summary:        Developmont files for %{name} consensus library
Requires:       lib%{name}consensus0 = %{version}-%{release}

%description -n lib%{name}consensus-devel
The purpose of this library is to make the verification functionality that
is critical to %{name_pretty}’s consensus available to other applications,
e.g. to language bindings such as python-%{name}lib or alternative node
implementations.

This package contains development files.
%endif

%package -n %{name}d
Summary:        Headless daemon for %{name_pretty} crypto-currency
Provides:       group(%{name})
Provides:       user(%{name})

%description -n %{name}d
%{name_pretty} is a peer-to-peer electronic cash system
that is completely decentralized, without the need for a central server or
trusted parties. Users hold the crypto keys to their own money and
transact directly with each other, with the help of a P2P network to check
for double-spending.

Full transaction history is stored locally at each client. This requires
several GB of space, slowly growing.

This package provides %{name}d, headless %{name} daemon.

%package test
Summary:        Automated tests for %{name} client

%description test
%{name_pretty} is a peer-to-peer electronic cash system
that is completely decentralized, without the need for a central server or
trusted parties. Users hold the crypto keys to their own money and
transact directly with each other, with the help of a P2P network to check
for double-spending.

Full transaction history is stored locally at each client. This requires
several GB of space, slowly growing.

This package provides automated tests for %{name}-qt6 and %{name}d.

%prep
%autosetup -p1

%build
# upstream switched from autotools to CMake in 29.0
%define __builder ninja
%cmake \
  -DBUILD_GUI=ON \
  -DBUILD_BENCH=ON \
  -DBUILD_TESTS=ON \
  -DWITH_ZMQ=ON \
  -DWITH_QRENCODE=ON \
  -DWITH_DBUS=ON \
  -DENABLE_WALLET=ON \
  -DENABLE_EXTERNAL_SIGNER=ON \
  -DINSTALL_MAN=ON \
  -DENABLE_IPC=OFF \
  -DWITH_CCACHE=OFF
%cmake_build

%check
%ctest

%install
%cmake_install

install -Dpm 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf

%if !%{is_base}
sed -i "s/%{base}/%{name}/g" %{SOURCE1}
sed -i "s/%{base}/%{name}/g" %{SOURCE2}
sed -i "s/%{base}/%{name}/g" %{SOURCE3}

sed -i "s/%{base_pretty}/%{name_pretty}/g" %{SOURCE1}
sed -i "s/%{base_pretty}/%{name_pretty}/g" %{SOURCE2}
sed -i "s/%{base_pretty}/%{name_pretty}/g" %{SOURCE3}
%endif

mkdir -p %{buildroot}/%{_localstatedir}/lib/%{name}

mkdir %{buildroot}%{_sbindir}
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}d
install -Dpm 0644 %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}d.service
install -Dpm 0644 %{SOURCE3} %{buildroot}/%{_tmpfilesdir}/%{name}d.conf

# install icon and desktop file
install -Dm 0644 share/pixmaps/bitcoin256.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dm 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}-qt.desktop

%if %{consensus} == 1
# do not ship these
rm -f %{buildroot}%{_libdir}/lib%{name}consensus.a
rm -f %{buildroot}%{_libdir}/lib%{name}consensus.la
%endif

%if %{consensus} == 1
%post -n lib%{name}consensus0 -p /sbin/ldconfig
%postun -n lib%{name}consensus0  -p /sbin/ldconfig
%endif

%pre -n %{name}d
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || useradd -r -g %{name} -d %{_localstatedir}/lib/%{name} -s /sbin/nologin -c "%{name_pretty} daemon" %{name}
%service_add_pre %{name}d.service

%post -n %{name}d
%service_add_post %{name}d.service
%if 0%{?suse_version} <= 1320
systemd-tmpfiles --create %{_tmpfilesdir}/%{name}d.conf >/dev/null 2>&1 || :
%else
%tmpfiles_create %{_tmpfilesdir}/%{name}d.conf
%endif

%preun -n %{name}d
%service_del_preun %{name}d.service

%postun -n %{name}d
%service_del_postun %{name}d.service

%files qt6
%license COPYING
%doc doc/README.md doc/release-notes.md
%{_bindir}/%{name}-qt
%{_datadir}/applications/%{name}-qt.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}-qt.1%{?ext_man}

%files utils
%license COPYING
%doc doc/README.md doc/release-notes.md
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_bindir}/%{name}-tx
%{_bindir}/%{name}-wallet
%{_bindir}/%{name}-util
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}-cli.1%{?ext_man}
%{_mandir}/man1/%{name}-tx.1%{?ext_man}
%{_mandir}/man1/%{name}-wallet.1%{?ext_man}
%{_mandir}/man1/%{name}-util.1%{?ext_man}

%if %{consensus} == 1
%files -n lib%{name}consensus0
%license COPYING
%doc doc/README.md doc/release-notes.md
%{_libdir}/lib%{name}consensus.so.*

%files -n lib%{name}consensus-devel
%license COPYING
%doc doc/README.md
%{_libdir}/lib%{name}consensus.so
%{_includedir}/%{name}consensus.h
%{_libdir}/pkgconfig/lib%{name}consensus.pc
%endif

%files -n %{name}d
%license COPYING
%doc doc/README.md doc/release-notes.md
%{_mandir}/man1/%{name}d.1%{?ext_man}
%{_bindir}/%{name}d
%dir %attr(700,%{name},%{name}) %{_var}/lib/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{_unitdir}/%{name}d.service
%{_sbindir}/rc%{name}d
%{_tmpfilesdir}/%{name}d.conf

%files test
%license COPYING
%doc doc/README.md doc/release-notes.md
# upstream installs internal (test/bench) binaries to libexec, not bindir
%{_libexecdir}/test_%{name}
%{_libexecdir}/test_%{name}-qt
%{_libexecdir}/bench_%{name}

%changelog
