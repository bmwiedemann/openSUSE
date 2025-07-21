#
# spec file for package perl-Moose
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


%define cpan_name Moose
Name:           perl-Moose
Version:        2.4000
Release:        0
#Upstream: Artistic-1.0 or GPL-1.0-or-later
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Postmodern object system for Perl 5
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Check) >= 0.11
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Carp) >= 1.22
BuildRequires:  perl(Class::Load) >= 0.90
BuildRequires:  perl(Class::Load::XS) >= 0.10
BuildRequires:  perl(Data::OptList) >= 0.107
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(Devel::OverloadInfo) >= 0.5
BuildRequires:  perl(Devel::StackTrace) >= 2.30
BuildRequires:  perl(Dist::CheckConflicts) >= 0.20
BuildRequires:  perl(Eval::Closure) >= 0.40
BuildRequires:  perl(List::Util) >= 1.56
BuildRequires:  perl(MRO::Compat) >= 0.50
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime) >= 0.14
BuildRequires:  perl(Module::Runtime::Conflicts) >= 0.2
BuildRequires:  perl(Package::DeprecationManager) >= 0.110
BuildRequires:  perl(Package::Stash) >= 0.320
BuildRequires:  perl(Package::Stash::XS) >= 0.240
BuildRequires:  perl(Params::Util) >= 1.0
BuildRequires:  perl(Scalar::Util) >= 1.19
BuildRequires:  perl(Sub::Exporter) >= 0.980
BuildRequires:  perl(Sub::Util) >= 1.40
BuildRequires:  perl(Test::Fatal) >= 0.1
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs) >= 0.2.10
BuildRequires:  perl(Try::Tiny) >= 0.170
BuildRequires:  perl(parent) >= 0.223
Requires:       perl(Carp) >= 1.22
Requires:       perl(Class::Load) >= 0.90
Requires:       perl(Class::Load::XS) >= 0.10
Requires:       perl(Data::OptList) >= 0.107
Requires:       perl(Devel::GlobalDestruction)
Requires:       perl(Devel::OverloadInfo) >= 0.5
Requires:       perl(Devel::StackTrace) >= 2.30
Requires:       perl(Dist::CheckConflicts) >= 0.20
Requires:       perl(Eval::Closure) >= 0.40
Requires:       perl(List::Util) >= 1.56
Requires:       perl(MRO::Compat) >= 0.50
Requires:       perl(Module::Runtime) >= 0.14
Requires:       perl(Module::Runtime::Conflicts) >= 0.2
Requires:       perl(Package::DeprecationManager) >= 0.110
Requires:       perl(Package::Stash) >= 0.320
Requires:       perl(Package::Stash::XS) >= 0.240
Requires:       perl(Params::Util) >= 1.0
Requires:       perl(Scalar::Util) >= 1.19
Requires:       perl(Sub::Exporter) >= 0.980
Requires:       perl(Sub::Util) >= 1.40
Requires:       perl(Try::Tiny) >= 0.170
Requires:       perl(parent) >= 0.223
Recommends:     perl(Data::OptList) >= 0.110
%{perl_requires}
# MANUAL BEGIN
Provides:       perl-Class-MOP = %{version}
Obsoletes:      perl-Class-MOP < %{version}
# MANUAL END

%description
Moose is an extension of the Perl 5 object system.

The main goal of Moose is to make Perl 5 Object Oriented programming
easier, more consistent, and less tedious. With Moose you can think more
about what you want to do and less about the mechanics of OOP.

Additionally, Moose is built on top of Class::MOP, which is a metaclass
system for Perl 5. This means that Moose not only makes building normal
Perl 5 objects better, but it provides the power of metaclass programming
as well.

%prep
%autosetup -n %{cpan_name}-%{version} -p1

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
%doc Changes Changes.Class-MOP doc README.md TODO
%license LICENSE

%changelog
