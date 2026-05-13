#
# spec file for package perl-CryptX
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


%define cpan_name CryptX
Name:           perl-CryptX
Version:        0.89.0
Release:        0
# 0.089 -> normalize -> 0.89.0
%define cpan_version 0.089
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Cryptographic toolkit
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIK/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Crypt::ASN1) = %{version}
Provides:       perl(Crypt::AuthEnc) = %{version}
Provides:       perl(Crypt::AuthEnc::CCM) = %{version}
Provides:       perl(Crypt::AuthEnc::ChaCha20Poly1305) = %{version}
Provides:       perl(Crypt::AuthEnc::EAX) = %{version}
Provides:       perl(Crypt::AuthEnc::GCM) = %{version}
Provides:       perl(Crypt::AuthEnc::OCB) = %{version}
Provides:       perl(Crypt::AuthEnc::SIV) = %{version}
Provides:       perl(Crypt::AuthEnc::XChaCha20Poly1305) = %{version}
Provides:       perl(Crypt::Checksum) = %{version}
Provides:       perl(Crypt::Checksum::Adler32) = %{version}
Provides:       perl(Crypt::Checksum::CRC32) = %{version}
Provides:       perl(Crypt::Cipher) = %{version}
Provides:       perl(Crypt::Cipher::AES) = %{version}
Provides:       perl(Crypt::Cipher::Anubis) = %{version}
Provides:       perl(Crypt::Cipher::Blowfish) = %{version}
Provides:       perl(Crypt::Cipher::CAST5) = %{version}
Provides:       perl(Crypt::Cipher::Camellia) = %{version}
Provides:       perl(Crypt::Cipher::DES) = %{version}
Provides:       perl(Crypt::Cipher::DES_EDE) = %{version}
Provides:       perl(Crypt::Cipher::IDEA) = %{version}
Provides:       perl(Crypt::Cipher::KASUMI) = %{version}
Provides:       perl(Crypt::Cipher::Khazad) = %{version}
Provides:       perl(Crypt::Cipher::MULTI2) = %{version}
Provides:       perl(Crypt::Cipher::Noekeon) = %{version}
Provides:       perl(Crypt::Cipher::RC2) = %{version}
Provides:       perl(Crypt::Cipher::RC5) = %{version}
Provides:       perl(Crypt::Cipher::RC6) = %{version}
Provides:       perl(Crypt::Cipher::SAFERP) = %{version}
Provides:       perl(Crypt::Cipher::SAFER_K128) = %{version}
Provides:       perl(Crypt::Cipher::SAFER_K64) = %{version}
Provides:       perl(Crypt::Cipher::SAFER_SK128) = %{version}
Provides:       perl(Crypt::Cipher::SAFER_SK64) = %{version}
Provides:       perl(Crypt::Cipher::SEED) = %{version}
Provides:       perl(Crypt::Cipher::SM4) = %{version}
Provides:       perl(Crypt::Cipher::Serpent) = %{version}
Provides:       perl(Crypt::Cipher::Skipjack) = %{version}
Provides:       perl(Crypt::Cipher::Twofish) = %{version}
Provides:       perl(Crypt::Cipher::XTEA) = %{version}
Provides:       perl(Crypt::Digest) = %{version}
Provides:       perl(Crypt::Digest::BLAKE2b_160) = %{version}
Provides:       perl(Crypt::Digest::BLAKE2b_256) = %{version}
Provides:       perl(Crypt::Digest::BLAKE2b_384) = %{version}
Provides:       perl(Crypt::Digest::BLAKE2b_512) = %{version}
Provides:       perl(Crypt::Digest::BLAKE2s_128) = %{version}
Provides:       perl(Crypt::Digest::BLAKE2s_160) = %{version}
Provides:       perl(Crypt::Digest::BLAKE2s_224) = %{version}
Provides:       perl(Crypt::Digest::BLAKE2s_256) = %{version}
Provides:       perl(Crypt::Digest::CHAES) = %{version}
Provides:       perl(Crypt::Digest::KangarooTwelve) = %{version}
Provides:       perl(Crypt::Digest::Keccak224) = %{version}
Provides:       perl(Crypt::Digest::Keccak256) = %{version}
Provides:       perl(Crypt::Digest::Keccak384) = %{version}
Provides:       perl(Crypt::Digest::Keccak512) = %{version}
Provides:       perl(Crypt::Digest::MD2) = %{version}
Provides:       perl(Crypt::Digest::MD4) = %{version}
Provides:       perl(Crypt::Digest::MD5) = %{version}
Provides:       perl(Crypt::Digest::RIPEMD128) = %{version}
Provides:       perl(Crypt::Digest::RIPEMD160) = %{version}
Provides:       perl(Crypt::Digest::RIPEMD256) = %{version}
Provides:       perl(Crypt::Digest::RIPEMD320) = %{version}
Provides:       perl(Crypt::Digest::SHA1) = %{version}
Provides:       perl(Crypt::Digest::SHA224) = %{version}
Provides:       perl(Crypt::Digest::SHA256) = %{version}
Provides:       perl(Crypt::Digest::SHA384) = %{version}
Provides:       perl(Crypt::Digest::SHA3_224) = %{version}
Provides:       perl(Crypt::Digest::SHA3_256) = %{version}
Provides:       perl(Crypt::Digest::SHA3_384) = %{version}
Provides:       perl(Crypt::Digest::SHA3_512) = %{version}
Provides:       perl(Crypt::Digest::SHA512) = %{version}
Provides:       perl(Crypt::Digest::SHA512_224) = %{version}
Provides:       perl(Crypt::Digest::SHA512_256) = %{version}
Provides:       perl(Crypt::Digest::SHAKE) = %{version}
Provides:       perl(Crypt::Digest::Tiger192) = %{version}
Provides:       perl(Crypt::Digest::TurboSHAKE) = %{version}
Provides:       perl(Crypt::Digest::Whirlpool) = %{version}
Provides:       perl(Crypt::KeyDerivation) = %{version}
Provides:       perl(Crypt::Mac) = %{version}
Provides:       perl(Crypt::Mac::BLAKE2b) = %{version}
Provides:       perl(Crypt::Mac::BLAKE2s) = %{version}
Provides:       perl(Crypt::Mac::F9) = %{version}
Provides:       perl(Crypt::Mac::HMAC) = %{version}
Provides:       perl(Crypt::Mac::OMAC) = %{version}
Provides:       perl(Crypt::Mac::PMAC) = %{version}
Provides:       perl(Crypt::Mac::Pelican) = %{version}
Provides:       perl(Crypt::Mac::Poly1305) = %{version}
Provides:       perl(Crypt::Mac::XCBC) = %{version}
Provides:       perl(Crypt::Misc) = %{version}
Provides:       perl(Crypt::Mode) = %{version}
Provides:       perl(Crypt::Mode::CBC) = %{version}
Provides:       perl(Crypt::Mode::CFB) = %{version}
Provides:       perl(Crypt::Mode::CTR) = %{version}
Provides:       perl(Crypt::Mode::ECB) = %{version}
Provides:       perl(Crypt::Mode::OFB) = %{version}
Provides:       perl(Crypt::PK) = %{version}
Provides:       perl(Crypt::PK::DH) = %{version}
Provides:       perl(Crypt::PK::DSA) = %{version}
Provides:       perl(Crypt::PK::ECC) = %{version}
Provides:       perl(Crypt::PK::Ed25519) = %{version}
Provides:       perl(Crypt::PK::Ed448) = %{version}
Provides:       perl(Crypt::PK::RSA) = %{version}
Provides:       perl(Crypt::PK::X25519) = %{version}
Provides:       perl(Crypt::PK::X448) = %{version}
Provides:       perl(Crypt::PRNG) = %{version}
Provides:       perl(Crypt::PRNG::ChaCha20) = %{version}
Provides:       perl(Crypt::PRNG::Fortuna) = %{version}
Provides:       perl(Crypt::PRNG::RC4) = %{version}
Provides:       perl(Crypt::PRNG::Sober128) = %{version}
Provides:       perl(Crypt::PRNG::Yarrow) = %{version}
Provides:       perl(Crypt::Stream::ChaCha) = %{version}
Provides:       perl(Crypt::Stream::RC4) = %{version}
Provides:       perl(Crypt::Stream::Rabbit) = %{version}
Provides:       perl(Crypt::Stream::Salsa20) = %{version}
Provides:       perl(Crypt::Stream::Sober128) = %{version}
Provides:       perl(Crypt::Stream::Sosemanuk) = %{version}
Provides:       perl(Crypt::Stream::XChaCha) = %{version}
Provides:       perl(Crypt::Stream::XSalsa20) = %{version}
Provides:       perl(CryptX) = %{version}
Provides:       perl(Math::BigInt::LTM) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Perl cryptographic modules built on the bundled at
https://github.com/libtom/libtomcrypt library. The distribution also
includes Math::BigInt::LTM, a Math::BigInt backend built on the bundled at
https://www.libtom.net/LibTomMath/ library used internally by LibTomCrypt.

This module mainly serves as the top-level distribution/documentation page.
For actual work, use one of the concrete modules listed below.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes README.md SECURITY.md
%license LICENSE

%changelog
