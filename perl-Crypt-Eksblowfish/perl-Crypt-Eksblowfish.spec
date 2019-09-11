#
# spec file for package perl-Crypt-Eksblowfish
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


Name:           perl-Crypt-Eksblowfish
Version:        0.009
Release:        0
%define cpan_name Crypt-Eksblowfish
Summary:        The Eksblowfish Block Cipher
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Crypt-Eksblowfish/
Source0:        Crypt-Eksblowfish-0.009.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Mix) >= 0.001
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.15
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
Requires:       perl(Class::Mix) >= 0.001
Requires:       perl(parent)
%{perl_requires}

%description
An object of this type encapsulates a keyed instance of the Eksblowfish
block cipher, ready to encrypt and decrypt.

Eksblowfish is a variant of the Blowfish cipher, modified to make the key
setup very expensive. ("Eks" stands for "expensive key schedule".) This
doesn't make it significantly cryptographically stronger, but is intended
to hinder brute-force attacks. It also makes it unsuitable for any
application requiring key agility. It was designed by Niels Provos and
David Mazieres for password hashing in OpenBSD. See the
Crypt::Eksblowfish::Bcrypt manpage for the hash algorithm. See the
Crypt::Eksblowfish::Blowfish manpage for the unmodified Blowfish cipher.

Eksblowfish is a parameterised (family-keyed) cipher. It takes a cost
parameter that controls how expensive the key scheduling is. It also takes
a family key, known as the "salt". Cost and salt parameters together define
a cipher family. Within each family, a key determines an encryption
function in the usual way. See the Crypt::Eksblowfish::Family manpage for a
way to encapsulate an Eksblowfish cipher family.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="%{optflags}"
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
