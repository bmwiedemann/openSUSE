#
# spec file for package perl-Template-Toolkit
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


%define cpan_name Template-Toolkit
Name:           perl-Template-Toolkit
Version:        3.102.0
Release:        0
# 3.102 -> normalize -> 3.102.0
%define cpan_version 3.102
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Comprehensive template processing system
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(AppConfig) >= 1.56
BuildRequires:  perl(Test::LeakTrace)
Requires:       perl(AppConfig) >= 1.56
Provides:       perl(Template) = %{version}
Provides:       perl(Template::App::ttree) = 2.910.0
Provides:       perl(Template::Base) = 3.100
Provides:       perl(Template::Config) = 3.100
Provides:       perl(Template::Constants) = 3.100
Provides:       perl(Template::Context) = 3.100
Provides:       perl(Template::Directive) = 3.100
Provides:       perl(Template::Document) = 3.100
Provides:       perl(Template::Exception) = 3.100
Provides:       perl(Template::Filters) = 3.100
Provides:       perl(Template::Grammar) = 3.100
Provides:       perl(Template::Iterator) = 3.100
Provides:       perl(Template::Monad::Assert)
Provides:       perl(Template::Monad::Scalar)
Provides:       perl(Template::Namespace::Constants) = 3.100
Provides:       perl(Template::Parser) = 3.100
Provides:       perl(Template::Perl)
Provides:       perl(Template::Plugin) = 3.100
Provides:       perl(Template::Plugin::Assert) = 3.100
Provides:       perl(Template::Plugin::Datafile) = 3.100
Provides:       perl(Template::Plugin::Date) = 3.100
Provides:       perl(Template::Plugin::Date::Calc)
Provides:       perl(Template::Plugin::Date::Manip)
Provides:       perl(Template::Plugin::Directory) = 3.100
Provides:       perl(Template::Plugin::Dumper) = 3.100
Provides:       perl(Template::Plugin::File) = 3.100
Provides:       perl(Template::Plugin::Filter) = 3.100
Provides:       perl(Template::Plugin::Format) = 3.100
Provides:       perl(Template::Plugin::HTML) = 3.100
Provides:       perl(Template::Plugin::Image) = 3.100
Provides:       perl(Template::Plugin::Iterator) = 3.100
Provides:       perl(Template::Plugin::Math) = 3.100
Provides:       perl(Template::Plugin::Pod) = 3.100
Provides:       perl(Template::Plugin::Procedural) = 3.100
Provides:       perl(Template::Plugin::Scalar) = 3.100
Provides:       perl(Template::Plugin::String) = 3.100
Provides:       perl(Template::Plugin::Table) = 3.100
Provides:       perl(Template::Plugin::URL) = 3.100
Provides:       perl(Template::Plugin::View) = 3.100
Provides:       perl(Template::Plugin::Wrap) = 3.100
Provides:       perl(Template::Plugins) = 3.100
Provides:       perl(Template::Provider) = 3.100
Provides:       perl(Template::Service) = 3.100
Provides:       perl(Template::Stash) = 3.100
Provides:       perl(Template::Stash::Context) = 3.100
Provides:       perl(Template::Stash::XS)
Provides:       perl(Template::Test) = 3.100
Provides:       perl(Template::TieString)
Provides:       perl(Template::Toolkit) = 3.100
Provides:       perl(Template::VMethods) = 3.100
Provides:       perl(Template::View) = 3.100
%undefine       __perllib_provides
%{perl_requires}

%description
comprehensive template processing system

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes HACKING.md README.md TODO

%changelog
