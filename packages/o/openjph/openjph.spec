#
# spec file for package openjph
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


Name:           openjph
Version:        0.26.3
Release:        0
Summary:        An implementation of JPEG2000 Part-15
License:        BSD-2-Clause
Group:          Productivity/Graphics/Convertors
URL:            https://github.com/aous72/OpenJPH
Source:         https://github.com/aous72/OpenJPH/archive/refs/tags/%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  cmake >= 3.10
BuildRequires:  gcc-c++
BuildRequires:  libtiff-devel

%description
This package contains libopenjph, a library implementing the JPEG-2000
standard Part 15.

%package -n libopenjph0_26
Summary:        JPEG-2000 Part-15 library
Group:          System/Libraries

%description -n libopenjph0_26
This is an implementation of High-throughput JPEG2000 (HTJ2K), also
known as JPH, JPEG2000 Part 15, ISO/IEC 15444-15, or ITU-T T.814.
Only the LGT 5/3 wavelet transform for lossless compression and the
CDF 9/7 wavelet transform for lossy compression are supported.

%package devel
Summary:        Development files for libopenjph, a JPEG-2000 Part 15 library
Group:          Development/Libraries/C and C++
Requires:       libjpeg-devel
Requires:       libopenjph0_26 = %{version}

%description devel
This package contains libopenjph, a library implementing the JPEG-2000
standard Part 15.

%prep
%autosetup -p1 -n OpenJPH-%{version}

%build
%ifarch x86_64
%cmake -DBUILD_SHARED_LIBS:BOOL=ON -DOJPH_DISABLE_INTEL_SIMD:BOOL=OFF
%else
%cmake -DBUILD_SHARED_LIBS:BOOL=ON -DOJPH_DISABLE_INTEL_SIMD:BOOL=ON
%endif

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n libopenjph0_26

%files
%license LICENSE
%doc README.md
%{_bindir}/ojph_compress
%{_bindir}/ojph_expand

%files -n libopenjph0_26
%{_libdir}/libopenjph*.so.*

%files devel
%{_includedir}/openjph/
%{_libdir}/libopenjph.so
%{_libdir}/pkgconfig/openjph.pc
%{_libdir}/cmake/openjph/

%changelog
