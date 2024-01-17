#
# spec file for package perl-CryptX
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


%define cpan_name CryptX
Name:           perl-CryptX
Version:        0.80.0
Release:        0
%define cpan_version 0.080
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Cryptographic toolkit
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIK/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Crypt::AuthEnc) = 0.80.0
Provides:       perl(Crypt::AuthEnc::CCM) = 0.80.0
Provides:       perl(Crypt::AuthEnc::ChaCha20Poly1305) = 0.80.0
Provides:       perl(Crypt::AuthEnc::EAX) = 0.80.0
Provides:       perl(Crypt::AuthEnc::GCM) = 0.80.0
Provides:       perl(Crypt::AuthEnc::OCB) = 0.80.0
Provides:       perl(Crypt::Checksum) = 0.80.0
Provides:       perl(Crypt::Checksum::Adler32) = 0.80.0
Provides:       perl(Crypt::Checksum::CRC32) = 0.80.0
Provides:       perl(Crypt::Cipher) = 0.80.0
Provides:       perl(Crypt::Cipher::AES) = 0.80.0
Provides:       perl(Crypt::Cipher::Anubis) = 0.80.0
Provides:       perl(Crypt::Cipher::Blowfish) = 0.80.0
Provides:       perl(Crypt::Cipher::CAST5) = 0.80.0
Provides:       perl(Crypt::Cipher::Camellia) = 0.80.0
Provides:       perl(Crypt::Cipher::DES) = 0.80.0
Provides:       perl(Crypt::Cipher::DES_EDE) = 0.80.0
Provides:       perl(Crypt::Cipher::IDEA) = 0.80.0
Provides:       perl(Crypt::Cipher::KASUMI) = 0.80.0
Provides:       perl(Crypt::Cipher::Khazad) = 0.80.0
Provides:       perl(Crypt::Cipher::MULTI2) = 0.80.0
Provides:       perl(Crypt::Cipher::Noekeon) = 0.80.0
Provides:       perl(Crypt::Cipher::RC2) = 0.80.0
Provides:       perl(Crypt::Cipher::RC5) = 0.80.0
Provides:       perl(Crypt::Cipher::RC6) = 0.80.0
Provides:       perl(Crypt::Cipher::SAFERP) = 0.80.0
Provides:       perl(Crypt::Cipher::SAFER_K128) = 0.80.0
Provides:       perl(Crypt::Cipher::SAFER_K64) = 0.80.0
Provides:       perl(Crypt::Cipher::SAFER_SK128) = 0.80.0
Provides:       perl(Crypt::Cipher::SAFER_SK64) = 0.80.0
Provides:       perl(Crypt::Cipher::SEED) = 0.80.0
Provides:       perl(Crypt::Cipher::Serpent) = 0.80.0
Provides:       perl(Crypt::Cipher::Skipjack) = 0.80.0
Provides:       perl(Crypt::Cipher::Twofish) = 0.80.0
Provides:       perl(Crypt::Cipher::XTEA) = 0.80.0
Provides:       perl(Crypt::Digest) = 0.80.0
Provides:       perl(Crypt::Digest::BLAKE2b_160) = 0.80.0
Provides:       perl(Crypt::Digest::BLAKE2b_256) = 0.80.0
Provides:       perl(Crypt::Digest::BLAKE2b_384) = 0.80.0
Provides:       perl(Crypt::Digest::BLAKE2b_512) = 0.80.0
Provides:       perl(Crypt::Digest::BLAKE2s_128) = 0.80.0
Provides:       perl(Crypt::Digest::BLAKE2s_160) = 0.80.0
Provides:       perl(Crypt::Digest::BLAKE2s_224) = 0.80.0
Provides:       perl(Crypt::Digest::BLAKE2s_256) = 0.80.0
Provides:       perl(Crypt::Digest::CHAES) = 0.80.0
Provides:       perl(Crypt::Digest::Keccak224) = 0.80.0
Provides:       perl(Crypt::Digest::Keccak256) = 0.80.0
Provides:       perl(Crypt::Digest::Keccak384) = 0.80.0
Provides:       perl(Crypt::Digest::Keccak512) = 0.80.0
Provides:       perl(Crypt::Digest::MD2) = 0.80.0
Provides:       perl(Crypt::Digest::MD4) = 0.80.0
Provides:       perl(Crypt::Digest::MD5) = 0.80.0
Provides:       perl(Crypt::Digest::RIPEMD128) = 0.80.0
Provides:       perl(Crypt::Digest::RIPEMD160) = 0.80.0
Provides:       perl(Crypt::Digest::RIPEMD256) = 0.80.0
Provides:       perl(Crypt::Digest::RIPEMD320) = 0.80.0
Provides:       perl(Crypt::Digest::SHA1) = 0.80.0
Provides:       perl(Crypt::Digest::SHA224) = 0.80.0
Provides:       perl(Crypt::Digest::SHA256) = 0.80.0
Provides:       perl(Crypt::Digest::SHA384) = 0.80.0
Provides:       perl(Crypt::Digest::SHA3_224) = 0.80.0
Provides:       perl(Crypt::Digest::SHA3_256) = 0.80.0
Provides:       perl(Crypt::Digest::SHA3_384) = 0.80.0
Provides:       perl(Crypt::Digest::SHA3_512) = 0.80.0
Provides:       perl(Crypt::Digest::SHA512) = 0.80.0
Provides:       perl(Crypt::Digest::SHA512_224) = 0.80.0
Provides:       perl(Crypt::Digest::SHA512_256) = 0.80.0
Provides:       perl(Crypt::Digest::SHAKE) = 0.80.0
Provides:       perl(Crypt::Digest::Tiger192) = 0.80.0
Provides:       perl(Crypt::Digest::Whirlpool) = 0.80.0
Provides:       perl(Crypt::KeyDerivation) = 0.80.0
Provides:       perl(Crypt::Mac) = 0.80.0
Provides:       perl(Crypt::Mac::BLAKE2b) = 0.80.0
Provides:       perl(Crypt::Mac::BLAKE2s) = 0.80.0
Provides:       perl(Crypt::Mac::F9) = 0.80.0
Provides:       perl(Crypt::Mac::HMAC) = 0.80.0
Provides:       perl(Crypt::Mac::OMAC) = 0.80.0
Provides:       perl(Crypt::Mac::PMAC) = 0.80.0
Provides:       perl(Crypt::Mac::Pelican) = 0.80.0
Provides:       perl(Crypt::Mac::Poly1305) = 0.80.0
Provides:       perl(Crypt::Mac::XCBC) = 0.80.0
Provides:       perl(Crypt::Misc) = 0.80.0
Provides:       perl(Crypt::Mode) = 0.80.0
Provides:       perl(Crypt::Mode::CBC) = 0.80.0
Provides:       perl(Crypt::Mode::CFB) = 0.80.0
Provides:       perl(Crypt::Mode::CTR) = 0.80.0
Provides:       perl(Crypt::Mode::ECB) = 0.80.0
Provides:       perl(Crypt::Mode::OFB) = 0.80.0
Provides:       perl(Crypt::PK) = 0.80.0
Provides:       perl(Crypt::PK::DH) = 0.80.0
Provides:       perl(Crypt::PK::DSA) = 0.80.0
Provides:       perl(Crypt::PK::ECC) = 0.80.0
Provides:       perl(Crypt::PK::Ed25519) = 0.80.0
Provides:       perl(Crypt::PK::RSA) = 0.80.0
Provides:       perl(Crypt::PK::X25519) = 0.80.0
Provides:       perl(Crypt::PRNG) = 0.80.0
Provides:       perl(Crypt::PRNG::ChaCha20) = 0.80.0
Provides:       perl(Crypt::PRNG::Fortuna) = 0.80.0
Provides:       perl(Crypt::PRNG::RC4) = 0.80.0
Provides:       perl(Crypt::PRNG::Sober128) = 0.80.0
Provides:       perl(Crypt::PRNG::Yarrow) = 0.80.0
Provides:       perl(Crypt::Stream::ChaCha) = 0.80.0
Provides:       perl(Crypt::Stream::RC4) = 0.80.0
Provides:       perl(Crypt::Stream::Rabbit) = 0.80.0
Provides:       perl(Crypt::Stream::Salsa20) = 0.80.0
Provides:       perl(Crypt::Stream::Sober128) = 0.80.0
Provides:       perl(Crypt::Stream::Sosemanuk) = 0.80.0
Provides:       perl(CryptX) = 0.80.0
Provides:       perl(Math::BigInt::LTM) = 0.80.0
%define         __perllib_provides /bin/true
%{perl_requires}

%description
Perl modules providing a cryptography based on at
https://github.com/libtom/libtomcrypt library.

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

Crypt::PK::RSA, Crypt::PK::DSA, Crypt::PK::ECC, Crypt::PK::DH,
Crypt::PK::Ed25519, Crypt::PK::X25519

* * Cryptographically secure random number generators - see Crypt::PRNG and
  related modules

Crypt::PRNG::Fortuna, Crypt::PRNG::Yarrow, Crypt::PRNG::RC4,
Crypt::PRNG::Sober128, Crypt::PRNG::ChaCha20

* * Key derivation functions - PBKDF1, PBKDF2 and HKDF

Crypt::KeyDerivation

* * Other handy functions related to cryptography

Crypt::Misc

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
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
