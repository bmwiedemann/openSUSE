#
# spec file for package kchmviewer
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


Name:           uChmViewer
Version:        8.3
Release:        0
Summary:        CHM and ePub Viewer
License:        GPL-3.0-only
Group:          Productivity/Office/Other
Obsoletes:      kchmviewer <= 8.0
# Something sorting just higher than the last kchmviewer version.
Provides:       kchmviewer = 8.0^fork
URL:            https://github.com/eBookProjects/uChmViewer
Source:         https://github.com/eBookProjects/uChmViewer/archive/refs/tags/v%{version}.tar.gz
# PATCH-FIX-OPENSUSE
Patch5:         InitialPreference-greater-than-okular.patch
BuildRequires:  chmlib-devel
BuildRequires:  cmake(libzip)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  hicolor-icon-theme
Requires:       hicolor-icon-theme
# Requires qtwebengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
This is a viewer for ebooks and documentation in CHM (Microsoft Compiled HTML) and ePub formats.
It supports complex searching for large books and has various viewing features.

%prep
%autosetup -p1

%build
%cmake_qt6 \
-DUSE_WEBENGINE=ON \
-DUSE_GETTEXT=ON \
-DUSE_DBUS=ON \

%qt6_build

%install
%qt6_install
#Add compatibility symlink
ln -srv %{buildroot}%{_bindir}/{u,k}chmviewer
%find_lang uchmviewer


%files -f uchmviewer.lang
%license AUTHORS.md COPYING
%doc ChangeLog DBUS-bindings NEWS.md README.md
%{_bindir}/kchmviewer
%{_bindir}/uchmviewer
%{_datadir}/applications/uchmviewer.desktop
%{_datadir}/icons/hicolor/128x128/apps/uchmviewer.png

%changelog
