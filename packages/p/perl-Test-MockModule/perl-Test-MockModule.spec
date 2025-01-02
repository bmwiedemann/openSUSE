#
# spec file for package perl-Test-MockModule
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


%define cpan_name Test-MockModule
Name:           perl-Test-MockModule
Version:        0.179.0
Release:        0
# v0.179.0 -> normalize -> 0.179.0
%define cpan_version v0.179.0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Override subroutines in a module for unit testing
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GF/GFRANKS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.4234
BuildRequires:  perl(SUPER) >= 1.20
BuildRequires:  perl(Software::License) >= 0.104.6
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warnings)
Requires:       perl(SUPER) >= 1.20
Requires:       perl(Software::License) >= 0.104.6
%{perl_requires}

%description
'Test::MockModule' lets you temporarily redefine subroutines in other
packages for the purposes of unit testing.

A 'Test::MockModule' object is set up to mock subroutines for a given
module. The object remembers the original subroutine so it can be easily
restored. This happens automatically when all MockModule objects for the
given module go out of scope, or when you 'unmock()' the subroutine.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md
%license LICENSE

%changelog
