#
# spec file for package tachyon
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


Name:           tachyon
%define lname	libtachyon-0_99_5
Version:        0.99.5
Release:        0
Summary:        Parallel ray tracing system
License:        BSD-3-Clause
Group:          Productivity/Graphics/Visualization/Raytracers
URL:            http://jedi.ks.uiuc.edu/~johns/raytracer/

Source:         http://jedi.ks.uiuc.edu/~johns/raytracer/files/%version/tachyon-%version.tar.gz
Patch1:         tachyon-automake.diff
BuildRequires:  autoconf
BuildRequires:  automake >= 1.10
BuildRequires:  libjpeg-devel
BuildRequires:  libtool >= 2
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(x11)

%description
A parallel ray tracing system supporting MPI and multithreaded
implementations.

Tachyon implements the basic geometric primitives such as triangles,
planes, spheres, cylinders, etc. Tachyon parallelizes unlike POV-Ray
and Rayshade.

%package -n %lname
Summary:        Core library for the Tachyon Parallel Ray Tracing System
Group:          System/Libraries

%description -n %lname
A parallel ray tracing system supporting MPI and multithreaded
implementations.

Tachyon implements the basic geometric primitives such as triangles,
planes, spheres, cylinders, etc. Tachyon parallelizes unlike POV-Ray
and Rayshade.

%package devel
Summary:        Development files for the Tachyon Ray Tracing System
Group:          Development/Libraries/C and C++
Requires:       %lname = %version-%release
Obsoletes:      libtachyon-devel < %version-%release
Provides:       libtachyon-devel = %version-%release

%description devel
A parallel ray tracing system supporting MPI and multithreaded
implementations.

This package contains the headers for the Tachyon library.

%prep
%autosetup -p1 -n %name

%build
autoreconf -fi
%configure --disable-static
%make_build

%install
b="%buildroot"
mkdir -p "$b/%_includedir/tachyon"
for i in tachyon.h tachyon_dep.h hash.h macros.h render.h quadric.h texture.h light.h util.h; do
	install -pm 0644 "src/$i" "$b/%_includedir/tachyon/$i"
done
%make_install
rm -f "$b/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%_bindir/tachyon
%license Copyright

%files -n %lname
%_libdir/libtachyon-*.so

%files devel
%_libdir/libtachyon.so
%_includedir/tachyon/

%changelog
