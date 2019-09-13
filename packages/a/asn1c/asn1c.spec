#
# spec file for package asn1c
#
# Copyright (c) 2014, Martin Hauke <mardnh@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           asn1c
Version:        0.9.28
Release:        0
Summary:        ASN.1 Compiler
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            http://lionet.info/asn1c/
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
%setup -q
sed -i 's|#!/usr/bin/env perl|#!/usr/bin/perl|g' examples/crfc2asn1.pl

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install
# remove duplicates
rm -rf %{buildroot}/%{_datadir}/doc/%{name}

%check
# Tests are broken - disabled for now
#make check %%{?_smp_mflags}

%files
%license LICENSE
%doc BUGS ChangeLog FAQ README.md TODO doc/asn1c-quick.pdf doc/asn1c-usage.pdf
%{_bindir}/*
%{_datadir}/asn1c
%{_mandir}/man1/*

%changelog
