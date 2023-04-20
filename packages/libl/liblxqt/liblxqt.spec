#
# spec file for package liblxqt
#
# Copyright (c) 2023 SUSE LLC
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
Version:        1.3.0
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
BuildRequires:  lxqt-build-tools-devel >= 0.13.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5WindowSystem) >= 5.36.0
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xdg) >= 3.9.0
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xscrnsaver)
Obsoletes:      liblxqt-qt5 < %{version}
Provides:       liblxqt-qt5 = %{version}
# moved files to correct location in liblxqt1 (/lxqt-backlight_backend, power.conf, polkit)
Conflicts:      liblxqt0
Requires:       /usr/bin/pkexec

%description
liblxqt represents the core library of LXQt providing essential
functionality needed by nearly all of its components.

%lang_package

%package -n liblxqt1
Summary:        LXQt core library
Group:          System/Libraries
Recommends:     %{name}-lang
Provides:       liblxqt
Recommends:     %{name} >= %{version}

%description -n liblxqt1
liblxqt represents the core library of LXQt providing essential
functionality needed by nearly all of its components.

%package devel
Summary:        Devel files for liblxqt
Group:          Development/Libraries/C and C++
Requires:       liblxqt1 = %{version}
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

%post -n liblxqt1 -p /sbin/ldconfig
%postun -n liblxqt1 -p /sbin/ldconfig

%files
%dir %{_datadir}/lxqt/
%{_datadir}/lxqt/power.conf
%{_bindir}/lxqt-backlight_backend
%dir %{_datadir}/polkit-1/
%{_datadir}/polkit-1/actions/

%files -n liblxqt1
%license COPYING
%doc AUTHORS
%{_libdir}/%{name}.so.?
%{_libdir}/%{name}.so.?.*

%files devel
%{_includedir}/lxqt/
%{_libdir}/pkgconfig/lxqt.pc
%{_libdir}/%{name}.so
%{_datadir}/cmake/lxqt/

%files lang -f %{name}.lang
%dir %{_datadir}/lxqt/translations
%dir %{_datadir}/lxqt/translations/liblxqt
%{_datadir}/lxqt/translations/liblxqt/*

%changelog
