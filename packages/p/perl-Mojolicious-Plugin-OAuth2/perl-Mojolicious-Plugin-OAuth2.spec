#
# spec file for package perl-Mojolicious-Plugin-OAuth2
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Mojolicious-Plugin-OAuth2
Name:           perl-Mojolicious-Plugin-OAuth2
Version:        2.02
Release:        0
Summary:        Auth against OAuth2 APIs including OpenID Connect
License:        Artistic-2.0
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Socket::SSL) >= 1.94
BuildRequires:  perl(Mojolicious) >= 8.25
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(IO::Socket::SSL) >= 1.94
Requires:       perl(Mojolicious) >= 8.25
Recommends:     perl(Crypt::OpenSSL::Bignum) >= 0.09
Recommends:     perl(Crypt::OpenSSL::RSA) >= 0.31
Recommends:     perl(Mojo::JWT) >= 0.09
%{perl_requires}

%description
This Mojolicious plugin allows you to easily authenticate against a at
http://oauth.net or at https://openid.net/connect/ provider. It includes
configurations for a few popular providers, but you can add your own as
well.

See register for a full list of bundled providers.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes README README.md

%changelog
