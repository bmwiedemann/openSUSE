#
# spec file for package perl-Code-TidyAll
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


%define cpan_name Code-TidyAll
Name:           perl-Code-TidyAll
Version:        0.83
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Engine for tidyall, your all-in-one code tidier and validator
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config::INI::Reader)
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(List::Compare)
BuildRequires:  perl(List::SomeUtils)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 2.000000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Path::Tiny) >= 0.098
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Specio) >= 0.40
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::Numeric)
BuildRequires:  perl(Specio::Library::Path::Tiny) >= 0.04
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(Test::Class::Most)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Text::Diff) >= 1.44
BuildRequires:  perl(Text::Diff::Table)
BuildRequires:  perl(Time::Duration::Parse)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(autodie)
BuildRequires:  perl(lib::relative)
Requires:       perl(Capture::Tiny)
Requires:       perl(Config::INI::Reader)
Requires:       perl(Date::Format)
Requires:       perl(Digest::SHA)
Requires:       perl(File::Which)
Requires:       perl(File::pushd)
Requires:       perl(IPC::Run3)
Requires:       perl(IPC::System::Simple)
Requires:       perl(List::Compare)
Requires:       perl(List::SomeUtils)
Requires:       perl(Log::Any)
Requires:       perl(Module::Runtime)
Requires:       perl(Moo) >= 2.000000
Requires:       perl(Moo::Role)
Requires:       perl(Path::Tiny) >= 0.098
Requires:       perl(Scope::Guard)
Requires:       perl(Specio) >= 0.40
Requires:       perl(Specio::Declare)
Requires:       perl(Specio::Library::Builtins)
Requires:       perl(Specio::Library::Numeric)
Requires:       perl(Specio::Library::Path::Tiny) >= 0.04
Requires:       perl(Specio::Library::String)
Requires:       perl(Text::Diff) >= 1.44
Requires:       perl(Text::Diff::Table)
Requires:       perl(Time::Duration::Parse)
Requires:       perl(Try::Tiny)
Recommends:     perl(Parallel::ForkManager)
%{perl_requires}

%description
This is the engine used by tidyall - read that first to get an overview.

You can call this API from your own program instead of executing 'tidyall'.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%license LICENSE

%changelog
