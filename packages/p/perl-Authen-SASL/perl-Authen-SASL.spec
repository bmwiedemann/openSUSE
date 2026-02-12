#
# spec file for package perl-Authen-SASL
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Authen-SASL
Name:           perl-Authen-SASL
Version:        2.200.0
Release:        0
# 2.2000 -> normalize -> 2.200.0
%define cpan_version 2.2000
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        SASL Authentication framework
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/EH/EHUELS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Digest::HMAC_MD5)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(Crypt::URandom)
Requires:       perl(Digest::HMAC_MD5)
Provides:       perl(Authen::SASL) = %{version}
Provides:       perl(Authen::SASL::CRAM_MD5) = %{version}
Provides:       perl(Authen::SASL::EXTERNAL) = %{version}
Provides:       perl(Authen::SASL::Perl) = %{version}
Provides:       perl(Authen::SASL::Perl::ANONYMOUS) = %{version}
Provides:       perl(Authen::SASL::Perl::CRAM_MD5) = %{version}
Provides:       perl(Authen::SASL::Perl::DIGEST_MD5) = %{version}
Provides:       perl(Authen::SASL::Perl::EXTERNAL) = %{version}
Provides:       perl(Authen::SASL::Perl::GSSAPI) = %{version}
Provides:       perl(Authen::SASL::Perl::LOGIN) = %{version}
Provides:       perl(Authen::SASL::Perl::OAUTHBEARER) = %{version}
Provides:       perl(Authen::SASL::Perl::PLAIN) = %{version}
Provides:       perl(Authen::SASL::Perl::XOAUTH2) = %{version}
%undefine       __perllib_provides
Recommends:     perl(GSSAPI)
%{perl_requires}

%description
SASL is a generic mechanism for authentication used by several network
protocols. *Authen::SASL* provides an implementation framework that all
protocols should be able to share.

The framework allows different implementations of the connection class to
be plugged in. At the time of writing there were two such plugins.

* Authen::SASL::Perl

This module implements several mechanisms and is implemented entirely in
Perl.

* Authen::SASL::XS

This module uses the Cyrus SASL C-library (both version 1 and 2 are
supported).

* Authen::SASL::Cyrus

This module is the predecessor to Authen::SASL::XS.

Until version 2.16, Authen::SASL::Cyrus was loaded as an alternative to
Authen::SASL::XS.

By default Authen::SASL tries to load Authen::SASL::XS first, followed by
Authen::SASL::Perl on failure. If you want to change the order or want to
specifically use one implementation only simply do

 use Authen::SASL qw(Perl);

or if you have another plugin module that supports the Authen::SASL API

 use Authen::SASL qw(My::SASL::Plugin);

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc api.txt Changes README
%license LICENSE

%changelog
