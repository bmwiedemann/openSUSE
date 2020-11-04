#
# spec file for package qtermwidget-qt5
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


%define qt_ver 5
%define pack_summ Qt5 terminal widget
%define pack_desc QTermWidget is a project based on the KDE4 \
Konsole application whose goal is to provide a Unicode-\
enabled, embeddable Qt widget to be used as a built-in console (or \
terminal emulation widget). Though Konsole is able of getting embedded, \
it is possible to have Qt without KDE. The original \
Konsole code was rewritten entirely with using Qt only, and all \
code dealing with user interface parts and session management was \
removed.
Name:           qtermwidget-qt5
Version:        0.16.0
Release:        0
Summary:        %{pack_summ}
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/qterminal/qtermwidget
Source:         https://github.com/lxqt/qtermwidget/releases/download/%{version}/qtermwidget-%{version}.tar.xz
Source1:        https://github.com/lxqt/qtermwidget/releases/download/%{version}/qtermwidget-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.1.9
BuildRequires:  lxqt-build-tools-devel >= 0.8.0
BuildRequires:  pkgconfig
BuildRequires:  utf8proc-devel
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.12

%description
%{pack_desc}

%package -n libqtermwidget%{qt_ver}-0
Summary:        %{pack_summ}
Group:          Development/Libraries/C and C++
Requires:       %{name}-data >= %{version}

%description -n libqtermwidget%{qt_ver}-0
%{pack_desc}

%package data
Summary:        QTermWidget data package
Group:          Development/Libraries/C and C++
Requires:       libqtermwidget%{qt_ver}-0 = %{version}
BuildArch:      noarch

%description data
Data files for qtermwidget library.

%package devel
Summary:        QTermWidget devel package
Group:          Development/Libraries/C and C++
Requires:       libqtermwidget%{qt_ver}-0 = %{version}

%description devel
Development environment for qtermwidget library.

%prep
%setup -q -n qtermwidget-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DPULL_TRANSLATIONS=no -DUSE_UTF8PROC=yes

make V=1 %{?_smp_mflags}

%install
%cmake_install

%post -n libqtermwidget%{qt_ver}-0 -p /sbin/ldconfig
%postun -n libqtermwidget%{qt_ver}-0 -p /sbin/ldconfig

%files -n libqtermwidget%{qt_ver}-0
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%{_libdir}/libqtermwidget*.so.*

%files data
%{_datadir}/qtermwidget%{qt_ver}

%files devel
%{_includedir}/qtermwidget%{qt_ver}
%{_libdir}/libqtermwidget*.so
%{_libdir}/pkgconfig/qtermwidget%{qt_ver}.pc
%{_libdir}/cmake/qtermwidget5/

%changelog
