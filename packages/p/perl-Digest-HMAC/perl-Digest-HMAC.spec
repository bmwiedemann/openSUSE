#
# spec file for package perl-Digest-HMAC
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


%define cpan_name Digest-HMAC
Name:           perl-Digest-HMAC
Version:        1.50.0
Release:        0
# 1.05 -> normalize -> 1.50.0
%define cpan_version 1.05
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Keyed-Hashing for Message Authentication
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARODLAND/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::SHA) >= 1
Requires:       perl(Digest::SHA) >= 1
Provides:       perl(Digest::HMAC) = %{version}
Provides:       perl(Digest::HMAC_MD5) = %{version}
Provides:       perl(Digest::HMAC_SHA1) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
HMAC is used for message integrity checks between two parties that share a
secret key, and works in combination with some other Digest algorithm,
usually MD5 or SHA-1. The HMAC mechanism is described in RFC 2104.

HMAC follow the common 'Digest::' interface, but the constructor takes the
secret key and the name of some other simple 'Digest::' as argument.

The hmac() and hmac_hex() functions and the Digest::HMAC->new() constructor
takes an optional $blocksize argument as well. The HMAC algorithm assumes
the digester to hash by iterating a basic compression function on blocks of
data and the $blocksize should match the byte-length of such blocks.

The default $blocksize is 64 which is suitable for the MD5 and SHA-1 digest
functions. For stronger algorithms the blocksize probably needs to be
increased.

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
%doc Changes README
%license LICENSE

%changelog
