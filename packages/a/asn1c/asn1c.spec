#
# spec file for package asn1c
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2014-2026, Martin Hauke <mardnh@gmx.de>
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


Name:           asn1c
Version:        0.9.29
Release:        0
Summary:        ASN.1 Compiler
License:        BSD-2-Clause
URL:            https://lionet.info/asn1c/
#Git-Clone:     https://github.com/vlm/asn1c.git
Source:         https://github.com/vlm/asn1c/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       asn1c-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  flex
BuildRequires:  libtool

%description
Compiles ASN.1 data structures into C source structures that can be
simply marshalled to/unmarshalled from: BER, DER, CER, BASIC-XER,
CXER, EXTENDED-XER, PER.

%prep
%autosetup
sed -i 's|#!%{_bindir}/env perl|#!%{_bindir}/perl|g' examples/crfc2asn1.pl

%build
autoreconf -fi
%configure
%make_build

%install
%make_install
# remove duplicates
rm -rf %{buildroot}/%{_datadir}/doc/%{name}

%check
# Tests are broken - disabled for now
#make check %%{?_smp_mflags}

%files
%license LICENSE
%doc BUGS ChangeLog FAQ README.md doc/asn1c-quick.pdf doc/asn1c-usage.pdf
%{_bindir}/asn1c
%{_bindir}/crfc2asn1.pl
%{_bindir}/enber
%{_bindir}/unber
%{_datadir}/asn1c
%{_mandir}/man1/asn1c.1%{?ext_man}
%{_mandir}/man1/enber.1%{?ext_man}
%{_mandir}/man1/unber.1%{?ext_man}

%changelog
