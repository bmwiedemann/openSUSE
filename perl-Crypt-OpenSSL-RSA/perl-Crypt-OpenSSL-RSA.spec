#
# spec file for package perl-Crypt-OpenSSL-RSA
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Crypt-OpenSSL-RSA
Version:        0.31
Release:        0
%define cpan_name Crypt-OpenSSL-RSA
Summary:        RSA encoding and decoding, using the openSSL libraries
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Crypt-OpenSSL-RSA/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         %{cpan_name}.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  openssl-devel
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Crypt::OpenSSL::Guess) >= 0.11
BuildRequires:  perl(Crypt::OpenSSL::Random)
Requires:       perl(Crypt::OpenSSL::Random)
Recommends:     perl(Crypt::OpenSSL::Bignum)
%{perl_requires}

%description
'Crypt::OpenSSL::RSA' provides the ability to RSA encrypt strings which are
somewhat shorter than the block size of a key. It also allows for
decryption, signatures and signature verification.

_NOTE_: Many of the methods in this package can croak, so use 'eval', or
Error.pm's try/catch mechanism to capture errors. Also, while some methods
from earlier versions of this package return true on success, this (never
documented) behavior is no longer the case.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0

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
%doc Changes README README.md
%license LICENSE

%changelog
