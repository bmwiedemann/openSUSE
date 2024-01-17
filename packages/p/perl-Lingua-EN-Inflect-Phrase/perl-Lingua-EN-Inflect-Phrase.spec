#
# spec file for package perl-Lingua-EN-Inflect-Phrase
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Lingua-EN-Inflect-Phrase
Version:        0.20
Release:        0
%define cpan_name Lingua-EN-Inflect-Phrase
Summary:        Inflect short English Phrases
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Lingua-EN-Inflect-Phrase/
Source0:        https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Lingua::EN::FindNumber)
BuildRequires:  perl(Lingua::EN::Inflect)
BuildRequires:  perl(Lingua::EN::Inflect::Number)
BuildRequires:  perl(Lingua::EN::Number::IsOrdinal)
BuildRequires:  perl(Lingua::EN::Tagger)
BuildRequires:  perl(Test::NoWarnings)
Requires:       perl(Lingua::EN::FindNumber)
Requires:       perl(Lingua::EN::Inflect)
Requires:       perl(Lingua::EN::Inflect::Number)
Requires:       perl(Lingua::EN::Number::IsOrdinal)
Requires:       perl(Lingua::EN::Tagger)
%{perl_requires}

%description
Attempts to pluralize or singularize short English phrases.

Does not throw exceptions at present, if you attempt to pluralize an
already pluralized phrase, it will leave it unchanged (and vice versa.)

The behavior of this module is subject to change as I tweak the heuristics,
as some things get fixed others might regress. The processing of natural
language is a messy business.

If it doesn't work, please email or submit to RT the example you tried, and
I'll try to fix it.

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
%doc Changes README
%license LICENSE

%changelog
