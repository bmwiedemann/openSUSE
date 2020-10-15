#
# spec file for package perl-Crypt-Rijndael
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Crypt-Rijndael
Version:        1.15
Release:        0
#Upstream: SUSE-Public-Domain
%define cpan_name Crypt-Rijndael
Summary:        Crypt::CBC compliant Rijndael encryption module
License:        LGPL-3.0-only
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module implements the Rijndael cipher, which has just been selected as
the Advanced Encryption Standard.

* keysize

Returns the keysize, which is 32 (bytes). The Rijndael cipher actually
supports keylengths of 16, 24 or 32 bytes, but there is no way to
communicate this to 'Crypt::CBC'.

* blocksize

The blocksize for Rijndael is 16 bytes (128 bits), although the algorithm
actually supports any blocksize that is any multiple of our bytes. 128
bits, is however, the AES-specified block size, so this is all we support.

* $cipher = Crypt::Rijndael->new( $key [, $mode] )

Create a new 'Crypt::Rijndael' cipher object with the given key (which must
be 128, 192 or 256 bits long). The additional '$mode' argument is the
encryption mode, either 'MODE_ECB' (electronic codebook mode, the default),
'MODE_CBC' (cipher block chaining, the same that 'Crypt::CBC' does),
'MODE_CFB' (128-bit cipher feedback), 'MODE_OFB' (128-bit output feedback),
or 'MODE_CTR' (counter mode).

ECB mode is very insecure (read a book on cryptography if you don't know
why!), so you should probably use CBC mode.

* $cipher->set_iv($iv)

This allows you to change the initial value vector used by the chaining
modes. It is not relevant for ECB mode.

* $cipher->encrypt($data)

Encrypt data. The size of '$data' must be a multiple of 'blocksize' (16
bytes), otherwise this function will croak. Apart from that, it can be of
(almost) any length.

* $cipher->decrypt($data)

Decrypts '$data'.

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
%doc Changes NEWS README
%license COPYING LICENSE

%changelog
