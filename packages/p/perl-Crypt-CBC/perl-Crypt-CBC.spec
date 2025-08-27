#
# spec file for package perl-Crypt-CBC
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name Crypt-CBC
Name:           perl-Crypt-CBC
Version:        3.70.0
Release:        0
# 3.07 -> normalize -> 3.70.0
%define cpan_version 3.07
#Upstream: Artistic-2.0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Encrypt Data with Cipher Block Chaining Mode
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Crypt::Cipher::AES)
BuildRequires:  perl(Crypt::PBKDF2)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Digest::SHA)
Requires:       perl(Crypt::Cipher::AES)
Requires:       perl(Crypt::PBKDF2)
Requires:       perl(Crypt::URandom)
Requires:       perl(Digest::SHA)
Provides:       perl(Crypt::CBC) = %{version}
Provides:       perl(Crypt::CBC::PBKDF) = %{version}
Provides:       perl(Crypt::CBC::PBKDF::none) = %{version}
Provides:       perl(Crypt::CBC::PBKDF::opensslv1) = %{version}
Provides:       perl(Crypt::CBC::PBKDF::opensslv2) = %{version}
Provides:       perl(Crypt::CBC::PBKDF::pbkdf2) = %{version}
Provides:       perl(Crypt::CBC::PBKDF::randomiv) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module is a Perl-only implementation of the cryptographic cipher block
chaining mode (CBC). In combination with a block cipher such as AES or
Blowfish, you can encrypt and decrypt messages of arbitrarily long length.
The encrypted messages are compatible with the encryption format used by
the *OpenSSL* package.

To use this module, you will first create a Crypt::CBC cipher object with
new(). At the time of cipher creation, you specify an encryption key to use
and, optionally, a block encryption algorithm. You will then call the
start() method to initialize the encryption or decryption process, crypt()
to encrypt or decrypt one or more blocks of data, and lastly finish(), to
pad and encrypt the final block. For your convenience, you can call the
encrypt() and decrypt() methods to operate on a whole data value at once.

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
%doc Changes README SECURITY.md vulnerabilities.txt
%license LICENSE

%changelog
