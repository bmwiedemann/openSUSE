#
# spec file for package openpace
#
# Copyright (c) 2024, Martin Hauke <mardnh@gmx.de>
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


%define sover 3
%define libname libeac%{sover}
Name:           openpace
Version:        1.1.3
Release:        0
Summary:        Cryptographic library for EAC version 2
License:        GPL-3.0-or-later
Group:          System/Libraries
#Git-Clone:     https://github.com/frankmorgner/openpace.git
URL:            https://frankmorgner.github.io/openpace/
Source:         https://github.com/frankmorgner/openpace/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gengetopt
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcrypto) >= 1.0.2

%description
OpenPACE implements Extended Access Control (EAC) version 2 as specified
in BSI TR-03110. OpenPACE comprises support for the following protocols:

 * Password Authenticated Connection Establishment (PACE)
 * Terminal Authentication (TA)
 * Chip Authentication (CA)

OpenPACE also supports Card Verifiable Certificates (CV Certificates)
and signing requests as well as easy to use wrappers for using the
established secure channels.

OpenPACE supports all variants of PACE (DH/ECDH, GM/IM), TA
(RSASSA-PKCS1-v1_5/RSASSA-PSS/ECDSA), CA (DH/ECDH) and all
standardised domain parameters (GFP/ECP).

%package -n %{libname}
Summary:        Cryptographic library for EAC version 2
Group:          System/Libraries

%description -n %{libname}
OpenPACE implements Extended Access Control (EAC) version 2 as specified
in BSI TR-03110. OpenPACE comprises support for the following protocols:
 
 * Password Authenticated Connection Establishment (PACE)
 * Terminal Authentication (TA)
 * Chip Authentication (CA)
 
OpenPACE also supports Card Verifiable Certificates (CV Certificates)
and signing requests as well as easy to use wrappers for using the
established secure channels.
 
OpenPACE supports all variants of PACE (DH/ECDH, GM/IM), TA
(RSASSA-PKCS1-v1_5/RSASSA-PSS/ECDSA), CA (DH/ECDH) and all
standardised domain parameters (GFP/ECP).

%package -n eac-devel
Summary:        Development files for libeac
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description -n eac-devel
This package contains headers and libraries required to build applications that
use libeac.

%package doc
Summary:        OpenPACE Documentation
License:        GPL-3.0-or-later
Group:          Documentation/Other
BuildArch:      noarch

%description doc
This package contains the OpenPACE documentation.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
    --disable-static \
    --docdir=%{_docdir}/%{name}
# parallel build is broken
make V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -v %{buildroot}%{_bindir}/example
rm -vf %{buildroot}%{_docdir}/%{name}/.nojekyll
%fdupes %{buildroot}%{_docdir}/%{name}

%ldconfig_scriptlets -n %{libname}

%files
%{_bindir}/cvc-create
%{_bindir}/cvc-print
%{_bindir}/eactest
%{_mandir}/man1/cvc-create.1%{?ext_man}
%{_mandir}/man1/cvc-print.1%{?ext_man}

%files -n %{libname}
%license COPYING
%doc README.md
%dir %{_sysconfdir}/eac/
%dir %{_sysconfdir}/eac/cvc
%config(noreplace) %{_sysconfdir}/eac/cvc/*
%dir %{_sysconfdir}/eac/x509/
%config(noreplace) %{_sysconfdir}/eac/x509/*
%{_libdir}/libeac.so.%{sover}*

%files -n eac-devel
%{_includedir}/eac/
%{_libdir}/libeac.so
%{_libdir}/pkgconfig/libeac.pc

%files doc
%{_docdir}/openpace/

%changelog
