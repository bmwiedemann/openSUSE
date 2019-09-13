#
# spec file for package perl-Crypt-SaltedHash
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


Name:           perl-Crypt-SaltedHash
Version:        0.09
Release:        0
%define cpan_name Crypt-SaltedHash
Summary:        Perl interface to functions that assist in working
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Crypt-SaltedHash/
Source:         http://www.cpan.org/authors/id/G/GS/GSHANK/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Fatal)
#BuildRequires: perl(Crypt::SaltedHash)
%{perl_requires}

%description
The 'Crypt::SaltedHash' module provides an object oriented interface to
create salted (or seeded) hashes of clear text data. The original
formalization of this concept comes from RFC-3112 and is extended by the
use of different digital agorithms.

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
%doc Changes LICENSE README

%changelog
