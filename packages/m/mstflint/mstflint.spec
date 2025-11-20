#
# spec file for package mstflint
#
# Copyright (c) 2025 SUSE LLC
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


%define git_ver -1.60.9ed9e8c3

Name:           mstflint
Version:        4.33.0
Release:        0
Summary:        Mellanox Firmware Burning and Diagnostics Tools
License:        BSD-2-Clause OR GPL-2.0-only
Group:          System/Console
URL:            http://www.openfabrics.org
Obsoletes:      mstflint-devel < %{version}
Source:         mstflint-%{version}%{?git_ver}.tar.gz
Source100:      README.md
Patch1:         Fix-gcc7-and-gcc8.patch
Patch2:         PIE.patch
BuildRequires:  gcc-c++
BuildRequires:  infiniband-diags-devel
BuildRequires:  libibverbs-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libtool
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains a burning tool and diagnostic tools for Mellanox
manufactured HCA/NIC cards. It also provides access to the relevant
source code. Please see the file LICENSE for licensing details.

This package is based on a subset of the Mellanox Firmware Tools (MFT)
package. For a full documentation of the MFT package, please refer to
the downloads page at the Mellanox web site.

%prep
%autosetup -p0 -n %{name}-%{version}%{git_ver}

%build
./autogen.sh
%configure
make %{?_smp_mflags} CFLAGS="%{optflags} -I. -fno-exceptions"

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
rm -rf %{buildroot}%{_includedir}/mstflint
rm -rf  %{buildroot}%{_libdir}/mstflint/*.a
rm -rf  %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_bindir}/hca_self_test.ofed

%files
%defattr(-, root, root)
%doc README
%license LICENSE COPYING
%{_bindir}/mstconfig
%{_bindir}/mstcongestion
%{_bindir}/mstdevices_info
%{_bindir}/mstflint
%{_bindir}/mstfwctrl
%{_bindir}/mstfwreset
%{_bindir}/mstmcra
%{_bindir}/mstmget_temp
%{_bindir}/mstmread
%{_bindir}/mstmtserver
%{_bindir}/mstmwrite
%{_bindir}/mstregdump
%{_bindir}/mstresourcedump
%{_bindir}/mstresourceparse
%{_bindir}/msttokengenerator
%{_bindir}/mstvpd
%{_bindir}/mstfwtrace
%{_mandir}/man1/*.1%{ext_man}
%{_libdir}/mstflint/
%{_datadir}/mstflint/

%changelog
