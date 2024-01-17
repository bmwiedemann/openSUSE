#
# spec file for package deepin-manual
#
# Copyright (c) 2022 SUSE LLC
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

Name:           deepin-manual
Version:        5.8.12
Release:        0
Summary:        Deepin Manual
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/linuxdeepin/deepin-manual
Source:         https://github.com/linuxdeepin/deepin-manual/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gtest
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libqt5-linguist
BuildRequires:  nodejs-common
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5WebChannel)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(dtkcore) >= 5.0.0
BuildRequires:  pkgconfig(dtkgui) >= 5.0.0
BuildRequires:  pkgconfig(dtkwidget) >= 5.0.0
BuildRequires:  rubygem(sass)
# Qt5WebEngineWidgets is invalid on these arches
ExcludeArch:    ppc ppc64 ppc64le s390 s390x
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Deepin Manual is designed to help users learn the operating system and its
applications, providing specific instructions and function descriptions.

%prep
%autosetup -p1
chmod -x LICENSE README.md
sed -i 's/lrelease/lrelease-qt5/g' translate_generation.sh

%build
%cmake -DVERSION=%{version}-%{distribution}

%install
%cmake_install
install -d %{buildroot}%{_datadir}/deepin-manual/manual-assets/application
find %{buildroot}%{_datadir}/deepin-manual -type f -name "*~" -delete -print
find %{buildroot}%{_datadir}/deepin-manual -type f -name "._*.svg" -delete -print
find %{buildroot}%{_datadir}/deepin-manual -type f -name ".DS_Store" -delete -print

%fdupes %{buildroot}%{_datadir}
%suse_update_desktop_file %{name} Utility Documentation Accessibility

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/dman
%{_bindir}/dmanHelper
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/com.deepin.Manual.*
%{_datadir}/deepin-manual
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%dir %{_datadir}/deepin-manual/manual-assets/application

%changelog
