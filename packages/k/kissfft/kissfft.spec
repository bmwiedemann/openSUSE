#
# spec file for package kissfft
#
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

# Please submit bugfixes or comments via https://bugs.links2linux.org/
#


%global _over   131
Name:           kissfft
Version:        1.3.1
Release:        0
Summary:        Fast Fourier Transform library
License:        BSD-3-Clause AND Unlicense
# was https://sourceforge.net/projects/kissfft
URL:            https://github.com/mborgerding/kissfft
Source0:        https://github.com/mborgerding/kissfft/archive/v%{_over}.tar.gz#/%{name}-%{_over}.tar.gz
# PATCH-FEATURE-OPENSUSE kissfft-shared.patch aloisio@gmx.com -- use correct build flags and soname for the library
Patch0:         %{name}-shared.patch
# PATCH-FIX-UPSTREAM kissfft-py3_1.patch
Patch1:         kissfft-py3_1.patch
# PATCH-FIX-UPSTREAM kissfft-py3_2.patch
Patch2:         kissfft-py3_2.patch
BuildRequires:  libtool
# TESTS
BuildRequires:  gcc-c++
BuildRequires:  procps
BuildRequires:  python3
BuildRequires:  python3-numpy
BuildRequires:  pkgconfig(fftw3)
# /TESTS
ExclusiveArch:  x86_64

%description
A Fast Fourier Transform based up on the principle, "Keep It Simple, Stupid".
Kiss FFT is a very small, reasonably efficient, mixed radix FFT library that
can use either fixed or floating point data types.

%package devel
Summary:        Fast Fourier Transform library
Requires:       lib%{name}-%{_over} = %{version}

%description devel
A Fast Fourier Transform based up on the principle, "Keep It Simple, Stupid".
Kiss FFT is a very small, reasonably efficient, mixed radix FFT library that
can use either fixed or floating point data types.

%package -n lib%{name}-%{_over}
Summary:        Fast Fourier Transform library

%description -n lib%{name}-%{_over}
A Fast Fourier Transform based up on the principle, "Keep It Simple, Stupid".
Kiss FFT is a very small, reasonably efficient, mixed radix FFT library that
can use either fixed or floating point data types.

%prep
%autosetup -p1 -n %{name}-%{_over}
sed -i -e '1s,%{_bindir}/env python,%{_bindir}/python3,' test/*.py

%build
%make_build

%install
%make_install

# creates support file for pkg-config
mkdir -pv %{buildroot}%{_libdir}/pkgconfig
tee %{buildroot}%{_libdir}/pkgconfig/%{name}.pc << "EOF"
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=${exec_prefix}/%{_lib}
includedir=${prefix}/include

Name: %{name}
Description: Fast Fourier Transform library
Version: %{version}
Libs: -L${libdir} -lkissfft
Cflags: -I${includedir}/kissfft
EOF

%check
make testall

%post -n lib%{name}-%{_over} -p /sbin/ldconfig
%postun -n lib%{name}-%{_over} -p /sbin/ldconfig

%files devel
%license LICENSES/BSD-3-Clause LICENSES/Unlicense
%doc CHANGELOG README
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/kfc.h
%{_includedir}/%{name}/kiss_fft.h
%{_includedir}/%{name}/kiss_fftnd.h
%{_includedir}/%{name}/kiss_fftndr.h
%{_includedir}/%{name}/kiss_fftr.h
%{_includedir}/%{name}/kissfft.hh
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n lib%{name}-%{_over}
%{_libdir}/lib%{name}-%{_over}.so

%changelog
