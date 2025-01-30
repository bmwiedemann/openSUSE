#
# spec file for package glaze
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Florian "sp1rit" <sp1rit@disroot.org>
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

%define debug_package %{nil}

Name:           glaze
Version:        4.3.1
Release:        0
Summary:        JSON library for modern C++
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/stephenberry/glaze
Source0:        https://github.com/stephenberry/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++ >= 12

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description
Glaze is a JSON library that reads/writes from/to object memory.
It also supports BEVE and CSV.

%description devel
Glaze is a JSON library that reads/writes from/to object memory. It
supports BEVE and CSV as well.

Glaze utilizes SIMD (SSE/AVX/NEON) and deals well with
out-of-sequence data and missing keys. Based on an August 2024
measurement on an Apple M1 CPU, it was measured at 1224/1366 MB/s,
outperforming other implementations like yyjson-0.10.0 by 10/35%% and
rapidjson-1.1.0 by 172/371%% (read/write speeds, respectively).

This subpackage contains development files for %{name}.

%prep
%autosetup -p1

%build
%cmake \
	-DBUILD_TESTING=OFF \
	-Dglaze_DEVELOPER_MODE=OFF \
	-Dglaze_ENABLE_FUZZING=OFF \
	%{nil}
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%doc docs
%{_includedir}/%{name}
%{_datadir}/%{name}

%changelog
