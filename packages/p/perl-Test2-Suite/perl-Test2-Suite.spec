#
# spec file for package perl-Test2-Suite
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Test2-Suite
Version:        0.000139
Release:        0
%define cpan_name Test2-Suite
Summary:        Distribution with a rich set of tools built upon the Test2
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Importer) >= 0.024
BuildRequires:  perl(Module::Pluggable) >= 2.7
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Sub::Info) >= 0.002
BuildRequires:  perl(Term::Table) >= 0.013
BuildRequires:  perl(Test2::API) >= 1.302176
Requires:       perl(Importer) >= 0.024
Requires:       perl(Module::Pluggable) >= 2.7
Requires:       perl(Scope::Guard)
Requires:       perl(Sub::Info) >= 0.002
Requires:       perl(Term::Table) >= 0.013
Requires:       perl(Test2::API) >= 1.302176
%{perl_requires}

%description
Rich set of tools, plugins, bundles, etc built upon the Test2 testing
library. If you are interested in writing tests, this is the distribution
for you.

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
%doc appveyor.yml Changes README README.md
%license LICENSE

%changelog
