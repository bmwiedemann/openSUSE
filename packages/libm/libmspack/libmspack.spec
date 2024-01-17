#
# spec file for package libmspack
#
# Copyright (c) 2023 SUSE LLC
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


# "alpha" in the version string just says that it is an alpha version.
%define _version %{version}alpha
Name:           libmspack
Version:        0.11
Release:        0
Summary:        Library That Implements Different Microsoft Compressions
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://www.cabextract.org.uk/libmspack/
Source:         https://www.cabextract.org.uk/libmspack/%{name}-%{_version}.tar.gz
Source2:        baselibs.conf
BuildRequires:  pkgconfig

%description
The purpose of libmspack is to provide both compression and
decompression of some loosely related file formats used by Microsoft.
Currently the most common formats are implemented.

%package -n libmspack0
Summary:        Library That Implements Different Microsoft Compressions
Group:          System/Libraries

%description -n libmspack0
The purpose of libmspack is to provide both compression and
decompression of some loosely related file formats used by Microsoft.
Currently the most common formats are implemented.

%package devel
Summary:        Static libraries, header files and documentation for libmspack
Group:          Development/Libraries/C and C++
Requires:       libmspack0 = %{version}

%description devel
The libmspack-devel package contains the header files and static
libraries necessary for developing programs using libmspack.

%package -n mspack-examples
Summary:        Library That Implements Different Microsoft Compressions
# Name up to 0.9 (SLE 15 *, Leap 15 *):
Group:          Productivity/File utilities
Provides:       mspack-tools = %{version}
Obsoletes:      mspack-tools < %{version}

%description -n mspack-examples
The purpose of libmspack is to provide both compression and
decompression of some loosely related file formats used by Microsoft.
Currently the most common formats are implemented.

This subpacke provides useful programs that make use of libmspack.
 * cabd_memory - An implementation of the mspack_system interface using
                 only memory
 * cabrip      - Extracts any CAB files embedded in another file.
 * chmextract  - Extracts all files in a CHM file to disk.
 * msexpand    - Expands an SZDD or KWAJ file.
 * multifh     - An implementation of the mspack_system interface which
                 can access many things: regular disk files, already
                 opened stdio FILE*  file pointers, open file
                 descriptors, blocks of memory
 * oabextract  - Extracts an Exchange Offline Address Book (.LZX) file.

%prep
%setup -q -n %{name}-%{_version}

%build
%configure\
	--disable-static
%make_build

%install
%make_install
cd examples
install -d %{buildroot}%{_bindir}
../libtool --mode=install %{_bindir}/install -c cabd_memory cabrip chmextract msexpand multifh oabextract %{buildroot}%{_bindir}
rm %{buildroot}%{_libdir}/*.*a

%check
%make_build check

%post -n libmspack0 -p /sbin/ldconfig
%postun -n libmspack0 -p /sbin/ldconfig

%files -n mspack-examples
%{_bindir}/cabd_memory
%{_bindir}/cabrip
%{_bindir}/chmextract
%{_bindir}/msexpand
%{_bindir}/multifh
%{_bindir}/oabextract

%files -n libmspack0
%license COPYING.LIB
# NEWS is empty
%doc AUTHORS ChangeLog README TODO
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%changelog
