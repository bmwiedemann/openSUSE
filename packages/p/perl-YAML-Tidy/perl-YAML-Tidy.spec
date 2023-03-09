#
# spec file for package perl-YAML-Tidy
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


%define cpan_name YAML-Tidy
Name:           perl-YAML-Tidy
Version:        0.007
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Tidy YAML files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Getopt::Long::Descriptive)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::Warnings) >= 0.029
BuildRequires:  perl(YAML::LibYAML::API) >= 0.013
BuildRequires:  perl(YAML::LibYAML::API::XS)
BuildRequires:  perl(YAML::PP::Common)
BuildRequires:  perl(YAML::PP::Highlight)
BuildRequires:  perl(YAML::PP::Parser)
BuildRequires:  perl(experimental)
Requires:       perl(Getopt::Long::Descriptive)
Requires:       perl(YAML::LibYAML::API) >= 0.013
Requires:       perl(YAML::LibYAML::API::XS)
Requires:       perl(YAML::PP::Common)
Requires:       perl(YAML::PP::Highlight)
Requires:       perl(YAML::PP::Parser)
Requires:       perl(experimental)
%{perl_requires}

%description
yamltidy can automatically tidy formatting in your YAML files, for example
adjust indentation and remove trailing spaces.

For more information, see https://github.com/perlpunk/yamltidy.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes CONTRIBUTING.md README.md
%license LICENSE

%changelog
