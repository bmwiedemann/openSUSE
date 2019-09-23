#
# spec file for package perl-Test-CleanNamespaces
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Test-CleanNamespaces
Version:        0.24
Release:        0
%define cpan_name Test-CleanNamespaces
Summary:        Check for uncleaned imports
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120620
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Package::Stash) >= 0.14
BuildRequires:  perl(Role::Tiny) >= 1.003000
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Identify)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(Test::Warnings) >= 0.009
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(parent)
Requires:       perl(Module::Runtime)
Requires:       perl(Package::Stash) >= 0.14
Requires:       perl(Role::Tiny) >= 1.003000
Requires:       perl(Sub::Identify)
Recommends:     perl(Package::Stash::XS)
%{perl_requires}

%description
This module lets you check your module's namespaces for imported functions
you might have forgotten to remove with namespace::autoclean or
namespace::clean and are therefore available to be called as methods, which
usually isn't want you want.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING LICENCE README

%changelog
