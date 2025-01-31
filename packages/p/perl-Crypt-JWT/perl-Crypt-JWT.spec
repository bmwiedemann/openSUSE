#
# spec file for package perl-Crypt-JWT
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


%define cpan_name Crypt-JWT
Name:           perl-Crypt-JWT
Version:        0.36.0
Release:        0
# 0.036 -> normalize -> 0.36.0
%define cpan_version 0.036
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        JSON Web Token
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIK/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(CryptX) >= 0.067
BuildRequires:  perl(JSON)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Compress::Raw::Zlib)
Requires:       perl(CryptX) >= 0.067
Requires:       perl(JSON)
Requires:       perl(Test::More) >= 0.88
Provides:       perl(Crypt::JWT) = %{version}
Provides:       perl(Crypt::KeyWrap) = %{version}
%undefine       __perllib_provides
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
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
