#
# spec file for package perl-Dist-Zilla
#
# Copyright (c) 2025 SUSE LLC
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
Version:        6.33.0
Release:        0
# 6.033 -> normalize -> 6.33.0
%define cpan_version 6.033
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Distribution builder; installer not included!
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(App::Cmd::Command::version)
BuildRequires:  perl(App::Cmd::Setup) >= 0.330
BuildRequires:  perl(App::Cmd::Tester) >= 0.306
BuildRequires:  perl(App::Cmd::Tester::CaptureExternal)
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(CPAN::Meta::Check) >= 0.11
BuildRequires:  perl(CPAN::Meta::Converter) >= 2.101550
BuildRequires:  perl(CPAN::Meta::Merge)
BuildRequires:  perl(CPAN::Meta::Prereqs) >= 2.120630
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:  perl(CPAN::Meta::Validator) >= 2.101550
BuildRequires:  perl(CPAN::Uploader) >= 0.103.4
BuildRequires:  perl(Config::INI::Reader)
BuildRequires:  perl(Config::MVP) >= 2.200.11
BuildRequires:  perl(Config::MVP::Assembler)
BuildRequires:  perl(Config::MVP::Assembler::WithBundles) >= 2.200.10
BuildRequires:  perl(Config::MVP::Reader) >= 2.101.540
BuildRequires:  perl(Config::MVP::Reader::Findable::ByExtension)
BuildRequires:  perl(Config::MVP::Reader::Finder)
BuildRequires:  perl(Config::MVP::Reader::INI) >= 2.101.461
BuildRequires:  perl(Config::MVP::Section) >= 2.200.9
BuildRequires:  perl(Data::Section) >= 0.200.2
BuildRequires:  perl(DateTime) >= 0.440
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(ExtUtils::Manifest) >= 1.66
BuildRequires:  perl(File::Copy::Recursive) >= 0.410
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install) >= 0.60
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Log::Dispatchouli) >= 1.102.220
BuildRequires:  perl(Mixin::Linewise::Readers) >= 0.100
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose) >= 0.920
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::LazyRequire)
BuildRequires:  perl(MooseX::Role::Parameterized) >= 1.10
BuildRequires:  perl(MooseX::SetOnce)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::Perl)
BuildRequires:  perl(PPI::Document) >= 1.222
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Path::Tiny) >= 0.52
BuildRequires:  perl(Perl::PrereqScanner) >= 1.16
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Software::License) >= 0.104.1
BuildRequires:  perl(Software::License::None)
BuildRequires:  perl(Software::LicenseUtils)
BuildRequires:  perl(String::Formatter) >= 0.100.680
BuildRequires:  perl(String::RewritePrefix) >= 0.6
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
BuildRequires:  perl(Text::Glob) >= 0.80
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
Requires:       perl(CPAN::Meta::Requirements) >= 2.121
Requires:       perl(CPAN::Meta::Validator) >= 2.101550
Requires:       perl(CPAN::Uploader) >= 0.103.4
Requires:       perl(Config::INI::Reader)
Requires:       perl(Config::MVP) >= 2.200.11
Requires:       perl(Config::MVP::Assembler)
Requires:       perl(Config::MVP::Assembler::WithBundles) >= 2.200.10
Requires:       perl(Config::MVP::Reader) >= 2.101.540
Requires:       perl(Config::MVP::Reader::Findable::ByExtension)
Requires:       perl(Config::MVP::Reader::Finder)
Requires:       perl(Config::MVP::Reader::INI) >= 2.101.461
Requires:       perl(Config::MVP::Section) >= 2.200.9
Requires:       perl(Data::Section) >= 0.200.2
Requires:       perl(DateTime) >= 0.440
Requires:       perl(ExtUtils::Manifest) >= 1.66
Requires:       perl(File::Copy::Recursive) >= 0.410
Requires:       perl(File::Find::Rule)
Requires:       perl(File::ShareDir)
Requires:       perl(File::ShareDir::Install) >= 0.30
Requires:       perl(File::pushd)
Requires:       perl(JSON::MaybeXS)
Requires:       perl(List::Util) >= 1.45
Requires:       perl(Log::Dispatchouli) >= 1.102.220
Requires:       perl(Mixin::Linewise::Readers) >= 0.100
Requires:       perl(Module::CoreList)
Requires:       perl(Module::Runtime)
Requires:       perl(Moose) >= 0.920
Requires:       perl(Moose::Role)
Requires:       perl(Moose::Util::TypeConstraints)
Requires:       perl(MooseX::LazyRequire)
Requires:       perl(MooseX::Role::Parameterized) >= 1.10
Requires:       perl(MooseX::SetOnce)
Requires:       perl(MooseX::Types)
Requires:       perl(MooseX::Types::Moose)
Requires:       perl(MooseX::Types::Perl)
Requires:       perl(PPI::Document) >= 1.222
Requires:       perl(Params::Util)
Requires:       perl(Path::Tiny) >= 0.52
Requires:       perl(Perl::PrereqScanner) >= 1.16
Requires:       perl(Pod::Simple)
Requires:       perl(Software::License) >= 0.104.1
Requires:       perl(Software::LicenseUtils)
Requires:       perl(String::Formatter) >= 0.100.680
Requires:       perl(String::RewritePrefix) >= 0.6
Requires:       perl(Sub::Exporter)
Requires:       perl(Sub::Exporter::ForMethods)
Requires:       perl(Sub::Exporter::Util)
Requires:       perl(Term::ANSIColor) >= 5.00
Requires:       perl(Term::Encoding)
Requires:       perl(Term::ReadKey)
Requires:       perl(Term::UI)
Requires:       perl(Test::Deep)
Requires:       perl(Text::Glob) >= 0.80
Requires:       perl(Text::Template)
Requires:       perl(Try::Tiny)
Requires:       perl(YAML::Tiny)
Requires:       perl(autodie)
Requires:       perl(experimental)
Requires:       perl(namespace::autoclean)
Requires:       perl(parent)
Requires:       perl(version)
Provides:       perl(Dist::Zilla) = %{version}
Provides:       perl(Dist::Zilla::App) = %{version}
Provides:       perl(Dist::Zilla::App::Command) = %{version}
Provides:       perl(Dist::Zilla::App::Command::add) = %{version}
Provides:       perl(Dist::Zilla::App::Command::authordeps) = %{version}
Provides:       perl(Dist::Zilla::App::Command::build) = %{version}
Provides:       perl(Dist::Zilla::App::Command::clean) = %{version}
Provides:       perl(Dist::Zilla::App::Command::install) = %{version}
Provides:       perl(Dist::Zilla::App::Command::listdeps) = %{version}
Provides:       perl(Dist::Zilla::App::Command::new) = %{version}
Provides:       perl(Dist::Zilla::App::Command::nop) = %{version}
Provides:       perl(Dist::Zilla::App::Command::release) = %{version}
Provides:       perl(Dist::Zilla::App::Command::run) = %{version}
Provides:       perl(Dist::Zilla::App::Command::setup) = %{version}
Provides:       perl(Dist::Zilla::App::Command::smoke) = %{version}
Provides:       perl(Dist::Zilla::App::Command::test) = %{version}
Provides:       perl(Dist::Zilla::App::Command::version) = %{version}
Provides:       perl(Dist::Zilla::App::Tester) = %{version}
Provides:       perl(Dist::Zilla::Chrome::Term) = %{version}
Provides:       perl(Dist::Zilla::Chrome::Test) = %{version}
Provides:       perl(Dist::Zilla::Dist::Builder) = %{version}
Provides:       perl(Dist::Zilla::Dist::Minter) = %{version}
Provides:       perl(Dist::Zilla::File::FromCode) = %{version}
Provides:       perl(Dist::Zilla::File::InMemory) = %{version}
Provides:       perl(Dist::Zilla::File::OnDisk) = %{version}
Provides:       perl(Dist::Zilla::MVP::Assembler) = %{version}
Provides:       perl(Dist::Zilla::MVP::Assembler::GlobalConfig) = %{version}
Provides:       perl(Dist::Zilla::MVP::Assembler::Zilla) = %{version}
Provides:       perl(Dist::Zilla::MVP::Reader::Finder) = %{version}
Provides:       perl(Dist::Zilla::MVP::Reader::Perl) = %{version}
Provides:       perl(Dist::Zilla::MVP::RootSection) = %{version}
Provides:       perl(Dist::Zilla::MVP::Section) = %{version}
Provides:       perl(Dist::Zilla::MintingProfile::Default) = %{version}
Provides:       perl(Dist::Zilla::Path) = %{version}
Provides:       perl(Dist::Zilla::Plugin::AutoPrereqs) = %{version}
Provides:       perl(Dist::Zilla::Plugin::AutoVersion) = %{version}
Provides:       perl(Dist::Zilla::Plugin::BrokenPlugin)
Provides:       perl(Dist::Zilla::Plugin::CPANFile) = %{version}
Provides:       perl(Dist::Zilla::Plugin::ConfirmRelease) = %{version}
Provides:       perl(Dist::Zilla::Plugin::DistINI) = %{version}
Provides:       perl(Dist::Zilla::Plugin::Encoding) = %{version}
Provides:       perl(Dist::Zilla::Plugin::ExecDir) = %{version}
Provides:       perl(Dist::Zilla::Plugin::ExtraTests) = %{version}
Provides:       perl(Dist::Zilla::Plugin::FakeRelease) = %{version}
Provides:       perl(Dist::Zilla::Plugin::FileFinder::ByName) = %{version}
Provides:       perl(Dist::Zilla::Plugin::FileFinder::Filter) = %{version}
Provides:       perl(Dist::Zilla::Plugin::FinderCode) = %{version}
Provides:       perl(Dist::Zilla::Plugin::GatherDir) = %{version}
Provides:       perl(Dist::Zilla::Plugin::GatherDir::Template) = %{version}
Provides:       perl(Dist::Zilla::Plugin::GatherFile) = %{version}
Provides:       perl(Dist::Zilla::Plugin::GenerateFile) = %{version}
Provides:       perl(Dist::Zilla::Plugin::InlineFiles) = %{version}
Provides:       perl(Dist::Zilla::Plugin::JustForManifestSkipTests)
Provides:       perl(Dist::Zilla::Plugin::License) = %{version}
Provides:       perl(Dist::Zilla::Plugin::MakeMaker) = %{version}
Provides:       perl(Dist::Zilla::Plugin::MakeMaker::Runner) = %{version}
Provides:       perl(Dist::Zilla::Plugin::Manifest) = %{version}
Provides:       perl(Dist::Zilla::Plugin::ManifestSkip) = %{version}
Provides:       perl(Dist::Zilla::Plugin::MetaConfig) = %{version}
Provides:       perl(Dist::Zilla::Plugin::MetaJSON) = %{version}
Provides:       perl(Dist::Zilla::Plugin::MetaNoIndex) = %{version}
Provides:       perl(Dist::Zilla::Plugin::MetaResources) = %{version}
Provides:       perl(Dist::Zilla::Plugin::MetaTests) = %{version}
Provides:       perl(Dist::Zilla::Plugin::MetaYAML) = %{version}
Provides:       perl(Dist::Zilla::Plugin::ModuleBuild) = %{version}
Provides:       perl(Dist::Zilla::Plugin::ModuleShareDirs) = %{version}
Provides:       perl(Dist::Zilla::Plugin::MungerThatPrunesPodFiles)
Provides:       perl(Dist::Zilla::Plugin::NextRelease) = %{version}
Provides:       perl(Dist::Zilla::Plugin::PkgDist) = %{version}
Provides:       perl(Dist::Zilla::Plugin::PkgVersion) = %{version}
Provides:       perl(Dist::Zilla::Plugin::PodCoverageTests) = %{version}
Provides:       perl(Dist::Zilla::Plugin::PodSyntaxTests) = %{version}
Provides:       perl(Dist::Zilla::Plugin::PodVersion) = %{version}
Provides:       perl(Dist::Zilla::Plugin::Prereqs) = %{version}
Provides:       perl(Dist::Zilla::Plugin::PruneCruft) = %{version}
Provides:       perl(Dist::Zilla::Plugin::PruneFiles) = %{version}
Provides:       perl(Dist::Zilla::Plugin::Readme) = %{version}
Provides:       perl(Dist::Zilla::Plugin::RemovePrereqs) = %{version}
Provides:       perl(Dist::Zilla::Plugin::ShareDir) = %{version}
Provides:       perl(Dist::Zilla::Plugin::TemplateModule) = %{version}
Provides:       perl(Dist::Zilla::Plugin::TestArchiveBuilder)
Provides:       perl(Dist::Zilla::Plugin::TestAutoLicense)
Provides:       perl(Dist::Zilla::Plugin::TestAutoName)
Provides:       perl(Dist::Zilla::Plugin::TestRelease) = %{version}
Provides:       perl(Dist::Zilla::Plugin::TestReleaseProvider)
Provides:       perl(Dist::Zilla::Plugin::UploadToCPAN) = %{version}
Provides:       perl(Dist::Zilla::Plugin::Versioned) = 1.234.0
Provides:       perl(Dist::Zilla::PluginBundle::Basic) = %{version}
Provides:       perl(Dist::Zilla::PluginBundle::Classic) = %{version}
Provides:       perl(Dist::Zilla::PluginBundle::FakeClassic) = %{version}
Provides:       perl(Dist::Zilla::PluginBundle::Filter) = %{version}
Provides:       perl(Dist::Zilla::Pragmas) = %{version}
Provides:       perl(Dist::Zilla::Prereqs) = %{version}
Provides:       perl(Dist::Zilla::Role::AfterBuild) = %{version}
Provides:       perl(Dist::Zilla::Role::AfterMint) = %{version}
Provides:       perl(Dist::Zilla::Role::AfterRelease) = %{version}
Provides:       perl(Dist::Zilla::Role::ArchiveBuilder) = %{version}
Provides:       perl(Dist::Zilla::Role::BeforeArchive) = %{version}
Provides:       perl(Dist::Zilla::Role::BeforeBuild) = %{version}
Provides:       perl(Dist::Zilla::Role::BeforeMint) = %{version}
Provides:       perl(Dist::Zilla::Role::BeforeRelease) = %{version}
Provides:       perl(Dist::Zilla::Role::BuildPL) = %{version}
Provides:       perl(Dist::Zilla::Role::BuildRunner) = %{version}
Provides:       perl(Dist::Zilla::Role::Chrome) = %{version}
Provides:       perl(Dist::Zilla::Role::ConfigDumper) = %{version}
Provides:       perl(Dist::Zilla::Role::EncodingProvider) = %{version}
Provides:       perl(Dist::Zilla::Role::ExecFiles) = %{version}
Provides:       perl(Dist::Zilla::Role::File) = %{version}
Provides:       perl(Dist::Zilla::Role::FileFinder) = %{version}
Provides:       perl(Dist::Zilla::Role::FileFinderUser) = %{version}
Provides:       perl(Dist::Zilla::Role::FileGatherer) = %{version}
Provides:       perl(Dist::Zilla::Role::FileInjector) = %{version}
Provides:       perl(Dist::Zilla::Role::FileMunger) = %{version}
Provides:       perl(Dist::Zilla::Role::FilePruner) = %{version}
Provides:       perl(Dist::Zilla::Role::InstallTool) = %{version}
Provides:       perl(Dist::Zilla::Role::LicenseProvider) = %{version}
Provides:       perl(Dist::Zilla::Role::MetaProvider) = %{version}
Provides:       perl(Dist::Zilla::Role::MintingProfile) = %{version}
Provides:       perl(Dist::Zilla::Role::MintingProfile::ShareDir) = %{version}
Provides:       perl(Dist::Zilla::Role::ModuleMaker) = %{version}
Provides:       perl(Dist::Zilla::Role::MutableFile) = %{version}
Provides:       perl(Dist::Zilla::Role::NameProvider) = %{version}
Provides:       perl(Dist::Zilla::Role::PPI) = %{version}
Provides:       perl(Dist::Zilla::Role::Plugin) = %{version}
Provides:       perl(Dist::Zilla::Role::PluginBundle) = %{version}
Provides:       perl(Dist::Zilla::Role::PluginBundle::Easy) = %{version}
Provides:       perl(Dist::Zilla::Role::PrereqScanner) = %{version}
Provides:       perl(Dist::Zilla::Role::PrereqSource) = %{version}
Provides:       perl(Dist::Zilla::Role::ReleaseStatusProvider) = %{version}
Provides:       perl(Dist::Zilla::Role::Releaser) = %{version}
Provides:       perl(Dist::Zilla::Role::ShareDir) = %{version}
Provides:       perl(Dist::Zilla::Role::Stash) = %{version}
Provides:       perl(Dist::Zilla::Role::Stash::Authors) = %{version}
Provides:       perl(Dist::Zilla::Role::Stash::Login) = %{version}
Provides:       perl(Dist::Zilla::Role::StubBuild) = %{version}
Provides:       perl(Dist::Zilla::Role::TestRunner) = %{version}
Provides:       perl(Dist::Zilla::Role::TextTemplate) = %{version}
Provides:       perl(Dist::Zilla::Role::VersionProvider) = %{version}
Provides:       perl(Dist::Zilla::Stash::Heap)
Provides:       perl(Dist::Zilla::Stash::Mint) = %{version}
Provides:       perl(Dist::Zilla::Stash::PAUSE) = %{version}
Provides:       perl(Dist::Zilla::Stash::Rights) = %{version}
Provides:       perl(Dist::Zilla::Stash::User) = %{version}
Provides:       perl(Dist::Zilla::Tester) = %{version}
Provides:       perl(Dist::Zilla::Tutorial) = %{version}
Provides:       perl(Dist::Zilla::Types) = %{version}
Provides:       perl(Dist::Zilla::Util) = %{version}
Provides:       perl(Dist::Zilla::Util::AuthorDeps) = %{version}
Provides:       perl(Test::DZil) = %{version}
%undefine       __perllib_provides
Recommends:     perl(App::cpanminus)
Recommends:     perl(Archive::Tar::Wrapper) >= 0.150
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
tutorial at *at https://dzil.org/*. If not, try Dist::Zilla::Tutorial.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
