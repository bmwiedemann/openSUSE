#
# spec file for package dwarves
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


Name:           dwarves
Version:        1.18
Release:        0
Summary:        DWARF utilities
License:        GPL-2.0-only
Group:          Development/Tools/Debuggers
URL:            http://acmel.wordpress.com/
#Git-Clone:	git://git.kernel.org/pub/scm/devel/pahole/pahole
#Git-Web:	http://git.kernel.org/cgit/devel/pahole/pahole.git
Source:         https://fedorapeople.org/~acme/dwarves/dwarves-%version.tar.xz
Source2:        https://fedorapeople.org/~acme/dwarves/dwarves-%version.tar.sign
Source9:        baselibs.conf
Patch1:         libbpf-Fix-libbpf-hashmap-on-I-LP32-architectures.patch
BuildRequires:  cmake
BuildRequires:  libdw-devel >= 0.170
%if 0%{?suse_version} < 1550
BuildRequires:  libebl-devel
%endif
BuildRequires:  libelf-devel
BuildRequires:  pkgconfig(zlib)
# Also known by its most prominent tool
Provides:       pahole = %version-%release

%description
dwarves is a set of tools that use the DWARF debugging information
inserted in ELF binaries by compilers such as GCC, used by well known
debuggers such as GDB, and more recent ones such as systemtap.

Utilities in the dwarves suite include pahole, that can be used to
find alignment holes in structs and classes in languages such as C,
C++, but not limited to these.

It also extracts other information such as CPU cacheline alignment,
helping pack those structures to achieve more cache hits.

A diff like tool, codiff can be used to compare the effects changes
in source code generate on the resulting binaries.

Another tool is pfunct, that can be used to find all sorts of
information about functions, inlines, decisions made by the compiler
about inlining, etc.

%package -n libdwarves1
Summary:        DWARF processing libraries of dwarves tools
Group:          System/Libraries
%if 0%{?suse_version} < 1550
Requires:       libebl-plugins
%endif

%description -n libdwarves1
This package contains the libdwarves shared library for the dwarves
toolset, providing processing for DWARF, a debugging data format
for ELF files.

dwarves is a set of tools that use the DWARF debugging information
inserted in ELF binaries by compilers such as GCC, used by well known
debuggers such as GDB, and more recent ones such as systemtap.

%package -n libdwarves-devel
Summary:        DWARF processing library development files
Group:          Development/Libraries/C and C++
Requires:       libdwarves1 = %version-%release

%description -n libdwarves-devel
This package contains the development files for libdwarves, a library
for processing DWARF, a debugging data format for ELF files.

%prep
%autosetup -p1

%build
sv="$PWD/lib.v"
echo "DWARVES_%version { global: *; };" >"$sv"
%cmake -DCMAKE_SHARED_LINKER_FLAGS:STRING="-Wl,--version-script=$sv"
%cmake_build

%install
%cmake_install

%post   -n libdwarves1 -p /sbin/ldconfig
%postun -n libdwarves1 -p /sbin/ldconfig

%files
%doc README NEWS
%_bindir/*
%_mandir/man*/*

%files -n libdwarves1
%_libdir/*.so.1*

%files -n libdwarves-devel
%_libdir/*.so
%_includedir/*
%_datadir/%name

%changelog
