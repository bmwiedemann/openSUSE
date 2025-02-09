#
# spec file for package libtasn1
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define somajor 6
Name:           libtasn1
Version:        4.20.0
Release:        0
Summary:        ASN.1 parsing library
License:        GFDL-1.3-or-later AND GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Networking/Security
URL:            https://www.gnu.org/software/libtasn1/
Source0:        http://ftp.gnu.org/gnu/libtasn1/%{name}-%{version}.tar.gz
Source1:        http://ftp.gnu.org/gnu/libtasn1/%{name}-%{version}.tar.gz.sig
Source2:        https://josefsson.org/key-20190320.txt#/%{name}.keyring
Source99:       baselibs.conf
BuildRequires:  pkgconfig

%description
This is the ASN.1 library used by GNUTLS. Abstract Syntax Notation One (ASN.1)
is a standardized data description and serialization language.

%package -n libtasn1-%{somajor}
Summary:        ASN.1 parsing library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libtasn1-%{somajor}
This is the ASN.1 library used by GNUTLS. Abstract Syntax Notation One (ASN.1)
is a standardized data description and serialization language.

%package tools
Summary:        ASN.1 parsing tools
License:        GFDL-1.3-or-later AND GPL-3.0-or-later
Group:          Productivity/Networking/Diagnostic
Obsoletes:      libtasn1 <= 4.16.0
Provides:       libtasn1 = %{version}

%description tools
This package contains various utilities for parting ASN.1 data.

%package devel
Summary:        Development files for the ASN.1 parsing library
License:        GFDL-1.3-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libtasn1-%{somajor} = %{version}

%description devel
This is the ASN.1 library used by GNUTLS. Abstract Syntax Notation One (ASN.1)
is a standardized data description and serialization language.

This package contains files required to build against libtasn1.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n libtasn1-%{somajor}

%files -n libtasn1-%{somajor}
%license COPYING.LESSERv2
%{_libdir}/*.so.%{somajor}*

%files tools
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}
%{_infodir}/*.info%{?ext_info}

%files devel
%license COPYING.LESSERv2
%doc NEWS README THANKS
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libtasn1.pc
%{_mandir}/man3/*.3%{?ext_man}

%changelog
