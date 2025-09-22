#
# spec file for package libdwarf
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        2.1.0
Release:        0
Summary:        Access DWARF debugging information
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://prevanders.net/dwarf.html
Source:         https://github.com/davea42/libdwarf-code/releases/download/v%{version}/libdwarf-%{version}.tar.xz
Patch0:         https://src.fedoraproject.org/rpms/libdwarf/raw/rawhide/f/libdwarf-both.patch
BuildRequires:  binutils-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libelf-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)

%description
libdwarf is a library of functions to provide read/write DWARF
debugging records.

%package -n libdwarf2
Summary:        Library to access DWARF information in object files
License:        LGPL-2.1-or-later
Group:          System/Libraries
Conflicts:      libdwarf1

%description -n libdwarf2
Library of functions to provide creation of DWARF debugging
information records, DWARF line number information, DWARF address
range and pubnames information, weak names information, and DWARF
frame description information.

%package devel
Summary:        Development files for libdwarf
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libdwarf2 = %{version}
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
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
# Debian name for the package; provide it for cross-discoverability.
Provides:       dwarfutils = %{version}-%{release}

%description tools
Contains dwarfdump, a tool to access DWARF debug information.

%package doc
Summary:        Documentation for libdwarf
License:        GPL-2.0-or-later
Group:          Documentation/Other
BuildArch:      noarch

%description doc
Documentation for libdwarf.

%prep
%autosetup -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%meson -Ddwarfgen=true --default-library=both
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets -n libdwarf2

%files -n libdwarf2
%license src/lib/libdwarf/LIBDWARFCOPYRIGHT src/lib/libdwarf/LGPL.txt
%{_libdir}/libdwarf.so.2*
%{_libdir}/libdwarfp.so.2*

%files devel
%{_includedir}/libdwarf-2
%{_libdir}/libdwarf.so
%{_libdir}/libdwarfp.so
%{_libdir}/pkgconfig/libdwarf.pc

%files devel-static
%{_libdir}/libdwarf.a
%{_libdir}/libdwarfp.a

%files tools
%license src/bin/dwarfdump/GPL.txt
%doc src/bin/dwarfdump/README
%{_bindir}/dwarfdump
%{_bindir}/dwarfgen
%{_mandir}/man1/dwarfdump.1%{?ext_man}
%{_mandir}/man1/dwarfgen.1%{?ext_man}
%dir %{_datadir}/dwarfdump
%{_datadir}/dwarfdump/dwarfdump.conf

%files doc
%doc doc/*.pdf
%doc src/lib/libdwarf/README

%changelog
