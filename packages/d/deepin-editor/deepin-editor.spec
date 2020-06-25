#
# spec file for package deepin-editor
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


Name:           deepin-editor
Version:        1.2.9
Release:        0
Summary:        A text editor for the Deepin environment
License:        GPL-3.0-or-later
Group:          Productivity/Text/Editors
URL:            https://github.com/linuxdeepin/deepin-editor
Source0:        https://github.com/linuxdeepin/deepin-editor/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/linuxdeepin/deepin-icon-theme/master/deepin/apps/256/%{name}.svg
# PATCH-FIX-UPSTEAM deepin-editor-qt-5_15.patch hillwood@opensuse.org - Support Qt 5.15
Patch0:         %{name}-Qt-5_15.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libqt5-linguist
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5SyntaxHighlighting) 
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dtkwidget)
Recommends:     %{name}-lang = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Deepin Editor is a desktop text editor that supports common text editing
features.

%lang_package

%prep
%setup
%if 0%{?suse_version} > 1500
%patch0 -p1
%endif
sed -i 's/lrelease/lrelease-qt5/g' translate_generation.sh

%build
%cmake
%make_build

%install
%cmake_install
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -m0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

%fdupes %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/dedit
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files lang
%defattr(-,root,root)
%{_datadir}/%{name}

%changelog
