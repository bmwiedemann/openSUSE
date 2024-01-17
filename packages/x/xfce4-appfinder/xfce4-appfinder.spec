#
# spec file for package xfce4-appfinder
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


%bcond_with git
Name:           xfce4-appfinder
Version:        4.18.0
Release:        0
Summary:        Application Finder for the Xfce Desktop Environment
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/xfce/xfce4-appfinder/start
Source:         https://archive.xfce.org/src/xfce/%{name}/4.18/%{name}-%{version}.tar.bz2
BuildRequires:  appstream-glib
BuildRequires:  intltool
BuildRequires:  update-desktop-files
BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(garcon-1) >= 0.3.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.50
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gthread-2.0) >= 2.50
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.10.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.15.2
BuildRequires:  pkgconfig(libxfconf-0) >= 4.10.0
# uses exo-open
Requires:       exo-tools
Recommends:     %{name}-lang = %{version}

%description
xfce4-appfinder is an application finder for the Xfce desktop environment. It
is a useful program that allows you to find applications on the system and
launch them. It provides easy keyboard navigation and can be used as a
replacement for xfrun4.

%lang_package

%prep
%autosetup

%build
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-maintainer-mode
%else
%configure
%endif
%make_build

%install
%make_install

%suse_update_desktop_file %{name} Utility DesktopUtility

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{?no_lang_C}

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files
%license COPYING
%doc AUTHORS NEWS README.md TODO
%{_bindir}/xfrun4
%{_bindir}/xfce4-appfinder
%{_datadir}/applications/*.desktop
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.xfce.xfce4-appfinder.appdata.xml
%{_datadir}/icons/hicolor/*/apps/org.xfce.appfinder.*

%files lang -f %{name}.lang

%changelog
