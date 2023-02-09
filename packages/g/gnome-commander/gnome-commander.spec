#
# spec file for package gnome-commander
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


Name:           gnome-commander
Version:        1.16.0
Release:        0
Summary:        A file manager for the GNOME desktop environment
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            http://gcmd.github.io/
Source:         https://download.gnome.org/sources/gnome-commander/1.16/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM 96f706fa7833af79e01625c0118b36f6c83c7d44.patch luc14n0@opensuse.org -- Do not install the static libgcmd library
Patch0:         https://gitlab.gnome.org/GNOME/gnome-commander/-/commit/96f706fa7833af79e01625c0118b36f6c83c7d44.patch

%if 0%{?suse_version} < 1550
BuildRequires:  gcc11
BuildRequires:  gcc11-c++
%else
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
%endif
BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(exiv2) >= 0.14
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.0.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.24.0
BuildRequires:  pkgconfig(libgsf-1) >= 1.12.0
BuildRequires:  pkgconfig(poppler-glib) >= 0.18
BuildRequires:  pkgconfig(taglib) >= 1.4
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < 1.14.1
# For xdg-su
Recommends:     xdg-utils

%description
GNOME Commander is a "two-pane" graphical file manager for the Linux
desktop using GNOME libraries. In addition to basic file manager
functions, the program is also an FTP client and can browse SMB
networks.

%package devel
Summary:        Development files for %{name}

%description devel
Development files for %{name}.

%lang_package

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1550
export CC=%{_bindir}/gcc-11
export CXX=%{_bindir}/g++-11
%endif
%meson \
	-Dsamba=disabled \
	-Dunique=disabled \
	%{nil}
%meson_build

%install
%meson_install
find %{buildroot}%{_datadir} -size 0 -delete
%find_lang %{name} %{?no_lang_C}
%fdupes -s %{buildroot}%{_datadir}
%fdupes %{buildroot}%{_libdir}

%check
%meson_test

%files
%license COPYING
%doc NEWS README.md
%{_datadir}/help/C/%{name}
%{_datadir}/metainfo/org.gnome.%{name}.appdata.xml
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml
%{_datadir}/pixmaps/%{name}
%{_libdir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%{_datadir}/icons/hicolor/scalable/apps/gnome-commander-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/gnome-commander.svg

%files devel
%doc AUTHORS TODO
%{_includedir}/%{name}/
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/internal_viewer_hacking.txt
%{_datadir}/%{name}/keys.txt

%files lang -f %{name}.lang

%changelog
