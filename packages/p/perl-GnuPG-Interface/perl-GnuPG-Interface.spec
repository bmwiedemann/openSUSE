#
# spec file for package perl-GnuPG-Interface
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


%define cpan_name GnuPG-Interface
Name:           perl-GnuPG-Interface
Version:        1.30.0
Release:        0
%define cpan_version 1.03
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Supply object methods for interacting with GnuPG
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
BuildRequires:  perl(Math::BigInt) >= 1.78
BuildRequires:  perl(Moo) >= 0.091011
BuildRequires:  perl(MooX::HandlesVia) >= 0.001004
BuildRequires:  perl(MooX::late) >= 0.014
Requires:       perl(Math::BigInt) >= 1.78
Requires:       perl(Moo) >= 0.091011
Requires:       perl(MooX::HandlesVia) >= 0.001004
Requires:       perl(MooX::late) >= 0.014
Provides:       perl(GnuPG::Fingerprint)
Provides:       perl(GnuPG::Handles)
Provides:       perl(GnuPG::HashInit)
Provides:       perl(GnuPG::Interface) = 1.30.0
Provides:       perl(GnuPG::Key)
Provides:       perl(GnuPG::Options)
Provides:       perl(GnuPG::PrimaryKey)
Provides:       perl(GnuPG::PublicKey)
Provides:       perl(GnuPG::Revoker)
Provides:       perl(GnuPG::SecretKey)
Provides:       perl(GnuPG::Signature)
Provides:       perl(GnuPG::SubKey)
Provides:       perl(GnuPG::UserAttribute)
Provides:       perl(GnuPG::UserId)
%define         __perllib_provides /bin/true
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  gpg2
Requires:       gpg2
# MANUAL END

%description
GnuPG::Interface and its associated modules are designed to provide an
object-oriented method for interacting with GnuPG, being able to perform
functions such as but not limited to encrypting, signing, decryption,
verification, and key-listing parsing.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
%make_build

# MANUAL BEGIN
chmod 755 ./test/fake-gpg-v*

# MANUAL END
%check
# RT#88963
%{__make} test || :
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
