#
# spec file for package libtool-testsuite
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


#####################################################################
#                                                                   #
#   NOTE: PLEASE RUN pre_checkin.sh BEFORE SUBMITTING THE PACKAGE   #
#                                                                   #
#####################################################################
Name:           libtool-testsuite
Version:        2.4.6
Release:        0
Summary:        A Tool to Build Shared Libraries
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND GFDL-1.2-or-later
Group:          Development/Tools/Building
Url:            http://www.gnu.org/software/libtool/
Source0:        http://ftp.gnu.org/gnu/libtool/libtool-%{version}.tar.xz
Source1:        http://ftp.gnu.org/gnu/libtool/libtool-%{version}.tar.xz.sig
Source2:        libtool.keyring
Source3:        baselibs.conf
Source4:        libtool-rpmlintrc
# PATCH-FIX-OPENSUSE -- do not add build host name boo#1084909
Patch0:         libtool-reproducible-hostname.patch
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  gcc-objc
BuildRequires:  help2man
BuildRequires:  lzma
BuildRequires:  makeinfo
BuildRequires:  zlib-devel
Requires:       automake > 1.4
Requires:       libltdl7 = %{version}
Requires:       m4 >= 1.4.16
Requires:       tar
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
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
%setup -q -n libtool-%{version}
%patch0 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
./configure CFLAGS="%{optflags}" \
   --prefix=%{_prefix} --infodir=%{_infodir} --libdir=%{_libdir}
# force rebuild with non-broken makeinfo
rm -f doc/libtool.info
make V=1 %{?_smp_mflags}

%if "%{name}" == "libtool-testsuite"
%check
trap 'test $? -ne 0 && cat tests/testsuite.log' EXIT
# Avoid spurious testsuite failures due to messages from icecream
PATH=%{_prefix}/bin:$PATH
make %{?_smp_mflags} check

%install
%else
%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
chmod +x %{buildroot}%{_datadir}/libtool/build-aux/ltmain.sh
# Do not add builder's hostname into generated scripts
sed -i "/uname -n/d" %{buildroot}%{_datadir}/aclocal/libtool.m4
%endif

%post
%install_info --info-dir=%{_infodir} %{_infodir}/libtool.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/libtool.info-1.gz
%install_info --info-dir=%{_infodir} %{_infodir}/libtool.info-2.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/libtool.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/libtool.info-1.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/libtool.info-2.gz

%post -n libltdl7 -p /sbin/ldconfig

%postun -n libltdl7 -p /sbin/ldconfig

%if "%{name}" == "libtool"
%files
%defattr(-, root, root)
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
%{_infodir}/libtool.info*
%{_mandir}/man1/libtool.1.gz
%{_mandir}/man1/libtoolize.1.gz
%{_datadir}/libtool

%files -n libltdl7
%defattr(-, root, root)
%{_libdir}/libltdl.so.*
%endif

%changelog
