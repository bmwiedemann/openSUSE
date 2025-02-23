#
# spec file for package liquid-dsp
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2017-2025, Martin Hauke <mardnh@gmx.de>
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


%define sover 1
%define libname libliquid%{sover}
Name:           liquid-dsp
Version:        1.7.0
Release:        0
Summary:        Digital signal processing library for software-defined radios
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://liquidsdr.org
#Git-Clone:     https://github.com/jgaeddert/liquid-dsp.git
Source:         https://github.com/jgaeddert/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-chromosome-32bit.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.10

%description
liquid-dsp is a signal processing library for software-defined
radios written in C. Its purpose is to provide a set of extensible DSP modules
that do no rely on external dependencies or cumbersome frameworks.

%package -n %{libname}
Summary:        Digital signal processing library for software-defined radios
Group:          Development/Libraries/C and C++
Obsoletes:      libliquid < %{version}
Provides:       libliquid = %{version}

%description -n %{libname}
liquid-dsp is a signal processing library for software-defined
radios written in C. Its purpose is to provide a set of extensible DSP modules
that do no rely on external dependencies or cumbersome frameworks.

%package devel
Summary:        Development files for the liquid-dsp library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Obsoletes:      libliquid-devel < %{version}
Provides:       libliquid-devel = %{version}

%description devel
liquid-dsp is a signal processing library for software-defined
radios written in C. Its purpose is to provide a set of extensible DSP modules
that do no rely on external dependencies or cumbersome frameworks.

This subpackage contains libraries and header files for developing
applications that want to make use of libliquid.

%prep
%autosetup -p1

%build
%cmake \
	-DBUILD_EXAMPLES=OFF \
	-DENABLE_SIMD=OFF \
	%{nil}
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license LICENSE
%doc CHANGELOG.md README.rst
%{_libdir}/libliquid.so.%{sover}
%{_libdir}/libliquid.so.%{sover}.*

%files devel
%license LICENSE
%{_includedir}/liquid
%{_libdir}/libliquid.so

%changelog
