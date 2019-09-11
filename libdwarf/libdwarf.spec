#
# spec file for package libdwarf
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libdwarf
Version:        20180129
Release:        0
Summary:        Access DWARF debugging information
License:        LGPL-2.1+ and GPL-2.0+
Group:          Development/Libraries/C and C++
Url:            http://prevanders.net/dwarf.html
#Git-Clone:	git://git.code.sf.net/p/libdwarf/code
Source:         http://prevanders.net/%{name}-%{version}.tar.gz
BuildRequires:  binutils-devel
BuildRequires:  libelf-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libdwarf is a library of functions to provide read/write DWARF
debugging records.

%package -n libdwarf1
Summary:        Library to access DWARF information in object files
License:        LGPL-2.1+
Group:          System/Libraries

%description -n libdwarf1
Library of functions to provide creation of DWARF debugging
information records, DWARF line number information, DWARF address
range and pubnames information, weak names information, and DWARF
frame description information.

%package devel
Summary:        Development files for libdwarf
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Requires:       libdwarf1 = %{version}

%description devel
Contains the static libraries and header files of libdwarf.

libdwarf is a library of functions to provide read/write DWARF
debugging records.

%package devel-static
Summary:        Static library for libdwarf
License:        LGPL-2.1+
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
License:        GPL-2.0+
Group:          Development/Tools/Building
Provides:       dwarfutils = %{version}-%{release}

%description tools
Contains dwarfdump, a tool to access DWARF debug information.

%package doc
Summary:        Documentation for libdwarf
License:        GPL-2.0+
Group:          Documentation/Other

%description doc
Documentation for libdwarf.

%prep
%setup -q -n dwarf-%{version}

%build
export CFLAGS="%{optflags}"
## libdwarf
cd libdwarf
CFLAGS="$CFLAGS -fPIC" %configure --enable-shared
make %{?_smp_mflags}
cd -
## dwarfdump
cd dwarfdump
%configure
# LD_LIBRARY_PATH required since libdwarf.so and libdwarf.a
# are available - and tag_tree_build get linked against
# shared library. This workaround avoids patching of dwarfdump
# Makefile
#  - dgollub (20081001)
LD_LIBRARY_PATH="../libdwarf" make %{?_smp_mflags}
cd -

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_includedir}/libdwarf
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 libdwarf/libdwarf.a %{buildroot}%{_libdir}
install -m 0644 libdwarf/libdwarf.so* %{buildroot}%{_libdir}
install -m 0755 dwarfdump/dwarfdump %{buildroot}%{_bindir}
install -m 0644 dwarfdump/dwarfdump.1 %{buildroot}%{_mandir}/man1/dwarfdump.1
install -m 0644 libdwarf/libdwarf.h %{buildroot}%{_includedir}/libdwarf
install -m 0644 libdwarf/dwarf.h %{buildroot}%{_includedir}/libdwarf

%post -n libdwarf1 -p /sbin/ldconfig
%postun -n libdwarf1 -p /sbin/ldconfig

%files -n libdwarf1
%defattr(-,root,root)
%doc libdwarf/LIBDWARFCOPYRIGHT libdwarf/COPYING libdwarf/LGPL.txt
%{_libdir}/libdwarf.so.1

%files devel
%defattr(-,root,root)
%{_libdir}/libdwarf.so
%{_includedir}/libdwarf

%files devel-static
%defattr(-,root,root)
%{_libdir}/libdwarf.a

%files tools
%defattr(-,root,root)
%{_bindir}/dwarfdump
%{_mandir}/man1/dwarfdump*
%doc dwarfdump/README libdwarf/COPYING dwarfdump/GPL.txt

%files doc
%defattr(-,root,root)
%doc libdwarf/*.pdf
%doc libdwarf/README

%changelog
