#
# spec file for package libsemanage
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


Name:           libsemanage
Version:        2.9
Release:        0
Summary:        SELinux policy management library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Url:            https://github.com/SELinuxProject/selinux/wiki/Releases
Source:         https://github.com/SELinuxProject/selinux/releases/download/20190315/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Source2:        semanage.conf
Patch0:         suse_path.patch
BuildRequires:  audit-devel
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  libbz2-devel
BuildRequires:  libselinux-devel
BuildRequires:  libsepol-devel
BuildRequires:  libustr-devel
BuildRequires:  pkg-config

%description
libsemanage is the policy management library. Using libsepol and
libselinux to interact with the SELinux system, it also calls helper
programs for loading policy and for checking whether the
file_contexts configuration is valid.

%package -n libsemanage1
Summary:        SELinux policy management library
Group:          System/Libraries
Suggests:       %{name}-migrate-store

%description -n libsemanage1
libsemanage is the policy management library. Using libsepol and
libselinux to interact with the SELinux system, it also calls helper
programs for loading policy and for checking whether the
file_contexts configuration is valid.

(Security-enhanced Linux is a feature of the kernel and some
utilities that implement mandatory access control policies, such as
Type Enforcement, Role-based Access Control and Multi-Level
Security.)

%package devel
Summary:        Header files and libraries for SELinux's policy management libary
Group:          Development/Libraries/C and C++
Requires:       libsemanage1 = %{version}
Requires:       libustr-devel

%description devel
The libsemanage-devel package contains the libraries and header files
needed for developing applications that manipulate SELinux policies.

%package devel-static
Summary:        Static archives for SELinux's policy management library
Group:          Development/Libraries/C and C++
Requires:       libsemanage-devel

%description devel-static
The libsemanage-devel-static package contains the static libraries
needed for developing applications that manipulate binary policies.

%package migrate-store
Summary:        SELinux Policy Store Migration
Group:          Productivity/Security

%description migrate-store
In version 2.4 of libsemanage, libsepol, and policycoreutils, the policy
module store was moved from /etc/selinux/<store>/modules/ to
/var/lib/selinux/<store>/. Once the libraries are upgraded, all policy
stores must be migrated before any commands that modify or use the store
(e.g. semodule, semanage) can be executed.

%prep
%setup -q
%patch0

%build
%define _lto_cflags %{nil}
make %{?_smp_mflags} clean
make -j1 CFLAGS="%{optflags}" CC="gcc"
make -j1 CFLAGS="%{optflags}" LIBDIR="%{_libdir}" LIBEXECDIR="%{_libexecdir}" SHLIBDIR="%{_lib}" CC="gcc" all

%install
mkdir -p %{buildroot}/%{_lib}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
%make_install LIBDIR="%{_libdir}" LIBEXECDIR="%{_libexecdir}" SHLIBDIR="%{_libdir}"
ln -sf  %{_libdir}/libsemanage.so.1 %{buildroot}/%{_libdir}/libsemanage.so
cp %{SOURCE2} %{buildroot}%{_sysconfdir}/selinux/semanage.conf
# Remove duplicate files
%fdupes -s %{buildroot}%{_mandir}

%post -n libsemanage1 -p /sbin/ldconfig
%postun -n libsemanage1 -p /sbin/ldconfig

%files -n libsemanage1
%dir %{_sysconfdir}/selinux
%config(noreplace) %{_sysconfdir}/selinux/semanage.conf
%{_libdir}/libsemanage.so.*

%files devel
%{_libdir}/libsemanage.so
%{_libdir}/pkgconfig/libsemanage.pc
%{_includedir}/semanage/
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/ru/man5/*

%files migrate-store
%dir %{_libexecdir}/selinux
%{_libexecdir}/selinux/

%files devel-static
%{_libdir}/libsemanage.a

%changelog
