#
# spec file for package libsemanage
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


%define soversion 2
%define libname libsemanage%{soversion}

Name:           libsemanage
Version:        3.6
Release:        0
Summary:        SELinux policy management library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/SELinuxProject/selinux/wiki/Releases
Source0:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        libsemanage.keyring
Source3:        baselibs.conf
Source4:        semanage.conf
# PATCH-FIX-UPSTREAM bsc#1133102 LTO: Update map file to include new symbols and remove wildcards
# For now we need to disable this. This breaks e.g. shadow and also other packages in security:SELinux
#Patch0:         libsemanage-update-map-file.patch
BuildRequires:  audit-devel
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  libbz2-devel
BuildRequires:  libselinux-devel
BuildRequires:  libsepol-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros

%description
libsemanage is the policy management library. Using libsepol and
libselinux to interact with the SELinux system, it also calls helper
programs for loading policy and for checking whether the
file_contexts configuration is valid.

%package -n %{libname}
Summary:        SELinux policy management library
Group:          System/Libraries
Suggests:       %{name}-migrate-store
Requires:       %{name}-conf >= %{version}

%description -n %{libname}
libsemanage is the policy management library. Using libsepol and
libselinux to interact with the SELinux system, it also calls helper
programs for loading policy and for checking whether the
file_contexts configuration is valid.

(Security-enhanced Linux is a feature of the kernel and some
utilities that implement mandatory access control policies, such as
Type Enforcement, Role-based Access Control and Multi-Level
Security.)

%package conf
Summary:        Configuration for the SELinux policy management library
# before 3.1 the config file wasn't separated, so no parallel install is possible
Group:          System/Libraries
Conflicts:      %{name}1 <= 3.1

%description conf
Configuration file for libsemanage. Moved to a separate package to allow
parallel installation

%package devel
Summary:        Header files and libraries for SELinux's policy management libary
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

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
# Replace /usr/libexec with whatever the distro defines as libexecdir - across all files
grep /usr/libexec . -rl | xargs sed -i "s|/usr/libexec|%{_libexecdir}|g"

%build
%make_build clean
%make_build CFLAGS="%{optflags} -fno-semantic-interposition -ffat-lto-objects" CC="gcc"
%make_build CFLAGS="%{optflags} -fno-semantic-interposition -ffat-lto-objects" LIBDIR="%{_libdir}" LIBEXECDIR="%{_libexecdir}" SHLIBDIR="%{_lib}" CC="gcc" all

%install
mkdir -p %{buildroot}/%{_lib}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_localstatedir}/lib/selinux
%make_install LIBDIR="%{_libdir}" LIBEXECDIR="%{_libexecdir}" SHLIBDIR="%{_libdir}"
ln -sf  %{_libdir}/libsemanage.so.%{soversion} %{buildroot}/%{_libdir}/libsemanage.so
cp %{SOURCE4} %{buildroot}%{_sysconfdir}/selinux/semanage.conf

# Fix shebang in scripts
for f in %{buildroot}%{_libexecdir}/selinux/*
do
  [ -f $f ] && sed -i "1s@#!.*python.*@#!$(realpath %__python3)@" $f
done
# Remove duplicate files
%fdupes -s %{buildroot}%{_mandir}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/libsemanage.so.*
%dir %{_localstatedir}/lib/selinux

%files conf
%dir %{_sysconfdir}/selinux
%config(noreplace) %{_sysconfdir}/selinux/semanage.conf

%files devel
%{_libdir}/libsemanage.so
%{_libdir}/pkgconfig/libsemanage.pc
%{_includedir}/semanage/
%{_mandir}/man3/*
%{_mandir}/man5/*

%files migrate-store
%dir %{_libexecdir}/selinux
%{_libexecdir}/selinux/

%files devel-static
%{_libdir}/libsemanage.a

%changelog
