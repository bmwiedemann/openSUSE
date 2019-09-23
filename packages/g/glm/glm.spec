#
# spec file for package glm
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           glm
Version:        0.9.9.5
Release:        0
Summary:        Header only C++ mathematics library for graphics
License:        MIT AND GPL-2.0-only
Group:          Development/Libraries/C and C++
Url:            https://glm.g-truc.net/
#Git-Clone:     https://github.com/g-truc/glm.git
Source:         https://github.com/g-truc/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE glm-cmake-config.patch -- Fix cmake config location
Patch1:         glm-cmake-config.patch
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
%setup -q
%patch1 -p1

%build
%cmake \
  -DCMAKE_CXX_FLAGS="%{optflags} -fPIC -fno-strict-aliasing" \
  -DGLM_TEST_ENABLE=ON
%make_jobs

%install
%cmake_install
%fdupes -s %{buildroot}
%fdupes -s doc/api

%check
%ctest

%files devel
%{_includedir}/glm/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%files doc
# See https://github.com/g-truc/glm/blob/master/manual.md#-licenses for license details
%license readme.md
%doc doc/api
%doc manual.md readme.md

%changelog
