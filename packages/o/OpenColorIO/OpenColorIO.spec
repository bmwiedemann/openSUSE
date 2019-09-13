#
# spec file for package OpenColorIO
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019 Asterios Dramis <asterios.dramis@gmail.com>.
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
Name:           OpenColorIO
Version:        1.1.1
Release:        0
Summary:        Color Management Solution Geared Towards Motion Picture Production
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            http://opencolorio.org/
######
######
# The package contains the below non OSS licensed files (see bnc#821203)
#
# ext/Pygments-1.6/tests/examplefiles/Sorting.mod
# ext/Pygments-1.6/tests/examplefiles/test.mod
#
# so a crippled tarball is used with these files removed. Steps to reproduce:
#
# tar zxf OpenColorIO-%%{version}.tar.gz
# pushd OpenColorIO-%%{version}/ext/
# tar zxf Pygments-1.6.tar.gz
# rm -f Pygments-1.6.tar.gz
# rm -f Pygments-1.6/tests/examplefiles/{Sorting.mod,test.mod}
# tar zcf Pygments-1.6.tar.gz Pygments-1.6/
# rm -rf Pygments-1.6/
# popd
# tar zcf OpenColorIO-%%{version}-crippled.tar.gz OpenColorIO-%%{version}/
# rm -f OpenColorIO-%%{version}.tar.gz
#
# NOTE: In newer OpenColorIO versions, Pygments (version 1.6) maybe updated.
# In this case check if the above files' license is changed, so no crippled tarball is needed.
#####
#####
Source0:        %{name}-%{version}-crippled.tar.gz
# PATCH-FIX-UPSTREAM OpenColorIO-setuptools.patch asterios.dramis@gmail.com -- Use external python-setuptools for building (taken from Fedora)
Patch0:         OpenColorIO-setuptools.patch
# PATCH-FIX-UPSTREAM 0003-Fix_Linux_compilation.patch asterios.dramis@gmail.com -- Fix Linux compilation (taken from Debian)
Patch1:         0003-Fix_Linux_compilation.patch
# PATCH-FIX-UPSTREAM 0004-Fix_build_with_GCC-8.patch asterios.dramis@gmail.com -- Fix build with GCC-8 (taken from Debian)
Patch2:         0004-Fix_build_with_GCC-8.patch
# PATCH-FIX-UPSTREAM 0005-Fix_build_with_yaml-cpp0.6.patch asterios.dramis@gmail.com -- Fix build with yaml-cpp0.6 (taken from Debian)
Patch3:         0005-Fix_build_with_yaml-cpp0.6.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  liblcms2-devel
BuildRequires:  pkgconfig
BuildRequires:  python-MarkupSafe
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  tinyxml-devel
BuildRequires:  yaml-cpp-devel >= 0.5.0
Recommends:     %{name}-doc = %{version}

%description
OpenColorIO (OCIO) is a color management solution geared towards motion picture
production with an emphasis on visual effects and computer animation.

OCIO is compatible with the Academy Color Encoding Specification (ACES) and is
LUT-format agnostic, supporting many popular formats.

%package devel
Summary:        Development Files for OpenColorIO
Group:          Development/Libraries/C and C++
Requires:       libOpenColorIO%{so_ver} = %{version}
Recommends:     %{name}-doc = %{version}

%description devel
This package provides development libraries and headers needed to build
software using OpenColorIO.

%package doc
Summary:        Documentation for OpenColorIO
Group:          Documentation/Other
BuildArch:      noarch

%description doc
This package contains documentation for OpenColorIO.

%package -n libOpenColorIO%{so_ver}
Summary:        Complete Color Management Solution Geared Towards Motion Picture Production
Group:          System/Libraries

%description -n libOpenColorIO%{so_ver}
OpenColorIO (OCIO) is a color management solution geared towards motion picture
production with an emphasis on visual effects and computer animation.

OCIO is compatible with the Academy Color Encoding Specification (ACES) and is
LUT-format agnostic, supporting many popular formats.

%package -n python-OpenColorIO
Summary:        Python Bindings for OpenColorIO
Group:          Development/Libraries/Python

%description -n python-OpenColorIO
This package contains python bindings for OpenColorIO.

%package -n python-OpenColorIO-devel
Summary:        Python Bindings for OpenColorIO
Group:          Development/Libraries/Python
Requires:       python-OpenColorIO = %{version}
Requires:       python-devel

%description -n python-OpenColorIO-devel
This package contains development files for python bindings for OpenColorIO.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Make sure that bundled libraries are not used
rm -f ext/lcms*
rm -f ext/tinyxml*
rm -f ext/yaml*

%build
%cmake \
    -DOCIO_BUILD_STATIC=OFF \
    -DOCIO_BUILD_DOCS=ON \
    -DOCIO_BUILD_TESTS=ON \
    -DOCIO_PYGLUE_LINK=ON \
%ifnarch x86_64
    -DOCIO_USE_SSE=OFF \
%endif
    -DUSE_EXTERNAL_YAML=ON \
    -DUSE_EXTERNAL_TINYXML=ON \
    -DUSE_EXTERNAL_LCMS=ON \
    -DUSE_EXTERNAL_SETUPTOOLS=ON \
    ..
%make_jobs

%install
%cmake_install

# Move documentation to the right location
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/OpenColorIO/html/ %{buildroot}%{_docdir}/%{name}/

# Move cmake files to the right location
mkdir -p %{buildroot}%{_datadir}/cmake/Modules
mv %{buildroot}%{_prefix}/*.cmake %{buildroot}%{_prefix}/cmake/*.cmake %{buildroot}%{_datadir}/cmake/Modules/

%post -n libOpenColorIO%{so_ver} -p /sbin/ldconfig
%postun -n libOpenColorIO%{so_ver} -p /sbin/ldconfig

%files
%license LICENSE
%doc ChangeLog README.md
%exclude %{_docdir}/%{name}/html/
%{_bindir}/*
%{_datadir}/ocio/

%files devel
%{_datadir}/cmake/Modules/*
%{_includedir}/OpenColorIO/
%{_libdir}/pkgconfig/OpenColorIO.pc
%{_libdir}/*.so

%files doc
%{_docdir}/%{name}/html/

%files -n libOpenColorIO%{so_ver}
%{_libdir}/libOpenColorIO.so.%{so_ver}*

%files -n python-OpenColorIO
%{python_sitearch}/PyOpenColorIO.so

%files -n python-OpenColorIO-devel
%{_includedir}/PyOpenColorIO/

%changelog
