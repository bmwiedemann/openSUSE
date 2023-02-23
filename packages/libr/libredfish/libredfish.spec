#
# spec file for package libredfish
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

%define 	MAJOR 1


Name:           libredfish
Version:        1.3.6.4+git.a0788d4
Release:        0%{?dist}
Summary:        Redfish C Client Library
License:        BSD-3-Clause
Group: 		Development/Libraries/C
URL:            https://github.com/DMTF/libredfish
Source0:        libredfish-%{version}.tar.xz
Patch1:		add_crypto.patch
BuildRequires:  gcc-c++
BuildRequires:  libczmq4
BuildRequires:  libopenssl1_1
BuildRequires:  libopenssl-1_1-devel
BuildRequires:  czmq
BuildRequires:  czmq-devel
BuildRequires:  cmake
BuildRequires:  libjansson-devel
BuildRequires:  libcurl-devel
BuildRequires:  readline-devel
Requires:       readline

%description
libRedfish is a C client library that allows for Creation of Entities (POST), Read of Entities (GET), Update of Entities (PATCH), Deletion of Entities (DELETE), running Actions (POST), receiving events, and providing some basic query abilities.

%package        devel
Summary:        Headers for building apps that use libredfish
Group:          Development/Libraries/C
Requires:       libredfish%{MAJOR} = %{version}

%description    devel
This package contains headers required to build applications that use libredfish.

%package        -n libredfish%{MAJOR}
Summary:        Headers for building apps that use libredfish
Group:          Development/Libraries/C

%description    -n libredfish%{MAJOR}
This package contains headers required to build applications that use libredfish.

%prep
%autosetup -p1

%build
%cmake -DLIB_INSTALL_DIR=%{_libdir}
%cmake_build

%install
%cmake_install

%check
%ctest

%post -n libredfish%{MAJOR} -p /sbin/ldconfig

%postun -n libredfish%{MAJOR} -p /sbin/ldconfig

%files
%{_bindir}/*

%files -n libredfish%{MAJOR}
%{_libdir}/libredfish.so.%{MAJOR}*

%files devel
%defattr(0644,root,root)
%{_libdir}/libredfish.so
%{_includedir}/*

%changelog

