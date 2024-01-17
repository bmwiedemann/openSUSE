#
# spec file for package elfutils
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


Name:           elfutils
Version:        0.189
Release:        0
Summary:        Higher-level library to access ELF files
License:        GPL-3.0-or-later
Group:          Development/Tools/Building
URL:            https://sourceware.org/elfutils/
#Git-Clone:	git://sourceware.org/git/elfutils
Source:         https://fedorahosted.org/releases/e/l/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source1:        README-BEFORE-ADDING-PATCHES
Source2:        baselibs.conf
Source4:        https://fedorahosted.org/releases/e/l/%{name}/%{version}/%{name}-%{version}.tar.bz2.sig
Source5:        %{name}.keyring
Source6:        elfutils-rpmlintrc
Patch1:         harden_debuginfod.service.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
# For libstdc++ demangle support
BuildRequires:  gcc-c++
BuildRequires:  libbz2-devel
BuildRequires:  libzstd-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  zstd

%description
elfutils is a collection of utilities and libraries to read, create
and modify ELF binary files, find and handle DWARF debug data,
symbols, thread state and stacktraces for processes and core files.

%package -n libasm1
Summary:        A collection of utilities and DSOs to handle compiled objects
Group:          System/Libraries
License:        GPL-2.0-or-later OR LGPL-3.0-or-later

%description -n libasm1
libasm contains the "asm" and "disasm" functions to assemble and
disassamble instructions. (There is only partial support for i686 and
BPF instructions.) This is part of the elfutils package.

%package -n libasm-devel
Summary:        A collection of utilities and DSOs to handle compiled objects
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libasm1 = %{version}
License:        GPL-2.0-or-later OR LGPL-3.0-or-later

%description -n libasm-devel
This package contains the headers and libraries needed to build
applications that require libasm.

%package -n libelf1
Summary:        Library to read and write ELF files
Group:          System/Libraries
License:        GPL-2.0-or-later OR LGPL-3.0-or-later

%description -n libelf1
This package provides a high-level library to read and write ELF files.
This is part of the elfutils package.

%package -n libelf-devel
Summary:        Development files for libelf
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libelf1 = %{version}
Conflicts:      libelf0-devel
License:        GPL-2.0-or-later OR LGPL-3.0-or-later

%description -n libelf-devel
This package contains the headers and libraries needed to build
applications that require libelf.

%package -n libdw1
Summary:        Library to access DWARF debugging information
Group:          System/Libraries
License:        GPL-2.0-or-later OR LGPL-3.0-or-later

%description -n libdw1
This package provides a high-level library to access the DWARF debugging
information. This is part of the elfutils package.

%package -n libdw-devel
Summary:        Development files for libdw
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libdw1 = %{version}
Requires:       libelf-devel = %{version}
License:        GPL-2.0-or-later OR LGPL-3.0-or-later

%description -n libdw-devel
This package contains the headers and libraries needed to build
applications that require libdw.

%package -n libdebuginfod1-dummy
Summary:        Library for build-id HTTP ELF/DWARF server
Group:          System/Libraries
Provides:       libdebuginfod1 = %{version}
License:        GPL-2.0-or-later OR LGPL-3.0-or-later

%description -n libdebuginfod1-dummy
The libdebuginfod1 package contains shared libraries
dynamically loaded from -ldw, which use a debuginfod service
to look up debuginfo and associated data. Also includes a
command-line frontend.
The package is dummy.

%package -n libdebuginfod-dummy-devel
Summary:        Libraries and headers to build debuginfod client applications
Group:          Development/Libraries/C and C++
Provides:       libdebuginfod-devel = %{version}
License:        GPL-2.0-or-later OR LGPL-3.0-or-later
Requires:       libdebuginfod1-dummy = %{version}

%description -n libdebuginfod-dummy-devel
The libdebuginfod-devel package contains the libraries
to create applications to use the debuginfod service.
The package is dummy.

%package -n debuginfod-dummy-client
Summary:        Command line client for build-id HTTP ELF/DWARF server
Group:          Development/Tools/Building
Provides:       debuginfod-client = %{version}

%description -n debuginfod-dummy-client
The elfutils-debuginfod-client package contains a command-line frontend.
The package is dummy.

%lang_package

%prep
%autosetup -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CFLAGS="%optflags -Werror=date-time"
CFLAGS+=" -g" # tests need debug info enabled (boo#1031556)
%ifarch %sparc
# Small PIC model not sufficient
CFLAGS+=" -fPIC"
%endif
autoreconf -fi
# some patches create new test scripts, which are created 644 by default
chmod a+x tests/run*.sh
%configure --program-prefix=eu- --disable-debuginfod --enable-libdebuginfod=dummy
%make_build

%install
%make_install
# remove unneeded files
rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_sysconfdir}/profile.d/debuginfod.*sh
rm -f %{buildroot}/%{_libdir}/pkgconfig/libdebuginfod.pc
ls -lR %{buildroot}/%{_libdir}/libelf*
%find_lang %{name}

%post -n libasm1 -p /sbin/ldconfig
%post -n libelf1 -p /sbin/ldconfig
%post -n libdw1 -p /sbin/ldconfig
%postun -n libasm1 -p /sbin/ldconfig
%postun -n libelf1 -p /sbin/ldconfig
%postun -n libdw1 -p /sbin/ldconfig
%post -n libdebuginfod1-dummy -p /sbin/ldconfig
%postun -n libdebuginfod1-dummy -p /sbin/ldconfig

%check
%if 0%{?qemu_user_space_build}
# qemu-linux-user does not support ptrace and a few other process details
export XFAIL_TESTS="dwfl-proc-attach run-backtrace-dwarf.sh run-backtrace-native.sh run-deleted.sh"
%endif
%make_build check

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS NOTES README THANKS TODO
%{_bindir}/eu-addr2line
%{_bindir}/eu-ar
%{_bindir}/eu-elfclassify
%{_bindir}/eu-elfcmp
%{_bindir}/eu-elfcompress
%{_bindir}/eu-elflint
%{_bindir}/eu-findtextrel
%{_bindir}/eu-make-debug-archive
%{_bindir}/eu-nm
%{_bindir}/eu-objdump
%{_bindir}/eu-ranlib
%{_bindir}/eu-readelf
%{_bindir}/eu-size
%{_bindir}/eu-stack
%{_bindir}/eu-strings
%{_bindir}/eu-strip
%{_bindir}/eu-unstrip
%{_mandir}/man1/eu-*.1*

%files -n libasm1
%{_libdir}/libasm.so.*
%{_libdir}/libasm-%{version}.so

%files -n libasm-devel
%{_libdir}/libasm.so
%{_libdir}/libasm.a
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/libasm.h

%files -n libelf1
%{_libdir}/libelf.so.*
%{_libdir}/libelf-%{version}.so

%files -n libelf-devel
%{_libdir}/libelf.so
%{_libdir}/libelf.a
%{_includedir}/libelf.h
%{_includedir}/gelf.h
%{_includedir}/nlist.h
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/elf-knowledge.h
%{_includedir}/elfutils/version.h
%{_libdir}/pkgconfig/libelf.pc
%{_mandir}/man3/elf_*.3*

%files -n libdw1
%{_libdir}/libdw.so.*
%{_libdir}/libdw-%{version}.so

%files -n libdw-devel
%{_libdir}/libdw.a
%{_libdir}/libdw.so
%{_includedir}/dwarf.h
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/libdw.h
%{_includedir}/elfutils/libdwelf.h
%{_includedir}/elfutils/libdwfl.h
%{_includedir}/elfutils/known-dwarf.h
%{_libdir}/pkgconfig/libdw.pc

%files -n libdebuginfod1-dummy
%{_libdir}/libdebuginfod.so.*
%{_libdir}/libdebuginfod-%{version}.so

%files -n libdebuginfod-dummy-devel
%{_mandir}/man3/debuginfod_*.3*
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/debuginfod.h
%{_libdir}/libdebuginfod.so

%files -n debuginfod-dummy-client
%{_bindir}/debuginfod-find
%{_mandir}/man1/debuginfod-find.1*
%{_mandir}/man7/debuginfod-client-config.7*

%files lang -f %{name}.lang

%changelog
