#
# spec file for package qatzip
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


Name:           qatzip
Version:        1.1.0
Release:        0
Summary:        Intel QuickAssist Technology (QAT) QATzip Library
License:        BSD-3-Clause
Group:          Hardware/Other
URL:            https://github.com/intel/QATzip
Source:         https://github.com/intel/QATzip/archive/refs/tags/v%{version}.tar.gz
Patch0:         qatzip-fortify_source=3.patch
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  liblz4-devel
BuildRequires:  libtool
BuildRequires:  qatlib-devel >= 22.07.0
BuildRequires:  zlib-devel >= 1.2.7
# This package can be built on all archs, but is useful only on enterprise-class intel.
ExclusiveArch:  x86_64

%description
QATzip is a user space library which builds on top of the Intel
QuickAssist Technology user space library, to provide extended
accelerated compression and decompression services by offloading the
actual compression and decompression request(s) to the Intel Chipset
Series. QATzip produces data using the standard gzip* format
(RFC1952) with extended headers. The data can be decompressed with a
compliant gzip* implementation. QATzip is designed to take full
advantage of the performance provided by Intel QuickAssist
Technology.

%package -n libqatzip3
Summary:        Libraries for the qatzip package
Group:          Hardware/Other

%description -n libqatzip3
This package contains libraries for applications to use
the QATzip APIs.

%package devel
Summary:        Development components for the libqatzip package
Group:          Hardware/Other
Requires:       libqatzip3%{?_isa} = %{version}-%{release}

%description devel
This package contains headers and libraries required to build
applications that use the QATzip APIs.

%prep
%autosetup -n QATzip-%{version}

%build
autoreconf -fiv
%configure --enable-symbol
%make_build

%install
%make_install
rm -vf %{buildroot}%{_mandir}/*.pdf
rm -vf %{buildroot}%{_libdir}/*.{la,a}

%post -n libqatzip3 -p /sbin/ldconfig
%postun -n libqatzip3 -p /sbin/ldconfig

%files
%license LICENSE*
%{_mandir}/man1/qzip.1%{?ext_man}
%{_bindir}/qzip

%files -n libqatzip3
%license LICENSE*
%{_libdir}/libqatzip.so.3*

%files devel
%doc docs/QATzip-man.pdf
%{_includedir}/qatzip.h
%{_libdir}/libqatzip.so

%changelog
