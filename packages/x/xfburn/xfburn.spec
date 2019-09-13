#
# spec file for package xfburn
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xfburn
Version:        0.5.5
Release:        0
Summary:        Simple CD/DVD Burning Application
License:        GPL-2.0+
Group:          Productivity/Multimedia/CD/Record
Url:            http://goodies.xfce.org/projects/applications/xfburn
Source:         http://archive.xfce.org/src/apps/xfburn/0.5/%{name}-%{version}.tar.bz2
BuildRequires:  ed
BuildRequires:  intltool
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(exo-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libburn-1)
BuildRequires:  pkgconfig(libisofs-1)
BuildRequires:  pkgconfig(libxfce4ui-1)
Recommends:     %{name}-lang = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Xfburn is a simple CD/DVD burning application based on the libburnia libraries.
It can blank CD-RWs, burn and create iso images, as well as burn personal
compositions of data to either CD or DVD.

%lang_package

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%suse_update_desktop_file %{name}

%find_lang %{name} %{?no_lang_C}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc README ChangeLog COPYING AUTHORS NEWS TODO
%{_bindir}/xfburn
%{_datadir}/applications/xfburn.desktop
%{_mandir}/man1/xfburn.1*
%{_datadir}/xfburn
%{_datadir}/icons/hicolor/*/*/*/*xfburn*
%dir %{_datadir}/Thunar
%dir %{_datadir}/Thunar/sendto
%{_datadir}/Thunar/sendto/thunar-sendto-xfburn.desktop
%{_datadir}/appdata/%{name}.appdata.xml

%files lang -f %{name}.lang

%changelog
