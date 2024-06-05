#
# spec file for package liblxqt
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


Name:           liblxqt
Version:        2.0.0
Release:        0
Summary:        Core utility library for LXQt
License:        LGPL-2.1-or-later
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.5.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6WindowSystem) >= 6.0.0
BuildRequires:  cmake(PolkitQt6-1) >= 0.200.0
BuildRequires:  cmake(Qt6DBus) >= 6.6
BuildRequires:  cmake(Qt6LinguistTools) >= 6.6
BuildRequires:  cmake(Qt6UiTools) >= 6.6
BuildRequires:  cmake(lxqt2-build-tools) >= 2.0.0
BuildRequires:  pkgconfig(Qt6Xdg) >= 4.0.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xscrnsaver)
Obsoletes:      liblxqt-qt5 < %{version}
Provides:       liblxqt-qt5 = %{version}
# moved files to correct location in liblxqt1 (/lxqt-backlight_backend, power.conf, polkit)
Conflicts:      liblxqt0
Conflicts:      liblxqt1
Requires:       /usr/bin/pkexec

%description
liblxqt represents the core library of LXQt providing essential
functionality needed by nearly all of its components.

%lang_package

%package -n liblxqt2
Summary:        LXQt core library
Recommends:     %{name}-lang
Requires:       %{name} >= %{version}

%description -n liblxqt2
liblxqt represents the core library of LXQt providing essential
functionality needed by nearly all of its components.

%package devel
Summary:        Devel files for liblxqt
Requires:       liblxqt2 = %{version}
Requires:       pkgconfig
Requires:       pkgconfig(Qt6Xdg) >= 4.0.0

%description devel
liblxqt represents the core library of LXQt providing essential
functionality needed by nearly all of its components.

This subpackage contains libraries and header files for developing
applications that want to make use of liblxqt.

%prep
%autosetup -p1

%build
%cmake_qt6
%{qt6_build}

%install
%{qt6_install}

%find_lang %{name} --with-qt

%ldconfig_scriptlets -n liblxqt2

%files
%dir %{_datadir}/lxqt/
%{_datadir}/lxqt/power.conf
%{_bindir}/lxqt-backlight_backend
%dir %{_datadir}/polkit-1/
%{_datadir}/polkit-1/actions/

%files -n liblxqt2
%license COPYING
%doc AUTHORS
%{_qt6_libdir}/%{name}.so.?
%{_qt6_libdir}/%{name}.so.?.*

%files devel
%{_includedir}/lxqt/
%{_qt6_libdir}/pkgconfig/lxqt.pc
%{_qt6_libdir}/%{name}.so
%{_datadir}/cmake/lxqt/

%files lang -f %{name}.lang
%dir %{_datadir}/lxqt/translations
%dir %{_datadir}/lxqt/translations/liblxqt
%{_datadir}/lxqt/translations/liblxqt/*

%changelog
