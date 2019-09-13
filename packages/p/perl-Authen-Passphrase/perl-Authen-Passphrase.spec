#
# spec file for package perl-Authen-Passphrase
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Authen-Passphrase
Version:        0.008
Release:        0
%define cpan_name Authen-Passphrase
Summary:        Hashed Passwords/Passphrases As Objects
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Authen-Passphrase/
Source0:        Authen-Passphrase-0.008.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Authen::DecHpwd) >= 2.003
BuildRequires:  perl(Crypt::DES)
BuildRequires:  perl(Crypt::Eksblowfish::Bcrypt) >= 0.008
BuildRequires:  perl(Crypt::Eksblowfish::Uklblowfish) >= 0.008
BuildRequires:  perl(Crypt::MySQL) >= 0.03
BuildRequires:  perl(Crypt::PasswdMD5) >= 1.0
BuildRequires:  perl(Crypt::UnixCrypt_XS) >= 0.08
BuildRequires:  perl(Data::Entropy::Algorithms)
BuildRequires:  perl(Digest::MD4) >= 1.2
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Runtime) >= 0.011
BuildRequires:  perl(Params::Classify)
BuildRequires:  perl(parent)
Requires:       perl(Authen::DecHpwd) >= 2.003
Requires:       perl(Crypt::DES)
Requires:       perl(Crypt::Eksblowfish::Bcrypt) >= 0.008
Requires:       perl(Crypt::Eksblowfish::Uklblowfish) >= 0.008
Requires:       perl(Crypt::MySQL) >= 0.03
Requires:       perl(Crypt::PasswdMD5) >= 1.0
Requires:       perl(Crypt::UnixCrypt_XS) >= 0.08
Requires:       perl(Data::Entropy::Algorithms)
Requires:       perl(Digest::MD4) >= 1.2
Requires:       perl(Digest::SHA)
Requires:       perl(Module::Runtime) >= 0.011
Requires:       perl(Params::Classify)
Requires:       perl(parent)
%{perl_requires}

%description
This is the base class for a system of objects that encapsulate
passphrases. An object of this type is a passphrase recogniser: its job is
to recognise whether an offered passphrase is the right one. For security,
such passphrase recognisers usually do not themselves know the passphrase
they are looking for; they can merely recognise it when they see it. There
are many schemes in use to achieve this effect, and the intent of this
class is to provide a consistent interface to them all, hiding the details.

The CPAN package Authen-Passphrase contains implementations of several
specific passphrase schemes in addition to the base class. See the specific
classes for notes on the security properties of each scheme. In new
systems, if there is a choice of which passphrase algorithm to use, it is
recommended to use the Authen::Passphrase::SaltedDigest manpage or the
Authen::Passphrase::BlowfishCrypt manpage. Most other schemes are too weak
for new applications, and should be used only for backward compatibility.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
