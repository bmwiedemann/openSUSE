#
# spec file for package tcl
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%global debug_package %{nil}
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define origname tcl

%if 0%{!?_rpmmacrodir:1}
%define _rpmmacrodir %{_rpmconfigdir}/macros.d
%endif
%define rrc %{nil}
%define TCL_MINOR %(echo %{version} | cut -c1-3)
%define itclver 4.3.7
%define scriptdir %{_libdir}/tcl
Name:           %{origname}%{psuffix}
Version:        8.6.18
Release:        0
Summary:        The Tcl Programming Language
License:        TCL
URL:            https://www.tcl-lang.org
Source0:        https://prdownloads.sourceforge.net/tcl/%{origname}%{version}%{rrc}-src.tar.gz
Source1:        tcl-rpmlintrc
Source2:        baselibs.conf
Source3:        macros.tcl
Patch0:         tcl-fix-socket-13.1.patch
BuildRequires:  autoconf
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
%if %{with test}
# Required for the test suite only.
BuildRequires:  timezone
%endif
%if %{without test}
# Require the extension from the SQLite package instead of shipping
# the embedded copy, which might be outdated.
Requires:       sqlite3-tcl
Provides:       itcl = %{itclver}
Provides:       tclsh
Provides:       tclsh%{TCL_MINOR}
Obsoletes:      itcl < %{itclver}
%endif
# The rings and staging build every flavour unless told otherwise; the test
# suite has no business in the bootstrap ring.
%if %{with test} && 0%{?_with_ringdisabled}
ExclusiveArch:  do_not_build
%endif

%description
Tcl (Tool Command Language) is a very powerful but easy to learn
dynamic programming language, suitable for a very wide range of uses,
including web and desktop applications, networking, administration,
testing and many more. Open source and business-friendly, Tcl is a
mature yet evolving language that is truly cross platform, easily
deployed and highly extensible.

For more information on Tcl see https://www.tcl-lang.org and
https://wiki.tcl-lang.org .

%if %{without test}
%package devel
Summary:        Header Files and C API Documentation for Tcl
Requires:       tcl = %{version}
Provides:       itcl-devel = %{itclver}
Obsoletes:      itcl-devel < %{itclver}

%description devel
This package contains header files and documentation needed for writing
Tcl extensions in compiled languages like C, C++, etc., or for
embedding the Tcl interpreter in programs written in such languages.

This package is not needed for writing extensions or applications in
the Tcl language itself.
%endif

%prep
%autosetup -p0 -n %{origname}%{version}
if ! test -d pkgs/itcl%{itclver}; then
   : New itcl version: pkgs/itcl* . Please update the %%itclver macro acordingly.
   exit 1
fi

# The SQLite extension is provided by the sqlite3 package,
# so don't build it here.
rm -r pkgs/sqlite3.*

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export TCL_PACKAGE_PATH="%{scriptdir}:%{_datadir}/tcl"
export TCL_LIBRARY="%{scriptdir}/tcl%{TCL_MINOR}"
cd unix
autoconf
%configure \
    --enable-man-symlinks \
    --enable-man-compression=gzip \
    --without-tzdata
%make_build \
    PACKAGE_DIR="%{scriptdir}"

%check
%if %{with test}
cd unix
# Some of the regression tests write to $HOME, so better redirect them
mkdir home
export HOME=$PWD/home
# Only arch-specific known failures are left; the 31 ids that used to be
# listed here all pass again on current Tcl and were dropped.
cat > known-failures <<EOF
%ifarch riscv64
binary-40.3
%endif
%if 0%{?qemu_user_space_build}
socket-14.15
thread-16.2
%endif
EOF
%ifnarch s390x
# pipefail so that an aborted or crashed run fails the build: tests/all.tcl
# exits 0 even on failures unless ERROR_ON_FAILURES is set, and without
# pipefail the pipeline below would only ever report tee's status.
set -o pipefail
make test 2>&1 | tee testresults
# known-failures is empty on most arches, and `grep -Fvwf` on an empty
# pattern file exits 1 instead of passing every line through -- which would
# silently tolerate ALL failures. Filter only when there is something to filter.
if test -s known-failures; then
    grep FAILED testresults | grep -Fvwf known-failures && exit 1
else
    grep FAILED testresults && exit 1
fi
%endif
%endif
exit 0

%install
%if %{without test}
make -C unix install install-private-headers \
    INSTALL_ROOT=%{buildroot}
rm -f %{buildroot}%{scriptdir}/tcl%{TCL_MINOR}/ldAix
ln -sf tclsh%{TCL_MINOR} %{buildroot}%{_bindir}/tclsh
ln -sf tclsh.1.gz %{buildroot}%{_mandir}/man1/tclsh%{TCL_MINOR}.1.gz
mkdir -p %{buildroot}%{_datadir}/tcl
install -D -m 0644 %{SOURCE3} %{buildroot}%{_rpmmacrodir}/macros.tcl

# The information in TCL_LIBS is not needed for shared libraries
# and we don't support static linking.
sed -i "/^TCL_LIBS=/s/'.*'$//" %{buildroot}%{_libdir}/tclConfig.sh
sed -i "/^Libs.private: /s/ .*$//" %{buildroot}%{_libdir}/pkgconfig/tcl.pc
%endif

%if %{without test}
%files
%doc README.md changes license.terms ChangeLog*
%docdir %{_mandir}/mann
%doc %{_mandir}/man1/*
%doc %{_mandir}/mann/*
%{_bindir}/*
%{_libdir}/lib*.so
%{_datadir}/tcl
%{scriptdir}
%exclude %{scriptdir}/*/*.a
%exclude %{scriptdir}/*/*Config.sh
%exclude %{scriptdir}/*/tclAppInit.c
%{_rpmmacrodir}/macros.tcl

%files devel
%doc %{_mandir}/man3/*
%{_includedir}/*
%{scriptdir}/*/tclAppInit.c
%attr(0644,root,root) %{_libdir}/*.a
%attr(0644,root,root) %{scriptdir}/*/*.a
%{scriptdir}/*/*Config.sh
%{_libdir}/*Config.sh
%{_libdir}/pkgconfig/*

%endif

%changelog
