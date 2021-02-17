#
# spec file for package deepin-editor
#
# Copyright (c) 2021 SUSE LLC
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


Name:           deepin-editor
Version:        5.9.0.32
Release:        0
Summary:        A text editor for the Deepin environment
License:        GPL-3.0-or-later
Group:          Productivity/Text/Editors
URL:            https://github.com/linuxdeepin/deepin-editor
Source0:        https://github.com/linuxdeepin/deepin-editor/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Use-librares-system-default.patch hillwood@opensuse.org - Use these librares in system default
Patch0:         Use-librares-system-default.patch
BuildRequires:  fdupes
BuildRequires:  gmock
BuildRequires:  gtest
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libqt5-linguist
BuildRequires:  recode-devel
BuildRequires:  cmake(DFrameworkdbus)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5SyntaxHighlighting) 
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dtkgui)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(enca)
BuildRequires:  pkgconfig(uchardet)
Recommends:     %{name}-lang = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Deepin Editor is a desktop text editor that supports common text editing
features.

%lang_package

%prep
%autosetup -p1
sed -i 's/lrelease/lrelease-qt5/g' translate_generation.sh
sed -i 's/Exec=deepin-editor/Exec=env QT_QPA_PLATFORMTHEME=deepin deepin-editor/g' \
deepin-editor.desktop

%build
%cmake
%make_build

%install
%cmake_install

%fdupes %{buildroot}%{_datadir}

%files
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files lang
%defattr(-,root,root)
%{_datadir}/%{name}

%changelog
