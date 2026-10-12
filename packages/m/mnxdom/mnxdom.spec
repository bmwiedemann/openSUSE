#
# spec file for package mnxdom
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


Name:           mnxdom
Version:        3.0.1
Release:        0
Summary:        DOM for the MNX music interchange format
License:        MIT
URL:            https://github.com/rpatters1/mnxdom
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  xxd
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  cmake(nlohmann_json_schema_validator)
BuildRequires:  cmake(GTest)

%description
Document object model for the MNX music interchange format. It is compatible with the C++17 standard.

    compatible with the C++17 standard and higher. (Currently tested with C++23.)
    uses nlohmann_json as its JSON parser.
    allows structured access to MNX objects, without the need of quoted strings.
    validates against the MNX schema using json-schema-validator.
    no class serialization beyond nlohmann.
    every MNX class is a wrapper around the root JSON object and a pointer to the location of the instance.

%package devel
Summary:        DOM for the MNX music interchange format
Group:          System/Libraries

%description devel
Document object model for the MNX music interchange format. It is compatible with the C++17 standard.

    compatible with the C++17 standard and higher. (Currently tested with C++23.)
    uses nlohmann_json as its JSON parser.
    allows structured access to MNX objects, without the need of quoted strings.
    validates against the MNX schema using json-schema-validator.
    no class serialization beyond nlohmann.
    every MNX class is a wrapper around the root JSON object and a pointer to the location of the instance.

%prep
%setup -q

%build
%cmake -DUSE_SYSTEM_NLOHMANN_JSON=ON \
       -DUSE_SYSTEM_JSON_SCHEMA_VALIDATOR=ON \
       -DUSE_SYSTEM_GOOGLETEST=ON
%cmake_build

%install
%cmake_install

rm -rf docs/doxygen-awesome-css/.github
rm docs/doxygen-awesome-css/.gitignore
rm docs/doxygen-awesome-css/.npmignore

%check
%ctest

%files devel
%license LICENSE
%_libdir/*.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%_libdir/pkgconfig/%{name}.pc
%doc docs/*

%changelog
