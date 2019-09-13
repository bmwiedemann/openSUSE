#
# spec file for package perl-CryptX
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-CryptX
Version:        0.064
Release:        0
%define cpan_name CryptX
Summary:        Cryptographic toolkit (self-contained, no external libraries needed)
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Cryptography in CryptX is based on https://github.com/libtom/libtomcrypt

Available modules:

* * Symmetric ciphers - see Crypt::Cipher and related modules

Crypt::Cipher::AES, Crypt::Cipher::Anubis, Crypt::Cipher::Blowfish,
Crypt::Cipher::Camellia, Crypt::Cipher::CAST5, Crypt::Cipher::DES,
Crypt::Cipher::DES_EDE, Crypt::Cipher::IDEA, Crypt::Cipher::KASUMI,
Crypt::Cipher::Khazad, Crypt::Cipher::MULTI2, Crypt::Cipher::Noekeon,
Crypt::Cipher::RC2, Crypt::Cipher::RC5, Crypt::Cipher::RC6,
Crypt::Cipher::SAFERP, Crypt::Cipher::SAFER_K128, Crypt::Cipher::SAFER_K64,
Crypt::Cipher::SAFER_SK128, Crypt::Cipher::SAFER_SK64, Crypt::Cipher::SEED,
Crypt::Cipher::Serpent, Crypt::Cipher::Skipjack, Crypt::Cipher::Twofish,
Crypt::Cipher::XTEA

* * Block cipher modes

Crypt::Mode::CBC, Crypt::Mode::CFB, Crypt::Mode::CTR, Crypt::Mode::ECB,
Crypt::Mode::OFB

* * Stream ciphers

Crypt::Stream::RC4, Crypt::Stream::ChaCha, Crypt::Stream::Salsa20,
Crypt::Stream::Sober128, Crypt::Stream::Sosemanuk, Crypt::Stream::Rabbit

* * Authenticated encryption modes

Crypt::AuthEnc::CCM, Crypt::AuthEnc::EAX, Crypt::AuthEnc::GCM,
Crypt::AuthEnc::OCB, Crypt::AuthEnc::ChaCha20Poly1305

* * Hash Functions - see Crypt::Digest and related modules

Crypt::Digest::BLAKE2b_160, Crypt::Digest::BLAKE2b_256,
Crypt::Digest::BLAKE2b_384, Crypt::Digest::BLAKE2b_512,
Crypt::Digest::BLAKE2s_128, Crypt::Digest::BLAKE2s_160,
Crypt::Digest::BLAKE2s_224, Crypt::Digest::BLAKE2s_256,
Crypt::Digest::CHAES, Crypt::Digest::MD2, Crypt::Digest::MD4,
Crypt::Digest::MD5, Crypt::Digest::RIPEMD128, Crypt::Digest::RIPEMD160,
Crypt::Digest::RIPEMD256, Crypt::Digest::RIPEMD320, Crypt::Digest::SHA1,
Crypt::Digest::SHA224, Crypt::Digest::SHA256, Crypt::Digest::SHA384,
Crypt::Digest::SHA512, Crypt::Digest::SHA512_224,
Crypt::Digest::SHA512_256, Crypt::Digest::Tiger192,
Crypt::Digest::Whirlpool, Crypt::Digest::Keccak224,
Crypt::Digest::Keccak256, Crypt::Digest::Keccak384,
Crypt::Digest::Keccak512, Crypt::Digest::SHA3_224, Crypt::Digest::SHA3_256,
Crypt::Digest::SHA3_384, Crypt::Digest::SHA3_512, Crypt::Digest::SHAKE

* * Checksums

Crypt::Checksum::Adler32, Crypt::Checksum::CRC32

* * Message Authentication Codes

Crypt::Mac::BLAKE2b, Crypt::Mac::BLAKE2s, Crypt::Mac::F9, Crypt::Mac::HMAC,
Crypt::Mac::OMAC, Crypt::Mac::Pelican, Crypt::Mac::PMAC, Crypt::Mac::XCBC,
Crypt::Mac::Poly1305

* * Public key cryptography

Crypt::PK::RSA, Crypt::PK::DSA, Crypt::PK::ECC, Crypt::PK::DH

* * Cryptographically secure random number generators - see Crypt::PRNG and
  related modules

Crypt::PRNG::Fortuna, Crypt::PRNG::Yarrow, Crypt::PRNG::RC4,
Crypt::PRNG::Sober128, Crypt::PRNG::ChaCha20

* * Key derivation functions - PBKDF1, PBKDF2 and HKDF

Crypt::KeyDerivation

* * Other handy functions related to cryptography

Crypt::Misc

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README.md
%license LICENSE

%changelog
