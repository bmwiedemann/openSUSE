#
# spec file for package perl-Test-CheckChanges
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_with pod

Name:           perl-Test-CheckChanges
Version:        0.14
Release:        0
%define cpan_name Test-CheckChanges
Summary:        Check that the Changes file matches the distribution.
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-CheckChanges/
#Source:         http://www.cpan.org/authors/id/G/GA/GAM/Test-CheckChanges-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Version)
BuildRequires:  perl(Test::More) >= 0.88
%if %{with pod}
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%endif
%{perl_requires}

%description
This module checks that you _Changes_ file has an entry for the current
version of the *Module* being tested.

The version information for the distribution being tested is taken out of
the Build data, or if that is not found, out of the Makefile.

It then attempts to open, in order, a file with the name _Changes_ or
_CHANGES_.

The _Changes_ file is then parsed for version numbers. If one and only one
of the version numbers matches the test passes. Otherwise the test fails.

A message with the current version is printed if the test passes, otherwise
dialog messages are printed to help explain the failure.

The _examples_ directory contains examples of the different formats of
_Changes_ files that are recognized.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(644,root,root,755)
%doc Changes examples README

%changelog
