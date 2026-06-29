#
# spec file for package perl-Test-JSON-Schema-Acceptance
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


%define cpan_name Test-JSON-Schema-Acceptance
Name:           perl-Test-JSON-Schema-Acceptance
Version:        1.37.0
Release:        0
# 1.037 -> normalize -> 1.37.0
%define cpan_version 1.037
License:        MIT
Summary:        Acceptance testing for JSON-Schema based validators
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Feature::Compat::Try)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install) >= 0.60
BuildRequires:  perl(Git::Wrapper)
BuildRequires:  perl(JSON::PP) >= 4.11
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojolicious) >= 7.870
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::TypeTiny) >= 0.2.2
BuildRequires:  perl(Path::Tiny) >= 0.69
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test2::Suite) >= 0.000131
BuildRequires:  perl(Test2::Todo)
BuildRequires:  perl(Test2::Tools::Compare)
BuildRequires:  perl(Test2::Tools::Exception)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test2::Warnings)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::File::ShareDir)
BuildRequires:  perl(Test::Simple) >= 1.302176
BuildRequires:  perl(Types::Common::Numeric)
BuildRequires:  perl(Types::Standard) >= 1.16.3
BuildRequires:  perl(autovivification)
BuildRequires:  perl(builtin::compat)
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(stable) >= 0.031
BuildRequires:  perl(strictures) >= 2
Requires:       perl(Feature::Compat::Try)
Requires:       perl(File::ShareDir)
Requires:       perl(Git::Wrapper)
Requires:       perl(JSON::PP) >= 4.11
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Mojo::JSON)
Requires:       perl(Mojolicious) >= 7.870
Requires:       perl(Moo)
Requires:       perl(MooX::TypeTiny) >= 0.2.2
Requires:       perl(Path::Tiny) >= 0.69
Requires:       perl(Ref::Util)
Requires:       perl(Test2::API)
Requires:       perl(Test2::Todo)
Requires:       perl(Test2::Tools::Compare)
Requires:       perl(Types::Common::Numeric)
Requires:       perl(Types::Standard) >= 1.16.3
Requires:       perl(autovivification)
Requires:       perl(experimental)
Requires:       perl(feature)
Requires:       perl(namespace::clean)
Requires:       perl(stable) >= 0.031
Requires:       perl(strictures) >= 2
Provides:       perl(Test::JSON::Schema::Acceptance) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
at http://json-schema.org is an IETF draft (at time of writing) which
allows you to define the structure of JSON.

From the overview of the draft 2020-12 version of the
specification|https://json-schema.org/draft/2020-12/json-schema-core.html#r
fc.section.3:

    This document proposes a new media type "application/schema+json" to
    identify a JSON Schema for describing JSON data. It also proposes a
    further optional media type, "application/schema-instance+json", to
    provide additional integration features. JSON Schemas are themselves
    JSON documents. This, and related specifications, define keywords
    allowing authors to describe JSON data in several ways.

    JSON Schema uses keywords to assert constraints on JSON instances or
    annotate those instances with additional information. Additional
    keywords are used to apply assertions and annotations to more complex
    JSON data structures, or based on some sort of condition.

This module allows other perl modules (for example JSON::Schema::Modern) to
test that they are JSON Schema-compliant, by running the tests from the
official test suite, without having to manually convert them to perl tests.

You are unlikely to want this module, unless you are attempting to write a
module which implements JSON Schema the specification, and want to test
your compliance.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes CONTRIBUTING examples README update-share
%license LICENCE

%changelog
