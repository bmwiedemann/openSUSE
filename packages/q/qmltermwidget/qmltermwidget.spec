#
# spec file for package qmltermwidget
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


Name:           qmltermwidget
Version:        0.2.0
Release:        0
Summary:        QML port of qtermwidget
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/Swordfish90/qmltermwidget
Source:         https://github.com/Swordfish90/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-Fix-missing-includes-in-TerminalCharacterDecoder-27.patch
Patch2:         0004-Refix-CTRL-SPACE-behaviour-on-QT5.patch
Patch3:         0005-QMAKE_POST_LINK-doesn-t-work-in-Qt-5.5.-10.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
This project provides a Unicode-enabled, embeddable QML widget for
using as a built-in console (or terminal emulation widget).

%prep
%autosetup -p1

%build
%qmake5 \
      QMAKE_CFLAGS+="%{optflags}" \
      QMAKE_CXXFLAGS+="%{optflags}"
%make_jobs

%install
%qmake5_install

%files
%license LICENSE
%doc AUTHORS README.md
%{_libqt5_archdatadir}/qml/QMLTermWidget

%changelog
