#
# spec file for package perl-Pod-Coverage-Moose
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Pod-Coverage-Moose
Name:           perl-Pod-Coverage-Moose
Version:        0.80.0
Release:        0
%define cpan_version 0.08
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Pod::Coverage extension for Moose
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Moose) >= 2.1300
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(namespace::autoclean) >= 0.08
Requires:       perl(Class::Load)
Requires:       perl(Moose) >= 2.1300
Requires:       perl(Pod::Coverage)
Requires:       perl(namespace::autoclean) >= 0.08
Provides:       perl(Pod::Coverage::Moose) = 0.80.0
%define         __perllib_provides /bin/true
%{perl_requires}

%description
When using Pod::Coverage in combination with Moose, it will report any
method imported from a role. This is especially bad when used in
combination with Test::Pod::Coverage, since it takes away its ease of use.

To use this module in combination with Test::Pod::Coverage, use something
like this:

  use Test::Pod::Coverage;
  all_pod_coverage_ok({ coverage_class => 'Pod::Coverage::Moose'});

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
%doc Changes CONTRIBUTING README
%license LICENCE

%changelog
