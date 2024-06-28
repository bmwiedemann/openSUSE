#
# spec file for package qtermwidget
#
# Copyright (c) 2024 SUSE LLC
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


%define  qt_ver 6
%define  sover  2
Name:           qtermwidget
Version:        2.0.1
Release:        0
Summary:        The terminal widget for QTerminal
License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/lxqt/qtermwidget
Source:         %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake
BuildRequires:  utempter-devel
BuildRequires:  utf8proc-devel
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(lxqt2-build-tools)

%description
QTermWidget is an open-source project originally based on the KDE4 Konsole
application, but it took its own direction later on. The main goal of this
project is to provide a Unicode-enabled, embeddable Qt widget for using as
a built-in console (or terminal emulation widget).

%package -n libqtermwidget%{qt_ver}-%{sover}
Summary:        The terminal widget for QTerminal
Group:          Development/Libraries/C and C++
Requires:       %{name}-data >= %{version}

%description -n libqtermwidget%{qt_ver}-%{sover}
QTermWidget is an open-source project originally based on the KDE4 Konsole
application, but it took its own direction later on. The main goal of this
project is to provide a Unicode-enabled, embeddable Qt widget for using as
a built-in console (or terminal emulation widget).

%package data
Summary:        QTermWidget data package
Group:          Development/Libraries/C and C++
Requires:       libqtermwidget%{qt_ver}-%{sover} = %{version}
BuildArch:      noarch

%description data
Data files for qtermwidget library.

%package devel
Summary:        QTermWidget devel package
Group:          Development/Libraries/C and C++
Requires:       libqtermwidget%{qt_ver}-%{sover} = %{version}

%description devel
Development environment for qtermwidget library.

%prep
%autosetup

%build
%cmake_qt6 \
    -DUSE_UTF8PROC=ON \
    -DQTERMWIDGET_USE_UTEMPTER=ON
%{qt6_build}

%install
%{qt6_install}

%ldconfig_scriptlets -n libqtermwidget%{qt_ver}-%{sover}

%files -n libqtermwidget%{qt_ver}-%{sover}
%doc AUTHORS CHANGELOG README.md
%{_libdir}/libqtermwidget%{qt_ver}.so.*
%license LICENSE*

%files data
%{_datadir}/qtermwidget%{qt_ver}

%files devel
%{_includedir}/qtermwidget%{qt_ver}
%{_libdir}/libqtermwidget%{qt_ver}.so
%{_libdir}/pkgconfig/qtermwidget%{qt_ver}.pc
%{_libdir}/cmake/qtermwidget%{qt_ver}

%changelog
