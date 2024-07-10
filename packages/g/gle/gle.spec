#
# spec file for package gle
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


Name:           gle
%define lname   libgle3
Version:        3.1.2
Release:        0
Summary:        The GLE Tubing and Extrusion Library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://linas.org/gle/
#Git-Clone:     https://github.com/linas/glextrusion
Source:         https://github.com/linas/glextrusion/archive/refs/tags/%name-%version.tar.gz
Patch1:         gle-3.1.0-fltmax.diff
BuildRequires:  freeglut-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xmu)

%description
The GLE Tubing and Extrusion Library is a graphics application
programming interface (API). The library consists of a number of C
language subroutines for drawing tubing and extrusions. The library is
distributed in source code form in a package that includes
documentation, a VRML proposal, make files, and full source code and
header files. It uses the OpenGL (TM) programming API to perform the
actual drawing of the tubing and extrusions.

%package -n %lname
Summary:        The GLE Tubing and Extrusion Library
Group:          System/Libraries

%description -n %lname
The GLE Tubing and Extrusion Library is a graphics application
programming interface (API). The library consists of a number of C
language subroutines for drawing tubing and extrusions. The library is
distributed in source code form in a package that includes
documentation, a VRML proposal, make files, and full source code and
header files. It uses the OpenGL (TM) programming API to perform the
actual drawing of the tubing and extrusions.

%package devel
Summary:        Development files for the GLE tubing and extrusion library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Provides:       libgle-devel = %version-%release
Obsoletes:      libgle-devel < %version-%release

%description devel
The GLE Tubing and Extrusion Library is a graphics application
programming interface (API). The library consists of a number of C
language subroutines for drawing tubing and extrusions. The library is
distributed in source code form in a package that includes
documentation, a VRML proposal, make files, and full source code and
header files. It uses the OpenGL (TM) programming API to perform the
actual drawing of the tubing and extrusions.

%prep
%autosetup -p0 -n glextrusion-%name-%version

%build
autoreconf -fi
%configure --disable-static
%make_build

%check
%make_build check

%install
%make_install
rm -rf "%buildroot/%_datadir/doc/gle" "%buildroot/%_libdir"/*.la

%ldconfig_scriptlets -n %lname

%files -n %lname
%doc COPYING doc/COPYING.artistic
%{_libdir}/lib*.so.*

%files devel
%doc AUTHORS README doc/html/*.jpg doc/html/*.gif doc/html/*.html doc/html/README doc/gle-*.lsm
%doc %{_mandir}/man3/*
%{_includedir}/GL
%{_libdir}/lib*.so

%changelog
