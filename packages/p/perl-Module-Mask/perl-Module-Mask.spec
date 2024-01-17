#
# spec file for package perl-Module-Mask
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Module-Mask
Name:           perl-Module-Mask
Version:        0.06
Release:        0
Summary:        Pretend certain modules are not installed
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATTLAW/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.400000
BuildRequires:  perl(Module::Util) >= 1.00
Requires:       perl(Module::Util) >= 1.00
Recommends:     perl(Test::Pod) >= 1.14
Recommends:     perl(Test::Pod::Coverage) >= 1.04
%{perl_requires}

%description
Sometimes you need to test what happens when a given module is not
installed. This module provides a way of temporarily hiding installed
modules from perl's require mechanism. The Module::Mask object adds itself
to @INC and blocks require calls to restricted modules.

Module::Mask will not affect modules already loaded at time of
instantiation.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
