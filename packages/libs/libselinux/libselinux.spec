#
# spec file for package libselinux
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


%define libsepol_ver 3.1
Name:           libselinux
Version:        3.1
Release:        0
Summary:        SELinux runtime library and utilities
License:        SUSE-Public-Domain
Group:          Development/Libraries/C and C++
URL:            https://github.com/SELinuxProject/selinux/wiki/Releases
Source:         https://github.com/SELinuxProject/selinux/releases/download/20200710/%{name}-%{version}.tar.gz
Source1:        selinux-ready
Source2:        baselibs.conf
# PATCH-FIX-UPSTREAM Include <sys/uio.h> for readv prototype
Patch4:         readv-proto.patch
Patch5:         skip_cycles.patch
BuildRequires:  fdupes
BuildRequires:  libsepol-devel >= %{libsepol_ver}
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig

%description
libselinux provides an interface to get and set process and file
security contexts and to obtain security policy decisions.

%package -n libselinux1
Summary:        SELinux runtime library
Group:          System/Libraries

%description -n libselinux1
libselinux provides an interface to get and set process and file
security contexts and to obtain security policy decisions.

(Security-enhanced Linux is a feature of the kernel and some
utilities that implement mandatory access control policies, such as
Type Enforcement, Role-based Access Control and Multi-Level
Security.)

%package -n selinux-tools
Summary:        SELinux command-line utilities
Group:          System/Base

%description -n selinux-tools
Security-enhanced Linux is a feature of the kernel and some
utilities that implement mandatory access control policies, such as
Type Enforcement, Role-based Access Control and Multi-Level
Security.

This subpackage contains utilities to inspect and administer the
system's SELinux state.

%package devel
Summary:        Development files for the SELinux runtime library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libselinux1 = %{version}
#Automatic dependency on libsepol-devel via pkgconfig

%description devel
libselinux provides an interface to get and set process and file
security contexts and to obtain security policy decisions.

This package contains the development files, which are
necessary to develop your own software using libselinux.

%package devel-static
Summary:        Static archives for the SELinux runtime
Group:          Development/Libraries/C and C++
Requires:       libselinux-devel = %{version}
Requires:       pkgconfig(libpcre)
Requires:       pkgconfig(libsepol)

%description devel-static
libselinux provides an interface to get and set process and file
security contexts and to obtain security policy decisions.

This package contains the static development files, which are
necessary to develop your own software using libselinux.

%prep
%setup -q
%patch4 -p1
%patch5 -p1

%build
%define _lto_cflags %{nil}
make %{?_smp_mflags} LIBDIR="%{_libdir}" CC="gcc" CFLAGS="%{optflags} -fno-semantic-interposition"

%install
mkdir -p %{buildroot}/%{_lib}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_sbindir}
make DESTDIR=%{buildroot} LIBDIR="%{_libdir}" SHLIBDIR="/%{_lib}" BINDIR="%{_sbindir}" install
mv %{buildroot}%{_sbindir}/getdefaultcon %{buildroot}%{_sbindir}/selinuxdefcon
mv %{buildroot}%{_sbindir}/getconlist %{buildroot}%{_sbindir}/selinuxconlist
install -m 0755 %{SOURCE1} %{buildroot}%{_sbindir}/selinux-ready
# Remove duplicate files
%fdupes -s %{buildroot}%{_mandir}

%post -n libselinux1 -p /sbin/ldconfig
%postun -n libselinux1 -p /sbin/ldconfig

%files -n selinux-tools
%{_sbindir}/avcstat
%{_sbindir}/getenforce
%{_sbindir}/getsebool
%{_sbindir}/matchpathcon
%{_sbindir}/selabel_digest
%{_sbindir}/selabel_lookup
%{_sbindir}/selinux_check_access
%{_sbindir}/selabel_lookup_best_match
%{_sbindir}/selabel_partial_match
%{_sbindir}/selinuxconlist
%{_sbindir}/selinuxdefcon
%{_sbindir}/selinuxenabled
%{_sbindir}/setenforce
%{_sbindir}/togglesebool
%{_sbindir}/selinux-ready
%{_sbindir}/selinuxexeccon
%{_sbindir}/sefcontext_compile
%{_sbindir}/compute_*
%{_sbindir}/getfilecon
%{_sbindir}/getpidcon
%{_sbindir}/policyvers
%{_sbindir}/setfilecon
%{_sbindir}/getseuser
%{_sbindir}/selinux_check_securetty_context
%{_sbindir}/selabel_get_digests_all_partial_matches
%{_sbindir}/validatetrans
%{_mandir}/man5/*
%{_mandir}/ru/man5/*
%{_mandir}/man8/*
%{_mandir}/ru/man8/*

%files -n libselinux1
/%{_lib}/libselinux.so.*

%files devel
%{_libdir}/libselinux.so
%{_includedir}/selinux/
%{_mandir}/man3/*
%{_libdir}/pkgconfig/libselinux.pc

%files devel-static
%{_libdir}/libselinux.a

%changelog
