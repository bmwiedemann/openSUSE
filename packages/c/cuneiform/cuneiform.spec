#
# spec file for package cuneiform
#
# Copyright (c) 2020 SUSE LLC
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


%define major   1
Name:           cuneiform
Version:        1.1.0
Release:        0
Summary:        OCR System
License:        BSD-3-Clause
Group:          Productivity/Graphics/Other
URL:            https://launchpad.net/cuneiform-linux
Source0:        http://launchpad.net/cuneiform-linux/1.1/1.1/+download/%{name}-linux-%{version}.tar.bz2
Source1:        cuneiform.1
Patch0:         cuneiform-1.1.0-c-assert.patch
Patch1:         cuneiform-1.1.0-fix_buffer_overflow.patch
Patch2:         cuneiform-1.1.0-fix_buffer_overflow_2.patch
Patch3:         cuneiform-1.1.0-gcc6.patch
Patch4:         cuneiform-1.1.0-gcc7.patch
Patch6:         cuneiform-1.1.0-libm.patch
Patch7:         cuneiform-1.1.0-strings.patch
Patch8:         cuneiform-1.1.0-typos.patch
Patch9:         cuneiform-brp.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libMagick++-devel
Conflicts:      cuneiform-multilang
Provides:       ocr-engine
ExclusiveArch:  %{ix86} x86_64

%description
Cuneiform is an multi-language OCR system originally developed and open
sourced by Cognitive Technologies. Cuneiform was originally a Windows
program, which was ported to Linux by Jussi Pakkanen.
Supported languages: eng ger fra rus swe spa ita ruseng ukr srp hrv pol
dan por dut cze rum hun bul slo lav lit est tur.

%package -n lib%{name}%{major}
Summary:        Cuneiform Shared Libraries
Group:          System/Libraries

%description -n lib%{name}%{major}
Shared libraries for the package cuneiform.

%package -n lib%{name}-devel
Summary:        Development Files for Cuneiform
Group:          Development/Libraries/C and C++
Requires:       libcuneiform%{major} = %{version}

%description -n lib%{name}-devel
Development files for the package cuneiform.

%prep
%autosetup -n %{name}-linux-%{version} -p1

%build
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=85788
export CXXFLAGS="%{optflags} -Wno-stringop-overflow"
export CFLAGS="%{optflags} -Wno-stringop-overflow -fcommon"
%cmake \
    -DBUILD_TESTING=ON
%cmake_build

%install
%cmake_install
install -Dpm 0644 %{SOURCE1} \
  %{buildroot}%{_mandir}/man1/%{name}.1
%fdupes %{buildroot}%{_datadir}

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%ctest

%post -n lib%{name}%{major} -p /sbin/ldconfig
%postun -n lib%{name}%{major} -p /sbin/ldconfig

%files
%license cuneiform_src/Kern/license.txt
%doc readme.txt issues.txt
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man?/*

%files -n lib%{name}%{major}
%{_libdir}/*.so.*

%files -n lib%{name}-devel
%{_libdir}/*.so
%{_includedir}/*.h

%changelog
