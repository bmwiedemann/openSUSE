#
# spec file for package lzo
#
# Copyright (c) 2024 SUSE LLC
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


%define library_package liblzo2-2
Name:           lzo
Version:        2.10
Release:        0
Summary:        A Real-Time Data Compression Library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.oberhumer.com/opensource/lzo/
Source:         https://www.oberhumer.com/opensource/%{name}/download/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
Patch1:         https://src.fedoraproject.org/rpms/lzo/raw/main/f/lzo-2.08-rhbz1309225.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
%{?suse_build_hwcaps_libs}

%description
LZO is a portable lossless data compression library written in ANSI C.
Decompression requires no memory. LZO is suitable for data compression
and decompression in real-time. This means it favors speed over
compression ratio.

%package -n %{library_package}
Summary:        A Real-Time Data Compression Library
Group:          System/Libraries
Provides:       lzo = %{version}-%{release}
Obsoletes:      lzo < %{version}

%description -n %{library_package}
LZO is a portable lossless data compression library written in ANSI C.
Decompression requires no memory. LZO is suitable for data compression
and decompression in real-time. This means it favors speed over
compression ratio.

%package devel
Summary:        Development files for lzo
Group:          Development/Languages/C and C++
Requires:       %{library_package} = %{version}

%description devel
LZO is a portable lossless data compression library written in ANSI C.
Decompression requires no memory. LZO is suitable for data
de-/compression in real-time. This means it favours speed over
compression ratio.

%package devel-static
Summary:        Development files for lzo
Group:          Development/Languages/C and C++
Requires:       lzo-devel = %{version}
Provides:       lzo-devel:%{_libdir}/liblzo.a

%description devel-static
LZO is a portable lossless data compression library written in ANSI C.
Decompression requires no memory. LZO is suitable for data
de-/compression in real-time. This means it favours speed over
compression ratio.

%prep
%autosetup -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CFLAGS="%{optflags} -fvisibility=hidden"
%configure --enable-shared \
           --enable-static \
           --disable-silent-rules \
           --docdir=%{_docdir}/%{name}-devel

#On windows, the build system defines __LZO_EXPORT1 to
# __attribute__((dllexport))) which we can abuse to make
#use of GCC visibility. ;-)
#see http://gcc.gnu.org/wiki/Visibility
#If you remove this, you must disable  -fvisibility=hidden in CFLAGS!

echo '#define __LZO_EXPORT1 __attribute__ ((visibility ("default")))' >> config.h

make %{?_smp_mflags}

%check
make %{?_smp_mflags} check test

%install
%make_install
rm -v %{buildroot}%{_libdir}/liblzo2.la
rm -v %{buildroot}%{_docdir}/%{name}-devel/COPYING

%post   -n %{library_package} -p /sbin/ldconfig
%postun -n %{library_package} -p /sbin/ldconfig

%files -n %{library_package}
%license COPYING
%{_libdir}/liblzo2.so.*

%files devel
%doc AUTHORS BUGS NEWS README THANKS
%doc doc/* util/*
%{_libdir}/liblzo2.so
%{_includedir}/lzo
%{_libdir}/pkgconfig/lzo2.pc

%files devel-static
%{_libdir}/liblzo2.a

%changelog
