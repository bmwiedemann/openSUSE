#
# spec file for package perl-ldap
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name perl-ldap
Name:           perl-ldap
Version:        0.68
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl::ldap Perl module
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARSCHAP/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Convert::ASN1) >= 0.2
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(Text::Soundex)
Requires:       perl(Convert::ASN1) >= 0.2
Recommends:     perl(Authen::SASL) >= 2.00
Recommends:     perl(IO::Socket::INET6)
Recommends:     perl(IO::Socket::SSL) >= 1.26
Recommends:     perl(URI::ldap) >= 1.10
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(IO::Socket::INET6)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(JSON)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(URI)
# MANUAL END

%description
perl::ldap Perl module

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644
# MANUAL BEGIN
find contrib -type f | xargs -n 1 sed -i "s@%{_prefix}/local/bin/perl@%{_bindir}/perl@"
# MANUAL END

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CREDITS README TODO

%changelog
