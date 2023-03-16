#
# spec file for package efivar
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


%define major 1
Name:           efivar
Version:        38
Release:        0
Summary:        Tools to manage UEFI variables
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/rhinstaller/efivar
Source:         https://github.com/rhinstaller/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
Patch0:         libefiboot-export-disk_get_partition_info.patch
Patch1:         efivar-bsc1202209-fix-glibc-2.36-build.patch
Patch2:         efivar-adjust-dependency.patch
Patch3:         efivar-filter-gcc-march.patch
Patch4:         efivar-bsc1206388-revamp-efi_well_known-variable-handling.patch
BuildRequires:  fdupes
BuildRequires:  mandoc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(popt)
Requires:       libefivar%{major} = %{version}-%{release}

%description
efivar provides a simple command line interface to the UEFI variable facility.

%package -n libefivar%{major}
Summary:        Library to manage UEFI variables
Group:          System/Libraries

%description -n libefivar%{major}
Library to allow for the simple manipulation of UEFI variables.

%package devel
Summary:        Development headers for libefivar
Group:          Development/Libraries/C and C++
Requires:       libefivar%{major} = %{version}-%{release}

%description devel
Development headers required to use libefivar.

%prep
%autosetup -p1

%build
CFLAGS="%{optflags} -Wno-nonnull -flto"
%ifarch ia64
  CFLAGS="${CFLAGS//-fstack-protector/}"
%endif
export CFLAGS
export LDFLAGS="-flto-partition=one"

%make_build

%install
%make_install \
  libdir=%{_libdir} \
  bindir=%{_bindir}

%fdupes -s %{buildroot}

# fail on undercover ABI changes
file %{buildroot}/%{_libdir}/lib%{name}.so.%{major}*

%ldconfig_scriptlets -n libefivar%{major}

%files
%license COPYING
%{_bindir}/efivar
%{_bindir}/efisecdb
%{_mandir}/man1/*

%files devel
%{_mandir}/man3/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n libefivar%{major}
%{_libdir}/*.so.*

%changelog
