#
# spec file for package efivar
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        39
Release:        0
Summary:        Tools to manage UEFI variables
License:        LGPL-2.1-only
URL:            https://github.com/rhboot/efivar
Source:         https://github.com/rhboot/efivar/archive/refs/tags/%{version}.tar.gz#/efivar-%{version}.tar.gz
Patch0:         libefiboot-export-disk_get_partition_info.patch
Patch1:         efivar-filter-gcc-march.patch
Patch2:         efivar-bsc1286645-revert-file-wrapper-removal.patch
Patch3:         efivar-bsc1262696-fix-stack-overflow-in-device-path-parsing.patch
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(popt)
Requires:       libefivar%{major} = %{version}-%{release}

%description
efivar provides a simple command line interface to the UEFI variable facility.

%package -n libefivar%{major}
Summary:        Library to manage UEFI variables

%description -n libefivar%{major}
Library to allow for the simple manipulation of UEFI variables.

%package devel
Summary:        Development headers for libefivar
Requires:       libefivar%{major} = %{version}-%{release}

%description devel
Development headers required to use libefivar.

%prep
%autosetup -p1

# Avoid rebuilding gh#rhboot/efivar#229 and gh#rhboot/efivar#253
mv -v docs/efisecdb.1{.mdoc,}

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
