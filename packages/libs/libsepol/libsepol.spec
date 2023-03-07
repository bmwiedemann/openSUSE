#
# spec file for package libsepol
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


%define libname libsepol2

Name:           libsepol
Version:        3.5
Release:        0
Summary:        SELinux binary policy manipulation library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/SELinuxProject/selinux/wiki/Releases
Source0:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        libsepol.keyring
Source3:        baselibs.conf
BuildRequires:  flex
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libsepol provides an API for the manipulation of SELinux binary
policies. It is used by checkpolicy (the policy compiler) and similar
tools, as well as by programs like load_policy that need to perform
specific transformations on binary policies such as customizing
policy boolean settings.

%package utils
Summary:        SELinux binary policy manipulation tools
Group:          System/Base

%description utils
libsepol provides an API for the manipulation of SELinux binary
policies. It is used by checkpolicy (the policy compiler) and similar
tools, as well as by programs like load_policy that need to perform
specific transformations on binary policies such as customizing
policy boolean settings.

%package -n %{libname}
Summary:        SELinux binary policy manipulation library
Group:          System/Libraries

%description -n %{libname}
libsepol provides an API for the manipulation of SELinux binary
policies. It is used by checkpolicy (the policy compiler) and similar
tools, as well as by programs like load_policy that need to perform
specific transformations on binary policies such as customizing
policy boolean settings.

(Security-enhanced Linux is a feature of the kernel and some
utilities that implement mandatory access control policies, such as
Type Enforcement, Role-based Access Control and Multi-Level
Security.)

%package devel
Summary:        Development files for SELinux's binary policy manipulation library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       glibc-devel

%description devel
The libsepol-devel package contains the libraries and header files
needed for developing applications that manipulate binary SELinux
policies.

%package devel-static
Summary:        Static archives for SELinux's binary policy manipulation library
Group:          Development/Libraries/C and C++
Requires:       libsepol-devel = %{version}

%description devel-static
The libsepol-devel-static package contains the static libraries
needed for developing applications that manipulate binary SELinux
policies.

%prep
%setup -q

%build
%define _lto_cflags %{nil}
export CFLAGS="%{optflags} -fcommon"
make %{?_smp_mflags}

%install
%make_install LIBDIR="%{_libdir}" SHLIBDIR="%{_libdir}"

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files utils
%defattr(-,root,root)
%{_bindir}/chkcon
%{_bindir}/sepol_check_access
%{_bindir}/sepol_compute_av
%{_bindir}/sepol_compute_member
%{_bindir}/sepol_compute_relabel
%{_bindir}/sepol_validate_transition
%{_mandir}/man8/*.8%{ext_man}
%{_mandir}/ru/man8/*.8%{ext_man}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libsepol.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libsepol.so
%{_mandir}/man3/*.3%{ext_man}
%{_includedir}/sepol/
%{_libdir}/pkgconfig/libsepol.pc

%files devel-static
%defattr(-,root,root)
%{_libdir}/libsepol.a

%changelog
