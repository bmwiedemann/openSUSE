#
# spec file for package openamp
#
# Copyright (c) 2020 SUSE LLC
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


%define libname libopen_amp1
Name:           openamp
Version:        2026.04.0
Release:        0
Summary:        Asymmetric Multiprocessing communication APIs
License:        BSD-3-Clause
URL:            https://github.com/OpenAMP/open-amp
Source:         https://github.com/OpenAMP/open-amp/archive/v%{version}.tar.gz#/open-amp-%{version}.tar.gz
# Keep plain -devel names: spec-cleaner --pkgconfig over-expands them
# into per-.pc deps; the -devel form pulls the same providers.
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libhugetlbfs-devel
BuildRequires:  libmetal-devel
BuildRequires:  make
BuildRequires:  sysfsutils-devel

%description
The OpenAMP framework provides software components that enable development
of software applications for Asymmetric Multiprocessing (AMP) systems.
The framework provides the following key capabilities.

1. Provides Life Cycle Management, and Inter Processor Communication
   capabilities for management of remote compute resources and their associated
   software contexts.
2. Provides a stand alone library usable with RTOS and Baremetal software
   environments
3. Compatibility with upstream Linux remoteproc and rpmsg components
4. Following AMP configurations supported
	a. Linux master/Generic(Baremetal) remote
	b. Generic(Baremetal) master/Linux remote
5. Proxy infrastructure and supplied demos showcase ability of proxy on master
   to handle printf, scanf, open, close, read, write calls from Bare metal
   based remote contexts.

%package -n %{libname}
Summary:        OpenAMP communication APIs
Provides:       %{name} = %{version}

%description -n %{libname}
The OpenAMP framework provides software components that enable development
of software applications for Asymmetric Multiprocessing (AMP) systems.
The framework provides the following key capabilities.

1. Provides Life Cycle Management, and Inter Processor Communication
   capabilities for management of remote compute resources and their associated
   software contexts.
2. Provides a stand alone library usable with RTOS and Baremetal software
   environments
3. Compatibility with upstream Linux remoteproc and rpmsg components
4. Following AMP configurations supported
	a. Linux master/Generic(Baremetal) remote
	b. Generic(Baremetal) master/Linux remote
5. Proxy infrastructure and supplied demos showcase ability of proxy on master
   to handle printf, scanf, open, close, read, write calls from Bare metal
   based remote contexts.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Requires:       %{libname} = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%autosetup -p1 -n open-amp-%{version}

%build
# Remove '-Wl,--no-undefined' from linker flags
%cmake \
  -DCMAKE_SHARED_LINKER_FLAGS='-Wl,--as-needed -Wl,-z,now' \
  -DWITH_STATIC_LIB=OFF
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license LICENSE.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/openamp/
%{_libdir}/*.so

%changelog
