#
# spec file for package perl-JSON-Validator
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


Name:           perl-JSON-Validator
Version:        4.09
Release:        0
%define cpan_name JSON-Validator
Summary:        Validate data against a JSON schema
License:        Artistic-2.0
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Mojolicious) >= 7.28
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 1.30
BuildRequires:  perl(YAML::PP) >= 0.020
BuildRequires:  perl(YAML::XS) >= 0.67
Requires:       perl(List::Util) >= 1.45
Requires:       perl(Mojolicious) >= 7.28
Requires:       perl(YAML::PP) >= 0.020
Requires:       perl(YAML::XS) >= 0.67
%{perl_requires}

%description
JSON::Validator is a data structure validation library based around at
https://json-schema.org/. This module can be used directly with a JSON
schema or you can use the elegant DSL schema-builder JSON::Validator::Joi
to define the schema programmatically.

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
%doc Changes CONTRIBUTING.md README.md

%changelog
