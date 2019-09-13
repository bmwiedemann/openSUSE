#
# spec file for package perl-Crypt-CBC
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Crypt-CBC
Version:        2.33
Release:        0
%define cpan_name Crypt-CBC
Summary:        Encrypt Data with Cipher Block Chaining Mode
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Crypt-CBC/
Source:         http://www.cpan.org/authors/id/L/LD/LDS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires: perl(Crypt::CBC)
#BuildRequires: perl(Crypt::IDEA)
%{perl_requires}

%description
This module is a Perl-only implementation of the cryptographic cipher block
chaining mode (CBC). In combination with a block cipher such as DES or
IDEA, you can encrypt and decrypt messages of arbitrarily long length. The
encrypted messages are compatible with the encryption format used by the
*OpenSSL* package.

To use this module, you will first create a Crypt::CBC cipher object with
new(). At the time of cipher creation, you specify an encryption key to use
and, optionally, a block encryption algorithm. You will then call the
start() method to initialize the encryption or decryption process, crypt()
to encrypt or decrypt one or more blocks of data, and lastly finish(), to
pad and encrypt the final block. For your convenience, you can call the
encrypt() and decrypt() methods to operate on a whole data value at once.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes Crypt-CBC-2.16-vulnerability.txt README

%changelog
