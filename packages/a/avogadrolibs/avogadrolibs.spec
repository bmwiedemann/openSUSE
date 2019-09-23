#
# spec file for package avogadrolibs
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


Name:           avogadrolibs
Version:        0.9.0
Release:        0
Summary:        Molecular simulation and visualization environment
# License note: There are GPL plugins in the source, but they are neither built nor installed by the package
License:        BSD-3-Clause
Group:          Productivity/Scientific/Other
URL:            http://www.openchemistry.org/projects/avogadro2
Source:         https://sourceforge.net/projects/avogadro/files/avogadro2/%{version}/%{name}-%{version}.tar.gz
#PATCH-FIX-OPENSUSE -- 0002-create-soversion-libs.patch tittiatcoke@gmail.com -- Make the libs versioned
Patch0:         0002-create-soversion-libs.patch
#PATCH-FIX-OPENSUSE -- fix-linking-issues.patch tittiatcoke@gmail.com -- Ensure that the qtplugins are linked properly
Patch1:         fix-linking-issues.patch
#PATCH-FIX-OPENSUSE -- use-system-libjsoncpp.patch tittiatcoke@gmail.com -- Use the system libjsoncpp
Patch2:         use-system-libjsoncpp.patch
#PATCH-FIX-UPSTREAM fix-gcc-version-check.patch
Patch3:         fix-gcc-version-check.patch
# PATCH-FIX-UPSTREAM -- Fix-build-with-Qt-511.patch
Patch4:         Fix-build-with-Qt-511.patch
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  glu-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libSM-devel
BuildRequires:  libXt-devel
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
In order to tackle molecular simulation and visualization challenges in key areas of materials
science, chemistry and biology it is necessary to move beyond fixed software applications. The
Avogadro project is in the final stages of an ambitious rewrite of its core data structures,
algorithms and visualization capabilities. The project began as a grass roots effort to address
deficiencies observed by many of the early contributors in existing commercial and open source
solutions. Avogadro is now a robust, flexible solution that can tie in to and harness the power of
VTK for additional analysis and visualization capabilities.

%package -n libavogadrolibs-suse0
Summary:        Main libraries for Avogadro
Group:          System/Libraries
Requires:       %{name}

%description -n libavogadrolibs-suse0
This package contains the main Avogadros libraries.

%package devel
Summary:        Development files for Avogadro
Group:          Development/Libraries/C and C++
Requires:       libavogadrolibs-suse0 = %{version}

%description devel
This package contains files to develop applications using
Avogadros libraries.

%prep
%autosetup -p1

# Remove unnecessary bits
# This file is part of the standard cmake install
rm cmake/GenerateExportHeader.cmake
# No longer needed when building against system libjsoncpp
rm -rf thirdparty/jsoncpp
rm thirdparty/CMakeLists.txt

%build
mkdir -p build
pushd build
# FIXME: you should use %%cmake macros
cmake ../ -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_SKIP_RPATH=YES -DBUILD_GPL_PLUGINS=OFF  \
      -DCMAKE_C_FLAGS="%{optflags} -DNDEBUG" \
      -DCMAKE_CXX_FLAGS="%{optflags} -DNDEBUG" \
      -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-Bsymbolic-functions" \
      -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-Bsymbolic-functions" \
      -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-Bsymbolic-functions" \
      -DCMAKE_VERBOSE_MAKEFILE=ON \
      -DINSTALL_DOC_DIR=%{_defaultdocdir} \
      -DBUILD_STATIC_PLUGINS=OFF -DUSE_QT=ON -DUSE_OPENGL=ON -DUSE_MOLEQUEUE=OFF
popd

pushd build
make %{?_smp_mflags}
popd

%install
pushd build
%make_install
popd
%fdupes %{buildroot}

%post   -n libavogadrolibs-suse0 -p /sbin/ldconfig
%postun -n libavogadrolibs-suse0 -p /sbin/ldconfig

%files
%doc %{_defaultdocdir}/%{name}
%license COPYING
%doc README.md
%{_libdir}/avogadro2/

%files -n libavogadrolibs-suse0
%license COPYING
%{_libdir}/libAvogadro*.so.suse0*

%files devel
%license COPYING
%{_includedir}/avogadro/
%{_libdir}/cmake/avogadrolibs/
%{_libdir}/libAvogadro*.so

%changelog
