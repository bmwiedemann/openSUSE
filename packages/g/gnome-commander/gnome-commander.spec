#
# spec file for package gnome-commander
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


Name:           gnome-commander
Version:        1.14.3
Release:        0
Summary:        A file manager for the GNOME desktop environment
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            http://gcmd.github.io/
Source:         https://download.gnome.org/sources/gnome-commander/1.14/%{name}-%{version}.tar.xz

%if 0%{?suse_version} < 1550
BuildRequires:  gcc11
BuildRequires:  gcc11-c++
%else
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
%endif
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  itstool
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(exiv2) >= 0.14
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.0.0
BuildRequires:  pkgconfig(gobject-2.0)
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

%lang_package

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1550
export CC=%{_bindir}/gcc-11
export CXX=%{_bindir}/g++-11
%endif
%configure\
	--disable-static \
	--without-unique \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot}%{_datadir} -size 0 -delete
%find_lang %{name} %{?no_lang_C}
%fdupes -s %{buildroot}%{_datadir}
%fdupes %{buildroot}%{_libdir}

%files
%license COPYING
%doc NEWS README
%doc AUTHORS ChangeLog TODO
%{_datadir}/help/C/%{name}
%{_datadir}/metainfo/org.gnome.%{name}.appdata.xml
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml
%{_datadir}/pixmaps/*.svg
%{_datadir}/pixmaps/%{name}
%{_libdir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%files lang -f %{name}.lang

%changelog
