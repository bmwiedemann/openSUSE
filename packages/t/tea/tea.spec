#
# spec file for package tea
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


%if 0%{?suse_version} >= 1550
%bcond_without qt6
%else
%bcond_with qt6
%endif
Name:           tea
Version:        61.2.0
Release:        0
Summary:        Qt-based text editor with image viewer
License:        GPL-3.0-or-later
URL:            http://semiletov.org/tea
Source:         https://github.com/psemiletov/tea-qt/archive/%{version}.tar.gz#/%{name}-qt-%{version}.tar.gz
# PATCH-FIX-OPENSUSE tea-fix-mimetype.patch -- Fix MimeType .desktop entry.
Patch0:         tea-fix-mimetype.patch
# PATCH-FEATURE-UPSTREAM -- https://github.com/psemiletov/tea-qt/pull/45
Patch1:         0001-Add-metainfo-use-GNUInstallDirs-install-metainfo-des.patch
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(zlib)
%if %{with qt6}
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
%else
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)
%endif

%description
TEA is a Qt-based text editor. It supports reading FB2, ODT, RTF,
DOCX, Abiword, KWord KWD and SWX documents, though only writes out
plaintext. Image viewing is possible as well. It has a built-in
Midnight-Commander-style file manager, integrates spell checking
(aspell/hunspell), and syntax highlighting for a number of languages.

%prep
%autosetup -n tea-qt-%{version} -p1

%build
%cmake \
  -DUSE_ASPELL=ON  \
  -DUSE_PRINTER=ON \
  -DUSE_PDF=ON     \
  -DUSE_DJVU=ON
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS* README.md TODO
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%{_datadir}/metainfo/org.semiletov.tea.metainfo.xml
%{_datadir}/applications/org.semiletov.tea.desktop

%changelog
