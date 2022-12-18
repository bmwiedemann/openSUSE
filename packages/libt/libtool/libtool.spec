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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "testsuite"
%define psuffix -testsuite
%else
%define psuffix %{nil}
%endif
Name:           libtool%{psuffix}
Version:        2.4.7
Release:        0
Summary:        A Tool to Build Shared Libraries
License:        GFDL-1.2-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Tools/Building
URL:            https://www.gnu.org/software/libtool/
Source0:        https://ftp.gnu.org/gnu/libtool/libtool-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/libtool/libtool-%{version}.tar.xz.sig
Source2:        libtool.keyring
Source3:        baselibs.conf
Source4:        libtool-rpmlintrc
# PATCH-FIX-OPENSUSE -- do not add build host name boo#1084909
Patch0:         libtool-reproducible-hostname.patch
# PATCH-FIX-OPENSUSE: workaround irrelevant compiler warning
Patch1:         handle-Werror-return-type.patch
# PATCH-FIX-OPENSUSE -- fix tests with GNU grep 3.8 boo#1203097
Patch2:         libtool-2.4.7-grep-3.8.patch
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  gcc-objc
BuildRequires:  help2man
BuildRequires:  lzma
BuildRequires:  makeinfo
BuildRequires:  pkgconfig(zlib)
Requires:       automake > 1.4
Requires:       libltdl7 = %{version}
Requires:       m4 >= 1.4.16
Requires:       tar
Provides:       libltdl-devel
# fedora name
Provides:       libtool-ltdl-devel

%description
GNU libtool is a set of shell scripts to automatically configure UNIX
architectures to build shared libraries in a generic fashion.

%package -n libltdl7
Summary:        Libtool Runtime Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++

%description -n libltdl7
Library needed by programs that use the ltdl interface of GNU libtool.

%prep
%autosetup -p1 -n libtool-%{version}

%build
%define _lto_cflags %{nil}
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure
rm -f doc/libtool.info
%make_build

%if "%{flavor}" == "testsuite"
%check
trap 'test $? -ne 0 && cat tests/testsuite.log' EXIT
%make_build check

%install
%else

%install
%make_install
chmod +x %{buildroot}%{_datadir}/libtool/build-aux/ltmain.sh
# Do not add builder's hostname into generated scripts
sed -i "/uname -n/d" %{buildroot}%{_datadir}/aclocal/libtool.m4
%endif

%post -n libltdl7 -p /sbin/ldconfig
%postun -n libltdl7 -p /sbin/ldconfig

%if "%{name}" == "libtool"
%files
%license COPYING
%doc AUTHORS NEWS README THANKS ChangeLog
%{_bindir}/libtool
%{_bindir}/libtoolize
%{_includedir}/libltdl
%{_includedir}/ltdl.h
%{_libdir}/libltdl.a
%attr(644, root, root) %{_libdir}/libltdl.la
%{_libdir}/libltdl.so
%{_datadir}/aclocal/*.m4
%{_infodir}/libtool.info%{?ext_info}
%{_infodir}/libtool.info-1%{?ext_info}
%{_infodir}/libtool.info-2%{?ext_info}
%{_mandir}/man1/libtool.1%{?ext_man}
%{_mandir}/man1/libtoolize.1%{?ext_man}
%{_datadir}/libtool

%files -n libltdl7
%{_libdir}/libltdl.so.7*
%endif

%changelog
