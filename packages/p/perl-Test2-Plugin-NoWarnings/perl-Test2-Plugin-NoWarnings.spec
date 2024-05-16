#
# spec file for package perl-Test2-Plugin-NoWarnings
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


%define cpan_name Test2-Plugin-NoWarnings
Name:           perl-Test2-Plugin-NoWarnings
Version:        0.100.0
Release:        0
# 0.10 -> normalize -> 0.100.0
%define cpan_version 0.10
License:        Artistic-2.0
Summary:        Fail if tests warn
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Test2) >= 1.302167
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test2::Event)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::Util::HashBase)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::More) >= 1.302015
BuildRequires:  perl(parent)
Requires:       perl(Test2) >= 1.302167
Requires:       perl(Test2::API)
Requires:       perl(Test2::Event)
Requires:       perl(Test2::Util::HashBase)
Requires:       perl(parent)
Provides:       perl(Test2::Event::Warning) = %{version}
Provides:       perl(Test2::Plugin::NoWarnings) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Loading this plugin causes your tests to fail if there any warnings while
they run. Each warning generates a new failing test and the warning content
is outputted via 'diag'.

This module uses '$SIG{__WARN__}', so if the code you're testing sets this,
then this module will stop working.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%license LICENSE

%changelog
