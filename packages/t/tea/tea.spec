#
# spec file for package tea
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


Name:           tea
Version:        50.1.0
Release:        0
Summary:        Qt-based text editor with image viewer
License:        GPL-3.0-or-later
URL:            http://semiletov.org/tea
Source:         https://github.com/psemiletov/tea-qt/archive/%{version}.tar.gz#/%{name}-qt-%{version}.tar.gz
Source1:        org.semiletov.tea.desktop
Source2:        org.semiletov.tea.appdata.xml
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(zlib)

%description
TEA is a Qt-based text editor. It supports reading FB2, ODT, RTF,
DOCX, Abiword, KWord KWD and SWX documents, though only writes out
plaintext. Image viewing is possible as well. It has a built-in
Midnight-Commander-style file manager, integrates spell checking
(aspell/hunspell), and syntax highlighting for a number of languages.

%prep
%setup -q -n tea-qt-%{version}

cp -a %{SOURCE1} org.semiletov.tea.desktop
cp -a %{SOURCE2} org.semiletov.tea.appdata.xml
sed -i '/DESTINATION share\/applications/d' CMakeLists.txt

%build
%cmake \
  -DUSE_ASPELL=ON  \
  -DUSE_PRINTER=ON \
  -DUSE_PDF=ON     \
  -DUSE_DJVU=ON    \
  -DUSE_QML=ON
%cmake_build

%install
%cmake_install

install -Dpm 0644 org.semiletov.tea.desktop %{buildroot}%{_datadir}/applications/org.semiletov.tea.desktop
install -Dpm 0644 icons/%{name}-icon-v3-01.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -Dpm 0644 org.semiletov.tea.appdata.xml %{buildroot}%{_datadir}/metainfo/org.semiletov.tea.appdata.xml

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS* README TODO
%{_bindir}/%{name}
%{_datadir}/applications/org.semiletov.tea.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/org.semiletov.tea.appdata.xml

%changelog
