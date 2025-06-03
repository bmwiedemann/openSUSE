#
# spec file for package perl-Crypt-Eksblowfish
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


%define cpan_name Crypt-Eksblowfish
Name:           perl-Crypt-Eksblowfish
Version:        0.9.0
Release:        0
# 0.009 -> normalize -> 0.9.0
%define cpan_version 0.009
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        The Eksblowfish block cipher
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/%{cpan_name}-%{cpan_version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Mix) >= 0.1
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.15
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
Requires:       perl(Class::Mix) >= 0.1
Requires:       perl(parent)
Provides:       perl(Crypt::Eksblowfish) = %{version}
Provides:       perl(Crypt::Eksblowfish::Bcrypt) = %{version}
Provides:       perl(Crypt::Eksblowfish::Blowfish) = %{version}
Provides:       perl(Crypt::Eksblowfish::Family) = %{version}
Provides:       perl(Crypt::Eksblowfish::Subkeyed) = %{version}
Provides:       perl(Crypt::Eksblowfish::Uklblowfish) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
An object of this type encapsulates a keyed instance of the Eksblowfish
block cipher, ready to encrypt and decrypt.

Eksblowfish is a variant of the Blowfish cipher, modified to make the key
setup very expensive. ("Eks" stands for "expensive key schedule".) This
doesn't make it significantly cryptographically stronger, but is intended
to hinder brute-force attacks. It also makes it unsuitable for any
application requiring key agility. It was designed by Niels Provos and
David Mazieres for password hashing in OpenBSD. See
Crypt::Eksblowfish::Bcrypt for the hash algorithm. See
Crypt::Eksblowfish::Blowfish for the unmodified Blowfish cipher.

Eksblowfish is a parameterised (family-keyed) cipher. It takes a cost
parameter that controls how expensive the key scheduling is. It also takes
a family key, known as the "salt". Cost and salt parameters together define
a cipher family. Within each family, a key determines an encryption
function in the usual way. See Crypt::Eksblowfish::Family for a way to
encapsulate an Eksblowfish cipher family.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor optimize="%{optflags}"
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
