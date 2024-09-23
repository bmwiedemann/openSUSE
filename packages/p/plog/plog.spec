#
# spec file for package plog
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


%global debug_package %{nil}
Name:           plog
Version:        1.1.10
Release:        0
Summary:        C++ logging library with versatile output
License:        MIT
URL:            https://github.com/SergiusTheBest/plog
Group:          Development/Libraries/C and C++
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

%description
Plog is a header-only C++ logging library. It supports multiple
logger objects, CSV output, wide string and UTF-8 support, colorized
output, hexdumping, showing localtime as well as UTC, and can even be
used in C++98 mode.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

%build
%cmake -DPLOG_BUILD_TESTS=ON
%cmake_build

%install
%cmake_install

# Delete wrongly installed doc content, we'll docify later
rm -rv %{buildroot}%{_datadir}/doc

%check
%ctest

%files devel
%license LICENSE
%doc README.md doc
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/

%changelog
