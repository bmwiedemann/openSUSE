#
# spec file for package eiskaltdcpp
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


Name:           eiskaltdcpp
Version:        2.3.0~git20200908.0e0ccde5
Release:        0
Summary:        Cross-platform program that uses the Direct Connect and ADC protocol
License:        GPL-3.0-only
URL:            https://github.com/eiskaltdcpp/eiskaltdcpp
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.firewalld
Patch0:         ru.ts.patch
BuildRequires:  aspell-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  libattr-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libidn-devel
BuildRequires:  libminiupnpc-devel
BuildRequires:  lua51-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(bzip2)
Requires:       aspell

%description
EiskaltDC++ is a cross-platform program that uses the Direct Connect and ADC
protocol. It is compatible with other DC clients, such as the original DC from
Neomodus, DC++ and derivatives. EiskaltDC++ also interoperates with all common
DC hub software. The minimum number of our patches to original DC++ kernel
makes it easy to upgrade to new versions and ensures compatibility with other
clients.

%package qt
Summary:        Qt frontend for %{name}

%description qt
EiskaltDC++ is a cross-platform program that uses the Direct Connect and ADC
protocol. It is compatible with other DC clients, such as the original DC from
Neomodus, DC++ and derivatives. EiskaltDC++ also interoperates with all common
DC hub software. The minimum number of our patches to original DC++ kernel
makes it easy to upgrade to new versions and ensures compatibility with other
clients. This is the Qt frontend.

%prep
%autosetup -p1

%build
%cmake -LA \
       -DJSONRPC_DAEMON=OFF \
       -DWITH_EXAMPLES=OFF
%cmake_build

%install
%cmake_install
install -Dm644 %{SOURCE1} %{buildroot}%{_prefix}/lib/firewalld/services/%{name}.xml
%fdupes %{buildroot}

%find_lang --with-qt lib%{name} %{name}.lang

%post qt -p /sbin/ldconfig
%postun qt -p /sbin/ldconfig

%files -f %{name}.lang qt
%license COPYING LICENSE
%doc AUTHORS ChangeLog.txt README.md TODO
%{_bindir}/%{name}-qt
%{_libdir}/lib%{name}.so.*
%{_mandir}/man?/%{name}-qt.?%{ext_man}
%{_datadir}/applications/%{name}-qt.desktop
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/emoticons
%{_datadir}/%{name}/luascripts
%{_datadir}/%{name}/sounds
%dir %{_datadir}/%{name}/qt
%dir %{_datadir}/%{name}/qt/client-res
%{_datadir}/%{name}/qt/client-res/default.rcc
%{_datadir}/%{name}/qt/icons
%{_datadir}/%{name}/qt/translations
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/%{name}.xml

%changelog
