#
# spec file for package perl-B-Hooks-EndOfScope
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name B-Hooks-EndOfScope
Name:           perl-B-Hooks-EndOfScope
Version:        0.26
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Execute code after a scope finished compilation
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Hash::Util::FieldHash)
BuildRequires:  perl(Module::Implementation) >= 0.05
BuildRequires:  perl(Sub::Exporter::Progressive) >= 0.001006
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Variable::Magic) >= 0.48
Requires:       perl(Hash::Util::FieldHash)
Requires:       perl(Module::Implementation) >= 0.05
Requires:       perl(Sub::Exporter::Progressive) >= 0.001006
Requires:       perl(Variable::Magic) >= 0.48
%{perl_requires}

%description
This module allows you to execute code when perl finished compiling the
surrounding scope.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes CONTRIBUTING README
%license LICENCE

%changelog
