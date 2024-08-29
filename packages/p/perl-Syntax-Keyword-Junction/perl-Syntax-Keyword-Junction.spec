#
# spec file for package perl-Syntax-Keyword-Junction
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Syntax-Keyword-Junction
Name:           perl-Syntax-Keyword-Junction
Version:        0.003009
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Comparisons against multiple values
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Sub::Exporter::Progressive) >= 0.001006
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs) >= 0.002006
BuildRequires:  perl(parent)
Requires:       perl(Sub::Exporter::Progressive) >= 0.001006
Requires:       perl(parent)
%{perl_requires}

%description
This is a lightweight module which provides 'Junction' operators, the most
commonly used being 'any' and 'all'.

Inspired by the Perl 6 design docs,
https://web.archive.org/web/20230922160729/https://raku.org/archive/doc/des
ign/exe/E06.html#The%20Wonderful%20World%20of%20Junctions.

Provides a limited subset of the functionality of Quantum::Superpositions,
see "SEE ALSO" for comment.

Notice in the SYNOPSIS above, that if you want to match against a regular
expression, you must use '==' or '!='. *Not* '=~' or '!~'. You must also
use a regex object, such as 'qr/\d/', not a plain regex such as '/\d/'.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes README
%license LICENSE

%changelog
