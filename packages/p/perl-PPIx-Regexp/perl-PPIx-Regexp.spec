#
# spec file for package perl-PPIx-Regexp
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name PPIx-Regexp
Name:           perl-PPIx-Regexp
Version:        0.086
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Parse regular expressions
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/W/WY/WYANT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.420000
BuildRequires:  perl(PPI::Document) >= 1.238
BuildRequires:  perl(PPI::Dumper) >= 1.238
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(PPI::Document) >= 1.238
Requires:       perl(PPI::Dumper) >= 1.238
Requires:       perl(Task::Weaken)
%{perl_requires}

%description
The purpose of the _PPIx-Regexp_ package is to parse regular expressions in
a manner similar to the way the PPI package parses Perl. This class forms
the root of the parse tree, playing a role similar to PPI::Document.

This package shares with PPI the property of being round-trip safe. That
is,

 my $expr = 's/ ( \d+ ) ( \D+ ) /$2$1/smxg';
 my $re = PPIx::Regexp->new( $expr );
 print $re->content() eq $expr ? "yes\n" : "no\n"

should print 'yes' for any valid regular expression.

Navigation is similar to that provided by PPI. That is to say, things like
'children', 'find_first', 'snext_sibling' and so on all work pretty much
the same way as in PPI.

The class hierarchy is also similar to PPI. Except for some utility classes
(the dumper, the lexer, and the tokenizer) all classes are descended from
PPIx::Regexp::Element, which provides basic navigation. Tokens are
descended from PPIx::Regexp::Token, which provides content. All containers
are descended from PPIx::Regexp::Node, which provides for children, and all
structure elements are descended from PPIx::Regexp::Structure, which
provides beginning and ending delimiters, and a type.

There are two features of PPI that this package does not provide -
mutability and operator overloading. There are no plans for serious
mutability, though something like PPI's 'prune' functionality might be
considered. Similarly there are no plans for operator overloading, which
appears to the author to represent a performance hit for little tangible
gain.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING README

%changelog
