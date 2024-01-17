#
# spec file for package perl-Test-CPAN-Meta
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


Name:           perl-Test-CPAN-Meta
Version:        0.25
Release:        0
%define cpan_name Test-CPAN-Meta
Summary:        Validate your CPAN META.yml files
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-CPAN-Meta/
Source0:        http://www.cpan.org/authors/id/B/BA/BARBIE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Parse::CPAN::Meta) >= 0.02
BuildRequires:  perl(Test::More) >= 0.70
Requires:       perl(Parse::CPAN::Meta) >= 0.02
Requires:       perl(Test::More) >= 0.70
Recommends:     perl(Test::Pod) >= 1.00
Recommends:     perl(Test::Pod::Coverage) >= 0.08
%{perl_requires}

%description
This distribution was written to ensure that a META.yml file, provided with
a standard distribution uploaded to CPAN, meets the specifications that are
slowly being introduced to module uploads, via the use of package makers
and installers such as the ExtUtils::MakeMaker manpage, the Module::Build
manpage and the Module::Install manpage.

See the CPAN::Meta manpage for further details of the CPAN Meta
Specification.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples LICENSE README

%changelog
