#
# spec file for package perl-Lingua-EN-Number-IsOrdinal
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Lingua-EN-Number-IsOrdinal
Version:        0.05
Release:        0
%define cpan_name Lingua-EN-Number-IsOrdinal
Summary:        detect if English number is ordinal or cardinal
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Lingua-EN-Number-IsOrdinal/
Source:         http://www.cpan.org/authors/id/R/RK/RKITOVER/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Lingua::EN::FindNumber)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Try::Tiny)
Requires:       perl(Lingua::EN::FindNumber)
%{perl_requires}

%description
This module will tell you if a number, either in words or as digits, is a
cardinal or the ordinal
number|http://www.ego4u.com/en/cram-up/vocabulary/numbers/ordinal manpage.

This is useful if you e.g. want to distinguish these types of numbers found
with the Lingua::EN::FindNumber manpage and take different actions.

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
