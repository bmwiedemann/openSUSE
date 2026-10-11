#
# spec file for package json-schema-validator
#
# Copyright (c) 2026 SUSE LLC
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

%define lname libnlohmann_json_schema_validator2
Name:           json-schema-validator
Version:        2.4.0
Release:        0
Summary:        JSON schema validator for "JSON for Modern C++"
License:        MIT
URL:            https://github.com/pboettch/json-schema-validator
Source0:        https://github.com/pboettch/json-schema-validator/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.xz
BuildRequires:  ninja
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(json-c)
BuildRequires:  cmake(nlohmann_json)

%description
Json schema validator library for C++ projects using nlohmann/json

%package -n %lname
Summary:        JSON schema validator for "JSON for Modern C++"

%description -n %lname
Json schema validator shared library for C++ projects using nlohmann/json

%package        devel
Summary:        Development files for JSON schema validator
Requires:       %lname = %version-%release
Requires:       cmake(json-c)

%description    devel
Json schema validator development files for C++ projects using nlohmann/json

%prep
%autosetup -p1


%build
%cmake \
    -DJSON_VALIDATOR_SHARED_LIBS=ON \
    -DJSON_VALIDATOR_INSTALL=ON \
    -DJSON_VALIDATOR_BUILD_EXAMPLES=OFF \
    -DJSON_VALIDATOR_BUILD_TESTS=ON

%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n %lname

%files -n %lname
%license LICENSE
%doc README.md
%{_libdir}/libnlohmann_json_schema_validator.so.*

%files devel
%{_libdir}/libnlohmann_json_schema_validator.so
%{_includedir}/nlohmann/json-schema.hpp
%{_libdir}/cmake/nlohmann_json_schema_validator

%changelog
