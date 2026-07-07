#
# spec file for package perl-JSON-Schema-Tiny
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name JSON-Schema-Tiny
Name:           perl-JSON-Schema-Tiny
Version:        0.33.0
Release:        0
# 0.033 -> normalize -> 0.33.0
%define cpan_version 0.033
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Validate data against a schema, minimally
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Feature::Compat::Try)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util) >= 1.50
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.34
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Mojo::File)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::JSON::Pointer)
BuildRequires:  perl(Mojo::URL)
BuildRequires:  perl(Mojolicious) >= 7.230
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test2::Warnings)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::JSON::Schema::Acceptance) >= 1.26
BuildRequires:  perl(autovivification)
BuildRequires:  perl(builtin::compat) >= 0.3.3
BuildRequires:  perl(experimental) >= 0.026
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(stable) >= 0.031
Requires:       perl(Feature::Compat::Try)
Requires:       perl(JSON::PP)
Requires:       perl(Mojo::JSON)
Requires:       perl(Mojo::JSON::Pointer)
Requires:       perl(Mojo::URL)
Requires:       perl(Mojolicious) >= 7.230
Requires:       perl(autovivification)
Requires:       perl(builtin::compat) >= 0.3.3
Requires:       perl(experimental) >= 0.026
Requires:       perl(namespace::clean)
Requires:       perl(stable) >= 0.031
Provides:       perl(JSON::Schema::Tiny) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(Cpanel::JSON::XS)
Requires:       perl(Cpanel::JSON::XS)
# MANUAL END

%description
This module aims to be a slimmed-down at https://json-schema.org/ evaluator
and validator, supporting the most popular keywords. (See UNSUPPORTED JSON
SCHEMA FEATURES below for exclusions.)

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING README
%license LICENCE

%changelog
