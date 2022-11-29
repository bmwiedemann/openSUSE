#
# spec file for package libiscsi
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


%define         sover 9
Name:           libiscsi
Version:        1.19.0+git.20221112
Release:        0
Summary:        iSCSI client library and utilities
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/sahlberg/libiscsi
Source:         %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bc
BuildRequires:  libgcrypt-devel
BuildRequires:  librdmacm-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cunit)

%description
libiscsi is a clientside library to implement the iSCSI protocol
that can be used to access resource of an iSCSI target.

%package -n %{name}%{sover}
Summary:        iSCSI client library and utilities
Group:          System/Libraries

%description -n %{name}%{sover}
libiscsi is a clientside library to implement the iSCSI protocol
that can be used to access resource of an iSCSI target.

The library is fully asynchronous with regards to iSCSI commands and
SCSI tasks, but a synchronous layer is also provided for ease of use
for simpler applications.

%package utils
Summary:        Some utilities for %{name}
Group:          Productivity/Networking/Other

%description utils
libiscsi is a clientside library to implement the iSCSI protocol that can
be used to access resource of an iSCSI target.

This package contains utilities based on %{name}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Languages/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
Development files for %{name}

%package test
Summary:        Test utilities for iSCSI
Group:          System/Base

%description test
A comprehensive iSCSI transport and SCSI block device test suite based on
CUnit.

%prep
%autosetup

%build
autoreconf -fiv
%configure \
  --enable-manpages \
  --disable-werror  \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%{_libdir}/libiscsi.so.%{sover}*

%files utils
%license COPYING
%doc LICENCE-* README.md
%{_bindir}/iscsi-inq
%{_bindir}/iscsi-ls
%{_bindir}/iscsi-swp
%{_bindir}/iscsi-perf
%{_bindir}/iscsi-pr
%{_bindir}/iscsi-readcapacity16
%{_mandir}/man1/iscsi-inq.1%{?ext_man}
%{_mandir}/man1/iscsi-ls.1%{?ext_man}
%{_mandir}/man1/iscsi-swp.1%{?ext_man}

%files devel
%{_libdir}/pkgconfig/libiscsi.pc
%{_includedir}/iscsi/
%{_libdir}/libiscsi.so

%files test
%{_bindir}/iscsi-test-cu
%{_mandir}/man1/iscsi-test-cu.1%{?ext_man}

%changelog
