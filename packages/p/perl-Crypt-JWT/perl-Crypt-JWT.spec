#
# spec file for package perl-Crypt-JWT
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


%define cpan_name Crypt-JWT
Name:           perl-Crypt-JWT
Version:        0.033
Release:        0
Summary:        JSON Web Token (JWT, JWS, JWE) as defined by RFC7519, RFC7515, RFC7516
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(CryptX) >= 0.067
BuildRequires:  perl(JSON)
Requires:       perl(Compress::Raw::Zlib)
Requires:       perl(CryptX) >= 0.067
Requires:       perl(JSON)
%{perl_requires}

%description
Implements *JSON Web Token (JWT)* - https://tools.ietf.org/html/rfc7519.
The implementation covers not only *JSON Web Signature (JWS)* -
https://tools.ietf.org/html/rfc7515, but also *JSON Web Encryption (JWE)* -
https://tools.ietf.org/html/rfc7516.

The module implements *all (100%) algorithms* defined in
https://tools.ietf.org/html/rfc7518 - *JSON Web Algorithms (JWA)*.

This module supports *Compact JWS/JWE* and *Flattened JWS/JWE JSON*
serialization, general JSON serialization is not supported yet.

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
%doc Changes README.md
%license LICENSE

%changelog
