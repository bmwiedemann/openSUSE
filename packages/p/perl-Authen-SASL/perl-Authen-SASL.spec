#
# spec file for package perl-Authen-SASL
#
# Copyright (c) 2023 SUSE LLC
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
Version:        2.170.0
Release:        0
%define cpan_version 2.1700
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        SASL Authentication framework
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/EH/EHUELS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::HMAC_MD5)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(Digest::HMAC_MD5)
Provides:       perl(Authen::SASL) = 2.170.0
Provides:       perl(Authen::SASL::CRAM_MD5) = 2.170.0
Provides:       perl(Authen::SASL::EXTERNAL) = 2.170.0
Provides:       perl(Authen::SASL::Perl) = 2.170.0
Provides:       perl(Authen::SASL::Perl::ANONYMOUS) = 2.170.0
Provides:       perl(Authen::SASL::Perl::CRAM_MD5) = 2.170.0
Provides:       perl(Authen::SASL::Perl::DIGEST_MD5) = 2.170.0
Provides:       perl(Authen::SASL::Perl::EXTERNAL) = 2.170.0
Provides:       perl(Authen::SASL::Perl::GSSAPI) = 2.170.0
Provides:       perl(Authen::SASL::Perl::LOGIN) = 2.170.0
Provides:       perl(Authen::SASL::Perl::PLAIN) = 2.170.0
%define         __perllib_provides /bin/true
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
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc api.txt Changes compat_pl example_pl README
%license LICENSE

%changelog
