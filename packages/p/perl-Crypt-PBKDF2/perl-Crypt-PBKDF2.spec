#
# spec file for package perl-Crypt-PBKDF2
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


%define cpan_name Crypt-PBKDF2
Name:           perl-Crypt-PBKDF2
Version:        0.261630
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        The PBKDF2 password hash algorithm
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARODLAND/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Digest) >= 1.16
BuildRequires:  perl(Digest::HMAC) >= 1.10
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Digest::SHA3) >= 0.220
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.34
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 2
BuildRequires:  perl(Moo::Role) >= 2
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Try::Tiny) >= 0.40
BuildRequires:  perl(Type::Tiny)
BuildRequires:  perl(Types::Standard) >= 1.0.5
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strictures) >= 2
Requires:       perl(Crypt::URandom)
Requires:       perl(Digest) >= 1.16
Requires:       perl(Digest::HMAC) >= 1.10
Requires:       perl(Digest::SHA)
Requires:       perl(Digest::SHA3) >= 0.220
Requires:       perl(Module::Runtime)
Requires:       perl(Moo) >= 2
Requires:       perl(Moo::Role) >= 2
Requires:       perl(Try::Tiny) >= 0.40
Requires:       perl(Type::Tiny)
Requires:       perl(Types::Standard) >= 1.0.5
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
%autosetup -n %{cpan_name}-%{version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
