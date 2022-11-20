#
# spec file for package gerbv
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


Name:           gerbv
%define libname lib%{name}
Version:        2.9.4
Release:        0
%define somajor 1
Summary:        Gerber File Viewer that supports the RS-274X Standard
License:        GPL-2.0-only
Group:          Productivity/Scientific/Electronics
URL:            http://gerbv.geda-project.org/
Source0:        https://github.com/gerbv/gerbv/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  opensp
BuildRequires:  pkgconfig
BuildRequires:  po4a
BuildRequires:  update-desktop-files

%description
Gerber Viewer (gerbv) is a viewer for Gerber files. Gerber files are
generated from PCB CAD system and sent to PCB manufacturers as basis
for the manufacturing process. The standard supported by gerbv is
RS-274X. The basic difference between RS-274D (the old standard) and
RS-274X is basically the addition of apertures in RS-274X. It might be
possible to make an RS-274X file out of an RS-274D file and an
aperture list.

%package -n     %{libname}%{somajor}
Summary:        Gerber File Viewer library
Group:          System/Libraries

%description -n %{libname}%{somajor}
Gerbv library , allows developers to include parsing, editing, exporting,
rendering of Gerber files into other programs.

%package        devel
Summary:        Gerber File Viewer that supports the RS-274X Standard
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{somajor} = %{version}
Requires:       gtk2-devel
Requires:       libpng-devel

%description    devel
This package contains development files for developing applications
that use gerbv library.

%prep
%autosetup -p1

%build
./autogen.sh
%configure  \
            --disable-static \
            --enable-unit-mm \
            --disable-update-desktop-database

%make_build

%install
%make_install
%suse_update_desktop_file -r %{name} Education Engineering
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

#move translated man page
mkdir -p %{buildroot}/%{_mandir}/ru/man1
mv %{buildroot}/%{_mandir}/man1/%{name}.ru.1 %{buildroot}/%{_mandir}/ru/man1/%{name}.1

%find_lang %{name}

%post -n %{libname}%{somajor} -p /sbin/ldconfig

%postun -n %{libname}%{somajor} -p /sbin/ldconfig

%files -f %{name}.lang
%license COPYING
%doc NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_mandir}/*/man1/%{name}*
%{_datadir}/%{name}/
%{_datadir}/icons/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.geda-user.%{name}.gschema.xml

%files -n %{libname}%{somajor}
%{_libdir}/%{libname}.so.%{somajor}*

%files devel
%{_includedir}/*
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc

%changelog
