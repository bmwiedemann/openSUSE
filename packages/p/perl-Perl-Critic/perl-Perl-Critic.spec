#
# spec file for package perl-Perl-Critic
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


%define cpan_name Perl-Critic
Name:           perl-Perl-Critic
Version:        1.144
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Critique Perl source code for best-practices
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(B::Keywords) >= 1.05
BuildRequires:  perl(Config::Tiny) >= 2
BuildRequires:  perl(Exception::Class) >= 1.23
BuildRequires:  perl(Exporter) >= 5.63
BuildRequires:  perl(File::Which)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(List::SomeUtils) >= 0.55
BuildRequires:  perl(Module::Build) >= 0.420400
BuildRequires:  perl(Module::Pluggable) >= 3.1
BuildRequires:  perl(PPI) >= 1.265
BuildRequires:  perl(PPI::Document) >= 1.265
BuildRequires:  perl(PPI::Document::File) >= 1.265
BuildRequires:  perl(PPI::Node) >= 1.265
BuildRequires:  perl(PPI::Token::Quote::Single) >= 1.265
BuildRequires:  perl(PPI::Token::Whitespace) >= 1.265
BuildRequires:  perl(PPIx::QuoteLike)
BuildRequires:  perl(PPIx::Regexp) >= 0.027
BuildRequires:  perl(PPIx::Regexp::Util) >= 0.068
BuildRequires:  perl(PPIx::Utilities::Node) >= 1.001
BuildRequires:  perl(PPIx::Utilities::Statement) >= 1.001
BuildRequires:  perl(Perl::Tidy)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(Pod::PlainText)
BuildRequires:  perl(Pod::Select)
BuildRequires:  perl(Pod::Spell) >= 1
BuildRequires:  perl(Readonly) >= 2
BuildRequires:  perl(String::Format) >= 1.18
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Term::ANSIColor) >= 2.02
BuildRequires:  perl(Test::Builder) >= 0.92
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(version) >= 0.77
Requires:       perl(B::Keywords) >= 1.05
Requires:       perl(Config::Tiny) >= 2
Requires:       perl(Exception::Class) >= 1.23
Requires:       perl(Exporter) >= 5.63
Requires:       perl(File::Which)
Requires:       perl(IO::String)
Requires:       perl(List::SomeUtils) >= 0.55
Requires:       perl(Module::Pluggable) >= 3.1
Requires:       perl(PPI) >= 1.265
Requires:       perl(PPI::Document) >= 1.265
Requires:       perl(PPI::Document::File) >= 1.265
Requires:       perl(PPI::Node) >= 1.265
Requires:       perl(PPI::Token::Quote::Single) >= 1.265
Requires:       perl(PPI::Token::Whitespace) >= 1.265
Requires:       perl(PPIx::QuoteLike)
Requires:       perl(PPIx::Regexp) >= 0.027
Requires:       perl(PPIx::Regexp::Util) >= 0.068
Requires:       perl(PPIx::Utilities::Node) >= 1.001
Requires:       perl(PPIx::Utilities::Statement) >= 1.001
Requires:       perl(Perl::Tidy)
Requires:       perl(Pod::Parser)
Requires:       perl(Pod::PlainText)
Requires:       perl(Pod::Select)
Requires:       perl(Pod::Spell) >= 1
Requires:       perl(Readonly) >= 2
Requires:       perl(String::Format) >= 1.18
Requires:       perl(Task::Weaken)
Requires:       perl(Term::ANSIColor) >= 2.02
Requires:       perl(Test::Builder) >= 0.92
Requires:       perl(version) >= 0.77
%{perl_requires}

%description
Perl::Critic is an extensible framework for creating and applying coding
standards to Perl source code. Essentially, it is a static source code
analysis engine. Perl::Critic is distributed with a number of
Perl::Critic::Policy modules that attempt to enforce various coding
guidelines. Most Policy modules are based on Damian Conway's book *Perl
Best Practices*. However, Perl::Critic is *not* limited to PBP and will
even support Policies that contradict Conway. You can enable, disable, and
customize those Polices through the Perl::Critic interface. You can also
create new Policy modules that suit your own tastes.

For a command-line interface to Perl::Critic, see the documentation for
perlcritic. If you want to integrate Perl::Critic with your build process,
Test::Perl::Critic provides an interface that is suitable for test
programs. Also, Test::Perl::Critic::Progressive is useful for gradually
applying coding standards to legacy code. For the ultimate convenience (at
the expense of some flexibility) see the criticism pragma.

If you'd like to try Perl::Critic without installing anything, there is a
web-service available at http://perlcritic.com. The web-service does not
yet support all the configuration features that are available in the native
Perl::Critic API, but it should give you a good idea of what it does.

Also, ActivePerl includes a very slick graphical interface to Perl-Critic
called 'perlcritic-gui'. You can get a free community edition of ActivePerl
from http://www.activestate.com.

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
%doc Changes CONTRIBUTING.md examples README README.md
%license LICENSE

%changelog
