#
# spec file for package perl-Mail-DKIM
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


%define cpan_name Mail-DKIM
Name:           perl-Mail-DKIM
Version:        1.20240619
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Signs/verifies Internet mail with DKIM/DomainKey signatures
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBRADSHAW/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Crypt::OpenSSL::RSA)
BuildRequires:  perl(Crypt::PK::Ed25519)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Mail::Address)
BuildRequires:  perl(Mail::AuthenticationResults::Header::AuthServID)
BuildRequires:  perl(Mail::AuthenticationResults::Parser)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(Net::DNS::Resolver)
BuildRequires:  perl(Net::DNS::Resolver::Mock)
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(YAML)
BuildRequires:  perl(YAML::XS)
Requires:       perl(Crypt::OpenSSL::RSA)
Requires:       perl(Crypt::PK::Ed25519)
Requires:       perl(Digest::SHA)
Requires:       perl(Mail::Address)
Requires:       perl(Mail::AuthenticationResults::Header::AuthServID)
Requires:       perl(Mail::AuthenticationResults::Parser)
Requires:       perl(Net::DNS)
%{perl_requires}

%description
This module implements the various components of the DKIM and DomainKeys
message-signing and verifying standards for Internet mail. It currently
tries to implement these specifications:

* RFC4871, for DKIM

* RFC4870, for DomainKeys

* draft-ietf-dmarc-arc-protocol-06, for ARC

The module uses an object-oriented interface. You use one of two different
classes, depending on whether you are signing or verifying a message. To
sign, use the Mail::DKIM::Signer class. To verify, use the
Mail::DKIM::Verifier class. Simple, eh?

Likewise for ARC, use the ARC modules Mail::DKIM::ARC::Signer and
Mail::DKIM::ARC::Verifier

If you're sending to test libraries which expect the tags in headers to be
sorted, you can set $Mail::DKIM::SORTTAGS to a true value, and all created
headers will get sorted keys

%prep
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes doc HACKING.DKIM README README.md TODO
%license LICENSE

%changelog
