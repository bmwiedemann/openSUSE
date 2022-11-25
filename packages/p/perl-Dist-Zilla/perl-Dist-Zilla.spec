#
# spec file for package perl-Dist-Zilla
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


%define cpan_name Dist-Zilla
Name:           perl-Dist-Zilla
Version:        6.028
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Distribution builder; installer not included!
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(App::Cmd::Command::version)
BuildRequires:  perl(App::Cmd::Setup) >= 0.330
BuildRequires:  perl(App::Cmd::Tester) >= 0.306
BuildRequires:  perl(App::Cmd::Tester::CaptureExternal)
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Converter) >= 2.101550
BuildRequires:  perl(CPAN::Meta::Merge)
BuildRequires:  perl(CPAN::Meta::Prereqs) >= 2.120630
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121000
BuildRequires:  perl(CPAN::Meta::Validator) >= 2.101550
BuildRequires:  perl(CPAN::Uploader) >= 0.103004
BuildRequires:  perl(Config::INI::Reader)
BuildRequires:  perl(Config::MVP) >= 2.200011
BuildRequires:  perl(Config::MVP::Assembler)
BuildRequires:  perl(Config::MVP::Assembler::WithBundles) >= 2.200010
BuildRequires:  perl(Config::MVP::Reader) >= 2.101540
BuildRequires:  perl(Config::MVP::Reader::Findable::ByExtension)
BuildRequires:  perl(Config::MVP::Reader::Finder)
BuildRequires:  perl(Config::MVP::Reader::INI) >= 2.101461
BuildRequires:  perl(Config::MVP::Section) >= 2.200009
BuildRequires:  perl(Data::Section) >= 0.200002
BuildRequires:  perl(DateTime) >= 0.44
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(ExtUtils::Manifest) >= 1.66
BuildRequires:  perl(File::Copy::Recursive) >= 0.41
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Log::Dispatchouli) >= 1.102220
BuildRequires:  perl(Mixin::Linewise::Readers) >= 0.100
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose) >= 0.92
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::LazyRequire)
BuildRequires:  perl(MooseX::Role::Parameterized) >= 1.01
BuildRequires:  perl(MooseX::SetOnce)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::Perl)
BuildRequires:  perl(PPI::Document) >= 1.222
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Path::Tiny) >= 0.052
BuildRequires:  perl(Perl::PrereqScanner) >= 1.016
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Software::License) >= 0.104001
BuildRequires:  perl(Software::License::None)
BuildRequires:  perl(Software::LicenseUtils)
BuildRequires:  perl(String::Formatter) >= 0.100680
BuildRequires:  perl(String::RewritePrefix) >= 0.006
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::ForMethods)
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(Term::ANSIColor) >= 5.00
BuildRequires:  perl(Term::Encoding)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Term::UI)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::File::ShareDir)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Text::Glob) >= 0.08
BuildRequires:  perl(Text::Template)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(YAML::Tiny)
BuildRequires:  perl(autodie)
BuildRequires:  perl(experimental)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(parent)
BuildRequires:  perl(version)
Requires:       perl(App::Cmd::Command::version)
Requires:       perl(App::Cmd::Setup) >= 0.330
Requires:       perl(App::Cmd::Tester) >= 0.306
Requires:       perl(App::Cmd::Tester::CaptureExternal)
Requires:       perl(Archive::Tar)
Requires:       perl(CPAN::Meta::Converter) >= 2.101550
Requires:       perl(CPAN::Meta::Merge)
Requires:       perl(CPAN::Meta::Prereqs) >= 2.120630
Requires:       perl(CPAN::Meta::Requirements) >= 2.121000
Requires:       perl(CPAN::Meta::Validator) >= 2.101550
Requires:       perl(CPAN::Uploader) >= 0.103004
Requires:       perl(Config::INI::Reader)
Requires:       perl(Config::MVP) >= 2.200011
Requires:       perl(Config::MVP::Assembler)
Requires:       perl(Config::MVP::Assembler::WithBundles) >= 2.200010
Requires:       perl(Config::MVP::Reader) >= 2.101540
Requires:       perl(Config::MVP::Reader::Findable::ByExtension)
Requires:       perl(Config::MVP::Reader::Finder)
Requires:       perl(Config::MVP::Reader::INI) >= 2.101461
Requires:       perl(Config::MVP::Section) >= 2.200009
Requires:       perl(Data::Section) >= 0.200002
Requires:       perl(DateTime) >= 0.44
Requires:       perl(ExtUtils::Manifest) >= 1.66
Requires:       perl(File::Copy::Recursive) >= 0.41
Requires:       perl(File::Find::Rule)
Requires:       perl(File::ShareDir)
Requires:       perl(File::ShareDir::Install) >= 0.03
Requires:       perl(File::pushd)
Requires:       perl(JSON::MaybeXS)
Requires:       perl(List::Util) >= 1.45
Requires:       perl(Log::Dispatchouli) >= 1.102220
Requires:       perl(Mixin::Linewise::Readers) >= 0.100
Requires:       perl(Module::CoreList)
Requires:       perl(Module::Runtime)
Requires:       perl(Moose) >= 0.92
Requires:       perl(Moose::Role)
Requires:       perl(Moose::Util::TypeConstraints)
Requires:       perl(MooseX::LazyRequire)
Requires:       perl(MooseX::Role::Parameterized) >= 1.01
Requires:       perl(MooseX::SetOnce)
Requires:       perl(MooseX::Types)
Requires:       perl(MooseX::Types::Moose)
Requires:       perl(MooseX::Types::Perl)
Requires:       perl(PPI::Document) >= 1.222
Requires:       perl(Params::Util)
Requires:       perl(Path::Tiny) >= 0.052
Requires:       perl(Perl::PrereqScanner) >= 1.016
Requires:       perl(Pod::Simple)
Requires:       perl(Software::License) >= 0.104001
Requires:       perl(Software::LicenseUtils)
Requires:       perl(String::Formatter) >= 0.100680
Requires:       perl(String::RewritePrefix) >= 0.006
Requires:       perl(Sub::Exporter)
Requires:       perl(Sub::Exporter::ForMethods)
Requires:       perl(Sub::Exporter::Util)
Requires:       perl(Term::ANSIColor) >= 5.00
Requires:       perl(Term::Encoding)
Requires:       perl(Term::ReadKey)
Requires:       perl(Term::UI)
Requires:       perl(Test::Deep)
Requires:       perl(Text::Glob) >= 0.08
Requires:       perl(Text::Template)
Requires:       perl(Try::Tiny)
Requires:       perl(YAML::Tiny)
Requires:       perl(autodie)
Requires:       perl(experimental)
Requires:       perl(namespace::autoclean)
Requires:       perl(parent)
Requires:       perl(version)
Recommends:     perl(App::cpanminus)
Recommends:     perl(Archive::Tar::Wrapper) >= 0.15
Recommends:     perl(Data::OptList) >= 0.110
Recommends:     perl(Term::ReadLine::Gnu)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  timezone
# MANUAL END

%description
Dist::Zilla builds distributions of code to be uploaded to the CPAN. In
this respect, it is like ExtUtils::MakeMaker, Module::Build, or
Module::Install. Unlike those tools, however, it is not also a system for
installing code that has been downloaded from the CPAN. Since it's only run
by authors, and is meant to be run on a repository checkout rather than on
published, released code, it can do much more than those tools, and is free
to make much more ludicrous demands in terms of prerequisites.

If you have access to the web, you can learn more and find an interactive
tutorial at *at http://dzil.org/*. If not, try Dist::Zilla::Tutorial.

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
