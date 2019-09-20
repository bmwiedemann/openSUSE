#
# spec file for package OpenSubdiv
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019 LISA GmbH, Bingen, Germany.
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

%define pkgver %(v=%version; echo -n "${v//\./_}")
%define libname libosdCPU%{pkgver}

Name:           OpenSubdiv
Version:        3.4.0
Release:        0
Summary:        Subdivision surface evaluation library
License:        Apache-2.0
Group:          Productivity/Graphics/Visualization/Raytracers
URL:            http://graphics.pixar.com/opensubdiv/docs/intro.html
Source:         https://github.com/PixarAnimationStudios/%{name}/archive/v3_4_0.tar.gz#/%{name}-3_4_0.tar.gz
BuildRequires:  cmake >= 2.8.6
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  cmake(TBB)

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
%setup -q -n %{name}-%{pkgver}

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
    -DGLEW_LOCATION=/usr \
    -DGLFW_LOCATION=/usr \
    -DOpenGL_GL_PREFERENCE=GLVND

make %{?_smp_mflags}

%install
%cmake_install
# remove unused build artefact
rm %{buildroot}%{_bindir}/stringify
rm %{buildroot}%{_libdir}/*.a

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE.txt
%doc NOTICE.txt README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/opensubdiv
%{_libdir}/*.so

%changelog
