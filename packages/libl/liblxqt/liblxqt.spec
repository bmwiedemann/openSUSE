#
# spec file for package liblxqt
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


Name:           liblxqt
Version:        0.16.0
Release:        0
Summary:        Core utility library for LXQt
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.1.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libqt5xdg-devel >= 3.5.0
BuildRequires:  lxqt-build-tools-devel >= 0.8.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5WindowSystem) >= 5.36.0
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xdg) >= 3.5.0
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xscrnsaver)
Obsoletes:      liblxqt-qt5 < %{version}
Provides:       liblxqt-qt5 = %{version}

%description
liblxqt represents the core library of LXQt providing essential
functionality needed by nearly all of its components.

%lang_package

%package -n liblxqt0
Summary:        LXQt core library
Group:          System/Libraries
Recommends:     %{name}-lang
Provides:       liblxqt

%description -n liblxqt0
liblxqt represents the core library of LXQt providing essential
functionality needed by nearly all of its components.

%package devel
Summary:        Devel files for liblxqt
Group:          Development/Libraries/C and C++
Requires:       liblxqt0 = %{version}
Requires:       pkgconfig
Requires:       pkgconfig(Qt5Xdg)

%description devel
liblxqt represents the core library of LXQt providing essential
functionality needed by nearly all of its components.

This subpackage contains libraries and header files for developing
applications that want to make use of liblxqt.

%prep
%setup -q -n liblxqt-%{version}

%build
%cmake -DPULL_TRANSLATIONS=No
%make_build

%install
%cmake_install

%find_lang %{name} --with-qt

%post -n liblxqt0 -p /sbin/ldconfig
%postun -n liblxqt0 -p /sbin/ldconfig

%files -n liblxqt0
%license COPYING
%doc AUTHORS
%{_libdir}/%{name}.so.0
%{_libdir}/%{name}.so.0.*
%dir %{_datadir}/lxqt/
%{_datadir}/lxqt/power.conf
%{_bindir}/lxqt-backlight_backend
%dir %{_datadir}/polkit-1/
%{_datadir}/polkit-1/actions/

%files devel
%{_includedir}/lxqt/
%{_datadir}/cmake/lxqt/
%{_libdir}/pkgconfig/lxqt.pc
%{_libdir}/%{name}.so

%files lang -f %{name}.lang
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%dir %{_datadir}/lxqt/translations/liblxqt
%{_datadir}/lxqt/translations/liblxqt/*

%changelog
