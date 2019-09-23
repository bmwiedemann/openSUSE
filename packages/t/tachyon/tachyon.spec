#
# spec file for package tachyon
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           tachyon
%define lname	libtachyon-0_99b6
Version:        0.99~b6
Release:        0
Summary:        Parallel ray tracing system
License:        BSD-3-Clause
Group:          Productivity/Graphics/Visualization/Raytracers
Url:            http://jedi.ks.uiuc.edu/~johns/raytracer/

Source:         http://jedi.ks.uiuc.edu/~johns/raytracer/files/0.99b6/tachyon-0.99b6.tar.gz
Patch1:         tachyon-automake.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake >= 1.10
BuildRequires:  libjpeg-devel
BuildRequires:  libtool >= 2
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(x11)

%description
A high performance parallel ray tracing system supporting MPI and
multithreaded implementations.

Tachyon implements all of the basic geometric primitives such as
triangles, planes, spheres, cylinders, etc. Some of the goals in
developing Tachyon were to make it fast and for it to parallelize
well. These are what set it apart from more full-featured programs
like POV-Ray, Rayshade, and others. Tachyon supports enough features
to be an excellent alternative to slower programs for demanding
animation and scientific visualization tasks.

%package -n %lname
Summary:        Core library for the Tachyon Parallel Ray Tracing System
Group:          System/Libraries

%description -n %lname
A high performance parallel ray tracing system supporting MPI and
multithreaded implementations.

Tachyon implements all of the basic geometric primitives such as
triangles, planes, spheres, cylinders, etc. Some of the goals in
developing Tachyon were to make it fast and for it to parallelize
well. These are what set it apart from more full-featured programs
like POV-Ray, Rayshade, and others. Tachyon supports enough features
to be an excellent alternative to slower programs for demanding
animation and scientific visualization tasks.

%package -n libtachyon-devel
Summary:        Development files for the Tachyon Ray Tracing System
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description -n libtachyon-devel
A high performance parallel ray tracing system supporting MPI and
multithreaded implementations.

Tachyon implements all of the basic geometric primitives such as
triangles, planes, spheres, cylinders, etc. Some of the goals in
developing Tachyon were to make it fast and for it to parallelize
well. These are what set it apart from more full-featured programs
like POV-Ray, Rayshade, and others. Tachyon supports enough features
to be an excellent alternative to slower programs for demanding
animation and scientific visualization tasks.

%prep
%setup -qn %name
%patch -P 1 -p1

%build
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags}

%install
b="%buildroot"
mkdir -p "$b/%_includedir/tachyon"
for i in tachyon.h tachyon_dep.h hash.h macros.h render.h quadric.h texture.h light.h util.h; do
	install -pm 0644 "src/$i" "$b/%_includedir/tachyon/$i"
done
%make_install
rm -f "$b/%_libdir"/*.la

%files
%defattr(-,root,root)
%_bindir/tachyon

%files -n %lname
%defattr(-,root,root)
%_libdir/libtachyon-*.so

%files -n libtachyon-devel
%defattr(-,root,root)
%_libdir/libtachyon.so
%_includedir/tachyon/

%changelog
