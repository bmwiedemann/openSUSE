#
# spec file for package gerbv
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        2.13.0
Release:        0
%define somajor 1
Summary:        Gerber File Viewer that supports the RS-274X Standard
License:        GPL-2.0-only
URL:            http://gerbv.geda-project.org/
Source0:        https://github.com/gerbv/gerbv/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         gerbv-build-with-g++-13.patch
Patch2:         gerbv-remove-unused-code.patch
Patch3:         gerbv-desktop-categories.patch
BuildRequires:  cmake
%if 0%{?suse_version} >= 1600
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc13-c++
%endif
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libpng)

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

%description -n %{libname}%{somajor}
Gerbv library, allows developers to include parsing, editing, exporting,
rendering of Gerber files into other programs.

%package        devel
Summary:        Gerber File Viewer that supports the RS-274X Standard
Requires:       %{libname}%{somajor} = %{version}
Requires:       pkgconfig(gtk+-2.0)
Requires:       pkgconfig(libpng)

%description    devel
This package contains development files for developing applications
that use gerbv library.

%prep
%setup -q
%if 0%{?suse_version} < 1600
%patch -P 1 -p1
%endif
%patch -P 2 -p1
%patch -P 3 -p1

%build
%cmake --preset linux-gnu-gcc
%cmake_build

%install
%cmake_install

find %{buildroot}%{_libdir} -name '*.a' -type f -delete -print

%find_lang %{name}

%check

%post -n %{libname}%{somajor} -p /sbin/ldconfig

%postun -n %{libname}%{somajor} -p /sbin/ldconfig

%files -f %{name}.lang
%license COPYING
%doc AUTHORS BUGS CONTRIBUTORS HACKING README.md
%doc example
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_datadir}/%{name}/
%{_datadir}/icons/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.geda-user.%{name}.gschema.xml

%files -n %{libname}%{somajor}
%{_libdir}/%{libname}.so.%{somajor}*

%files devel
%dir %{_includedir}/gerbv/
%{_includedir}/gerbv/gerbv.h
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc

%changelog
