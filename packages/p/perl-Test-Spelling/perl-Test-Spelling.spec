#
# spec file for package perl-Test-Spelling
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Test-Spelling
Version:        0.25
Release:        0
%define cpan_name Test-Spelling
Summary:        Check for spelling errors in POD files
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Pod::Spell)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Tester)
Requires:       perl(IPC::Run3)
Requires:       perl(Pod::Spell)
%{perl_requires}

%description
Test::Spelling lets you check the spelling of a 'POD' file, and report its
results in standard Test::More fashion. This module requires a spellcheck
program such as at http://hunspell.github.io/, _aspell_, _spell_, or,
_ispell_. We suggest using Hunspell.

    use Test::Spelling;
    pod_file_spelling_ok('lib/Foo/Bar.pm', 'POD file spelling OK');

Note that it is a bad idea to run spelling tests during an ordinary CPAN
distribution install, or in a package that will run in an uncontrolled
environment. There is no way of predicting whether the word list or
spellcheck program used will give the same results. You *can* include the
test in your distribution, but be sure to run it only for authors of the
module by guarding it in a 'skip_all unless $ENV{AUTHOR_TESTING}' clause,
or by putting the test in your distribution's _xt/author_ directory.
Anyway, people installing your module really do not need to run such tests,
as it is unlikely that the documentation will acquire typos while in
transit.

You can add your own stop words, which are words that should be ignored by
the spell check, like so:

    add_stopwords(qw(asdf thiswordiscorrect));

Adding stop words in this fashion affects all files checked for the
remainder of the test script. See Pod::Spell (which this module is built
upon) for a variety of ways to add per-file stop words to each .pm file.

If you have a lot of stop words, it's useful to put them in your test
file's 'DATA' section like so:

    use strict;
    use warnings;
    use Test::More;

    use Test::Spelling;
    use Pod::Wordlist;

    add_stopwords(<DATA>);
    all_pod_files_spelling_ok();

    __DATA__
    folksonomy
    Jifty
    Zakirov

To maintain backwards compatibility, comment markers and some whitespace
are ignored. In the near future, the preprocessing we do on the arguments
to Test::Spelling/"add_stopwords" will be changed and documented properly.

%prep
%setup -q -n %{cpan_name}-%{version}
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

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
%doc Changes README
%license LICENSE

%changelog
