#
# spec file for package gnome-pie
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gnome-pie
Version:        0.7.1
Release:        0
Summary:        A circular application launcher for GNOME
License:        GPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            https://simmesimme.github.io/gnome-pie.html
Source:         https://github.com/Simmesimme/Gnome-Pie/archive/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM gnome-pie-fix-build-vala042.patch -- Fix build with vala 0.42.x
Patch0:         gnome-pie-fix-build-vala042.patch

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.22
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libbamf3)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)

%description
GNOME-Pie is a circular application launcher (pie menu).
It is made of several pies, each consisting of multiple slices.
The user presses a key stroke which opens the desired pie. By
activating one of its slices, applications may be launched, key
presses may be simulated or files can be opened.

%prep
%setup -q -n Gnome-Pie-%{version}
%if %{pkg_vcmp vala > 0.42}
%patch0 -p1
%endif

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
%suse_update_desktop_file %{name} -r Utilities DesktopUtility
%fdupes %{buildroot}%{_datadir}

%if 0%{?suse_version} && 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license COPYING
%doc AUTHORS TRANSLATING
%{_bindir}/gnome-pie
%{_datadir}/applications/gnome-pie.desktop
%{_datadir}/doc/gnome-pie/
%dir %{_datadir}/gnome-pie/
%dir %{_datadir}/gnome-pie/themes/
%{_datadir}/gnome-pie/themes/adwaita/
%{_datadir}/gnome-pie/themes/adwaita_big/
%{_datadir}/gnome-pie/themes/bright/
%{_datadir}/gnome-pie/themes/elementary/
%{_datadir}/gnome-pie/themes/funky/
%{_datadir}/gnome-pie/themes/gloss/
%{_datadir}/gnome-pie/themes/minimalistic_text/
%{_datadir}/gnome-pie/themes/numix/
%{_datadir}/gnome-pie/themes/o-pie/
%{_datadir}/gnome-pie/themes/simple/
%{_datadir}/gnome-pie/themes/simple_clock/
%{_datadir}/gnome-pie/themes/slim/
%{_datadir}/gnome-pie/themes/space_clock/
%{_datadir}/gnome-pie/themes/unity/
%{_datadir}/gnome-pie/ui/
%{_datadir}/gnome-pie/ui/shapes/
%{_datadir}/icons/hicolor/scalable/apps/gnome-pie-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/gnome-pie.svg
%{_datadir}/locale/zanata.xml
%{_mandir}/man1/gnome-pie.1%{?ext_man}

%changelog
