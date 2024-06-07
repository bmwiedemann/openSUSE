#
# spec file for package hashcat
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


%define lname	libhashcat6_2_6
Name:           hashcat
Version:        6.2.6
Release:        0
Summary:        CPU-based password recovery utility
License:        GPL-2.0-or-later AND MIT
Group:          Productivity/Security
URL:            https://hashcat.net/
Source:         https://hashcat.net/files/%name-%version.tar.gz
Source2:        https://hashcat.net/files/%name-%version.tar.gz.asc
#  Key ID: 2048R/8A16544F. Fingerprint: A708 3322 9D04 0B41 99CC 0052 3C17 DA8B 8A16 544F
Source3:        %name.keyring
Source9:        %name-rpmlintrc
Patch1:         system-libs.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  xxhash-devel
BuildRequires:  pkgconfig(clzma)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(zlib)
Provides:       bundled(lzma-sdk) = 21.02
ExclusiveArch:  %ix86 x86_64

%description
Hashcat is a password recovery utility, supporting seven
unique modes of testing for over 100 optimized hashing algorithms.

GPU Driver requirements:

 * AMD GPUs on Linux require "RadeonOpenCompute (ROCm)" Software
   Platform (3.1 or later)
 * AMD GPUs on Windows require "AMD Radeon Adrenalin 2020
   Edition" (20.2.2 or later)
 * Intel and AMD CPUs require "OpenCL Runtime for Intel Core and
   Intel Xeon Processors" (16.1.1 or later)
 * NVIDIA GPUs require "NVIDIA Driver" (440.64 or later) and
   "CUDA Toolkit" (9.0 or later)

%package -n %lname
Summary:        Implementation of the hashcat engine
Group:          System/Libraries

%description -n %lname
Hashcat is a password recovery utility, supporting seven
unique modes of testing for over 100 optimized hashing algorithms.

%package devel
Summary:        Header files for making hashcat plugins
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Hashcat is a password recovery utility, supporting seven
unique modes of testing for over 100 optimized hashing algorithms.

This subpackage contains the header files.

%prep
%autosetup -p1
find . -name .lock -type f -delete

%build
%global margs DOCUMENT_FOLDER="%_docdir/%name" our_CFLAGS="%optflags" LIBRARY_FOLDER="%_libdir"
%make_build %margs -j1

%install
%make_install %margs
b="%buildroot"
ln -s libhashcat.so.%version "$b/%_libdir/libhashcat.so"
# fix stupid placement of arch-dep files
mkdir "$b/%_libdir/%name"
mv "$b/%_datadir/%name/modules" "$b/%_libdir/%name/"
ln -s "%_libdir/%name/modules" "$b/%_datadir/%name/"
%fdupes %buildroot/%_prefix

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%doc README.md
%_bindir/hashcat
%_docdir/%name/
%_libdir/%name/
%_datadir/%name/

%files -n %lname
%_libdir/libhashcat.so.%version

%files devel
%_includedir/hashcat/
%_libdir/libhashcat.so

%changelog
