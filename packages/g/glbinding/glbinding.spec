#
# spec file for package glbinding
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


%define shlib libglbinding3
Name:           glbinding
Version:        3.5.0
Release:        0
Summary:        C++ binding for the OpenGL API
License:        MIT
URL:            https://github.com/cginternals/glbinding
Source:         https://github.com/cginternals/glbinding/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM glbinding-install-libdir.patch gh#cginternals/glbinding#206 badshah400@gmail.com -- Fix install libdir; part of un-merged upstream PR
Patch0:         glbinding-install-libdir.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkgconfig(glfw3)

%description
glbinding is a C++ binding for the OpenGL API.

%package -n %{shlib}
Summary:        C++ binding for the OpenGL API

%description -n %{shlib}
glbinding is a C++ binding for the OpenGL API.

This package provides the shared library for glbinding.

%package devel
Summary:        Headers and objects to build against glbinding
Requires:       %{shlib} = %{version}

%description devel
glbinding is a C++ binding for the OpenGL API.

This package provides headers and objects to build against %{name}.

%package -n libglbinding-aux3
Summary:        Auxiliary shared library for glbinding

%description -n libglbinding-aux3
glbinding is a C++ binding for the OpenGL API.

This package provides the shared library for additional, auxiliary features as
logging, meta information, or debugging functionality

%package aux-devel
Summary:        Headers and objects for building against glbinding's auxiliary features
Requires:       %{shlib} = %{version}
Requires:       libglbinding-aux3 = %{version}
Requires:       %{name}-devel = %{version}

%description aux-devel
glbinding is a C++ binding for the OpenGL API.

This package provides the headers and objects to build against glbinding's
auxiliary features including logging, meta information, or debugging
functionality.

%prep
%autosetup -p1

%build
%cmake \
  -DINSTALL_SHARED=%{_libdir} \
	-DOPTION_BUILD_EXAMPLES:BOOL=OFF \
	%{nil}
%cmake_build

%install
%cmake_install

# Packaged using %%doc
rm %{buildroot}%{_datadir}/glbinding/{LICENSE,README.md}

%ldconfig_scriptlets -n %{shlib}
%ldconfig_scriptlets -n libglbinding-aux3

%files -n %{shlib}
%license LICENSE
%{_libdir}/libglbinding.so.3*

%files devel
%license LICENSE
%{_bindir}/*
%{_libdir}/libglbinding.so
%{_includedir}/glbinding
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/cmake/glbinding-aux

%files -n libglbinding-aux3
%license LICENSE
%{_libdir}/libglbinding-aux.so.3*

%files aux-devel
%license LICENSE
%{_libdir}/libglbinding-aux.so
%{_includedir}/glbinding-aux/
%{_datadir}/%{name}/cmake/glbinding-aux/

%changelog
