#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%define flavor @BUILD_FLAVOR@%{nil}

%bcond_with ringdisabled

%if "%flavor" == "testsuite"
%if %{with ringdisabled}
ExclusiveArch:  do_not_build
%endif
%define build_main 0
%define build_testsuite 1
%else
%define build_main 1
%define build_testsuite 0
%endif

%if %{build_testsuite}
%define debug_package %{nil}
%endif

%if %{build_main}
%define name_suffix %{nil}
%else
%define name_suffix -%{flavor}
%endif

Name:           dwz%{name_suffix}
Version:        0.15
Release:        0
%if %{build_main}
Summary:        DWARF optimization and duplicate removal tool
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Development/Tools/Building
%endif
%if %{build_testsuite}
Summary:        Testsuite results from DWZ
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Development/Tools/Building
%endif
#Git-Clone:	git://sourceware.org/git/dwz
#Git-Web:	https://sourceware.org/git/?p=dwz.git;a=summary
Source:         dwz-%{version}.tar.xz
URL:            https://sourceware.org/dwz/
BuildRequires:  gcc-c++
BuildRequires:  libelf-devel
BuildRequires:  xxhash-devel
BuildRequires:  xz
%if %{build_testsuite}
BuildRequires:  dejagnu
BuildRequires:  elfutils
BuildRequires:  gdb
%endif

%if !%{build_main}
# It's a bit pointless to ship two identical source packages, one for dwz and
# one for dwz-testsuite.  So we make the second one small by excluding the
# source archive.  We could do the same for the patches with NoPatch, but the
# gain is smaller there and looks more cumbersome to maintain.
NoSource:       0
%endif

Source1:        dwz-rpmlintrc
Source2:        tramp3d-v4.cpp.xz

Patch1:         dwz-enable-odr-by-default.patch
Patch2:         dwz-remove-odr-struct-multifile.sh.patch

%if %{build_main}
%description
dwz optimizes DWARF debugging information contained in ELF shared
libraries and executables for size, by replacing DWARF information
representation with equivalent smaller representation where possible,
and by reducing the amount of duplication using techniques from the
DWARF standard appendix E - creating DW_TAG_partial_unit compilation
units (CUs) for duplicated information and using DW_TAG_imported_unit
to import it into each CU that needs it.

The tool handles DWARF 32-bit format debugging sections of versions
2, 3 and 4 and GNU extensions on top of those, though using DWARF 4
or worst case DWARF 3 is strongly recommended.

When not using the -m option (multifile mode), GDB CVS snapshot (soon to be
7.5) is sufficient, when using -m option, GDB from a git branch
http://sources.redhat.com/git/?p=archer.git;a=shortlog;h=refs/heads/archer-tromey-dwz-multifile
is needed.
%endif

%if %{build_testsuite}
%description
This package contains the testsuite results from DWZ.
%endif

%prep
%setup -q -n dwz
%patch1 -p1
%patch2 -p1
cp ../../SOURCES/tramp3d-v4.cpp.xz .
xz -d tramp3d-v4.cpp.xz

%build
%define flags %{optflags} -O3

# Do PGO with tramp3d as input file
%make_build CFLAGS="%{flags} -fprofile-generate" LDFLAGS="-fprofile-generate"
g++ tramp3d-v4.cpp -O2 -g -w -o t1
cp t1 t2
cp t1 t3
cp t1 t4
./dwz -j 1 -m tmp.debug t1 t2 t3 t4
make clean
%make_build CFLAGS="%{flags} -fprofile-use" LDFLAGS="-fprofile-use"

%check
%if %{build_testsuite}
make -k check
%endif

%install
%if %{build_main}
%make_install
%endif

%if %{build_main}
%files
%license COPYING
%{_bindir}/dwz
%{_mandir}/man1/dwz.1%{?ext_man}
%endif

%if %{build_testsuite}
%files
%defattr(-,root,root)
%doc dwz.sum
%doc dwz.log
%endif

%changelog
