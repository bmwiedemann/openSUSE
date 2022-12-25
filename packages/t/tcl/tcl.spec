#
# spec file for package tcl
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


%if 0%{!?_rpmmacrodir:1}
%define _rpmmacrodir %{_rpmconfigdir}/macros.d
%endif

Name:           tcl
URL:            http://www.tcl.tk
Version:        8.6.13
Release:        0
%define         rrc %{nil}
%define TCL_MINOR %(echo %version | cut -c1-3)
%define itclver 4.2.3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        The Tcl Programming Language
License:        TCL
Group:          Development/Languages/Tcl
Provides:       itcl = %itclver
Provides:       tclsh
Provides:       tclsh%{TCL_MINOR}
Obsoletes:      itcl < %itclver
# Require the extension from the SQLite package instead of shipping
# the embedded copy, which might be outdated.
Requires:       sqlite3-tcl
# bug437293
%ifarch ppc64
Obsoletes:      tcl-64bit
%endif
#
PreReq:         /bin/rm
Source0:        http://prdownloads.sourceforge.net/tcl/%{name}%{version}%{rrc}-src.tar.gz
Source1:        tcl-rpmlintrc
Source2:        baselibs.conf
Source3:        macros.tcl
Patch0:         tcl-refchan-mode-needed.patch
Patch1:         tcl-string-compare.patch
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
if ! test -d pkgs/itcl%itclver; then
   : Version mismatch in itcl, please chek the %%itclver macro!
   exit 1
fi
%patch0
%patch1

# The SQLite extension is provided by the sqlite3 package,
# so don't build it here.
rm -r pkgs/sqlite3.*

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%define scriptdir %_libdir/tcl
export TCL_PACKAGE_PATH="%scriptdir %_datadir/tcl"
export TCL_LIBRARY="%scriptdir/tcl%TCL_MINOR"
cd unix
autoconf
%configure \
	--enable-man-symlinks \
	--enable-man-compression=gzip \
	--without-tzdata
make %{?_smp_mflags} \
	PACKAGE_DIR="%scriptdir"

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
%if 0%{?qemu_user_space_build}
socket-14.15
thread-16.2
%endif
EOF
%ifnarch s390 s390x
make test 2>&1 | tee testresults
grep FAILED testresults | grep -Fvwf known-failures && exit 1
%endif
exit 0

%install
make -C unix install install-private-headers \
	INSTALL_ROOT=%buildroot
rm -f %buildroot%scriptdir/tcl%TCL_MINOR/ldAix
ln -sf tclsh%TCL_MINOR %buildroot%_prefix/bin/tclsh
ln -sf tclsh.1.gz %buildroot%_mandir/man1/tclsh%TCL_MINOR.1.gz
mkdir -p %buildroot%_datadir/tcl
install -D %{S:3} -m 644 %buildroot%_rpmmacrodir/macros.tcl

# The information in TCL_LIBS is not needed for shared libraries
# and we don't support static linking.
sed -i "/^TCL_LIBS=/s/'.*'$//" %buildroot%_libdir/tclConfig.sh
sed -i "/^Libs.private: /s/ .*$//" %buildroot%_libdir/pkgconfig/tcl.pc

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
%_rpmmacrodir/macros.tcl

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
