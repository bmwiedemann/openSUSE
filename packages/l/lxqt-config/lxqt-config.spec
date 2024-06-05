#
# spec file for package lxqt-config
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


Name:           lxqt-config
Version:        2.0.0
Release:        0
Summary:        LXQt Control Center
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            http://www.lxqt.org
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        lxqt-config.keyring
BuildRequires:  cmake >= 3.5.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel
BuildRequires:  cmake(KF6Screen) >= 6.0.0
BuildRequires:  cmake(KF6WindowSystem) >= 6.0.0
BuildRequires:  cmake(Qt6Concurrent) >= 6.6
BuildRequires:  cmake(Qt6DBus) >= 6.6
BuildRequires:  cmake(Qt6LinguistTools) >= 6.6
BuildRequires:  cmake(Qt6Svg) >= 6.6
BuildRequires:  cmake(Qt6Xml) >= 6.6
BuildRequires:  cmake(lxqt) >= %{version}
BuildRequires:  cmake(lxqt-menu-data) >= %{version}
BuildRequires:  cmake(lxqt2-build-tools) >= %{version}
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xorg-libinput)
BuildRequires:  pkgconfig(zlib)
Requires(post): desktop-file-utils
Requires(pre):  desktop-file-utils

%description
System Configuration and Control Center for LXQt

%lang_package

%prep
%autosetup -p1
# Changing LXQt into X-LXQt in desktop files to be freedesktop compliant and shut rpmlint warnings
#find -name '*desktop.in*' -exec sed -ri 's/(LXQt;)/X-\1/' {} +

%build
%cmake_qt6
%{qt6_build}

%install
%{qt6_install}
install -Dm 0644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -Dm 0644 lib%{name}-cursor/man/%{name}-mouse.1 %{buildroot}%{_mandir}/man1/%{name}-mouse.1
install -Dm 0644 %{name}-appearance/man/%{name}-appearance.1 %{buildroot}%{_mandir}/man1/%{name}-appearance.1

%fdupes -s %{buildroot}/%{_datadir}

%find_lang %{name} --with-qt

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
cat <<EOF >%{buildroot}%{_sysconfdir}/ld.so.conf.d/lxqt-config.conf
%{_libdir}/%{name}
EOF

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc AUTHORS
%dir %{_qt6_libdir}/lxqt-config
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/icons
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/48x48/apps
%config %{_sysconfdir}/ld.so.conf.d/lxqt-config.conf
%{_bindir}/%{name}*
%{_qt6_libdir}/%{name}/lib%{name}-cursor.so
%{_datadir}/applications/
%{_datadir}/icons/hicolor/48x48/apps/
%{_datadir}/lxqt/icons/
%{_mandir}/man?/%{name}*.?%{ext_man}

%files lang -f %{name}.lang
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%{_datadir}/lxqt/translations/%{name}*

%changelog
