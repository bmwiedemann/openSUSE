#
# spec file for package perl-Pod-Coverage-Moose
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Pod-Coverage-Moose
Version:        0.07
Release:        0
%define cpan_name Pod-Coverage-Moose
Summary:        Pod::Coverage extension for Moose
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Pod-Coverage-Moose/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Moose) >= 2.1300
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(namespace::autoclean) >= 0.08
Requires:       perl(Class::Load)
Requires:       perl(Moose) >= 2.1300
Requires:       perl(Pod::Coverage)
Requires:       perl(namespace::autoclean) >= 0.08
%{perl_requires}

%description
When using the Pod::Coverage manpage in combination with the Moose manpage,
it will report any method imported from a Role. This is especially bad when
used in combination with the Test::Pod::Coverage manpage, since it takes
away its ease of use.

To use this module in combination with the Test::Pod::Coverage manpage, use
something like this:

  use Test::Pod::Coverage;
  all_pod_coverage_ok({ coverage_class => 'Pod::Coverage::Moose'});

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING LICENSE README

%changelog
