#
# spec file for package tcl
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


Name:           tcl
URL:            http://www.tcl.tk
Version:        8.6.10
Release:        0
%define         rrc %{nil}
%define TCL_MINOR %(echo %version | cut -c1-3)
%define itclver 4.2.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        The Tcl Programming Language
License:        TCL
Group:          Development/Languages/Tcl
Provides:       itcl = %itclver
Provides:       tclsh
Provides:       tclsh%{TCL_MINOR}
Obsoletes:      itcl < %itclver
# bug437293
%ifarch ppc64
Obsoletes:      tcl-64bit
%endif
#
PreReq:         /bin/rm
Source0:        ftp://ftp.tcl.tk/pub/tcl/tcl8_6/%{name}%{version}%{rrc}-src.tar.gz
Source1:        tcl-rpmlintrc
Source2:        baselibs.conf
Source3:        macros.tcl
BuildRequires:  autoconf
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
# Required for test suite:
BuildRequires:  timezone

%description
Tcl (Tool Command Language) is a very powerful but easy to learn
dynamic programming language, suitable for a very wide range of uses,
including web and desktop applications, networking, administration,
testing and many more. Open source and business-friendly, Tcl is a
mature yet evolving language that is truly cross platform, easily
deployed and highly extensible.

For more information on Tcl see http://www.tcl.tk and
http://wiki.tcl.tk .

%package devel
Summary:        Header Files and C API Documentation for Tcl
Group:          Development/Libraries/Tcl
Requires:       tcl = %version
# bug437293
%ifarch ppc64
Obsoletes:      tcl-devel-64bit
%endif
Obsoletes:      itcl-devel < %itclver
Provides:       itcl-devel = %itclver
#

%description devel
This package contains header files and documentation needed for writing
Tcl extensions in compiled languages like C, C++, etc., or for
embedding the Tcl interpreter in programs written in such languages.

This package is not needed for writing extensions or applications in
the Tcl language itself.

%prep
%setup -q -n %name%version

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
cd unix
autoconf
%configure \
	--enable-man-symlinks \
	--enable-man-compression=gzip \
	--without-tzdata
%define scriptdir %_libdir/tcl
make %{?_smp_mflags} \
        PACKAGE_DIR=%_libdir/tcl \
	TCL_LIBRARY="%scriptdir/tcl%TCL_MINOR" \
	TCL_PACKAGE_PATH="%_libdir/tcl %_datadir/tcl"

%check
cd unix
# Some of the regressioin tests write to $HOME, so better redirect them
mkdir home
export HOME=$PWD/home
# Run the testsuite to gather some data for the profile-based
# optimisation and let rpmbuild fail on unexpected test failures.
cat > known-failures <<EOF
async-4.2
async-4.3
chan-17.4
chan-io-53.9
clock-33.5a
clock-33.8
clock-33.8a
event-7.5
event-11.4
event-12.4
exec-19.1
http-3.25
interp-34.9
interp-34.13
interp-36.7
io-53.9
msgcat-14.2
socket_inet6-2.13
timer-1.1
timer-2.1
timer-3.2
timer-6.4
timer-6.5
thread-7.24
thread-7.25
thread-7.28
thread-7.29
thread-7.30
thread-7.31
thread-20.9
thread-21.16
%ifarch riscv64
binary-40.3
%endif
EOF
%ifnarch s390 s390x
make test 2>&1 | tee testresults
grep FAILED testresults | grep -Fvwf known-failures && exit 1
%endif
exit 0

%install
make -C unix install install-private-headers \
	INSTALL_ROOT=%buildroot \
	TCL_LIBRARY="%scriptdir/tcl%TCL_MINOR" 
rm -f %buildroot%scriptdir/tcl%TCL_MINOR/ldAix
ln -sf tclsh%TCL_MINOR %buildroot%_prefix/bin/tclsh
mkdir -p %buildroot%_datadir/tcl
install -D %{S:3} -m 644 %buildroot/etc/rpm/macros.tcl

%if "%_lib" == "lib64"
%post
test -L /usr/lib/tcl%TCL_MINOR && /bin/rm -f /usr/lib/tcl%TCL_MINOR
exit 0
%endif

%files
%defattr(-,root,root,755)
%doc README.md changes license.terms ChangeLog*
%docdir %_mandir/mann
%doc %_mandir/man1/*
%doc %_mandir/mann/*
%_prefix/bin/*
%_libdir/lib*.so
%_datadir/tcl
%scriptdir
%exclude %scriptdir/*/*.a
%exclude %scriptdir/*/*Config.sh
%exclude %scriptdir/*/tclAppInit.c
%config /etc/rpm/macros.tcl

%files devel
%defattr(-,root,root)
%doc %_mandir/man3/*
%_includedir/*
%scriptdir/*/tclAppInit.c
%attr(0644,root,root) %_libdir/*.a
%attr(0644,root,root) %scriptdir/*/*.a
%scriptdir/*/*Config.sh
%_libdir/*Config.sh
%_libdir/pkgconfig/*

%changelog
