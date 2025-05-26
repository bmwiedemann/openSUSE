#
# spec file for package xfce4-panel-profiles
#
# Copyright (c) 2025 SUSE LLC
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


%define xfce_version 4.16
Name:           xfce4-panel-profiles
Version:        1.1.1
Release:        0
Summary:        Simple application to manage Xfce panel layouts
License:        GPL-3.0-only
Group:          System/GUI/Other
URL:            https://git.xfce.org/apps/xfce4-panel-profiles/about/
#Git-Clone:     https://gitlab.xfce.org/apps/xfce4-panel-profiles.git
Source:         https://archive.xfce.org/src/apps/xfce4-panel-profiles/1.1/%{name}-%{version}.tar.xz
BuildRequires:  appstream-glib
BuildRequires:  findutils
BuildRequires:  gobject-introspection
BuildRequires:  meson >= 0.54.0
BuildRequires:  python3
BuildRequires:  python3-base
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-Gdk
BuildRequires:  python3-psutil
BuildRequires:  pkgconfig(gio-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{xfce_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{xfce_version}
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{xfce_version}
Requires:       python3
Requires:       python3-base
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-psutil
Requires:       xfce4-panel
Recommends:     %{name}-lang
Recommends:     xfce4-panel-plugin-whiskermenu
BuildArch:      noarch

%description
Simple application to manage Xfce panel layouts.

This tool makes it possible to backup, restore, import, and export panel layouts.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

# Remove not needed doc files
rm %{buildroot}%{_datadir}/doc/%{name}/{AUTHORS,COPYING,INSTALL,NEWS,README.md}

# Avoid rpmlint messages
chmod a-x %{buildroot}%{_datadir}/%{name}/%{name}/info.py
find %{buildroot}%{_datadir} \! -type d -print0 | xargs -0 -r chmod a-x
find %{buildroot}%{_datadir} -type d -print0 | xargs -0 -r chmod a+x
sed -i -e '/^Keywords=Configuration;User;/ d' %{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name}

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files -f %{name}.lang
%doc AUTHORS NEWS README.md
%license COPYING
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/layouts
%dir %{_datadir}/%{name}/%{name}
%dir %{_datadir}/icons/hicolor/*
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%attr(644, root, root) %{_datadir}/%{name}/layouts/*
%{_datadir}/%{name}/%{name}/*.py
%attr(644, root, root) %{_datadir}/%{name}/%{name}/%{name}.glade
%attr(644, root, root) %{_datadir}/metainfo/org.xfce.PanelProfiles.appdata.xml
%{_datadir}/icons/hicolor/*/*
%attr(644, root, root) %{_mandir}/man1/xfce4-panel-profiles.1.gz

%changelog
