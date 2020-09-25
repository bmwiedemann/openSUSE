#
# spec file for package hashcat
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


Name:           hashcat
%define lname	libhashcat6_1_1
Version:        6.1.1
Release:        0
Summary:        CPU-based password recovery utility
License:        MIT AND GPL-2.0-or-later
Group:          Productivity/Security
URL:            https://hashcat.net/

Source:         https://github.com/hashcat/hashcat/archive/v%version.tar.gz
Patch1:         system-libs.patch
BuildRequires:  fdupes
BuildRequires:  gmp-devel
BuildRequires:  xxhash-devel
BuildRequires:  pkgconfig(clzma)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(zlib)
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

%build
%global margs DOCUMENT_FOLDER="%_docdir/%name" our_CFLAGS="%optflags" LIBRARY_FOLDER="%_libdir"
%make_build %margs

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
%dir %_datadir/%name/
%_datadir/%name/modules
%_datadir/%name/hashcat.hcstat2
%_datadir/%name/hashcat.hctune
%dir %_datadir/%name/OpenCL/
%_datadir/%name/OpenCL/*.cl

%files -n %lname
%_libdir/libhashcat.so.%version

%files devel
%_includedir/hashcat/
%_libdir/libhashcat.so
%dir %_datadir/%name/
%_datadir/%name/OpenCL/*.h

%changelog
