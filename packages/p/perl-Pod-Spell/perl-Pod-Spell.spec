#
# spec file for package perl-Pod-Spell
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Pod-Spell
Name:           perl-Pod-Spell
Version:        1.26
Release:        0
License:        Artistic-2.0
Summary:        Formatter for spellchecking Pod
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(Lingua::EN::Inflect)
BuildRequires:  perl(Pod::Escapes)
BuildRequires:  perl(Pod::Simple) >= 3.27
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(parent)
Requires:       perl(Class::Tiny)
Requires:       perl(File::ShareDir)
Requires:       perl(Lingua::EN::Inflect)
Requires:       perl(Pod::Escapes)
Requires:       perl(Pod::Simple) >= 3.27
Requires:       perl(parent)
%{perl_requires}

%description
Pod::Spell is a Pod formatter whose output is good for spellchecking.
Pod::Spell is rather like Pod::Text, except that it doesn't put much effort
into actual formatting, and it suppresses things that look like Perl
symbols or Perl jargon (so that your spellchecking program won't complain
about mystery words like "'$thing'" or "'Foo::Bar'" or "hashref").

This class works by filtering out words that look like Perl or any form of
computerese (like "'$thing'" or "'N>7'" or "'@{$foo}{'bar','baz'}'",
anything in C<...> or F<...> codes, anything in verbatim paragraphs (code
blocks), and anything in the stopword list. The default stopword list for a
document starts out from the stopword list defined by Pod::Wordlist, and
can be supplemented (on a per-document basis) by having '"=for stopwords"'
/ '"=for :stopwords"' region(s) in a document.

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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
