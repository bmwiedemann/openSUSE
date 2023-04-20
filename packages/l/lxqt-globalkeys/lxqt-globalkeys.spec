#
# spec file for package lxqt-globalkeys
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


Name:           lxqt-globalkeys
Version:        1.3.0
Release:        0
Summary:        Global keyboard shortcuts registration
License:        LGPL-2.1-or-later
URL:            https://www.lxqt.org
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
BuildRequires:  pkgconfig(Qt5UiTools) >= 5.15.0
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(lxqt) >= %{version}
Requires(post): desktop-file-utils
Requires(pre):  desktop-file-utils
Obsoletes:      lxqt-globalkeys-qt5 < %{version}
Provides:       lxqt-globalkeys-qt5 = %{version}

%description
Daemon and library for global keyboard shortcuts registration

%lang_package

%package devel
Summary:        Development files for lxqt-globalkeys
Requires:       %{name} = %{version}
Requires:       liblxqt-globalkeys-ui1 = %{version}
Requires:       liblxqt-globalkeys1 = %{version}
Requires:       pkgconfig

%description devel
Development files for lxqt-globalkeys including headers and libraries

%package -n liblxqt-globalkeys1
Summary:        Lxqt-globalkeys libraries
# liblxqt-globalkeys0 already contained a file liblxqt-globalkeys.so.1.0.0 by mistake
Conflicts:      liblxqt-globalkeys0

%description -n liblxqt-globalkeys1
lxqt-globalkeys main system library

%package -n liblxqt-globalkeys-ui1
Summary:        UI lxqt-globalkeys libraries
Recommends:     %{name}-lang
# liblxqt-globalkeys-ui0 already contained a file liblxqt-globalkeys-ui.so.1.0.0 by mistake
Conflicts:      liblxqt-globalkeys-ui0

%description -n liblxqt-globalkeys-ui1
UI system libraries for lxqt-globalkeys

%prep
%setup -q
# Changing LXQt into X-LXQt in desktop files to be freedesktop compliant and shut rpmlint warnings
#find -name '*desktop.in*' -exec sed -ri 's/(LXQt;)/X-\1/' {} +

%build
%cmake -DPULL_TRANSLATIONS=No

%install
%cmake_install
%fdupes -s %{buildroot}

%find_lang lxqt-config-globalkeyshortcuts --with-qt

%post -n liblxqt-globalkeys1 -p /sbin/ldconfig
%postun -n liblxqt-globalkeys1 -p /sbin/ldconfig
%post -n liblxqt-globalkeys-ui1 -p /sbin/ldconfig
%postun -n liblxqt-globalkeys-ui1 -p /sbin/ldconfig

%files
%license LICENSE
%doc AUTHORS
%{_bindir}/lxqt-globalkeysd
%{_bindir}/lxqt-config-globalkeyshortcuts
%{_datadir}/applications/lxqt-config-globalkeyshortcuts.desktop
%config %{_sysconfdir}/xdg/autostart/lxqt-globalkeyshortcuts.desktop
%{_datadir}/lxqt/globalkeyshortcuts.conf

%files devel
%{_includedir}/%{name}
%{_includedir}/lxqt-globalkeys-ui
%{_libdir}/pkgconfig/*.pc
%{_libdir}/liblxqt-globalkeys.so
%{_libdir}/liblxqt-globalkeys-ui.so
%dir %{_datadir}/cmake/lxqt-globalkeys
%dir %{_datadir}/cmake/lxqt-globalkeys-ui
%{_datadir}/cmake/lxqt-globalkeys/*
%{_datadir}/cmake/lxqt-globalkeys-ui/*

%files -n liblxqt-globalkeys1
%{_libdir}/liblxqt-globalkeys.so.1*

%files -n liblxqt-globalkeys-ui1
%{_libdir}/liblxqt-globalkeys-ui.so.1*

%files lang -f lxqt-config-globalkeyshortcuts.lang
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%{_datadir}/lxqt/translations/lxqt-config-globalkeyshortcuts

%changelog
