#
# spec file for package perl-YAML-LibYAML
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


%define cpan_name YAML-LibYAML
Name:           perl-YAML-LibYAML
Version:        0.903.0
Release:        0
# v0.903.0 -> normalize -> 0.903.0
%define cpan_version v0.903.0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl YAML Serialization using XS and libyaml
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.9
%{perl_requires}

%description
Perl YAML Serialization using XS and libyaml

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.md README
%license LICENSE

%changelog
