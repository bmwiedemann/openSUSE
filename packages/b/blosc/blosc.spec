#
# spec file for package blosc
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
%define libname lib%{name}%{major}
Name:           blosc
Version:        1.19.0
Release:        0
Summary:        A blocking, shuffling and lossless compression library
License:        MIT AND BSD-3-Clause AND BSD-2-Clause
Group:          Productivity/Archiving/Compression
URL:            https://www.blosc.org/
Source:         https://github.com/Blosc/c-blosc/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libzstd-devel
BuildRequires:  pkgconfig
BuildRequires:  snappy-devel
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(zlib)

%description
Blosc is a compressor for binary data, designed to transmit data to
the processor cache faster than the traditional, non-compressed,
direct memory fetch approach via a memcpy() call. Blosc is not only a
compressor for data size reduction, but also for accelerating
memory-bound computations.

It uses the blocking technique to reduce activity on the memory bus,
which works by dividing datasets in blocks that are small enough to
fit in caches of processors and perform (de)compression there. SIMD
and multi-threading capabilities are leveraged if available.

Blosc is a metacompressor; it can use different compression
algorithms, such as BloscLZ, LZ4, LZ4HC, Snappy and Zlib.

%package -n %{libname}
Summary:        A blocking, shuffling and lossless compression library
Group:          System/Libraries

%description -n %{libname}
Blosc is a metacompressor (using actual algorithms like BloscLZ, LZ4,
LZ4HC, Snappy or Zlib) for binary data, with a focus on reducing
memory bus activity.

%package devel
Summary:        Development libraries for %{libname}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
This package provides development libraries and headers
for %{libname}.

%prep
%setup -q -n c-blosc-%{version}

%build
%cmake \
  -DPREFER_EXTERNAL_SNAPPY=ON \
  -DPREFER_EXTERNAL_ZLIB=ON \
  -DPREFER_EXTERNAL_ZSTD=ON \
  -DPREFER_EXTERNAL_LZ4=ON \
  -DBUILD_STATIC=OFF
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_libdir}/libblosc.a

# Put .pc files in right directory
if [ "%{_libdir}" != "%{_libexecdir}" ] ; then
mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}%{_libexecdir}/pkgconfig %{buildroot}%{_libdir}/pkgconfig
rm -d %{buildroot}%{_libexecdir}
fi

%check
export LD_PRELOAD="$LD_PRELOAD  %{buildroot}%{_libdir}/libblosc.so  %{buildroot}%{_libdir}/libblosc.so.%{major} `pwd`/build/blosc/libblosc_testing.so"
%ctest

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc LICENSES/*.txt
%doc ANNOUNCE.rst README.md README_THREADED.rst RELEASE_NOTES.rst THANKS.rst
%{_libdir}/libblosc.so.%{major}
%{_libdir}/libblosc.so.%{version}

%files devel
%doc README_HEADER.rst
%doc examples/
%{_includedir}/blosc.h
%{_includedir}/blosc-export.h
%{_libdir}/libblosc.so
%{_libdir}/pkgconfig/blosc.pc

%changelog
