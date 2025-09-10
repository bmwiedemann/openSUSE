#
# spec file for package perl-Mojolicious-Plugin-OpenAPI
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


%define cpan_name Mojolicious-Plugin-OpenAPI
Name:           perl-Mojolicious-Plugin-OpenAPI
Version:        5.110.0
Release:        0
# 5.11 -> normalize -> 5.110.0
%define cpan_version 5.11
License:        Artistic-2.0
Summary:        OpenAPI / Swagger plugin for Mojolicious
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHTHORSEN/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(JSON::Validator) >= 5.130
BuildRequires:  perl(Mojolicious) >= 9.0
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(JSON::Validator) >= 5.130
Requires:       perl(Mojolicious) >= 9.0
Provides:       perl(Mojolicious::Plugin::OpenAPI) = %{version}
Provides:       perl(Mojolicious::Plugin::OpenAPI::Cors)
Provides:       perl(Mojolicious::Plugin::OpenAPI::Parameters)
Provides:       perl(Mojolicious::Plugin::OpenAPI::Security)
Provides:       perl(Mojolicious::Plugin::OpenAPI::SpecRenderer)
%undefine       __perllib_provides
Recommends:     perl(Text::Markdown) >= 1.0.31
%{perl_requires}

%description
Mojolicious::Plugin::OpenAPI is Mojolicious::Plugin that add routes and
input/output validation to your Mojolicious application based on a OpenAPI
(Swagger) specification. This plugin supports both version 2.0 and 3.x,
though 3.x _might_ have some missing features.

Have a look at the SEE ALSO for references to plugins and other useful
documentation.

Please report in at https://github.com/jhthorsen/json-validator/issues or
open pull requests to enhance the 3.0 support.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes

%changelog
