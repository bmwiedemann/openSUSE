#
# spec file for package rapidyaml
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover_ryml 0_8_0
%define sover_c4core 0_2_5
Name:           rapidyaml
Version:        0.8.0
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

%package -n libc4core%{sover_c4core}
Summary:        Utility library of rapidyaml
Group:          System/Libraries

%description -n libc4core%{sover_c4core}
ryml is a C++ library to parse and emit YAML.

%package -n libryml%{sover_ryml}
Summary:        A library to parse and emit YAML
Group:          System/Libraries

%description -n libryml%{sover_ryml}
ryml is a C++ library to parse and emit YAML.

ryml parses both read-only and in-situ source buffers; the resulting
data nodes hold only views to sub-ranges of the source buffer. No
string copies or duplications are done.

%package devel
Summary:        Header files for rapidyaml, a library to parse and emit YAML
Group:          Development/Libraries/C and C++
Requires:       libc4core%{sover_c4core} = %{version}-%{release}
Requires:       libryml%{sover_ryml} = %{version}-%{release}

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

%check
%ctest

%ldconfig_scriptlets -n libc4core%{sover_c4core}
%ldconfig_scriptlets -n libryml%{sover_ryml}

%files -n libc4core%{sover_c4core}
%license LICENSE.txt
%{_libdir}/libc4core.so.*

%files -n libryml%{sover_ryml}
%license LICENSE.txt
%{_libdir}/libryml.so.*

%files devel
%license LICENSE.txt
%doc README.md
%{_includedir}/*
%{_libdir}/cmake/c4core
%{_libdir}/cmake/ryml
%{_libdir}/libc4core.so
%{_libdir}/libryml.so

%changelog
