#
# spec file for package plugin-sdk-cpp
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           plugin-sdk-cpp
Version:        0.4.1
Release:        0
Summary:        C++ SDK for writing Falcosecurity plugins
License:        Apache-2.0
URL:            https://github.com/falcosecurity/plugin-sdk-cpp
Source0:        https://github.com/falcosecurity/plugin-sdk-cpp/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE plugin-sdk-cpp-system-gtest.patch -- use system googletest; FetchContent cannot clone in the offline OBS build
Patch0:         plugin-sdk-cpp-system-gtest.patch
BuildArch:      noarch
# C++20 codec tests; skip the compile on Leap 15.x (gcc 7)
%if 0%{?suse_version} >= 1600
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake(GTest)
%endif

%description
The Falcosecurity Plugin SDK for C++ is a header-only library that wraps
the Falcosecurity plugin API and makes it easy to write plugins (event
sourcing, field extraction, parsing, async events) for Falco and the
falcosecurity libs (libsinsp) in C++.

%package devel
Summary:        Development files for %{name}
Requires:       libstdc++-devel

%description devel
Header files of the Falcosecurity Plugin SDK for C++ (header-only).

%prep
%autosetup -p1

%build
# header-only INTERFACE library: cmake is used only to build the tests
%if 0%{?suse_version} >= 1600
%cmake
%cmake_build
%endif

%install
mkdir -p %{buildroot}%{_includedir}
cp -r include/falcosecurity %{buildroot}%{_includedir}/
find %{buildroot}%{_includedir}/falcosecurity -type f -exec chmod 0644 {} +

%if 0%{?suse_version} >= 1600
%check
# noarch: %%ifnarch is evaluated against target=noarch, not the worker.
# Variable-length fields encode sizeof(size_t); tests hard-code 8-byte sizes.
if [ "$(getconf LONG_BIT)" = 64 ]; then
%ctest
else
  echo "skipping codec tests: upstream hard-codes 64-bit size_t"
fi
%endif

%files devel
%license LICENSE
%doc README.md
%dir %{_includedir}/falcosecurity
%{_includedir}/falcosecurity/*.h
%{_includedir}/falcosecurity/events/
%{_includedir}/falcosecurity/internal/

%changelog
