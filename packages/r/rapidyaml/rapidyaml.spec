#
# spec file for package rapidyaml
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define sover_ryml 0_16
Name:           rapidyaml
Version:        0.16.0
Release:        0
Summary:        A library to parse and emit YAML
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/biojppm/%{name}
Source0:        https://github.com/biojppm/%{name}/releases/download/v%{version}/%{name}.v%{version}.src.tgz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git

%description
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
Requires:       libryml%{sover_ryml} = %{version}-%{release}

%description devel
ryml is a C++ library to parse and emit YAML.

This package contains development headers and examples.

%prep
%autosetup -n %{name}.v%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n libryml%{sover_ryml}

%files -n libryml%{sover_ryml}
%license LICENSE.txt
%{_libdir}/libryml.so.*

%files devel
%license LICENSE.txt
%doc README.md
%{_includedir}/*
%{_libdir}/cmake/ryml
%{_libdir}/libryml.so
%{_datadir}/ryml

%changelog
