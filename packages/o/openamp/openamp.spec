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


%define libname libopen_amp0
Name:           openamp
Version:        2020.01
Release:        0
Summary:        Asymmetric Multiprocessing communication APIs
License:        BSD-3-Clause
URL:            https://github.com/OpenAMP/open-amp
Source:         https://github.com/OpenAMP/open-amp/archive/v%{version}.tar.gz#/open-amp-%{version}.tar.gz
# https://github.com/OpenAMP/open-amp/pull/196
Patch0:         openamp-fix-build-with-libmetal.patch
# https://github.com/OpenAMP/open-amp/pull/197
Patch1:         openamp-wait-when-no-more-buffer-avail.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libhugetlbfs-devel
BuildRequires:  libmetal-devel
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

%package examples
Summary:        Example applications for OpenAMP
Requires:       %{libname} = %{version}

%description examples
This package contains example binaries for OpenAMP.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Requires:       %{libname} = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q -n open-amp-%{version}
%patch0 -p1
%patch1 -p1

%build
# Remove '-Wl,--no-undefined' from linker flags and build example apps
%cmake \
  -DWITH_APPS:BOOL=ON \
  -DCMAKE_SHARED_LINKER_FLAGS='-Wl,--as-needed -Wl,-z,now' \
  -DWITH_STATIC_LIB=OFF
%cmake_build

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE.md
%{_libdir}/*.so.*

%files examples
%{_bindir}/msg-test-rpmsg-flood-ping-shared
%{_bindir}/msg-test-rpmsg-ping-shared
%{_bindir}/msg-test-rpmsg-update-shared
%{_bindir}/rpmsg-echo-ping-shared
%{_bindir}/rpmsg-echo-shared
%{_bindir}/rpmsg-sample-echo-shared
%{_bindir}/rpmsg-sample-ping-shared
%{_bindir}/matrix_multiply-shared
%{_bindir}/matrix_multiplyd-shared
%{_bindir}/rpc_demod-shared

%files devel
%{_includedir}/openamp/
%{_libdir}/*.so

%changelog
