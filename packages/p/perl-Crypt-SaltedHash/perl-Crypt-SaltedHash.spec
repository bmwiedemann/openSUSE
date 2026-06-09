#
# spec file for package perl-Crypt-SaltedHash
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


%define cpan_name Crypt-SaltedHash
Name:           perl-Crypt-SaltedHash
Version:        0.120.0
Release:        0
# 0.12 -> normalize -> 0.120.0
%define cpan_version 0.12
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl interface to functions that assist in working with salted hashes
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRWO/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Crypt::SysRandom)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Test::Fatal)
Requires:       perl(Crypt::SysRandom)
Provides:       perl(Crypt::SaltedHash) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The 'Crypt::SaltedHash' module provides an object oriented interface to
create salted (or seeded) hashes of clear text data. The original
formalization of this concept comes from RFC-3112 and is extended by the
use of different digital algorithms.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes doap.xml README
%license LICENSE

%changelog
