#
# spec file for package perl-String-ToIdentifier-EN
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


Name:           perl-String-ToIdentifier-EN
Version:        0.12
Release:        0
%define cpan_name String-ToIdentifier-EN
Summary:        Convert Strings to English Program Identifiers
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/String-ToIdentifier-EN/
Source0:        https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Lingua::EN::Inflect::Phrase)
BuildRequires:  perl(Text::Unidecode)
BuildRequires:  perl(namespace::clean)
Requires:       perl(Lingua::EN::Inflect::Phrase)
Requires:       perl(Text::Unidecode)
Requires:       perl(namespace::clean)
%{perl_requires}

%description
This module provides a utility method, to_identifier for converting an
arbitrary string into a readable representation using the ASCII subset of
'\w' for use as an identifier in a computer program. The intent is to make
unique identifier names from which the content of the original string can
be easily inferred by a human just by reading the identifier.

If you need the full set of '\w' including Unicode, see the subclass
String::ToIdentifier::EN::Unicode.

Currently, this process is one way only, and will likely remain this way.

The default is to create camelCase identifiers, or you may pass in a
separator char of your choice such as '_'.

Binary char groups will be separated by '_' even in camelCase identifiers
to make them easier to read, e.g.: 'foo_2_0xFF_Bar'.

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
