#
# spec file for package QLog
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>:
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


Name:           QLog
Version:        0.46.2
Release:        0
Summary:        Amateur radio logbook software
License:        GPL-3.0-or-later
Group:          Productivity/Hamradio/Other
URL:            https://github.com/foldynl/QLog
Source:         %{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  pkgconfig(Qt6Charts)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6SerialPort)
BuildRequires:  pkgconfig(Qt6Sql)
BuildRequires:  pkgconfig(Qt6WebEngineWidgets)
BuildRequires:  pkgconfig(Qt6WebSockets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(hamlib)
BuildRequires:  pkgconfig(sqlite3)
Requires:       qt6-sql-sqlite
Recommends:     tqsl

%description
QLog is an Amateur Radio logging application. It is based on the Qt framework
and uses SQLite as database backend.

QLogs aims to be as simple as possible, but to provide everything the operator
expects from the log to be. This log is not currently focused on contests.

%prep
%autosetup -p1

%build
%{qmake6} \
	PREFIX=%{_prefix} \
	%{nil}
%make_build

%install
%make_install \
	INSTALL_ROOT=%{buildroot} \
	%{nil}

%files
%license LICENSE
%doc AUTHORS README.md Changelog
%{_bindir}/qlog
%{_datadir}/applications/qlog.desktop
%{_datadir}/icons/hicolor
%{_datadir}/metainfo/io.github.foldynl.QLog.metainfo.xml

%changelog
