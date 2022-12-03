#
# spec file for package cglm
#
# Copyright (c) 2022 SUSE LLC
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


%define sover 0
Name:           cglm
Version:        0.8.7
Release:        0
Summary:        OpenGL mathematics (glm) for C
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/recp/cglm
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  python3-sphinx_rtd_theme
ExcludeArch:    %{ix86}

%description
cglm is a C99-compatible version of the previous OpenGL Mathematics
(GLM) implementation, a mathematics library for graphics software
based on the OpenGL Shading Language (GLSL) specifications.

%package -n libcglm%{sover}
Summary:        OpenGL mathematics (glm) for C
Group:          System/Libraries

%description -n libcglm%{sover}
cglm is a C99-compatible version of the previous OpenGL Mathematics
(GLM) implementation, a mathematics library for graphics software
based on the OpenGL Shading Language (GLSL) specifications.

%package devel
Summary:        Header files for C OpenGL Mathematics
Group:          Development/Libraries/C and C++
Requires:       libcglm%{sover} = %{version}

%description devel
This package contains development files for cglm.

%package devel-doc
Summary:        Documentation for C OpenGL Mathematics
Group:          Documentation/HTML
BuildArch:      noarch

%description devel-doc
This package contains documentation files for cglm.

%prep
%autosetup -p1

%build
%meson -Dbuild_tests=true
%meson_build
cd docs
sphinx-build source html
rm -rf html/.{buildinfo,doctrees,nojekyll}
%fdupes html

%install
%meson_install
%fdupes %{buildroot}/%{_prefix}
%fdupes -s docs/html

%check
%meson_test

%post -n libcglm%{sover} -p /sbin/ldconfig
%postun -n libcglm%{sover} -p /sbin/ldconfig

%files -n libcglm%{sover}
%license LICENSE
%{_libdir}/libcglm.so.%{sover}*

%files devel
%doc README.md CREDITS
%{_includedir}/cglm
%{_libdir}/libcglm.so
%{_libdir}/pkgconfig/cglm.pc

%files devel-doc
%doc docs/html

%changelog
