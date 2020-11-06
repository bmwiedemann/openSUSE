#
# spec file for package perl-Convert-ASN1
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Convert-ASN1
Version:        0.27
Release:        0
%define cpan_name Convert-ASN1
Summary:        ASN.1 Encode/Decode library
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GB/GBARR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
# MANUAL BEGIN
Patch0:         Convert-ASN1-0.22-test.diff
# PATCH-FIX-UPSTREAM bsc#1168934 CVE-2013-7488 Infinite loop via unexpected input
Patch1:         perl-Convert-ASN1-CVE-2013-7488.patch
# MANUAL END
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Math::BigInt) >= 1.997
BuildRequires:  perl(Test::More) >= 0.90
%{perl_requires}

%description
Convert::ASN1 encodes and decodes ASN.1 data structures using BER/DER
rules.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 
%patch1 

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc ChangeLog examples mkparse OldChanges parser.y README.md
%license LICENSE

%changelog
