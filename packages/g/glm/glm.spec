#
# spec file for package glm
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


Name:           glm
Version:        1.0.1
Release:        0
Summary:        Header only C++ mathematics library for graphics
License:        GPL-2.0-only AND MIT
Group:          Development/Libraries/C and C++
URL:            https://glm.g-truc.net/
#Git-Clone:     https://github.com/g-truc/glm.git
Source:         https://github.com/g-truc/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE glm-1.0.1-pkgconfig.patch add pkgconfig file -- aloisio@gmx.com, updated by buschmann23@opensuse.org
Patch3:         glm-1.0.1-pkgconfig.patch
# PATCH-FIX-UPSTREAM glm-1.0.1-fix-tests-big-endian.patch
Patch4:         glm-1.0.1-fix-tests-big-endian.patch
# PATCH-FIX-OPENSUSE glm-1.0.1-without-werror.patch
Patch5:         glm-1.0.1-without-werror.patch
# PATCH-FIX-OPENSUSE glm-1.0.1-fix-install-cmake-files.patch
Patch6:         glm-1.0.1-fix-install-cmake-files.patch
# PATCH-FIX-OPENSUSE glm-1.0.1-noarch.patch
Patch7:         glm-1.0.1-noarch.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
OpenGL Mathematics (GLM) is a header only C++ mathematics library for graphics
software based on the OpenGL Shading Language (GLSL) specification.

GLM provides classes and functions designed and implemented with the same naming
conventions and functionalities than GLSL so that when a programmer knows GLSL,
he knows GLM as well which makes it really easy to use.

%package        devel
Summary:        Header only C++ mathematics library for graphics
Group:          Development/Libraries/C and C++
Requires:       cmake
BuildArch:      noarch

%description    devel
OpenGL Mathematics (GLM) is a header only C++ mathematics library for graphics
software based on the OpenGL Shading Language (GLSL) specification.

GLM provides classes and functions designed and implemented with the same naming
conventions and functionalities than GLSL so that when a programmer knows GLSL,
he knows GLM as well which makes it really easy to use.

%package        doc
Summary:        Documentation for GLM library
Group:          Documentation/Other
BuildArch:      noarch

%description    doc
This package provides the documentation for GLM library.

%prep
%autosetup -p1

%build
%cmake \
  -DCMAKE_CXX_FLAGS="%{optflags} -fPIC -fno-strict-aliasing" \
  -DGLM_BUILD_LIBRARY=OFF \
  -DGLM_BUILD_TESTS=ON \
  -DGLM_BUILD_INSTALL=ON
%cmake_build

%install
%cmake_install
%fdupes -s %{buildroot}
%fdupes -s doc/api

%check
%ctest

%files devel
%{_includedir}/glm
%{_datadir}/cmake/%{name}
%{_datadir}/pkgconfig/%{name}.pc

%files doc
# See https://github.com/g-truc/glm/blob/master/manual.md#-licenses for license details
%license readme.md
%doc doc/api
%doc manual.md readme.md

%changelog
