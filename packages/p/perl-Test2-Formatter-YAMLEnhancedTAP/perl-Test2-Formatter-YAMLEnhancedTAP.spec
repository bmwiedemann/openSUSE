#
# spec file for package perl-Test2-Formatter-YAMLEnhancedTAP
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Test2-Formatter-YAMLEnhancedTAP
Name:           perl-Test2-Formatter-YAMLEnhancedTAP
Version:        0.0.5
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        YAML-enhanced TAP output for your tests
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JG/JGOMEZ/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(TAP::Harness) >= 3.12
BuildRequires:  perl(Test::More) >= 1.302087
Requires:       perl(TAP::Harness) >= 3.12
%{perl_requires}

%description
'Test2::Formatter::YAMLEnhancedTAP' provides context on failed assertions
as YAML snippets following TAP version 13 grammar.

The sole purpose of this module is to be used with
TAP::Formatter::GitHubActions to bring more accurate annotations.

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
%doc Changes

%changelog
