#
# spec file for package perl-Test2-Plugin-NoWarnings
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Test2-Plugin-NoWarnings
Version:        0.07
Release:        0
%define cpan_name Test2-Plugin-NoWarnings
Summary:        Fail if tests warn
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Test2) >= 1.302096
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test2::Event)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::Util::HashBase)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::More) >= 1.302015
BuildRequires:  perl(parent)
Requires:       perl(Test2) >= 1.302096
Requires:       perl(Test2::API)
Requires:       perl(Test2::Event)
Requires:       perl(Test2::Util::HashBase)
Requires:       perl(parent)
%{perl_requires}

%description
Loading this plugin causes your tests to fail if there any warnings while
they run. Each warning generates a new failing test and the warning content
is outputted via 'diag'.

This module uses '$SIG{__WARN__}', so if the code you're testing sets this,
then this module will stop working.

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%license LICENSE

%changelog
