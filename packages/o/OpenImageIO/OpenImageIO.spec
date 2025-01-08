#
# spec file for package OpenImageIO
#
# Copyright (c) 2025 SUSE LLC
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


%ifarch aarch64 %{arm}
%bcond_with imageviewer
%else
%bcond_without imageviewer
%endif
%if 0%{?suse_version} > 1500
%bcond_without libheif
%else
%bcond_with libheif
%endif
%bcond_without opencv
%bcond_without python_bindings
%bcond_with apidocs
%bcond_with ptex

%define images_ts 20241104T095817
%define so_ver 2_5
%define major_minor_ver 2.5
Name:           OpenImageIO
Version:        2.5.18.0
Release:        0
Summary:        Library for Reading and Writing Images
License:        BSD-3-Clause
Group:          Productivity/Graphics/Other
URL:            https://www.openimageio.org/
Source0:        https://github.com/AcademySoftwareFoundation/OpenImageIO/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# this contains the actual test images, only used during build
Source1:        oiio-images-%{images_ts}.tar.xz
# NOTE: Please don't uncomment a build requirement unless you have submitted the package to factory and it exists
#BuildRequires:  Field3D-devel
BuildRequires:  cmake >= 3.18.2
BuildRequires:  dcmtk-devel
%if %{with apidocs}
BuildRequires:  doxygen
%endif
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel >= 5.0
BuildRequires:  hdf5-devel
# can be dropped when upgrading to 3.x again
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
#/ can be dropped when upgrading to 3.x again
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel >= 1.6.0
BuildRequires:  openvdb-devel >= 9.0
BuildRequires:  pkgconfig
BuildRequires:  pugixml-devel
%if %{with python_bindings}
BuildRequires:  python3-devel >= 3.7
BuildRequires:  python3-pybind11-devel >= 2.7
# required for testsuite
BuildRequires:  python3-numpy
%endif
BuildRequires:  robin-map-devel >= 1.2.0
BuildRequires:  tbb-devel
BuildRequires:  txt2man
BuildRequires:  pkgconfig(OpenColorIO) >= 2.2
BuildRequires:  pkgconfig(OpenEXR) >= 3.1
%if %{with ptex}
BuildRequires:  ptex-devel-static
%endif
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(freetype2) >= 2.10
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libjxl)
%if %{with libheif}
BuildRequires:  pkgconfig(libheif) >= 1.11
%endif
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libxml-2.0)
%if %{with imageviewer}
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Widgets)
%endif
BuildRequires:  pkgconfig(libraw) >= 0.20
BuildRequires:  pkgconfig(libtiff-4) > 4.0
BuildRequires:  pkgconfig(libwebp) >= 1.1
BuildRequires:  pkgconfig(libwebpdecoder)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(libwebpmux)
%if %{with opencv}
BuildRequires:  pkgconfig(opencv4)
%endif
BuildRequires:  pkgconfig(zlib)
Recommends:     google-droid-fonts

%description
OpenImageIO is a library for reading and writing images, and a bunch of related
classes, utilities, and applications. There is a particular emphasis on formats
and functionality used in professional, large-scale animation and visual
effects work for film. OpenImageIO is used extensively in animation and VFX
studios all over the world, and is also incorporated into several commercial
products.

%package devel
Summary:        Development Files for OpenImageIO
Group:          Development/Libraries/C and C++
# Make the cmake finder happy
Requires:       OpenImageIO = %{version}
Requires:       pkgconfig(Imath)
# /Make the cmake finder happy
Requires:       fmt-devel
Requires:       libOpenImageIO%{so_ver} = %{version}
Requires:       libOpenImageIO_Util%{so_ver} = %{version}
Suggests:       %{name}-devel-doc

%description devel
This package provides development libraries and headers needed to build
software using OpenImageIO.

%package devel-doc
Summary:        API documentation for OpenImageIO
Group:          Productivity/Graphics/Other
Requires:       %{name}-devel
BuildArch:      noarch

%description devel-doc
This package provides the API documentation for OpenImageIO.

%package -n libOpenImageIO%{so_ver}
Summary:        Library for Reading and Writing Images
Group:          System/Libraries
# this is unfortunate and a fallout of properly naming the lib after fixing so_ver
Conflicts:      libOpenColorIO2_0 = 2.1.1
Conflicts:      libOpenColorIO2_0 = 2.1.2

%description -n libOpenImageIO%{so_ver}
OpenImageIO is a library for reading and writing images, and a bunch of related
classes, utilities, and applications. There is a particular emphasis on formats
and functionality used in professional, large-scale animation and visual
effects work for film. OpenImageIO is used extensively in animation and VFX
studios all over the world, and is also incorporated into several commercial
products.

%package -n libOpenImageIO_Util%{so_ver}
Summary:        Library for Reading and Writing Images
Group:          System/Libraries

%description -n libOpenImageIO_Util%{so_ver}
OpenImageIO is a library for reading and writing images, and a bunch of related
classes, utilities, and applications. There is a particular emphasis on formats
and functionality used in professional, large-scale animation and visual
effects work for film. OpenImageIO is used extensively in animation and VFX
studios all over the world, and is also incorporated into several commercial
products.

%package -n python3-OpenImageIO
Summary:        Python Bindings for OpenImageIO
Group:          Development/Libraries/Python

%description -n python3-OpenImageIO
This package contains python bindings for OpenImageIO.

%prep
%autosetup -p1 -b 1
# CMake looks for images at <CMAKE_BINARY_DIR>/testsuite/oiio-images
mkdir -p %{__builddir}/testsuite
ln -sf %{_builddir}/oiio-images-%{images_ts} %{__builddir}/testsuite/oiio-images

# Make sure that bundled libraries are not used
rm -f src/include/pugiconfig.hpp \
      src/include/pugixml.hpp
rm -rf src/include/tbb/

find . -iname \*.py -print -exec sed -i '1s@^#!.*@#!%{_bindir}/python3@' '{}' \;

%build
%cmake \
%ifarch ppc
    -DNOTHREADS=ON \
%endif
    -DCMAKE_CXX_STANDARD=17 \
    -DINSTALL_DOCS:BOOL=ON \
    -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
    -DCMAKE_INSTALL_MANDIR:PATH=%{_mandir}/man1 \
    -DINSTALL_FONTS:BOOL=OFF \
    -DLINKSTATIC:BOOL=OFF \
    -DUSE_EXTERNAL_PUGIXML:BOOL=ON \
    -DUSE_FFMPEG:BOOL=ON \
    -DUSE_Nuke:BOOL=OFF \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DUSE_OPENCV:BOOL=%{?with_opencv:ON}%{!?with_opencv:OFF} \
    -DUSE_PYTHON:BOOL=%{?with_python_bindings:ON}%{!?with_python_bindings:OFF} \
    -DUSE_Ptex:BOOL=%{?with_ptex:ON}%{!?with_ptex:OFF} \
    -DPYTHON_EXECUTABLE:PATH=%{_bindir}/python3 \
    -DPLUGIN_SEARCH_PATH:PATH=%{_libdir}/%{name}-%{major_minor_ver} \
    ..
%cmake_build

%if %{with apidocs}
cd ..
make %{?_smp_mflags} doxygen
%endif

%install
%cmake_install

# Create and own the default plugin directory
mkdir -p %{buildroot}%{_libdir}/%{name}-%{major_minor_ver}

%if %{with apidocs}
# Install additional devel documentation
cp -a src/doc/doxygen/html/ %{buildroot}%{_docdir}/%{name}-devel/
%endif

# Clean up licenses installed in _licensedir
rm %{buildroot}%{_docdir}/%{name}/LICENSE*md

%fdupes -s %{buildroot}

%check
# Make sure testsuite can find required fonts
mkdir -p ~/fonts
ln -sf $(pwd)/src/fonts/Droid_Serif/DroidSerif.ttf ~/fonts/DroidSerif.ttf
ln -sf $(pwd)/src/fonts/Droid_Sans/DroidSans.ttf ~/fonts/DroidSans.ttf
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
# used as suffix for python binary
export PYTHON_VERSION=3
export PYTHONPATH=%{buildroot}%{python3_sitearch}
export PYTHONDONTWRITEBYTECODE=1
# Exclude known broken tests
# timer tests won't do reliably in OBS
%define disabled_tests 'cmake-consumer|docs-examples-cpp|oiiotool|oiiotool-copy|oiiotool-subimage|oiiotool-text|texture-udim|texture-udim2|texture-udim.batch|texture-udim2.batch|docs-examples-python|python-texturesys|python-imagebufalgo|heif|ptex-broken|oiiotool|oiiotool-copy|oiiotool-subimage|texture-udim|texture-udim2|texture-udim.batch|texture-udim2.batch|python-texturesys'
%define texture_tests  'texture-icwrite'
%ifarch x86_64
%ctest '-E' %{disabled_tests}
%ctest '-R' %{texture_tests} || true
#%%ctest '-j1' '-R' 'unit_timer'
%else
# Many test cases are failing on PPC, ARM, ix64 ... ignore for now
%ctest '-E' %{disabled_tests} || true
%ctest '-R' %{texture_tests} || true
#%%ctest '-j1' '-R' 'unit_timer'
%endif

%ldconfig_scriptlets -n libOpenImageIO%{so_ver}
%ldconfig_scriptlets -n libOpenImageIO_Util%{so_ver}

%files
%doc CHANGES.md CREDITS.md README.md THIRD-PARTY.md
%doc src/doc/CHANGES-0.x.md src/doc/CHANGES-1.x.md
%license LICENSE.md
%{_bindir}/*
%{_mandir}/man1/*.1%{ext_man}

%if %{with apidocs}
%files devel-doc
%doc %{_docdir}/%{name}-devel/
%endif

%files devel
%{_includedir}/%{name}
%{_libdir}/pkgconfig/OpenImageIO.pc
%{_libdir}/cmake
%{_libdir}/libOpenImageIO.so
%{_libdir}/libOpenImageIO_Util.so

%files -n lib%{name}%{so_ver}
%{_libdir}/lib%{name}.so.*
%dir %{_libdir}/%{name}-%{major_minor_ver}

%files -n lib%{name}_Util%{so_ver}
%{_libdir}/lib%{name}_Util.so.*

%if %{with python_bindings}
%files -n python3-%{name}
%dir %{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}/__init__.py
%{python3_sitearch}/%{name}/%{name}.*.so
%endif

%changelog
