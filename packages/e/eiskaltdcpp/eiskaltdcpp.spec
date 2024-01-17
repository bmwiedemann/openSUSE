#
# spec file for package eiskaltdcpp
#
# Copyright (c) 2021 SUSE LLC
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


%define sover   2_4
Name:           eiskaltdcpp
Version:        2.4.2
Release:        0
Summary:        Program that uses the Direct Connect and ADC protocols
License:        GPL-3.0-or-later
URL:            https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.firewalld
Patch0:         ru.ts.patch
BuildRequires:  aspell-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  hicolor-icon-theme
BuildRequires:  libattr-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(libpcrecpp)
BuildRequires:  pkgconfig(lua5.1)
BuildRequires:  pkgconfig(miniupnpc)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
This package contains the EiskaltDC++ program with a GUI based on Qt.
EiskaltDC++ is a program that uses the Direct Connect and Advanced
Direct Connect protocols. It is compatible with DC++, AirDC++,
FlylinkDC++ and other DC clients. EiskaltDC++ also interoperates with
all common DC hub software.

%package common
Summary:        Shared data for %{name}
Requires:       lib%{name}%{sover} = %{version}
BuildArch:      noarch

%description common
This package contains shared data for EiskaltDC++.

%package -n lib%{name}%{sover}
Summary:        Shared library for %{name}

%description -n lib%{name}%{sover}
This package contains Shared library for EiskaltDC++.

%package qt
Summary:        Qt frontend for %{name}
Requires:       %{name}-common = %{version}
Requires:       aspell
Recommends:     %{name}-qt-lang

%description qt
This package contains the EiskaltDC++ program with GUI based on Qt.
EiskaltDC++ is a program that uses the Direct Connect and Advanced
Direct Connect protocols. It is compatible with DC++, AirDC++,
FlylinkDC++ and other DC clients. EiskaltDC++ also interoperates with
all common DC hub software.

%package daemon
Summary:        Daemon for %{name}
Requires:       %{name}-common = %{version}
Suggests:       %{name}-cli = %{version}

%description daemon
This package contains only the EiskaltDC++ daemon, without any GUI.
Support for control via JSON-RPC is enabled. The EiskaltDC++ CLI and
Web UI programs can be used to control it.
EiskaltDC++ Qt and GTK+ UI may be used for configuring the
EiskaltDC++ daemon (they use the same settings from core library),
but they should not be launched simultaneously.
EiskaltDC++ is a program that uses the Direct Connect and Advanced
Direct Connect protocols. It is compatible with DC++, AirDC++,
FlylinkDC++ and other DC clients. EiskaltDC++ also interoperates with
all common DC hub software.

%package cli
Summary:        CLI frontend for %{name}
Requires:       %{name}-common = %{version}
Requires:       perl(JSON::RPC)
Suggests:       %{name}-daemon = %{version}

%description cli
This package contains the EiskaltDC++ CLI (command-line interface) written in Perl.
This program is used to control the EiskaltDC++ daemon via the JSON-RPC protocol.
EiskaltDC++ is a program that uses the Direct Connect and Advanced
Direct Connect protocols. It is compatible with DC++, AirDC++,
FlylinkDC++ and other DC clients. EiskaltDC++ also interoperates with
all common DC hub software.

%lang_package -n %{name}-common
%lang_package -n %{name}-qt

%prep
%autosetup -p1

%build
%cmake -LA \
       -DNO_UI_DAEMON=ON \
       -DUSE_CLI_JSONRPC=ON \
       -DWITH_EXAMPLES=OFF
%cmake_build

%install
%cmake_install
install -Dpm0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/firewalld/services/%{name}.xml
%fdupes %{buildroot}
%find_lang lib%{name} %{name}-common.lang
%find_lang %{name} %{name}-qt.lang --with-qt --without-mo --all-name

%post   -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files common
%license COPYING LICENSE
%doc AUTHORS ChangeLog.txt README.md TODO
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/emoticons
%{_datadir}/%{name}/luascripts
%{_datadir}/%{name}/sounds
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/%{name}.xml

%files common-lang -f %{name}-common.lang

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.*

%files qt
%{_bindir}/%{name}-qt
%{_mandir}/man?/%{name}-qt.?%{ext_man}
%{_datadir}/applications/%{name}-qt.desktop
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/qt
%dir %{_datadir}/%{name}/qt/client-res
%{_datadir}/%{name}/qt/client-res/default.rcc
%{_datadir}/%{name}/qt/icons

%files qt-lang -f %{name}-qt.lang
%dir %{_datadir}/%{name}/qt/translations

%files daemon
%{_bindir}/%{name}-daemon
%{_mandir}/man?/%{name}-daemon.?%{ext_man}

%files cli
%{_bindir}/%{name}-cli-jsonrpc
%dir %{_datadir}/%{name}/cli
%{_datadir}/%{name}/cli/cli-jsonrpc-config.pl
%{_mandir}/man?/%{name}-cli-jsonrpc.?%{ext_man}

%changelog
