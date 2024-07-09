#
# spec file for package ima-evm-utils
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


%define sover 5
%define libname libimaevm%{sover}
Name:           ima-evm-utils
Version:        1.6
Release:        0
Summary:        IMA/EVM control utility
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND GPL-2.0-or-later WITH Linux-syscall-note
Group:          System/Base
URL:            https://sourceforge.net/projects/linux-ima/
Source0:        https://github.com/mimizohar/ima-evm-utils/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  asciidoc
BuildRequires:  attr
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  e2fsprogs
BuildRequires:  keyutils-devel
BuildRequires:  libattr-devel
BuildRequires:  libtool
BuildRequires:  libxslt-tools
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  tpm2-0-tss-devel
BuildRequires:  util-linux
BuildRequires:  vim

%description
This package provides the control utility for IMA/EVM (Integrity
Measurement Architecture/ Linux Extended Verification Module).

%package devel
Summary:        Development files for the IMA/EVM control utility library
License:        LGPL-2.0-or-later AND GPL-2.0-or-later WITH Linux-syscall-note
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       openssl-devel

%description devel
This package contains the header files and the utilities for %{name}.

%package -n %{libname}
Summary:        IMA/EVM control utility libary
License:        LGPL-2.0-or-later AND GPL-2.0-or-later WITH Linux-syscall-note
Group:          System/Libraries

%description -n %{libname}
This package provides the shared library for IMA/EVM (Integrity
Measurement Architecture/Extended Verification Module).

%package -n evmctl
Summary:        IMA/EVM signing utility
License:        GPL-2.0-or-later AND GPL-2.0-or-later WITH Linux-syscall-note
Group:          System/Kernel
Provides:       ima-evm-utils = %{version}
Obsoletes:      ima-evm-utils < %{version}

%description -n evmctl
The evmctl utility can be used for producing and verifying digital signatures,
which are used by Linux kernel integrity subsystem (IMA/EVM). It can be also
used to import keys into the kernel keyring.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
  --disable-static
make %{?_smp_mflags}

%install
%make_install
# Let do it by ourselves later...
rm -rf %{buildroot}%{_datadir}/doc
find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files devel
%doc examples/*
%{_includedir}/*
%{_libdir}/libimaevm.so

%files -n %{libname}
%doc README NEWS AUTHORS
%license LICENSES.txt
%{_libdir}/libimaevm.so.%{sover}*

%files -n evmctl
%{_bindir}/evmctl
%{_mandir}/man1/evmctl.1%{ext_man}

%changelog
