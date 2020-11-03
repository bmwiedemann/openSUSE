#
# spec file for package perl-Pod-Spell
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Pod-Spell
Version:        1.20
Release:        0
%define cpan_name Pod-Spell
Summary:        Formatter for spellchecking Pod
License:        Artistic-2.0
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOLMEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(Lingua::EN::Inflect)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::Escapes)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(parent)
Requires:       perl(Class::Tiny)
Requires:       perl(File::ShareDir)
Requires:       perl(Lingua::EN::Inflect)
Requires:       perl(Path::Tiny)
Requires:       perl(Pod::Escapes)
Requires:       perl(Pod::Parser)
Requires:       perl(parent)
%{perl_requires}

%description
Pod::Spell is a Pod formatter whose output is good for spellchecking.
Pod::Spell rather like Pod::Text, except that it doesn't put much effort
into actual formatting, and it suppresses things that look like Perl
symbols or Perl jargon (so that your spellchecking program won't complain
about mystery words like "'$thing'" or "'Foo::Bar'" or "hashref").

This class provides no new public methods. All methods of interest are
inherited from Pod::Parser (which see). The especially interesting ones are
'parse_from_filehandle' (which without arguments takes from STDIN and sends
to STDOUT) and 'parse_from_file'. But you can probably just make do with
the examples in the synopsis though.

This class works by filtering out words that look like Perl or any form of
computerese (like "'$thing'" or "'N>7'" or "'@{$foo}{'bar','baz'}'",
anything in C<...> or F<...> codes, anything in verbatim paragraphs (code
blocks), and anything in the stopword list. The default stopword list for a
document starts out from the stopword list defined by Pod::Wordlist, and
can be supplemented (on a per-document basis) by having '"=for stopwords"'
/ '"=for :stopwords"' region(s) in a document.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
