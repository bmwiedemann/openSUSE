#
# spec file for package perl-Crypt-PBKDF2
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Crypt-PBKDF2
Name:           perl-Crypt-PBKDF2
Version:        0.161520
Release:        0
Summary:        The PBKDF2 password hashing algorithm
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARODLAND/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Digest) >= 1.16
BuildRequires:  perl(Digest::HMAC) >= 1.01
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Digest::SHA3) >= 0.22
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 2
BuildRequires:  perl(Moo::Role) >= 2
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Try::Tiny) >= 0.04
BuildRequires:  perl(Type::Tiny)
BuildRequires:  perl(Types::Standard) >= 1.000005
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strictures) >= 2
Requires:       perl(Digest) >= 1.16
Requires:       perl(Digest::HMAC) >= 1.01
Requires:       perl(Digest::SHA)
Requires:       perl(Digest::SHA3) >= 0.22
Requires:       perl(Module::Runtime)
Requires:       perl(Moo) >= 2
Requires:       perl(Moo::Role) >= 2
Requires:       perl(Try::Tiny) >= 0.04
Requires:       perl(Type::Tiny)
Requires:       perl(Types::Standard) >= 1.000005
Requires:       perl(namespace::autoclean)
Requires:       perl(strictures) >= 2
%{perl_requires}

%description
PBKDF2 is a secure password hashing algorithm that uses the techniques of
"key strengthening" to make the complexity of a brute-force attack
arbitrarily high. PBKDF2 uses any other cryptographic hash or cipher (by
convention, usually HMAC-SHA1, but 'Crypt::PBKDF2' is fully pluggable), and
allows for an arbitrary number of iterations of the hashing function, and a
nearly unlimited output hash size (up to 2**32 - 1 times the size of the
output of the backend hash). The hash is salted, as any password hash
should be, and the salt may also be of arbitrary size.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes
%license LICENSE

%changelog
