#
# spec file for package healpix
#
# Copyright (c) 2024 SUSE LLC
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


%define cpkg chealpix
%define clib lib%{cpkg}0
%define cxxpkg healpix_cxx
%define cxxlib lib%{cxxpkg}4
Name:           healpix
Version:        3.83
Release:        0
Summary:        Data Analysis, Simulations and Visualization on the Sphere
License:        GPL-2.0-or-later
URL:            https://healpix.sourceforge.io
Source:         %{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(libsharp)
BuildRequires:  pkgconfig(zlib)

%description
HEALPix is a Hierarchical, Equal Area, and iso-Latitude Pixelation of the
sphere designed to support efficiently (1) local operations on the pixel set,
(2) a hierarchical tree structure for multi-resolution applications, and (3)
the global Fast Spherical Harmonic transform.

%package -n %{clib}
Summary:        Shared library for healpix - C bindings

%description -n %{clib}
HEALPix is a Hierarchical, Equal Area, and iso-Latitude Pixelation of the
sphere designed to support efficiently (1) local operations on the pixel set,
(2) a hierarchical tree structure for multi-resolution applications, and (3)
the global Fast Spherical Harmonic transform.

This package provides the shared library for the C bindings of healpix.

%package -n %{cpkg}-devel
Summary:        Headers and devel files for healpix - C bindings
Requires:       %{clib} = %{version}
Requires:       pkgconfig(cfitsio)
Requires:       pkgconfig(libsharp)

%description -n %{cpkg}-devel
HEALPix is a Hierarchical, Equal Area, and iso-Latitude Pixelation of the
sphere designed to support efficiently (1) local operations on the pixel set,
(2) a hierarchical tree structure for multi-resolution applications, and (3)
the global Fast Spherical Harmonic transform.

This package provides the headers and devel files for building apps with
healpix in the C language.

%package -n %{cxxlib}
Summary:        Shared library for healpix - C++ bindings

%description -n %{cxxlib}
HEALPix is a Hierarchical, Equal Area, and iso-Latitude Pixelation of the
sphere designed to support efficiently (1) local operations on the pixel set,
(2) a hierarchical tree structure for multi-resolution applications, and (3)
the global Fast Spherical Harmonic transform.

This package provides the shared library for the C++ bindings of healpix.

%package -n %{cxxpkg}-devel
Summary:        Headers and devel files for healpix - C++ bindings
Requires:       %{cxxlib} = %{version}
Requires:       pkgconfig(cfitsio)
Requires:       pkgconfig(libsharp)
Requires:       pkgconfig(zlib)

%description -n %{cxxpkg}-devel
HEALPix is a Hierarchical, Equal Area, and iso-Latitude Pixelation of the
sphere designed to support efficiently (1) local operations on the pixel set,
(2) a hierarchical tree structure for multi-resolution applications, and (3)
the global Fast Spherical Harmonic transform.

This package provides the headers and devel files for building apps with
healpix in the C++ language.

%prep
%autosetup -p1

%build
# Top-level configure script is useless, need to use individual dir scripts
for d in src/C/autotools src/cxx
do
pushd ${d}
autoreconf -fvi
%configure --disable-static
%make_build
popd
done

%install
for d in src/C/autotools src/cxx
do
pushd ${d}
%make_install
popd
done

find %{buildroot} -type f -name "*.la" -delete -print

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
for d in src/C/autotools src/cxx
do
pushd ${d}
%make_build check
popd
done

%post -n %{clib} -p /sbin/ldconfig
%postun -n %{clib} -p /sbin/ldconfig
%post -n %{cxxlib} -p /sbin/ldconfig
%postun -n %{cxxlib} -p /sbin/ldconfig

%files
%license COPYING READ_Copyrights_Licenses.txt
%doc README
%{_bindir}/*

%files -n %{clib}
%license COPYING READ_Copyrights_Licenses.txt
%{_libdir}/lib%{cpkg}.so.*

%files -n %{cpkg}-devel
%license COPYING READ_Copyrights_Licenses.txt
%{_libdir}/lib%{cpkg}.so
%{_libdir}/pkgconfig/%{cpkg}.pc
%{_includedir}/%{cpkg}.h

%files -n %{cxxlib}
%license COPYING READ_Copyrights_Licenses.txt
%{_libdir}/lib%{cxxpkg}.so.*

%files -n %{cxxpkg}-devel
%license COPYING READ_Copyrights_Licenses.txt
%{_libdir}/lib%{cxxpkg}.so
%{_libdir}/pkgconfig/%{cxxpkg}.pc
%{_includedir}/%{cxxpkg}/

%changelog
