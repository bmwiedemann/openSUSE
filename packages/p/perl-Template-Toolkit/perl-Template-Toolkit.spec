#
# spec file for package perl-Template-Toolkit
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        3.106.0
Release:        0
# 3.106 -> normalize -> 3.106.0
%define cpan_version 3.106
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Comprehensive template processing system
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(AppConfig) >= 1.560
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.48
BuildRequires:  perl(Test::LeakTrace)
Requires:       perl(AppConfig) >= 1.560
Provides:       perl(Template) = %{version}
Provides:       perl(Template::App::ttree) = %{version}
Provides:       perl(Template::Base) = %{version}
Provides:       perl(Template::Config) = %{version}
Provides:       perl(Template::Constants) = %{version}
Provides:       perl(Template::Context) = %{version}
Provides:       perl(Template::Directive) = %{version}
Provides:       perl(Template::Document) = %{version}
Provides:       perl(Template::Exception) = %{version}
Provides:       perl(Template::Filters) = %{version}
Provides:       perl(Template::Grammar) = %{version}
Provides:       perl(Template::Iterator) = %{version}
Provides:       perl(Template::Monad::Assert)
Provides:       perl(Template::Monad::Scalar)
Provides:       perl(Template::Namespace::Constants) = %{version}
Provides:       perl(Template::Parser) = %{version}
Provides:       perl(Template::Perl)
Provides:       perl(Template::Plugin) = %{version}
Provides:       perl(Template::Plugin::Assert) = %{version}
Provides:       perl(Template::Plugin::Datafile) = %{version}
Provides:       perl(Template::Plugin::Date) = %{version}
Provides:       perl(Template::Plugin::Date::Calc)
Provides:       perl(Template::Plugin::Date::Manip)
Provides:       perl(Template::Plugin::Directory) = %{version}
Provides:       perl(Template::Plugin::Dumper) = %{version}
Provides:       perl(Template::Plugin::File) = %{version}
Provides:       perl(Template::Plugin::Filter) = %{version}
Provides:       perl(Template::Plugin::Format) = %{version}
Provides:       perl(Template::Plugin::HTML) = %{version}
Provides:       perl(Template::Plugin::Image) = %{version}
Provides:       perl(Template::Plugin::Iterator) = %{version}
Provides:       perl(Template::Plugin::List) = %{version}
Provides:       perl(Template::Plugin::Math) = %{version}
Provides:       perl(Template::Plugin::Pod) = %{version}
Provides:       perl(Template::Plugin::Procedural) = %{version}
Provides:       perl(Template::Plugin::Scalar) = %{version}
Provides:       perl(Template::Plugin::String) = %{version}
Provides:       perl(Template::Plugin::Table) = %{version}
Provides:       perl(Template::Plugin::URL) = %{version}
Provides:       perl(Template::Plugin::View) = %{version}
Provides:       perl(Template::Plugin::Wrap) = %{version}
Provides:       perl(Template::Plugins) = %{version}
Provides:       perl(Template::Provider) = %{version}
Provides:       perl(Template::Service) = %{version}
Provides:       perl(Template::Stash) = %{version}
Provides:       perl(Template::Stash::Context) = %{version}
Provides:       perl(Template::Stash::XS)
Provides:       perl(Template::Test) = %{version}
Provides:       perl(Template::TieString)
Provides:       perl(Template::Toolkit) = %{version}
Provides:       perl(Template::VMethods) = %{version}
Provides:       perl(Template::View) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
comprehensive template processing system

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc AI_POLICY.md Changes HACKING.md README.md SECURITY.md TODO

%changelog
