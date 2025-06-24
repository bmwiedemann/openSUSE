#
# spec file for package perl-Test-CleanNamespaces
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


%define cpan_name Test-CleanNamespaces
Name:           perl-Test-CleanNamespaces
Version:        0.240.0
Release:        0
# 0.24 -> normalize -> 0.240.0
%define cpan_version 0.24
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Check for uncleaned imports
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Package::Stash) >= 0.140
BuildRequires:  perl(Role::Tiny) >= 1.3
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Identify)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(Test::Warnings) >= 0.9
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(parent)
Requires:       perl(Module::Runtime)
Requires:       perl(Package::Stash) >= 0.140
Requires:       perl(Role::Tiny) >= 1.3
Requires:       perl(Sub::Identify)
Provides:       perl(Test::CleanNamespaces) = %{version}
%undefine       __perllib_provides
Recommends:     perl(Package::Stash::XS)
%{perl_requires}

%description
This module lets you check your module's namespaces for imported functions
you might have forgotten to remove with namespace::autoclean or
namespace::clean and are therefore available to be called as methods, which
usually isn't want you want.

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
%license LICENCE

%changelog
