#
# spec file for package rapidyaml
#
# Copyright (c) 2023 SUSE LLC
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


Name:           rapidyaml
Version:        0.5.0
Release:        0
Summary:        A library to parse and emit YAML
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/biojppm/%{name}
Source0:        https://github.com/biojppm/%{name}/releases/download/v%{version}/%{name}-%{version}-src.tgz
Patch0:         cmake.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git

%description
ryml is a C++ library to parse and emit YAML.

%package -n libc4core0_1_11
Summary:        Utility library of rapidyaml
Group:          System/Libraries

%description -n libc4core0_1_11
ryml is a C++ library to parse and emit YAML.

%package -n libryml0_5_0
Summary:        A library to parse and emit YAML
Group:          System/Libraries

%description -n libryml0_5_0
ryml is a C++ library to parse and emit YAML.

ryml parses both read-only and in-situ source buffers; the resulting
data nodes hold only views to sub-ranges of the source buffer. No
string copies or duplications are done.

%package devel
Summary:        Header files for rapidyaml, a library to parse and emit YAML
Group:          Development/Libraries/C and C++
Requires:       libc4core0_1_11 = %{version}-%{release}
Requires:       libryml0_5_0 = %{version}-%{release}

%description devel
ryml is a C++ library to parse and emit YAML.

This package contains development headers and examples.

%prep
%autosetup -n %{name}-%{version}-src -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%post   -n libc4core0_1_11 -p /sbin/ldconfig
%postun -n libc4core0_1_11 -p /sbin/ldconfig
%post   -n libryml0_5_0 -p /sbin/ldconfig
%postun -n libryml0_5_0 -p /sbin/ldconfig

%files -n libc4core0_1_11
%license LICENSE.txt
%{_libdir}/libc4core.so.*

%files -n libryml0_5_0
%{_libdir}/libryml.so.*

%files devel
%doc README.md
%license LICENSE.txt
%{_includedir}/*
%{_libdir}/cmake/c4core
%{_libdir}/cmake/ryml
%{_libdir}/libc4core.so
%{_libdir}/libryml.so

%changelog
