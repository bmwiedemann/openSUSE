#
# spec file for package perl-GnuPG-Interface
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


Name:           perl-GnuPG-Interface
Version:        1.02
Release:        0
%define         cpan_name GnuPG-Interface
Summary:        Perl interface to GnuPG
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Math::BigInt) >= 1.78
BuildRequires:  perl(Moo) >= 0.091011
BuildRequires:  perl(MooX::HandlesVia) >= 0.001004
BuildRequires:  perl(MooX::late) >= 0.014
Requires:       perl(Math::BigInt) >= 1.78
Requires:       perl(Moo) >= 0.091011
Requires:       perl(MooX::HandlesVia) >= 0.001004
Requires:       perl(MooX::late) >= 0.014
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
%setup -q -n %{cpan_name}-%{version}
# remove tests that require an online system (OBS workers have no network)
rm t/get_public_keys.t 

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
# RT#88963
%{__make} test || :
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
