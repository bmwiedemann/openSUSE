#
# spec file for package sparsehash
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           sparsehash
Version:        2.0.3
Release:        0
Summary:        Memory-efficient hash_map implementation
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            https://github.com/sparsehash/sparsehash
Source:         https://github.com/sparsehash/sparsehash/archive/sparsehash-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Google SparseHash project contains several C++ template hash-map
implementations with different performance characteristics, including
an implementation that optimizes for space and one that optimizes for
speed.

%package        devel
Summary:        Memory-efficient C++ hash_map implementation
Group:          Development/Libraries/C and C++

%description    devel
The Google SparseHash project contains several C++ template hash-map
implementations with different performance characteristics, including
an implementation that optimizes for space and one that optimizes for
speed.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
%make_install
# upstream did not change version to 2.0.3 with new release
rm %{buildroot}%{_datadir}/doc/%{name}-2.0.2/INSTALL
rm %{buildroot}%{_datadir}/doc/%{name}-2.0.2/README_windows.txt

%files devel
%defattr(-,root,root)
%doc %{_datadir}/doc/%{name}-2.0.2/
%{_includedir}/google/
%{_includedir}/sparsehash/
%{_libdir}/pkgconfig/*.pc

%changelog
