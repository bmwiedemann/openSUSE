#
# spec file for package dwz
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           dwz
Version:        0.12
Release:        0
Summary:        DWARF optimization and duplicate removal tool
#Git-Clone:	git://sourceware.org/git/dwz
#Git-Web:	https://sourceware.org/git/?p=dwz.git;a=summary
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Development/Tools/Building
Source:         %{name}-%{version}.tar.xz
Patch0:         dwz-0.12-ignore-nobits.patch
Patch1:         dwz-0.12-DW_OP_GNU_variable_value.patch
Patch2:         dwz-low-mem-Fix-DW_OP_GNU_parameter_ref-handling-in-read_exprloc.patch
BuildRequires:  libelf-devel
BuildRequires:  xz

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

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%make_install

%files
%license COPYING
%{_bindir}/dwz
%{_mandir}/man1/dwz.1%{?ext_man}

%changelog
