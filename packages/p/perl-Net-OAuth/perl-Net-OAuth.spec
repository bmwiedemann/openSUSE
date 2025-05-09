#
# spec file for package perl-Net-OAuth
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Net-OAuth
Name:           perl-Net-OAuth
Version:        0.310.0
Release:        0
# 0.31 -> normalize -> 0.310.0
%define cpan_version 0.31
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        OAuth 1.0 for Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRWO/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor) >= 0.31
BuildRequires:  perl(Class::Data::Inheritable) >= 0.60.0
BuildRequires:  perl(Crypt::URandom) >= 0.370
BuildRequires:  perl(Digest::SHA) >= 5.47
BuildRequires:  perl(Encode) >= 2.35
BuildRequires:  perl(LWP::UserAgent) >= 1
BuildRequires:  perl(Test::More) >= 0.66
BuildRequires:  perl(Test::Warn) >= 0.21
BuildRequires:  perl(URI) >= 5.150
Requires:       perl(Class::Accessor) >= 0.31
Requires:       perl(Class::Data::Inheritable) >= 0.60.0
Requires:       perl(Crypt::URandom) >= 0.370
Requires:       perl(Digest::SHA) >= 5.47
Requires:       perl(Encode) >= 2.35
Requires:       perl(LWP::UserAgent) >= 1
Requires:       perl(Test::More) >= 0.66
Requires:       perl(Test::Warn) >= 0.21
Requires:       perl(URI) >= 5.150
Provides:       perl(Net::OAuth) = %{version}
Provides:       perl(Net::OAuth::AccessToken)
Provides:       perl(Net::OAuth::AccessTokenRequest)
Provides:       perl(Net::OAuth::AccessTokenResponse)
Provides:       perl(Net::OAuth::Client) = %{version}
Provides:       perl(Net::OAuth::ConsumerRequest)
Provides:       perl(Net::OAuth::Message)
Provides:       perl(Net::OAuth::ProtectedResourceRequest)
Provides:       perl(Net::OAuth::Request) = %{version}
Provides:       perl(Net::OAuth::RequestTokenRequest)
Provides:       perl(Net::OAuth::RequestTokenResponse)
Provides:       perl(Net::OAuth::Response)
Provides:       perl(Net::OAuth::SignatureMethod::HMAC_SHA1)
Provides:       perl(Net::OAuth::SignatureMethod::HMAC_SHA256)
Provides:       perl(Net::OAuth::SignatureMethod::PLAINTEXT)
Provides:       perl(Net::OAuth::SignatureMethod::RSA_SHA1)
Provides:       perl(Net::OAuth::UserAuthRequest)
Provides:       perl(Net::OAuth::UserAuthResponse)
Provides:       perl(Net::OAuth::V1_0A::AccessTokenRequest)
Provides:       perl(Net::OAuth::V1_0A::RequestTokenRequest)
Provides:       perl(Net::OAuth::V1_0A::RequestTokenResponse)
Provides:       perl(Net::OAuth::V1_0A::UserAuthResponse)
Provides:       perl(Net::OAuth::XauthAccessTokenRequest)
Provides:       perl(Net::OAuth::YahooAccessTokenRefreshRequest)
%undefine       __perllib_provides
%{perl_requires}

%description
OAuth 1.0 for Perl

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README SECURITY.md

%changelog
