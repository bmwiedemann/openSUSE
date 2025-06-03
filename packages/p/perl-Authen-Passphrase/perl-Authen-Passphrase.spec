#
# spec file for package perl-Authen-Passphrase
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Authen-Passphrase
Name:           perl-Authen-Passphrase
Version:        0.8.0
Release:        0
# 0.008 -> normalize -> 0.8.0
%define cpan_version 0.008
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Hashed passwords/passphrases as objects
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Authen::DecHpwd) >= 2.3
BuildRequires:  perl(Crypt::DES)
BuildRequires:  perl(Crypt::Eksblowfish::Bcrypt) >= 0.8
BuildRequires:  perl(Crypt::Eksblowfish::Uklblowfish) >= 0.8
BuildRequires:  perl(Crypt::MySQL) >= 0.30
BuildRequires:  perl(Crypt::PasswdMD5) >= 1.0.0
BuildRequires:  perl(Crypt::UnixCrypt_XS) >= 0.80
BuildRequires:  perl(Data::Entropy::Algorithms)
BuildRequires:  perl(Digest::MD4) >= 1.200
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Runtime) >= 0.11
BuildRequires:  perl(Params::Classify)
BuildRequires:  perl(parent)
Requires:       perl(Authen::DecHpwd) >= 2.3
Requires:       perl(Crypt::DES)
Requires:       perl(Crypt::Eksblowfish::Bcrypt) >= 0.8
Requires:       perl(Crypt::Eksblowfish::Uklblowfish) >= 0.8
Requires:       perl(Crypt::MySQL) >= 0.30
Requires:       perl(Crypt::PasswdMD5) >= 1.0.0
Requires:       perl(Crypt::UnixCrypt_XS) >= 0.80
Requires:       perl(Data::Entropy::Algorithms)
Requires:       perl(Digest::MD4) >= 1.200
Requires:       perl(Digest::SHA)
Requires:       perl(Module::Runtime) >= 0.11
Requires:       perl(Params::Classify)
Requires:       perl(parent)
Provides:       perl(Authen::Passphrase) = %{version}
Provides:       perl(Authen::Passphrase::AcceptAll) = %{version}
Provides:       perl(Authen::Passphrase::BigCrypt) = %{version}
Provides:       perl(Authen::Passphrase::BlowfishCrypt) = %{version}
Provides:       perl(Authen::Passphrase::Clear) = %{version}
Provides:       perl(Authen::Passphrase::Crypt16) = %{version}
Provides:       perl(Authen::Passphrase::DESCrypt) = %{version}
Provides:       perl(Authen::Passphrase::EggdropBlowfish) = %{version}
Provides:       perl(Authen::Passphrase::LANManager) = %{version}
Provides:       perl(Authen::Passphrase::LANManagerHalf) = %{version}
Provides:       perl(Authen::Passphrase::MD5Crypt) = %{version}
Provides:       perl(Authen::Passphrase::MySQL323) = %{version}
Provides:       perl(Authen::Passphrase::MySQL41) = %{version}
Provides:       perl(Authen::Passphrase::NTHash) = %{version}
Provides:       perl(Authen::Passphrase::NetscapeMail) = %{version}
Provides:       perl(Authen::Passphrase::PHPass) = %{version}
Provides:       perl(Authen::Passphrase::RejectAll) = %{version}
Provides:       perl(Authen::Passphrase::SaltedDigest) = %{version}
Provides:       perl(Authen::Passphrase::VMSPurdy) = %{version}
%undefine       __perllib_provides
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
recommended to use Authen::Passphrase::SaltedDigest or
Authen::Passphrase::BlowfishCrypt. Most other schemes are too weak for new
applications, and should be used only for backward compatibility.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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

%changelog
