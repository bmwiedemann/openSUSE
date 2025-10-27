#
# spec file for package kvirc
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define kf6_version 6.0.0
%define qt6_version 6.5.0

%ifarch x86_64 aarch64 riscv64
%bcond_without qtwebengine
%endif
Name:           kvirc
Version:        5.2.8
Release:        0
Summary:        Graphical Front-End for IRC
License:        GPL-2.0-or-later AND (GPL-3.0-only OR SUSE-LGPL-2.1-with-digia-exception-1.1)
URL:            https://www.kvirc.net/
Source:         https://github.com/kvirc/KVIrc/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  enchant-devel
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libX11-devel
BuildRequires:  libopenssl-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  zlib-devel
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6MultimediaWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
%if %{with qtwebengine}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
%endif
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
Requires:       qt6-sql-sqlite >= %{qt6_version}
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

%cmake_kf6 \
  -DWANT_ESD:BOOL=FALSE \
  -DWANT_OSS:BOOL=FALSE \
  -DWANT_AUDIOFILE:BOOL=FALSE \
  $EXTRA_FLAGS
%{nil}

%kf6_build

%install
%kf6_install

rm %{buildroot}%{_kf6_libdir}/libkvilib.so

%fdupes %{buildroot}

%ldconfig_scriptlets

%files
%doc README.md RELEASES
%license COPYING
%{_kf6_applicationsdir}/net.kvirc.KVIrc5.desktop
%{_kf6_bindir}/kvirc
%{_kf6_bindir}/kvirc-config
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_libdir}/kvirc/
%{_kf6_libdir}/libkvilib.so.*
%{_kf6_mandir}/*/man?/kvirc.*
%{_kf6_mandir}/man?/kvirc.*
%{_kf6_sharedir}/kvirc/
%{_kf6_sharedir}/pixmaps/kvirc.png

%changelog
