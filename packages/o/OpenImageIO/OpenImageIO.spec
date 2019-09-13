#
# spec file for package OpenImageIO
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


%ifarch aarch64 %{arm}
%bcond_with imageviewer
%else
%bcond_without imageviewer
%endif

%define so_ver 1_8
%global gccv %(gcc  -dumpversion)
Name:           OpenImageIO
Version:        1.8.17
Release:        0
Summary:        Library for Reading and Writing Images
License:        BSD-3-Clause
Group:          Productivity/Graphics/Other
Url:            http://www.openimageio.org/
Source0:        https://github.com/OpenImageIO/oiio/archive/Release-%{version}.tar.gz#/oiio-Release-%{version}.tar.gz
Patch0:         oiio-clusterfit-boundscheck.patch
Patch1:         oiio-detectplatform-others.patch
Patch2:         oiio_gcc6_missleading_indentation.patch
Patch3:         oiio-add-libdl-for-plugin.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  hdf5-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  pugixml-devel
BuildRequires:  txt2man
BuildRequires:  pkgconfig(IlmBase)
# NOTE: Please don't uncomment a build requirement unless you have submitted the package to factory and it exists
#BuildRequires:  Field3D-devel
BuildRequires:  pkgconfig(OpenColorIO)
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libopenjpeg)
BuildRequires:  pkgconfig(libopenjpeg1)
%if %{with imageviewer}
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5Widgets)
%endif
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libraw_r)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpdecoder)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(libwebpmux)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
Recommends:     google-droid-fonts
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%else
BuildRequires:  boost-devel
%endif

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
Requires:       libOpenImageIO%{so_ver} = %{version}
Requires:       libOpenImageIO_Util%{so_ver} = %{version}

%description devel
This package provides development libraries and headers needed to build
software using OpenImageIO.

%package -n libOpenImageIO%{so_ver}
Summary:        Library for Reading and Writing Images
Group:          System/Libraries

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

%if 1 == 0
%package -n python-OpenImageIO
Summary:        Python Bindings for OpenImageIO
Group:          Development/Libraries/Python

%description -n python-OpenImageIO
This package contains python bindings for OpenImageIO.
%endif

%prep
%setup -q -n oiio-Release-%{version}
%patch0
%patch1
%patch2
%patch3
echo "gcc version %{gccv}"

# Make sure that bundled libraries are not used
rm -f src/include/pugiconfig.hpp \
      src/include/pugixml.hpp
rm -rf src/include/tbb/

%build
# This is for build debugging purposed
export OIIOINC=`echo $PWD`
%define pwd $OIIOINC
%define oiioinclude %{pwd}/src/include
echo %{pwd}
%if 1 == 0
%define gcc_version 8
export CC=gcc-8
export CPP=cpp-8
export CXX=g++-8
%endif

export CFLAGS="%{optflags} -Wno-error=deprecated-declarations"
%if 0%{?gcc_version} >= 7
#This host of flags to allow oiio to build with gcc7 are the result of oiio being built with -Werror"
export CXXFLAGS="%{optflags} -Wno-error=maybe-uninitialized -Wno-error=noexcept-type -Wno-error=format-truncation= -Wno-error=aligned-new= -Wno-error=deprecated-declarations"
%if 0%{?gcc_version} >= 8
export CXXFLAGS="$CXXFLAGS -Wno-error=class-memaccess -Wno-error=sizeof-pointer-memaccess -Wno-error=uninitialized"
%endif
%else
export CXXFLAGS="%{optflags} -Wno-error=deprecated-declarations"
%endif
%cmake \
%ifarch ppc
    -DNOTHREADS=ON \
%endif
    -DINSTALL_DOCS:BOOL=ON \
    -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
    -DCMAKE_INSTALL_MANDIR:PATH=%{_mandir}/man1 \
    -DINSTALL_FONTS:BOOL=ON \
    -DBUILDSTATIC:BOOL=OFF \
    -DLINKSTATIC:BOOL=OFF \
    -DUSE_EXTERNAL_PUGIXML:BOOL=ON \
    -DUSE_FFMPEG:BOOL=OFF \
    -DUSE_OPENSSL:BOOL=ON \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DUSE_OPENCV:BOOL=OFF \
    -DUSE_PYTHON:BOOL=OFF \
    -DCMAKE_DL_LIBS=dl \
        ..
#    -DPYLIB_INSTALL_DIR=%%{python3_sitearch} \
make %{?_smp_mflags} VERBOSE=1
#|| \
#make -j1 VERBOSE=1
cd ..
make %{?_smp_mflags} doxygen

%install
%make_install -C build

# Delete bundled fonts
rm -Rf %{buildroot}%{_datadir}/fonts/%{name}

# Move devel documentation to the right location
mkdir -p %{buildroot}%{_docdir}/%{name}-devel
mv %{buildroot}%{_docdir}/%{name}/openimageio.pdf %{buildroot}%{_docdir}/%{name}-devel/
%if 1 == 0
# Install additional devel documentation
cp -a src/doc/doxygen/html/ %{buildroot}%{_docdir}/%{name}-devel/
%endif

%fdupes -s %{buildroot}

%post -n libOpenImageIO%{so_ver} -p /sbin/ldconfig
%postun -n libOpenImageIO%{so_ver} -p /sbin/ldconfig
%post -n libOpenImageIO_Util%{so_ver} -p /sbin/ldconfig
%postun -n libOpenImageIO_Util%{so_ver} -p /sbin/ldconfig

%files
%doc CHANGES.md CREDITS.md LICENSE README.md
%{_bindir}/*
%{_mandir}/man1/*.1%{ext_man}

%files devel
%doc %{_docdir}/%{name}-devel/
%{_includedir}/%{name}/
%{_libdir}/*.so

%files -n lib%{name}%{so_ver}
%{_libdir}/lib%{name}.so.*

%files -n lib%{name}_Util%{so_ver}
%{_libdir}/lib%{name}_Util.so.*

%if 1 == 0
%files -n python-%{name}
%{python3_sitearch}/%{name}.so
%endif

%changelog
