#
# spec file for package glu
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           glu
%define lname	libGLU1
Version:        9.0.3
Release:        0
Summary:        OpenGL utility library
License:        SGI-B-2.0
Group:          Development/Libraries/C and C++
URL:            http://cgit.freedesktop.org/mesa/glu/

#Git-Clone:	git://anongit.freedesktop.org/mesa/glu
#Git-Web:	http://cgit.freedesktop.org/mesa/glu/
Source:         https://mesa.freedesktop.org/archive/glu/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gl)

%description
GLU offers simple interfaces for building mipmaps; checking for the
presence of extensions in the OpenGL (or other libraries which follow
the same conventions for advertising extensions); drawing
piecewise-linear curves, NURBS, quadrics and other primitives
(including, but not limited to, teapots); tesselating surfaces;
setting up projection matrices and unprojecting screen coordinates to
world coordinates.

%package -n %lname
Summary:        OpenGL utility library
# O/P since 12.3. This Obsoletes is special (since glu is in fact Mesa),
# and should not be copy-pasted without review.
Group:          System/Libraries
Obsoletes:      Mesa-libGLU1 < %version-%release
Provides:       Mesa-libGLU1 = %version-%release

%description -n %lname
GLU offers simple interfaces for building mipmaps; checking for the
presence of extensions in the OpenGL (or other libraries which follow
the same conventions for advertising extensions); drawing
piecewise-linear curves, NURBS, quadrics and other primitives
(including, but not limited to, teapots); tesselating surfaces;
setting up projection matrices and unprojecting screen coordinates to
world coordinates.

This package provides the SGI implementation of GLU previously shipped
with Mesa, but meanwhile developed separately.

%package devel
Summary:        Development files for the GLU API
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       pkgconfig(gl)
# O/P since 12.3
Obsoletes:      Mesa-libGLU-devel < %version-%release
Provides:       Mesa-libGLU-devel = %version-%release

%description devel
GLU offers simple interfaces for building mipmaps; checking for the
presence of extensions in the OpenGL (or other libraries which follow
the same conventions for advertising extensions); drawing
piecewise-linear curves, NURBS, quadrics and other primitives
(including, but not limited to, teapots); tesselating surfaces;
setting up projection matrices and unprojecting screen coordinates to
world coordinates.

This package contains includes headers and static libraries for
compiling programs with GLU.

%prep
%setup -q
cat > LICENSE << EOF
SGI FREE SOFTWARE LICENSE B
(Version 2.0, Sept. 18, 2008)

Copyright (C) [dates of first publication] Silicon Graphics, Inc. All Rights
Reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice including the dates of first publication and either
this permission notice or a reference to http://oss.sgi.com/projects/FreeB/
shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
SILICON GRAPHICS, INC. BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Except as contained in this notice, the name of Silicon Graphics, Inc. shall
not be used in advertising or otherwise to promote the sale, use or other
dealings in this Software without prior written authorization from Silicon
Graphics, Inc.
EOF

%build
%meson -Ddefault_library=shared
%meson_build

%install
%meson_install

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%license LICENSE
%_libdir/libGLU.so.*

%files devel
%defattr(-,root,root)
%_includedir/GL
%_libdir/libGLU.so
%_libdir/pkgconfig/glu.pc

%changelog
