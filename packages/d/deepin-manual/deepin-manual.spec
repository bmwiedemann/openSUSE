#
# spec file for package deepin-manual
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%if 0%{?is_opensuse}
    %define  distribution  openSUSE-Edition
%else
    %define  distribution  SUSE-Edition
%endif

Name:           deepin-manual
Version:        5.7.0.35
Release:        0
License:        GPL-3.0+
Summary:        Deepin Manual
Url:            https://github.com/linuxdeepin/deepin-manual
Group:          System/GUI/Other
Source:         https://github.com/linuxdeepin/deepin-manual/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREA support-Qt-5_15+.patch hillwood@opensuse.org
Patch0:         support-Qt-5_15+.patch
BuildRequires:  fdupes
BuildRequires:  rubygem(sass)
# BuildRequires:  npm
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  nodejs-common
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5WebChannel)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(dtkgui) >= 5.0.0
BuildRequires:  pkgconfig(dtkwidget) >= 5.0.0
BuildRequires:  pkgconfig(dtkcore) >= 5.0.0
# Qt5WebEngineWidgets is invalid on these arches
ExcludeArch:    ppc ppc64 ppc64le s390 s390x
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Deepin Manual is designed to help users learn the operating system and its
applications, providing specific instructions and function descriptions.

%prep
%autosetup -p1
chmod -x LICENSE README.md 

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
%{_bindir}/dman-search
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/com.deepin.Manual.*
%{_datadir}/deepin-manual
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%dir %{_datadir}/deepin-manual/manual-assets/application

%changelog

