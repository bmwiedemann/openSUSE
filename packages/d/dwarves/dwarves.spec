#
# spec file for package dwarves
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


%if (0%{?sle_version} && 0%{?sle_version} >= 150600) || (0%{?suse_version} && 0%{?suse_version} > 1500)
# have libbpf >= 1.0.1 and linux-glibc-devel >= 5.16
%define have_libbpf 1
%endif
%if (0%{?sle_version} && 0%{?sle_version} <= 150300) || (0%{?suse_version} && 0%{?suse_version} < 1500)
%define have_libebl_plugins 1
%endif

Name:           dwarves
Version:        1.27
Release:        0
Summary:        DWARF utilities
License:        GPL-2.0-only
Group:          Development/Tools/Debuggers
URL:            https://acmel.wordpress.com/
#Git-Clone:	git://git.kernel.org/pub/scm/devel/pahole/pahole
#Git-Web:	http://git.kernel.org/cgit/devel/pahole/pahole.git
Source:         https://fedorapeople.org/~acme/dwarves/dwarves-%version.tar.xz
Source2:        https://fedorapeople.org/~acme/dwarves/dwarves-%version.tar.sign
Source8:        dwarves.keyring
Source9:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  libdw-devel >= 0.171
BuildRequires:  libelf-devel
BuildRequires:  pkgconfig
%if 0%{?have_libbpf}
BuildRequires:  linux-glibc-devel >= 5.16
BuildRequires:  pkgconfig(libbpf) >= 1.0.0
%endif
BuildRequires:  pkgconfig(zlib)
# Also known by its most prominent tool
Provides:       pahole = %version-%release
%if 0%{?have_libebl_plugins}
BuildRequires:  libebl-devel
%endif

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
%if 0%{?have_libebl_plugins}
Requires:       libebl-plugins
%endif

%description -n libdwarves1
This package contains the libdwarves shared library for the dwarves
toolset, providing processing for DWARF, a debugging data format
for ELF files.

dwarves is a set of tools that use the DWARF debugging information
inserted in ELF binaries by compilers such as GCC, used by well known
debuggers such as GDB, and more recent ones such as systemtap.

%package devel
Summary:        DWARF processing library development files
Group:          Development/Libraries/C and C++
Requires:       libdwarves1 = %version-%release
Obsoletes:      libdwarves-devel < %version-%release
Provides:       libdwarves-devel = %version-%release

%description devel
This package contains the development files for libdwarves, a library
for processing DWARF, a debugging data format for ELF files.

%prep
%autosetup -p1

%build
sv="$PWD/lib.v"
ver=$(echo %version | cut -d+ -f1)
echo "DWARVES_$ver{ global: *; };" >"$sv"
%cmake \
%if 0%{?have_libbpf}
	-DLIBBPF_EMBEDDED=OFF \
%endif
	-DCMAKE_SHARED_LINKER_FLAGS:STRING="-Wl,--version-script=$sv"
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n libdwarves1

%files
%doc README NEWS
%_bindir/*
%_mandir/man*/*

%files -n libdwarves1
%_libdir/*.so.1*

%files devel
%_libdir/*.so
%_includedir/*
%_datadir/%name

%changelog
