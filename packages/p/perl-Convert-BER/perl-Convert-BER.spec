#
# spec file for package perl-Convert-BER
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           perl-Convert-BER
%define cpan_name Convert-BER
Version:        1.32
Release:        9
Provides:       perl_ber
Obsoletes:      perl_ber
AutoReqProv:    on
Url:            http://search.cpan.org/dist/%{cpan_name}
License:        GPL-2.0+
Group:          Development/Libraries/Perl
Summary:        ASN.1 Basic Encoding Rules
Source:         %{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
Convert::BER is a Perl object class implementation for encoding and
decoding objects as described by ITU-T standard X.209 (ASN.1) using
Basic Encoding Rules (BER).

WARNING this module is no longer supported, See Convert::ASN1 

%prep
%setup -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Convert
%{perl_vendorarch}/auto/Convert

%changelog
