#
# spec file for package perl-Test-Mock-Guard
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Test-Mock-Guard
Version:        0.10
Release:        0
%define cpan_name Test-Mock-Guard
Summary:        Simple mock test library using RAII.
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Mock-Guard/
Source:         http://www.cpan.org/authors/id/X/XA/XAICRON/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(Class::Load) >= 0.06
BuildRequires:  perl(Exporter) >= 5.63
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(Module::Build) >= 0.38
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Class::Load) >= 0.06
Requires:       perl(Exporter) >= 5.63
%{perl_requires}

%description
Test::Mock::Guard is mock test library using RAII. This module is able to
change method behavior by each scope. See SYNOPSIS's sample code.

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

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes cpanfile LICENSE minil.toml README.md

%changelog
