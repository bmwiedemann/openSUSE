#
# spec file for package gl2ps
#
# Copyright (c) 2020 SUSE LLC
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


%define so_ver 1
Name:           gl2ps
Version:        1.4.2
Release:        0
Summary:        OpenGL to PostScript Printing Library
License:        LGPL-2.0-or-later OR SUSE-GL2PS-2.0
Group:          Development/Libraries/C and C++
URL:            http://www.geuz.org/gl2ps/
Source0:        http://geuz.org/gl2ps/src/%{name}-%{version}.tgz
BuildRequires:  cmake
BuildRequires:  freeglut-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(gl)

%description
GL2PS is a C library providing vector output for any OpenGL
application. It uses sorting algorithms capable of handling
intersecting and stretched polygons, as well as non-manifold objects.
GL2PS provides smooth shading and text rendering, culling of
invisible primitives and mixed vector/bitmap output.

GL2PS can create PostScript (PS), Encapsulated PostScript (EPS),
Portable Document Format (PDF) and Scalable Vector Graphics (SVG)
files, as well as LaTeX files for the text fragments. It also
provides limited, experimental support for Portable LaTeX Graphics
(PGF).

%package devel
Summary:        Development files for GL2PS
Group:          Development/Libraries/C and C++
Requires:       libgl2ps%{so_ver} = %{version}

%description devel
This package provides development libraries and headers needed to build
software using GL2PS.

%package -n libgl2ps%{so_ver}
Summary:        OpenGL to PostScript Printing Library
Group:          System/Libraries

%description -n libgl2ps%{so_ver}
GL2PS is a C library providing vector output for any OpenGL
application. It uses sorting algorithms capable of handling
intersecting and stretched polygons, as well as non-manifold objects.
GL2PS provides smooth shading and text rendering, culling of
invisible primitives and mixed vector/bitmap output.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
# Remove static libraries
rm -f %{buildroot}%{_libdir}/libgl2ps.a
# Remove doc files (they are installed in the %%files section)
rm -rf %{buildroot}%{_datadir}/doc/gl2ps/

%post -n libgl2ps%{so_ver} -p /sbin/ldconfig

%postun -n libgl2ps%{so_ver} -p /sbin/ldconfig

%files devel
%license COPYING.GL2PS COPYING.LGPL
%doc README.txt gl2ps.pdf gl2psTest*.c
%{_includedir}/gl2ps.h
%{_libdir}/libgl2ps.so

%files -n libgl2ps%{so_ver}
%{_libdir}/libgl2ps.so.%{so_ver}*

%changelog
