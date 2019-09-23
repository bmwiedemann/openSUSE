#
# spec file for package occt
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           occt
Version:        7.3.0
Release:        0
%define soname 7
Summary:        OpenCASCADE Official Edition
License:        LGPL-2.1 WITH OCCT-exception-1.0
Group:          Productivity/Graphics/CAD
Url:            http://www.opencascade.org/
# Password protected URL, factory validation will fail
# https://www.opencascade.com/sites/default/files/private/occt/OCC_%{version}_release/opencascade-%{version}.tgz
Source0:        opencascade-%{version}.tgz
Patch1:         fix_build.patch
Patch2:         enable-exceptions.patch
Patch3:         use-local-mathjax.patch
Provides:       OpenCASCADE = %{version}
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  mathjax
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
#Requires:       tcsh

%description
OpenCASCADE is a suite for 3D surface and solid modeling, visualization, data
exchange and rapid application development. It is an excellent platform for
development of numerical simulation software including CAD/CAM/CAE, AEC and
GIS, as well as PDM applications.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Provides:       OpenCASCADE-devel = %{version}
Requires:       %{name} = %{version}
Requires:       %{name}-DRAWEXE = %{version}
Requires:       freetype2-devel
Requires:       libopencascade%{soname} = %{version}
Requires:       tcl-devel
Requires:       tk-devel
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glu)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xext)
Requires:       pkgconfig(xmu)
Requires:       pkgconfig(xt)
Conflicts:      oce-devel

%description devel
This package contains the files needed for development with OpenCASCADE.

%package devel-doc
BuildArch:      noarch
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++

%description devel-doc
Developer documentation for OpenCASCADE

%package -n libopencascade%{soname}
Summary:        OpenCASCADE libraries
Group:          Development/Libraries/C and C++

%description -n libopencascade%{soname}
This package contain the needed libraries for OpenCASCADE

%package DRAWEXE
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Conflicts:      oce-DRAWEXE

%description DRAWEXE
This package contains the DRAWEXE executable of OpenCASCADE.

%prep
%setup -q -n opencascade-%{version}
%patch1 -p0
%patch2 -p0
%patch3 -p0
# update patch if the path is not matching anymore
[ -e /usr/share/javascript/mathjax/MathJax.js ] || exit 1

%build
mkdir build && cd build
cmake -DCMAKE_C_FLAGS:"STRING=$RPM_OPT_FLAGS" \
  -DCMAKE_CXX_FLAGS:"STRING=$RPM_OPT_FLAGS" \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_SKIP_RPATH=ON \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_libdir}" == "/usr/lib64"
  -DLIB_SUFFIX=64 \
%endif
  ..
make %{?_smp_mflags}

cd ..
./gendoc -refman
# fix permission bits
find doc README.txt LICENSE_LGPL_21.txt OCCT_LGPL_EXCEPTION.txt -type f | xargs chmod 0644

%install
cd build
make install DESTDIR=%buildroot

chmod 0755 %buildroot/usr/bin/*

# fixing up broken files
mv %buildroot/usr/lib/cmake/opencascade/OpenCASCADECompileDefinitionsAndFlags-relwithdebinfo.cmake/OpenCASCADECompileDefinitionsAndFlags-relwithdebinfo.cmake w
rmdir %buildroot/usr/lib/cmake/opencascade/OpenCASCADECompileDefinitionsAndFlags-relwithdebinfo.cmake
mv -v w %buildroot/usr/lib/cmake/opencascade/OpenCASCADECompileDefinitionsAndFlags-relwithdebinfo.cmake
if [ "%_libdir" == "/usr/lib64" ] ;then
  mkdir -p %buildroot/usr/lib64
  mv %buildroot/usr/lib/lib* %buildroot/usr/lib64/
  sed -i -e 's,lib\\${OCCT_INSTALL_BIN_LETTER}/,lib64/,' %buildroot%{_prefix}/lib/cmake/*/*
else
  sed -i -e 's,lib\\${OCCT_INSTALL_BIN_LETTER}/,lib/,' %buildroot%{_prefix}/lib/cmake/*/*
fi

rm -rf %buildroot/usr/share/doc

%fdupes -s %{buildroot}

%post -n libopencascade%{soname} -p /sbin/ldconfig

%postun -n libopencascade%{soname} -p /sbin/ldconfig

%files
%license LICENSE_LGPL_21.txt OCCT_LGPL_EXCEPTION.txt
%doc README.txt

%files -n libopencascade%{soname}
%_libdir/lib*.so.%{soname}*

%files DRAWEXE
/usr/bin/DRAWEXE*

%files devel
/usr/bin/custom*
/usr/bin/draw.sh
/usr/bin/env.sh
/usr/include/opencascade
/usr/share/opencascade
/usr/lib/cmake
%_libdir/lib*.so

%files devel-doc
%doc doc/refman/html

%changelog
