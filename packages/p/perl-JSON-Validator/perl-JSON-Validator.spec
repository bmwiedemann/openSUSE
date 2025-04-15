#
# spec file for package perl-JSON-Validator
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name JSON-Validator
Name:           perl-JSON-Validator
Version:        5.150.0
Release:        0
# 5.15 -> normalize -> 5.150.0
%define cpan_version 5.15
License:        Artistic-2.0
Summary:        Validate data against a JSON schema
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Mojolicious) >= 7.280
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 1.30
BuildRequires:  perl(YAML::XS) >= 0.670
Requires:       perl(List::Util) >= 1.45
Requires:       perl(Mojolicious) >= 7.280
Requires:       perl(YAML::XS) >= 0.670
Provides:       perl(JSON::Validator) = %{version}
Provides:       perl(JSON::Validator::Error)
Provides:       perl(JSON::Validator::Formats)
Provides:       perl(JSON::Validator::Joi)
Provides:       perl(JSON::Validator::Schema)
Provides:       perl(JSON::Validator::Schema::Draft201909)
Provides:       perl(JSON::Validator::Schema::Draft4)
Provides:       perl(JSON::Validator::Schema::Draft6)
Provides:       perl(JSON::Validator::Schema::Draft7)
Provides:       perl(JSON::Validator::Schema::OpenAPIv2)
Provides:       perl(JSON::Validator::Schema::OpenAPIv3)
Provides:       perl(JSON::Validator::Store)
Provides:       perl(JSON::Validator::URI)
Provides:       perl(JSON::Validator::Util)
%undefine       __perllib_provides
%{perl_requires}

%description
JSON::Validator is a data structure validation library based around at
https://json-schema.org/. This module can be used directly with a JSON
schema or you can use the elegant DSL schema-builder JSON::Validator::Joi
to define the schema programmatically.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes CONTRIBUTING.md

%changelog
