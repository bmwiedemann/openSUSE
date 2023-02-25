#
# spec file for package kissfft
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2020 Packman Team <packman@links2linux.de>
# Copyright (c) 2017-2020 Fedora Release Engineering <releng@fedoraproject.org>
# Copyright (c) 2016 František Dvořák <valtri@civ.zcu.cz>
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


%define sover   131
Name:           kissfft
Version:        131.1.0
Release:        0
Summary:        Fast Fourier Transform library
License:        BSD-3-Clause AND Unlicense
# was https://sourceforge.net/projects/kissfft
URL:            https://github.com/mborgerding/kissfft
Source0:        https://github.com/mborgerding/kissfft/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
# TESTS
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  python3
BuildRequires:  python3-numpy
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libpng)
# /TESTS

%description
A Fast Fourier Transform based up on the principle, "Keep It Simple, Stupid".
Kiss FFT is a very small, reasonably efficient, mixed radix FFT library that
can use either fixed or floating point data types.

%package devel
Summary:        Fast Fourier Transform library
Requires:       lib%{name}-float%{sover} = %{version}

%description devel
A Fast Fourier Transform based up on the principle, "Keep It Simple, Stupid".
Kiss FFT is a very small, reasonably efficient, mixed radix FFT library that
can use either fixed or floating point data types.

%package -n lib%{name}-float%{sover}
Summary:        Fast Fourier Transform library

%description -n lib%{name}-float%{sover}
A Fast Fourier Transform based up on the principle, "Keep It Simple, Stupid".
Kiss FFT is a very small, reasonably efficient, mixed radix FFT library that
can use either fixed or floating point data types.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%if 0%{?suse_version} <= 1500
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(pwd)/build
%endif
%ctest

%post -n lib%{name}-float%{sover} -p /sbin/ldconfig
%postun -n lib%{name}-float%{sover} -p /sbin/ldconfig

%files
%{_bindir}/fastconv-float
%{_bindir}/fastconvr-float
%{_bindir}/fft-float
%{_bindir}/psdpng-float

%files devel
%license LICENSES/BSD-3-Clause LICENSES/Unlicense
%doc CHANGELOG README.md
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/kiss_fft.h
%{_includedir}/%{name}/kiss_fftnd.h
%{_includedir}/%{name}/kiss_fftndr.h
%{_includedir}/%{name}/kiss_fftr.h
%{_includedir}/%{name}/kissfft.hh
%{_libdir}/lib%{name}-float.so
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}-float.pc

%files -n lib%{name}-float%{sover}
%{_libdir}/lib%{name}-float.so.%{sover}*

%changelog
