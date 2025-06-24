#
# spec file for package perl-MooseX-Storage
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


%define cpan_name MooseX-Storage
Name:           perl-MooseX-Storage
Version:        0.530.0
Release:        0
# 0.53 -> normalize -> 0.530.0
%define cpan_version 0.53
#Upstream: Artistic-1.0 or GPL-1.0-or-later
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Serialization framework for Moose classes
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:  perl(IO::AtomicFile)
BuildRequires:  perl(JSON::MaybeXS) >= 1.1
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose) >= 0.990
BuildRequires:  perl(Moose::Meta::Attribute)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Deep::JSON)
BuildRequires:  perl(Test::Deep::Type)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(YAML::Any)
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(IO::AtomicFile)
Requires:       perl(JSON::MaybeXS) >= 1.1
Requires:       perl(Module::Runtime)
Requires:       perl(Moose) >= 0.990
Requires:       perl(Moose::Meta::Attribute)
Requires:       perl(Moose::Role)
Requires:       perl(String::RewritePrefix)
Requires:       perl(YAML::Any)
Requires:       perl(namespace::autoclean)
Provides:       perl(MooseX::Storage) = %{version}
Provides:       perl(MooseX::Storage::Base::WithChecksum) = %{version}
Provides:       perl(MooseX::Storage::Basic) = %{version}
Provides:       perl(MooseX::Storage::Deferred) = %{version}
Provides:       perl(MooseX::Storage::Engine) = %{version}
Provides:       perl(MooseX::Storage::Engine::IO::AtomicFile) = %{version}
Provides:       perl(MooseX::Storage::Engine::IO::File) = %{version}
Provides:       perl(MooseX::Storage::Engine::Trait::DisableCycleDetection) = %{version}
Provides:       perl(MooseX::Storage::Engine::Trait::OnlyWhenBuilt) = %{version}
Provides:       perl(MooseX::Storage::Format::JSON) = %{version}
Provides:       perl(MooseX::Storage::Format::Storable) = %{version}
Provides:       perl(MooseX::Storage::Format::YAML) = %{version}
Provides:       perl(MooseX::Storage::IO::AtomicFile) = %{version}
Provides:       perl(MooseX::Storage::IO::File) = %{version}
Provides:       perl(MooseX::Storage::IO::StorableFile) = %{version}
Provides:       perl(MooseX::Storage::Meta::Attribute::DoNotSerialize) = %{version}
Provides:       perl(MooseX::Storage::Meta::Attribute::Trait::DoNotSerialize) = %{version}
Provides:       perl(MooseX::Storage::Traits::DisableCycleDetection) = %{version}
Provides:       perl(MooseX::Storage::Traits::OnlyWhenBuilt) = %{version}
Provides:       perl(MooseX::Storage::Util) = %{version}
%undefine       __perllib_provides
Recommends:     perl(IO::AtomicFile)
Recommends:     perl(JSON::MaybeXS) >= 1.1
Recommends:     perl(YAML)
Recommends:     perl(YAML::Any)
Recommends:     perl(YAML::Syck)
Recommends:     perl(YAML::XS)
%{perl_requires}

%description
MooseX::Storage is a serialization framework for Moose, it provides a very
flexible and highly pluggable way to serialize Moose classes to a number of
different formats and styles.

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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
