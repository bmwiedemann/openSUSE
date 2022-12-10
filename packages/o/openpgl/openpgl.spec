#
# spec file for package openpgl
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2022 LISA GmbH, Bingen, Germany.
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


%define libname libopenpgl0

Name:           openpgl
Version:        0.4.0
Release:        0
Summary:        Open Path Guiding Library
License:        Apache-2.0
Group:          Productivity/Graphics/Other
URL:            https://github.com/OpenPathGuidingLibrary/openpgl
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  tbb-devel
BuildRequires:  pkgconfig(zlib)
ExclusiveArch:  x86_64 aarch64

%description
Open Path Guiding Library (Intel® Open PGL) implements a set of representations
and training algorithms needed to integrate path guiding into a renderer. Open
PGL offers implementations of current state-of-the-art path guiding methods,
which increase the sampling quality and, therefore, the efficiency of a
renderer.

%package -n %{libname}
Summary:        Open Path Guiding Library
Group:          Productivity/Graphics/Other

%description -n %{libname}
Open Path Guiding Library (Intel® Open PGL) implements a set of representations
and training algorithms needed to integrate path guiding into a renderer. Open
PGL offers implementations of current state-of-the-art path guiding methods,
which increase the sampling quality and, therefore, the efficiency of a
renderer.

%package devel
Summary:        Development files for the Open Path Guiding library
Group:          Development/Libraries/Other
Requires:       %{libname} = %{version}

%description devel
Development files for the Open Path Guiding library.

%package doc
Summary:        Documentation files for the Open Path Guiding library
Group:          Development/Libraries/Other
BuildArch:      noarch

%description doc
Documentation files for the Open Path Guiding library.

%prep
%autosetup

%build
# https://github.com/embree/embree/issues/410
%global optflags %{optflags} -flax-vector-conversions
%cmake
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/doc

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE.txt
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%dir %{_libdir}/cmake/%{name}-%{version}
%{_libdir}/cmake/%{name}-%{version}/*

%files doc
%license LICENSE.txt
%doc CHANGELOG.md README.md third-party-programs-*.txt doc

%changelog
