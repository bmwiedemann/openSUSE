#
# spec file for package perl-Crypt-OpenSSL-RSA
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


%define cpan_name Crypt-OpenSSL-RSA
Name:           perl-Crypt-OpenSSL-RSA
Version:        0.370.0
Release:        0
# 0.37 -> normalize -> 0.370.0
%define cpan_version 0.37
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        RSA encoding and decoding, using the openSSL libraries
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
Patch0:         Crypt-OpenSSL-RSA.patch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Crypt::OpenSSL::Guess) >= 0.110
BuildRequires:  perl(Crypt::OpenSSL::Random)
Requires:       perl(Crypt::OpenSSL::Random)
Provides:       perl(Crypt::OpenSSL::RSA) = %{version}
%undefine       __perllib_provides
Recommends:     perl(Crypt::OpenSSL::Bignum)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  openssl-devel
# MANUAL END

%description
'Crypt::OpenSSL::RSA' provides the ability to RSA encrypt strings which are
somewhat shorter than the block size of a key. It also allows for
decryption, signatures and signature verification.

_NOTE_: Many of the methods in this package can croak, so use 'eval', or
Error.pm's try/catch mechanism to capture errors. Also, while some methods
from earlier versions of this package return true on success, this (never
documented) behavior is no longer the case.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README README.md
%license LICENSE

%changelog
