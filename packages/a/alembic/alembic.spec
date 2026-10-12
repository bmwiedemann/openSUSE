#
# spec file for package alembic
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2019-2026 LISA GmbH, Bingen, Germany.
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


%define libname libAlembic1_8
Name:           alembic
Version:        1.8.12
Release:        0
Summary:        Computer graphics interchange framework
License:        BSD-3-Clause
URL:            https://www.alembic.io
Source:         https://github.com/%{name}/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.29
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  cmake(Imath) >= 3.0
BuildRequires:  pkgconfig(zlib)
# Ogawa does only support little endianess
ExcludeArch:    ppc64 s390x

%description
Alembic distills complex, animated scenes into a non-procedural, application-
independent set of baked geometric results. This ‘distillation’ of scenes into
baked geometry is exactly analogous to the distillation of lighting and
rendering scenes into rendered image data.

%package -n %{libname}
Summary:        Sparse volume data structure library

%description -n %{libname}
Alembic distills complex, animated scenes into a non-procedural, application-
independent set of baked geometric results. This ‘distillation’ of scenes into
baked geometry is exactly analogous to the distillation of lighting and
rendering scenes into rendered image data.

%package devel
Summary:        Development files for alembic
Requires:       %{libname} = %{version}
Requires:       cmake(Imath) >= 3.0

%description	devel
This package contains the C++ header files and symbolic links to the shared
libraries for %{name}. If you would like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%autosetup -p1

%build
%cmake \
    -DUSE_ARNOLD=OFF \
    -DUSE_BINARIES=OFF \
    -DCMAKE_SKIP_BUILD_RPATH=ON \
    -DUSE_TESTS=ON

%make_build

%check
export LD_LIBRARY_PATH="%{buildroot}%{_libdir}"
# CurvesTest and GeomBaseTest both write and read curves1.abc in the same
# directory, so they fail randomly when ctest runs them in parallel
%ctest --verbose --parallel 1

%install
%cmake_install

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license LICENSE.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/Alembic
%{_libdir}/*.so
%{_libdir}/cmake/Alembic
%doc ACKNOWLEDGEMENTS.txt FEEDBACK.txt NEWS.txt README.txt

%changelog
