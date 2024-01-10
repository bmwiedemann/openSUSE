#
# spec file for package perl-YAML
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


%define cpan_name YAML
Name:           perl-YAML
Version:        1.310.0
Release:        0
%define cpan_version 1.31
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        YAML Ain't Markup Language™
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::YAML) >= 1.05
Provides:       perl(YAML) = %{version}
Provides:       perl(YAML::Any) = %{version}
Provides:       perl(YAML::Dumper)
Provides:       perl(YAML::Dumper::Base)
Provides:       perl(YAML::Error)
Provides:       perl(YAML::Loader)
Provides:       perl(YAML::Loader::Base)
Provides:       perl(YAML::Marshall)
Provides:       perl(YAML::Mo)
Provides:       perl(YAML::Node)
Provides:       perl(YAML::Tag)
Provides:       perl(YAML::Type::blessed)
Provides:       perl(YAML::Type::code)
Provides:       perl(YAML::Type::glob)
Provides:       perl(YAML::Type::ref)
Provides:       perl(YAML::Type::regexp)
Provides:       perl(YAML::Type::undef)
Provides:       perl(YAML::Types)
Provides:       perl(YAML::Warning)
Provides:       perl(yaml_mapping)
Provides:       perl(yaml_scalar)
Provides:       perl(yaml_sequence)
%define         __perllib_provides /bin/true
%{perl_requires}

%description
The YAML.pm module implements a YAML Loader and Dumper based on the YAML
1.0 specification. http://www.yaml.org/spec/

YAML is a generic data serialization language that is optimized for human
readability. It can be used to express the data structures of most modern
programming languages. (Including Perl!!!)

For information on the YAML syntax, please refer to the YAML specification.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%license LICENSE

%changelog
