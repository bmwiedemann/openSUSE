#
# spec file for package kvirc
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


%define kf5_version 5.2.0
%define qt5_version 5.15.2

%ifnarch ppc64 ppc64le s390x
%bcond_without qtwebengine
%endif
Name:           kvirc
Version:        5.2.4
Release:        0
Summary:        Graphical Front-End for IRC
License:        GPL-2.0-or-later AND (GPL-3.0-only OR SUSE-LGPL-2.1-with-digia-exception-1.1)
URL:            https://www.kvirc.net/
Source:         https://github.com/kvirc/KVIrc/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  enchant-devel
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  fdupes
BuildRequires:  libX11-devel
BuildRequires:  libopenssl-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  zlib-devel
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(KF5Parts) >= %{kf5_version}
BuildRequires:  cmake(KF5Service) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(KF5XmlGui) >= %{kf5_version}
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Concurrent) >= %{qt5_version}
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Multimedia) >= %{qt5_version}
BuildRequires:  cmake(Qt5MultimediaWidgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5Network) >= %{qt5_version}
BuildRequires:  cmake(Qt5PrintSupport) >= %{qt5_version}
BuildRequires:  cmake(Qt5Sql) >= %{qt5_version}
BuildRequires:  cmake(Qt5Svg) >= %{qt5_version}
%if %{with qtwebengine}
BuildRequires:  cmake(Qt5WebEngineWidgets) >= %{qt5_version}
%endif
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5X11Extras) >= %{qt5_version}
BuildRequires:  cmake(Qt5Xml) >= %{qt5_version}
Requires:       libQt5Sql5-sqlite >= %{qt5_version}
%requires_eq    perl
Obsoletes:      kvirc-devel < %{version}

%description
IRC (Internet Relay Chat) client with an MDI interface; scripting,
pop-up, alias, and event editor, DCC (SEND CHAT VOICE and RESUME),
SOCKSV4 & V5 support and more.

%prep
%autosetup -p1 -n KVIrc-%{version}

%build
EXTRA_FLAGS="-UCMAKE_MODULE_LINKER_FLAGS \
-DCMAKE_SKIP_RPATH:BOOL=TRUE \
%if "%{?_lib}" == "lib64"
-DLIB_SUFFIX:STRING=64 \
%endif
%if %{without qtwebengine}
-DWANT_QTWEBENGINE:BOOL=FALSE
%endif
"

%cmake_kf5 -d build -- -DWANT_ESD:BOOL=FALSE -DWANT_OSS:BOOL=FALSE -DWANT_AUDIOFILE:BOOL=FALSE $EXTRA_FLAGS

%cmake_build

%install
%kf5_makeinstall -C build

rm %{buildroot}%{_kf5_libdir}/libkvilib.so

%fdupes %{buildroot}

%ldconfig_scriptlets

%files
%doc README.md RELEASES
%license COPYING
%{_kf5_applicationsdir}/net.kvirc.KVIrc5.desktop
%{_kf5_bindir}/kvirc
%{_kf5_bindir}/kvirc-config
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_libdir}/kvirc/
%{_kf5_libdir}/libkvilib.so.*
%{_kf5_mandir}/*/man?/kvirc.*
%{_kf5_mandir}/man?/kvirc.*
%{_kf5_sharedir}/kvirc/
%{_kf5_sharedir}/pixmaps/kvirc.png

%changelog
