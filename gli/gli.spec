#
# spec file for package gli
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


Name:           gli
Version:        0.8.2.0
Release:        0
Summary:        Header only C++ image library for graphics software
License:        MIT AND GPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            https://gli.g-truc.net/
#Git-Clone:     https://github.com/g-truc/gli.git
Source:         https://github.com/g-truc/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE gli-cmake-config.patch -- Fix cmake config location
Patch1:         gli-cmake-config.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  glm-devel
%if 0%{?suse_version} < 1500
BuildRequires:  gcc7
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc
BuildRequires:  gcc-c++
%endif

%description
OpenGL Image (GLI) is a header only C++ image library for graphics software.

GLI provides classes and functions to load image files (KTX and DDS),
facilitate graphics APIs texture creation, compare textures, access texture
texels, sample textures, convert textures, generate mipmaps, etc.

This library works perfectly with OpenGL or Vulkan but it also ensures
interoperability with other third party libraries and SDK. It is a good
candidate for software rendering (raytracing / rasterisation), image
processing, image based software testing or any development context that
requires a simple and convenient image library.

%package        devel
Summary:        Header only C++ image library for graphics software
Group:          Development/Libraries/C and C++
Requires:       cmake

%description    devel
OpenGL Image (GLI) is a header only C++ image library for graphics software.

GLI provides classes and functions to load image files (KTX and DDS),
facilitate graphics APIs texture creation, compare textures, access texture
texels, sample textures, convert textures, generate mipmaps, etc.

This library works perfectly with OpenGL or Vulkan but it also ensures
interoperability with other third party libraries and SDK. It is a good
candidate for software rendering (raytracing / rasterisation), image
processing, image based software testing or any development context that
requires a simple and convenient image library.

%package        doc
Summary:        Documentation for GLI library
Group:          Documentation/Other
BuildArch:      noarch

%description    doc
This package provides the documentation for GLI library.

%prep
%setup -q
%patch1 

%build
%if 0%{?suse_version} < 1500
%cmake \
    -DCMAKE_C_COMPILER=gcc-7 \
    -DCMAKE_CXX_COMPILER=g++-7 
%else
%cmake
%endif
%make_jobs

%install
%cmake_install
%fdupes -s %{buildroot}
%fdupes -s doc/api

%check
%ctest

%files devel
%{_includedir}/gli/
%{_libdir}/cmake/%{name}/
#%{_libdir}/pkgconfig/%{name}.pc

%files doc
# See https://github.com/g-truc/gli/blob/master/manual.md#-licenses for license details
%license readme.md
%doc doc/api
%doc manual.md readme.md

%changelog
