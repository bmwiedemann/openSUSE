#
# spec file for package deepin-compressor
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2021 Hillwood Yang <hillwood@opensuse.org>
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


%if 0%{?is_opensuse}
    %define  distribution  openSUSE-Edition
%else
    %define  distribution  SUSE-Edition
%endif

Name:           deepin-compressor
Version:        5.12.13
Release:        0
License:        GPL-3.0-or-later
Summary:        Archive Manager for Deepin Desktop
URL:            https://github.com/linuxdeepin/deepin-compressor
Group:          Productivity/Archiving/Compression
Source0:        https://github.com/linuxdeepin/deepin-compressor/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 002-install-compressor-ChardetDetector.patch hillwood@opensuse.org
# Install libcompressor-ChardetDetector.so
Patch1:         002-install-compressor-ChardetDetector.patch
# PATCH-FIX-UPSTREAM fix-Zip-Path-Traversal.patch - fix Zip Path Traversal
# backport form https://github.com/linuxdeepin/deepin-compressor/commit/82f668c78c133873f5094cfab6e4eabc0b70e4b6
Patch2:         fix-Zip-Path-Traversal.patch
BuildRequires:  fdupes
BuildRequires:  gtest
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(minizip)
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Archive Manager is a fast and lightweight application for creating and
extracting archives.

%lang_package

%prep
%autosetup -p1
sed -i 's/lrelease/lrelease-qt5/g' src/translate_generation.sh
sed -i 's|/usr/lib/|%{_libdir}/|g' src/source/common/pluginmanager.cpp
%ifarch armv6l armv7l aarch64
sed -i '/#include <map>/a#include <cstdint>' tests/UnitTest/include/gtest/src/stub.h
%endif

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
       -DCMAKE_BUILD_TYPE=Release \
       -DAPP_VERSION=%{version}-%{distribution} \
       -DVERSION=%{version}-%{distribution}
%make_build

%install
%cmake_install

rm %{buildroot}%{_libdir}/deepin-compressor/plugins/libcompressor-ChardetDetector.a
chmod -x %{buildroot}%{_datadir}/applications/%{name}.desktop

%fdupes %{buildroot}%{_datadir}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/applications/context-menus
%{_datadir}/applications/context-menus/compressor-*.conf
%dir %{_datadir}/%{name}
%{_datadir}/deepin-manual
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/mime/packages/deepin-compressor.xml

%files lang
%{_datadir}/%{name}/translations

%changelog
