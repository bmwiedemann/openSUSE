#
# spec file for package perl-MooseX-Types-Common
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


%define cpan_name MooseX-Types-Common
Name:           perl-MooseX-Types-Common
Version:        0.001015
Release:        0
#Upstream: Artistic-1.0 or GPL-1.0-or-later
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Library of commonly used type constraints
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.34.0
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warnings) >= 0.5.0
Requires:       perl(Moose)
Requires:       perl(MooseX::Types)
Requires:       perl(MooseX::Types::Moose)
%{perl_requires}

%description
A set of commonly-used type constraints that do not ship with Moose by
default.

%prep
%autosetup  -n %{cpan_name}-%{version} -p1

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
