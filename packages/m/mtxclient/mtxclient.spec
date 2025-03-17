#
# spec file for package mtxclient
#
# Copyright (c) 2021 SUSE LLC
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


%define libname libmatrix_client%(echo %{version} | tr . _)
%define sover 0
Name:           mtxclient
Version:        0.10.0
Release:        0
Summary:        Client API library for Matrix, built on top of Boost.Asio
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/Nheko-Reborn/mtxclient
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-build-with-fmt11.patch
BuildRequires:  cmake >= 3.13
BuildRequires:  fdupes
%if 0%{?suse_version} <= 1600
BuildRequires: gcc12
BuildRequires: gcc12-c++
%else
BuildRequires: gcc
BuildRequires: gcc-c++
%endif
BuildRequires:  libsodium-devel
BuildRequires:  mpark-variant-devel
BuildRequires:  ninja
BuildRequires:  nlohmann_json-devel >= 3.1.2
BuildRequires:  olm-devel
BuildRequires:  openssl-devel
BuildRequires:  spdlog-devel >= 0.16
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libevent_core)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(coeurl) >= 0.3.0
BuildRequires:  cmake(re2)

%description
Client API library for the Matrix protocol, built on top of Boost.Asio.

%package doc
Summary:        License and documentation files for %{name}
Group:          Documentation/Other
BuildArch:      noarch

%description doc
Client API library for the Matrix protocol, built on top of Boost.Asio.

%package -n %{libname}
Summary:        Client API library for Matrix, built on top of Boost.Asio
Group:          System/Libraries
Recommends:     %{name}-doc = %{version}

%description -n %{libname}
Client API library for the Matrix protocol, built on top of Boost.Asio.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       %{name}-doc = %{version}

%description devel
Client API library for Matrix, built on top of Boost.Asio

%prep
%autosetup -p1

%build
%if 0%{?suse_version} <= 1600
export CC=gcc-12
export CXX=g++-12
%endif
%define __builder ninja
%cmake \
    -DBUILD_LIB_TESTS=OFF \
    -DBUILD_LIB_EXAMPLES=OFF \
    -DCMAKE_BUILD_TYPE=Release \
    -DHUNTER_ENABLED=OFF \
    -DUSE_BUNDLED_BOOST=OFF \
    -DUSE_BUNDLED_SPDLOG=OFF \
    -DUSE_BUNDLED_OLM=OFF \
    -DUSE_BUNDLED_GTEST=OFF \
    -DUSE_BUNDLED_JSON=OFF \
    -DUSE_BUNDLED_OPENSSL=OFF \
    -DASAN=OFF \
    -DCOVERAGE=OFF \
    -DIWYU=OFF
%cmake_build

%install
%cmake_install

%fdupes %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files doc
%doc README.md
%license LICENSE

%files -n %{libname}
%{_libdir}/*.so.*

%files devel
%{_includedir}/mtx.hpp
%{_includedir}/mtx
%{_includedir}/%{name}
%{_libdir}/cmake/MatrixClient
%{_libdir}/*.so

%changelog
