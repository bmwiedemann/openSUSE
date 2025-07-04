#
# spec file for package libaec
#
# Copyright (c) 2025 SUSE LLC
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


Name:           libaec
Version:        1.1.4
Release:        0
Summary:        Adaptive Entropy Coding library
License:        BSD-2-Clause
Group:          Productivity/Archiving/Compression
URL:            https://gitlab.dkrz.de/k202009/libaec
Source:         https://gitlab.dkrz.de/k202009/libaec/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Libaec provides lossless compression of signed or unsigned integers
(samples) of sizes 1 to 32 bits wide. The library achieves best
results for low entropy data as often encountered in space imaging
instrument data or numerical model output from weather or climate
simulations.

%package -n libaec0
Summary:        Adaptive Entropy Coding library
Group:          System/Libraries

%description -n libaec0
Libaec provides lossless compression of signed or unsigned integers
(samples) of sizes 1 to 32 bits wide. The library achieves best
results for low entropy data as often encountered in space imaging
instrument data or numerical model output from weather or climate
simulations. While floating point representations are not directly
supported, they can also be efficiently coded by grouping exponents
and mantissa.

Libaec implements Golomb Rice coding as defined in the Space Data
System Standard documents 121.0-B-3 and 120.0-G-2.

%package devel
Summary:        Development files for libaec (Adaptive Entropy Coding library)
Group:          Development/Libraries/C and C++
Requires:       libaec0 = %{version}-%{release}

%description devel
Development files for libaec (Adaptive Entropy Coding library), a lossless
compression library for low entropy data.

%package -n libsz2
Summary:        Lossless compression library for scientific data
Group:          System/Libraries

%description -n libsz2
Lossless compression library for scientific data. Libsz2 is a drop-in
replacement for the SZIP library (http://www.hdfgroup.org/doc_resource/SZIP).

%package -n sz2-devel
Summary:        Development files for libsz2
Group:          Development/Libraries/C and C++
Requires:       libaec-devel = %{version}-%{release}
Requires:       libsz2 = %{version}-%{release}
Provides:       libsz2-devel = %{version}-%{release}
Obsoletes:      libsz2-devel < %{version}-%{release}

%description -n sz2-devel
Header files for libsz2, a drop-in replacement for the
SZIP library (http://www.hdfgroup.org/doc_resource/SZIP).

%prep
%autosetup -n "%{name}-v%{version}"

%build
%cmake \
  -DBUILD_STATIC_LIBS=OFF
%cmake_build

%check
%ctest

%install
%cmake_install

%post -n libaec0 -p /sbin/ldconfig
%post -n libsz2 -p /sbin/ldconfig
%postun -n libaec0 -p /sbin/ldconfig
%postun -n libsz2 -p /sbin/ldconfig

%files -n libaec0
%license LICENSE.txt
%doc README.md CHANGELOG.md
%{_libdir}/libaec.so.0*

%files devel
%{_libdir}/cmake/%{name}
%{_includedir}/libaec.h
%{_libdir}/libaec.so

%files -n libsz2
%license LICENSE.txt
%doc README.SZIP
%{_libdir}/libsz.so.2*

%files -n sz2-devel
%{_includedir}/szlib.h
%{_libdir}/libsz.so

%changelog
