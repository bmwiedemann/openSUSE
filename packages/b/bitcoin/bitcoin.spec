#
# spec file for package bitcoin
#
# Copyright (c) 2024 SUSE LLC
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
%define consensus 1
%define is_base 1
Name:           bitcoin
Version:        27.1
Release:        0
Summary:        P2P Digital Currency
License:        MIT
URL:            https://%{name}.org
Source0:        %{name}-%{version}.tar.gz
Source1:        %{base}d.service
Source3:        %{base}d.conf
Source4:        %{base}.conf
Patch0:         harden_bitcoind.service.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  java-devel
BuildRequires:  lcov
BuildRequires:  libboost_filesystem-devel >= 1.73.0
BuildRequires:  libboost_program_options-devel >= 1.73.0
BuildRequires:  libboost_system-devel >= 1.73.0
BuildRequires:  libboost_test-devel >= 1.73.0
BuildRequires:  libboost_thread-devel >= 1.73.0
BuildRequires:  libdb-4_8-devel
BuildRequires:  libminiupnpc-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sqlite3)

%description
%{name_pretty} is a peer-to-peer electronic cash system
that is completely decentralized, without the need for a central server or
trusted parties. Users hold the crypto keys to their own money and
transact directly with each other, with the help of a P2P network to check
for double-spending.

Full transaction history is stored locally at each client. This requires
several GB of space, slowly growing.

%package qt5
Summary:        An end-user Qt5 GUI for the %{name_pretty} crypto-currency
Requires(post): update-desktop-files
Requires(postun): update-desktop-files

%description qt5
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

This package provides automated tests for %{name}-qt5 and %{name}d.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
  --with-asm=auto \
  --with-cli=yes \
  --with-daemon=yes \
  --with-gui=qt5 \
  --with-miniupnpc \
  --with-qrencode \
  --with-sqlite=yes \
  --enable-lto \
%if %{consensus} == 0
  --without-libs \
%endif
  --disable-hardening
%make_build

%check
%make_build LC_ALL=C.UTF-8 check

%install
%make_install

install -Dpm 0644 doc/man/%{name}d.1 %{buildroot}%{_mandir}/man1/%{name}d.1
install -Dpm 0644 doc/man/%{name}-qt.1 %{buildroot}%{_mandir}/man1/%{name}-qt.1

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

# install desktop file
install -Dm 0644 share/pixmaps/bitcoin256.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%suse_update_desktop_file -c %{name}-qt %{name_pretty} "%{name_pretty} Wallet" %{name}-qt %{name} Office Finance

%if %{consensus} == 1
# do not ship these
rm -f %{buildroot}%{_libdir}/lib%{name}consensus.a
rm -f %{buildroot}%{_libdir}/lib%{name}consensus.la
%endif

%post qt5
%desktop_database_post

%postun qt5
%desktop_database_postun

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

%files qt5
%license COPYING
%doc doc/README.md doc/release-notes.md
%{_bindir}/%{name}-qt
%{_datadir}/applications/%{name}-qt.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}-qt.1%{?ext_man}

%files utils
%license COPYING
%doc doc/README.md doc/release-notes.md
%{_bindir}/%{name}-cli
%{_bindir}/%{name}-tx
%{_bindir}/%{name}-wallet
%{_bindir}/%{name}-util
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
%{_bindir}/test_%{name}
%{_bindir}/test_%{name}-qt
%{_bindir}/bench_%{name}

%changelog
