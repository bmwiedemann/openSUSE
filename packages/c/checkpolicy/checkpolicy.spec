#
# spec file for package checkpolicy
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
Name:           checkpolicy
Version:        3.1
Release:        0
Summary:        SELinux policy compiler
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            https://github.com/SELinuxProject/selinux
Source0:        https://github.com/SELinuxProject/selinux/releases/download/20200710/%{name}-%{version}.tar.gz
Source1:        checkpolicy-tests.tar.gz
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libselinux-devel
BuildRequires:  libsepol-devel-static => %{libsepol_ver}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
checkpolicy is the SELinux policy compiler. It uses libsepol to
generate the binary policy.

(Security-enhanced Linux is a feature of the kernel and some
utilities that implement mandatory access control policies, such as
Type Enforcement, Role-based Access Control and Multi-Level
Security.)

%package devel
Summary:        Development files for SELinux policy compiler
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
checkpolicy is the SELinux policy compiler. It uses libsepol to
generate the binary policy.

This package contains the development files, which are
necessary to develop your own software using checkpolicy.

%package -n python3-%{name}
Summary:        Python bindings for SELinux policy compiler
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}

%description -n python3-%{name}
checkpolicy is the SELinux policy compiler. It uses libsepol to
generate the binary policy.

This package contains the Python bindindgs, which are necessary
to use checkpolicy from Python.

%prep
%setup -q

%build
make clean
make LIBDIR="%{_libdir}" CFLAGS="%{optflags}" %{?_smp_mflags}
make -C test LIBDIR="%{_libdir}" CFLAGS="%{optflags}" %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_bindir}
%make_install LIBDIR="%{_libdir}"
install test/dismod %{buildroot}/%{_bindir}/sedismod
install test/dispol %{buildroot}/%{_bindir}/sedispol

%files
%defattr(-,root,root)
%{_bindir}/checkpolicy
%{_bindir}/checkmodule
%{_bindir}/sedismod
%{_bindir}/sedispol
%{_mandir}/man8/check*.*%{ext_man}
%{_mandir}/ru/man8/check*.*%{ext_man}

%changelog
