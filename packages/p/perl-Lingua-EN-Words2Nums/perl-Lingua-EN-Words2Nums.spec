#
# spec file for package perl-Lingua-EN-Words2Nums
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Lingua-EN-Words2Nums
Version:        0.18
Release:        0
%define cpan_name Lingua-EN-Words2Nums
Summary:        convert English text to numbers
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Lingua-EN-Words2Nums/
Source:         http://www.cpan.org/authors/id/J/JO/JOEY/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}
# MANUAL
# License: perl 

%description
This module converts English text into numbers. It supports both ordinal
and cardinal numbers, negative numbers, and very large numbers.

The main subroutine, which is exported by default, is words2nums(). This
subroutine, when fed a string, will attempt to convert it into a number. If
it succeeds, the number will be returned. If it fails, it returns undef.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

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
%doc README samples testnum TODO

%changelog
