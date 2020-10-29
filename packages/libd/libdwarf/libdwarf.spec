#
# spec file for package libdwarf
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


Name:           libdwarf
Version:        20201020
Release:        0
Summary:        Access DWARF debugging information
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://prevanders.net/dwarf.html
Source:         http://prevanders.net/%{name}-%{version}.tar.gz
BuildRequires:  binutils-devel
BuildRequires:  libelf-devel

%description
libdwarf is a library of functions to provide read/write DWARF
debugging records.

%package -n libdwarf1
Summary:        Library to access DWARF information in object files
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libdwarf1
Library of functions to provide creation of DWARF debugging
information records, DWARF line number information, DWARF address
range and pubnames information, weak names information, and DWARF
frame description information.

%package devel
Summary:        Development files for libdwarf
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libdwarf1 = %{version}
Requires:       libelf-devel

%description devel
Contains the static libraries and header files of libdwarf.

libdwarf is a library of functions to provide read/write DWARF
debugging records.

%package devel-static
Summary:        Static library for libdwarf
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Provides:       libdwarf-devel:%{_libdir}/libdwarf.a

%description devel-static
Contains the static library of libdwarf.

libdwarf is a library of functions to provide read/write DWARF
debugging records.

%package tools
Summary:        DWARF-related tools
# Debian name for the package; provide it for cross-discoverability.
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
Provides:       dwarfutils = %{version}-%{release}

%description tools
Contains dwarfdump, a tool to access DWARF debug information.

%package doc
Summary:        Documentation for libdwarf
License:        GPL-2.0-or-later
Group:          Documentation/Other

%description doc
Documentation for libdwarf.

%prep
%setup -q

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CFLAGS="%{optflags}"
CFLAGS="$CFLAGS -fPIC" %configure --enable-shared
%make_build

%install
%make_install
mkdir %{buildroot}%{_includedir}/libdwarf
mv %{buildroot}%{_includedir}/*.h %{buildroot}%{_includedir}/libdwarf
rm -r %{buildroot}/%{_datadir}/libdwarf/

%post -n libdwarf1 -p /sbin/ldconfig
%postun -n libdwarf1 -p /sbin/ldconfig

%files -n libdwarf1
%license libdwarf/COPYING libdwarf/LIBDWARFCOPYRIGHT libdwarf/LGPL.txt
%{_libdir}/libdwarf.so.1*

%files devel
%{_libdir}/libdwarf.la
%{_libdir}/libdwarf.so
%{_includedir}/libdwarf

%files devel-static
%{_libdir}/libdwarf.a

%files tools
%{_bindir}/dwarfdump
%{_mandir}/man1/dwarfdump*
%license libdwarf/COPYING
%dir %{_datadir}/dwarfdump
%{_datadir}/dwarfdump/dwarfdump.conf
%doc dwarfdump/README dwarfdump/GPL.txt

%files doc
%doc libdwarf/*.pdf
%doc libdwarf/README

%changelog
