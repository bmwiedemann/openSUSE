#
# spec file for package OpenSubdiv
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2019-2020 LISA GmbH, Bingen, Germany.
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


%define pkgver 3_6_1
%define libname libosdCPU%{pkgver}
Name:           OpenSubdiv
Version:        3.6.1
Release:        0
Summary:        Subdivision surface evaluation library
License:        Apache-2.0
Group:          Productivity/Graphics/Visualization/Raytracers
URL:            https://graphics.pixar.com/opensubdiv/docs/intro.html
Source:         https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v%{pkgver}.tar.gz#/%{name}-%{pkgver}.tar.gz
Patch0:         remove-rpath-fiddling.diff
Patch1:         no-static.patch
BuildRequires:  cmake >= 2.8.6
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  tbb-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xxf86vm)

%description
%{name} is a set of libraries that implement subdivision surface
(subdiv) evaluation on massively parallel CPU and GPU architectures.

%package -n %{libname}
Summary:        Subdivision surface evaluation library
Group:          System/Libraries

%description -n %{libname}
%{name} is a set of libraries that implement subdivision surface
(subdiv) evaluation on massively parallel CPU and GPU architectures.
This code path is optimized for drawing deforming surfaces with
static topology at interactive framerates.

%{name} is an API for use by 3rd party digital content creation
tools. It is not an application, nor a tool that can be used directly
to create digital assets.

%package devel
Summary:        Development files for OpenSubdiv
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
This package contains the C++ header files and symbolic links to the shared
libraries for %{name}. If you would like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%autosetup -p1 -n %{name}-%{pkgver}

# work around linking glitch
sed -i 's/${PLATFORM_GPU_LIBRARIES}/${PLATFORM_GPU_LIBRARIES} ${CMAKE_DL_LIBS}/' opensubdiv/CMakeLists.txt

%build
# sse options only on supported archs
%ifarch x86_64
sseflags='-msse -msse2'
%endif

%cmake \
    -DCMAKE_C_FLAGS:STRING="$CFLAGS %{optflags} -fPIC ${sseflags}" \
    -DCMAKE_CXX_FLAGS:STRING="$CXXFLAGS %{optflags} -fPIC ${sseflags}" \
    -DCMAKE_LIBDIR_BASE=%{_libdir} \
    -DNO_PTEX=1 \
    -DNO_DOC=1 \
    -DNO_CUDA=1 \
    -DNO_CLEW=1 \
    -DNO_OPENCL=1 \
    -DNO_TUTORIALS=1 \
    -DNO_REGRESSION=1 \
    -DNO_EXAMPLES=1 \
    -DGLEW_LOCATION=%{_prefix} \
    -DGLFW_LOCATION=%{_prefix} \
    -DOpenGL_GL_PREFERENCE=GLVND
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license LICENSE.txt
%doc NOTICE.txt README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/opensubdiv
%{_libdir}/*.so
%dir %{_libdir}/cmake/OpenSubdiv/
%{_libdir}/cmake/OpenSubdiv/OpenSubdivConfig.cmake
%{_libdir}/cmake/OpenSubdiv/OpenSubdivConfigVersion.cmake
%{_libdir}/cmake/OpenSubdiv/OpenSubdivTargets-relwithdebinfo.cmake
%{_libdir}/cmake/OpenSubdiv/OpenSubdivTargets.cmake

%changelog
