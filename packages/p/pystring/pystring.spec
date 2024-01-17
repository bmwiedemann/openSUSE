#
# spec file for package pystring
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2021 LISA GmbH, Bingen, Germany
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

%define so_ver  0_0
Name:           pystring
Version:        1.1.3
Release:        0
Summary:        Collection of C++ functions emulating Python's string class methods
License:        BSD-2-Clause
URL:            https://github.com/imageworks/pystring
Source:         https://github.com/imageworks/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source100:      CMakeLists.txt
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{so_ver} = %{version}-%{release}
	
%description devel
%{summary}.

%package -n lib%{name}%{so_ver}
Summary:        Collection of C++ functions emulating Python's string class methods

%description -n lib%{name}%{so_ver}
Pystring is a collection of C++ functions which match the interface and
behavior of Python's string class methods using std::string. Implemented in
C++, it does not require or make use of a Python interpreter. It provides
convenience and familiarity for common string operations not included in the
standard C++ library. It's also useful in environments where both C++ and
Python are used.
	
Overlapping functionality (such as index and slice/substr) of std::string is
included to match Python interfaces.
	
Originally developed at Sony Pictures Imageworks.
http://opensource.imageworks.com/

%prep
%autosetup -p1
cp %{SOURCE100} .

%build
%cmake
%cmake_build

%install
%cmake_install

%check
pushd build
./test
 
%post -n lib%{name}%{so_ver} -p /sbin/ldconfig
%postun -n lib%{name}%{so_ver} -p /sbin/ldconfig

%files -n lib%{name}%{so_ver}
%license LICENSE
%doc README
%{_libdir}/lib%{name}.so.0.0

%files devel
%{_includedir}/pystring/
%{_libdir}/lib%{name}.so
 
%changelog
