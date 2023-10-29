#
# spec file for package perl-MooseX-App
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


%define cpan_name MooseX-App
Name:           perl-MooseX-App
Version:        1.430.0
Release:        0
%define cpan_version 1.43
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Write user-friendly command line apps with even less suffering
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAROS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(List::Util) >= 1.44
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Moose) >= 2.00
BuildRequires:  perl(Pod::Elemental)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(Config::Any)
Requires:       perl(List::Util) >= 1.44
Requires:       perl(Module::Pluggable)
Requires:       perl(Moose) >= 2.00
Requires:       perl(Pod::Elemental)
Requires:       perl(namespace::autoclean)
Provides:       perl(Moose::Meta::Attribute::Custom::Trait::AppDepends)
Provides:       perl(Moose::Meta::Attribute::Custom::Trait::AppMutexGroup)
Provides:       perl(Moose::Meta::Attribute::Custom::Trait::AppOption)
Provides:       perl(Moose::Meta::Attribute::Custom::Trait::AppTerm)
Provides:       perl(MooseX::App) = 1.430.0
Provides:       perl(MooseX::App::Command)
Provides:       perl(MooseX::App::Exporter)
Provides:       perl(MooseX::App::Message::Block)
Provides:       perl(MooseX::App::Message::BlockColor)
Provides:       perl(MooseX::App::Message::Envelope)
Provides:       perl(MooseX::App::Meta::Role::Attribute::Option)
Provides:       perl(MooseX::App::Meta::Role::Class::Base)
Provides:       perl(MooseX::App::Meta::Role::Class::Command)
Provides:       perl(MooseX::App::Meta::Role::Class::Documentation)
Provides:       perl(MooseX::App::Meta::Role::Class::Simple)
Provides:       perl(MooseX::App::Null)
Provides:       perl(MooseX::App::ParsedArgv)
Provides:       perl(MooseX::App::ParsedArgv::Element)
Provides:       perl(MooseX::App::ParsedArgv::Value)
Provides:       perl(MooseX::App::Plugin::BashCompletion)
Provides:       perl(MooseX::App::Plugin::BashCompletion::Command)
Provides:       perl(MooseX::App::Plugin::BashCompletion::Meta::Class)
Provides:       perl(MooseX::App::Plugin::Color)
Provides:       perl(MooseX::App::Plugin::Color::Meta::Class)
Provides:       perl(MooseX::App::Plugin::Config)
Provides:       perl(MooseX::App::Plugin::Config::Meta::Class)
Provides:       perl(MooseX::App::Plugin::ConfigHome)
Provides:       perl(MooseX::App::Plugin::ConfigHome::Meta::Class)
Provides:       perl(MooseX::App::Plugin::Depends)
Provides:       perl(MooseX::App::Plugin::Depends::Meta::Attribute)
Provides:       perl(MooseX::App::Plugin::Depends::Meta::Class)
Provides:       perl(MooseX::App::Plugin::Env)
Provides:       perl(MooseX::App::Plugin::Fuzzy)
Provides:       perl(MooseX::App::Plugin::Man)
Provides:       perl(MooseX::App::Plugin::Man::Command)
Provides:       perl(MooseX::App::Plugin::Man::Meta::Class)
Provides:       perl(MooseX::App::Plugin::MutexGroup)
Provides:       perl(MooseX::App::Plugin::MutexGroup::Meta::Attribute)
Provides:       perl(MooseX::App::Plugin::MutexGroup::Meta::Class)
Provides:       perl(MooseX::App::Plugin::Term)
Provides:       perl(MooseX::App::Plugin::Term::Meta::Attribute)
Provides:       perl(MooseX::App::Plugin::Term::Meta::Class)
Provides:       perl(MooseX::App::Plugin::Typo)
Provides:       perl(MooseX::App::Plugin::Typo::Meta::Class)
Provides:       perl(MooseX::App::Plugin::Version)
Provides:       perl(MooseX::App::Plugin::Version::Command)
Provides:       perl(MooseX::App::Plugin::Version::Meta::Class)
Provides:       perl(MooseX::App::Role)
Provides:       perl(MooseX::App::Role::Base)
Provides:       perl(MooseX::App::Role::Common)
Provides:       perl(MooseX::App::Simple) = 1.42
Provides:       perl(MooseX::App::Utils)
%define         __perllib_provides /bin/true
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(Config::Any)
# MANUAL END

%description
MooseX-App is a highly customisable helper to write user-friendly command
line applications without having to worry about most of the annoying things
usually involved. Just take any existing Moose class, add a single line
('use MooseX-App qw(PluginA PluginB ...);') and create one class for each
command in an underlying namespace. Options and positional parameters can
be defined as simple Moose accessors using the 'option' and 'parameter'
keywords respectively.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes README.md TODO
%license LICENSE

%changelog
