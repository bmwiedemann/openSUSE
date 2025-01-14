#
# spec file for package perl-MooseX-Getopt
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


%define cpan_name MooseX-Getopt
Name:           perl-MooseX-Getopt
Version:        0.780.0
Release:        0
# 0.78 -> normalize -> 0.780.0
%define cpan_version 0.78
#Upstream: Artistic-1.0 or GPL-1.0-or-later
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Moose role for processing command line options
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Getopt::Long) >= 2.37
BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.088
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Meta::Attribute)
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Role) >= 0.56
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Role::Parameterized) >= 1.01
BuildRequires:  perl(Path::Tiny) >= 0.009
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal) >= 0.003
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Trap)
BuildRequires:  perl(Test::Warnings) >= 0.009
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(Getopt::Long) >= 2.37
Requires:       perl(Getopt::Long::Descriptive) >= 0.088
Requires:       perl(Moose)
Requires:       perl(Moose::Meta::Attribute)
Requires:       perl(Moose::Role) >= 0.56
Requires:       perl(Moose::Util::TypeConstraints)
Requires:       perl(MooseX::Role::Parameterized) >= 1.01
Requires:       perl(Try::Tiny)
Requires:       perl(namespace::autoclean)
Provides:       perl(MooseX::Getopt) = %{version}
Provides:       perl(MooseX::Getopt::Basic) = %{version}
Provides:       perl(MooseX::Getopt::Dashes) = %{version}
Provides:       perl(MooseX::Getopt::GLD) = %{version}
Provides:       perl(MooseX::Getopt::Meta::Attribute) = %{version}
Provides:       perl(MooseX::Getopt::Meta::Attribute::NoGetopt) = %{version}
Provides:       perl(MooseX::Getopt::Meta::Attribute::Trait) = %{version}
Provides:       perl(MooseX::Getopt::Meta::Attribute::Trait::NoGetopt) = %{version}
Provides:       perl(MooseX::Getopt::OptionTypeMap) = %{version}
Provides:       perl(MooseX::Getopt::ProcessedArgv) = %{version}
Provides:       perl(MooseX::Getopt::Strict) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This is a role which provides an alternate constructor for creating objects
using parameters passed in from the command line.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
