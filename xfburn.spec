#
# spec file for package xfburn
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


Name:           xfburn
Version:        0.7.0
Release:        0
Summary:        Simple CD/DVD Burning Application
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/CD/Record
URL:            https://docs.xfce.org/apps/xfburn/start
Source:         https://archive.xfce.org/src/apps/xfburn/0.7/%{name}-%{version}.tar.bz2
BuildRequires:  appstream-glib
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(exo-2) >= 0.11.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.38
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gthread-2.0) >= 2.38
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libburn-1) >= 0.4.2
BuildRequires:  pkgconfig(libisofs-1) >= 0.6.2
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.12.0
Recommends:     %{name}-lang = %{version}

%description
Xfburn is a simple CD/DVD burning application based on the libburnia libraries.
It can blank CD-RWs, burn and create iso images, as well as burn personal
compositions of data to either CD or DVD.

%lang_package

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%find_lang %{name} %{?no_lang_C}

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files
%license COPYING
%doc README.md AUTHORS NEWS TODO
%{_bindir}/xfburn
%{_datadir}/applications/xfburn.desktop
%{_mandir}/man1/xfburn.1%{?ext_man}
%{_datadir}/xfburn
%{_datadir}/icons/hicolor/*/*/*/*xfburn*
%dir %{_datadir}/Thunar
%dir %{_datadir}/Thunar/sendto
%{_datadir}/Thunar/sendto/thunar-sendto-xfburn.desktop
%{_datadir}/metainfo/*.appdata.xml

%files lang -f %{name}.lang

%changelog
