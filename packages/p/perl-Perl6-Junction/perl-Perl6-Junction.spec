#
# spec file for package perl-Perl6-Junction
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


Name:           perl-Perl6-Junction
Version:        1.60000
Release:        0
%define cpan_name Perl6-Junction
Summary:        Perl6 style Junction operators in Perl5.
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Perl6-Junction/
Source:         http://www.cpan.org/authors/id/C/CF/CFRANKS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires: perl(Perl6::Junction)
#BuildRequires: perl(Perl6::Junction::All)
#BuildRequires: perl(Perl6::Junction::Any)
#BuildRequires: perl(Perl6::Junction::Base)
#BuildRequires: perl(Perl6::Junction::None)
#BuildRequires: perl(Perl6::Junction::One)
%{perl_requires}

%description
This is a lightweight module which provides 'Junction' operators, the most
commonly used being 'any' and 'all'.

Inspired by the Perl6 design docs, the
http://dev.perl.org/perl6/doc/design/exe/E06.html manpage.

Provides a limited subset of the functionality of the
Quantum::Superpositions manpage, see the /"SEE ALSO" manpage for comment.

Notice in the the /SYNOPSIS manpage above, that if you want to match
against a regular expression, you must use '==' or '!='. *Not* '=~' or
'!~'. You must also use a regex object, such as 'qr/\d/', not a plain regex
such as '/\d/'.

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
%doc Changes MYMETA.json MYMETA.yml README

%changelog
