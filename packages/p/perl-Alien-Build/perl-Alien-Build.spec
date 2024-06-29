#
# spec file for package perl-Alien-Build
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


%define cpan_name Alien-Build
Name:           perl-Alien-Build
Version:        2.830.0
Release:        0
# 2.83 -> normalize -> 2.830.0
%define cpan_version 2.83
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Build external dependencies for use in CPAN
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny) >= 0.17
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.30
BuildRequires:  perl(FFI::CheckLib) >= 0.11
BuildRequires:  perl(File::Which) >= 1.10
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Path::Tiny) >= 0.077
BuildRequires:  perl(Test2::API) >= 1.302096
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(Text::ParseWords) >= 3.26
BuildRequires:  perl(parent)
Requires:       perl(Capture::Tiny) >= 0.17
Requires:       perl(Digest::SHA)
Requires:       perl(ExtUtils::CBuilder)
Requires:       perl(ExtUtils::MakeMaker) >= 6.64
Requires:       perl(ExtUtils::ParseXS) >= 3.30
Requires:       perl(FFI::CheckLib) >= 0.11
Requires:       perl(File::Which) >= 1.10
Requires:       perl(File::chdir)
Requires:       perl(JSON::PP)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Path::Tiny) >= 0.077
Requires:       perl(Test2::API) >= 1.302096
Requires:       perl(Text::ParseWords) >= 3.26
Requires:       perl(parent)
Provides:       perl(Alien::Base) = %{version}
Provides:       perl(Alien::Base::PkgConfig) = %{version}
Provides:       perl(Alien::Base::Wrapper) = %{version}
Provides:       perl(Alien::Build) = %{version}
Provides:       perl(Alien::Build::CommandSequence) = %{version}
Provides:       perl(Alien::Build::Helper)
Provides:       perl(Alien::Build::Interpolate) = %{version}
Provides:       perl(Alien::Build::Interpolate::Default) = %{version}
Provides:       perl(Alien::Build::Interpolate::Helper)
Provides:       perl(Alien::Build::Log) = %{version}
Provides:       perl(Alien::Build::Log::Abbreviate) = %{version}
Provides:       perl(Alien::Build::Log::Default) = %{version}
Provides:       perl(Alien::Build::MM) = %{version}
Provides:       perl(Alien::Build::Meta)
Provides:       perl(Alien::Build::Plugin) = %{version}
Provides:       perl(Alien::Build::Plugin::Build::Autoconf) = %{version}
Provides:       perl(Alien::Build::Plugin::Build::CMake) = %{version}
Provides:       perl(Alien::Build::Plugin::Build::Copy) = %{version}
Provides:       perl(Alien::Build::Plugin::Build::MSYS) = %{version}
Provides:       perl(Alien::Build::Plugin::Build::Make) = %{version}
Provides:       perl(Alien::Build::Plugin::Build::SearchDep) = %{version}
Provides:       perl(Alien::Build::Plugin::Core::CleanInstall) = %{version}
Provides:       perl(Alien::Build::Plugin::Core::Download) = %{version}
Provides:       perl(Alien::Build::Plugin::Core::FFI) = %{version}
Provides:       perl(Alien::Build::Plugin::Core::Gather) = %{version}
Provides:       perl(Alien::Build::Plugin::Core::Legacy) = %{version}
Provides:       perl(Alien::Build::Plugin::Core::Override) = %{version}
Provides:       perl(Alien::Build::Plugin::Core::Setup) = %{version}
Provides:       perl(Alien::Build::Plugin::Core::Tail) = %{version}
Provides:       perl(Alien::Build::Plugin::Decode::DirListing) = %{version}
Provides:       perl(Alien::Build::Plugin::Decode::DirListingFtpcopy) = %{version}
Provides:       perl(Alien::Build::Plugin::Decode::HTML) = %{version}
Provides:       perl(Alien::Build::Plugin::Decode::Mojo) = %{version}
Provides:       perl(Alien::Build::Plugin::Digest::Negotiate) = %{version}
Provides:       perl(Alien::Build::Plugin::Digest::SHA) = %{version}
Provides:       perl(Alien::Build::Plugin::Digest::SHAPP) = %{version}
Provides:       perl(Alien::Build::Plugin::Download::Negotiate) = %{version}
Provides:       perl(Alien::Build::Plugin::Extract::ArchiveTar) = %{version}
Provides:       perl(Alien::Build::Plugin::Extract::ArchiveZip) = %{version}
Provides:       perl(Alien::Build::Plugin::Extract::CommandLine) = %{version}
Provides:       perl(Alien::Build::Plugin::Extract::Directory) = %{version}
Provides:       perl(Alien::Build::Plugin::Extract::File) = %{version}
Provides:       perl(Alien::Build::Plugin::Extract::Negotiate) = %{version}
Provides:       perl(Alien::Build::Plugin::Fetch::CurlCommand) = %{version}
Provides:       perl(Alien::Build::Plugin::Fetch::HTTPTiny) = %{version}
Provides:       perl(Alien::Build::Plugin::Fetch::LWP) = %{version}
Provides:       perl(Alien::Build::Plugin::Fetch::Local) = %{version}
Provides:       perl(Alien::Build::Plugin::Fetch::LocalDir) = %{version}
Provides:       perl(Alien::Build::Plugin::Fetch::NetFTP) = %{version}
Provides:       perl(Alien::Build::Plugin::Fetch::Wget) = %{version}
Provides:       perl(Alien::Build::Plugin::Gather::IsolateDynamic) = %{version}
Provides:       perl(Alien::Build::Plugin::PkgConfig::CommandLine) = %{version}
Provides:       perl(Alien::Build::Plugin::PkgConfig::LibPkgConf) = %{version}
Provides:       perl(Alien::Build::Plugin::PkgConfig::MakeStatic) = %{version}
Provides:       perl(Alien::Build::Plugin::PkgConfig::Negotiate) = %{version}
Provides:       perl(Alien::Build::Plugin::PkgConfig::PP) = %{version}
Provides:       perl(Alien::Build::Plugin::Prefer::BadVersion) = %{version}
Provides:       perl(Alien::Build::Plugin::Prefer::GoodVersion) = %{version}
Provides:       perl(Alien::Build::Plugin::Prefer::SortVersions) = %{version}
Provides:       perl(Alien::Build::Plugin::Probe::CBuilder) = %{version}
Provides:       perl(Alien::Build::Plugin::Probe::CommandLine) = %{version}
Provides:       perl(Alien::Build::Plugin::Probe::Vcpkg) = %{version}
Provides:       perl(Alien::Build::Plugin::Test::Mock) = %{version}
Provides:       perl(Alien::Build::PluginMeta)
Provides:       perl(Alien::Build::Temp) = %{version}
Provides:       perl(Alien::Build::TempDir)
Provides:       perl(Alien::Build::Util) = %{version}
Provides:       perl(Alien::Build::Version::Basic) = %{version}
Provides:       perl(Alien::Build::rc) = %{version}
Provides:       perl(Alien::Role) = %{version}
Provides:       perl(Alien::Util) = %{version}
Provides:       perl(Test::Alien) = %{version}
Provides:       perl(Test::Alien::Build) = %{version}
Provides:       perl(Test::Alien::CanCompile) = %{version}
Provides:       perl(Test::Alien::CanPlatypus) = %{version}
Provides:       perl(Test::Alien::Diag) = %{version}
Provides:       perl(Test::Alien::Run) = %{version}
Provides:       perl(Test::Alien::Synthetic) = %{version}
Provides:       perl(alienfile) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  pkg-config
# MANUAL END

%description
This module provides tools for building external (non-CPAN) dependencies
for CPAN. It is mainly designed to be used at install time of a CPAN
client, and work closely with Alien::Base which is used at runtime.

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
%doc Changes Changes.Alien-Base Changes.Alien-Base-Wrapper Changes.Alien-Build-Decode-Mojo Changes.Test-Alien example README SUPPORT
%license LICENSE

%changelog
