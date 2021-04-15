#
# spec file for package perl-Mojo-DOM58
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Mojo-DOM58
Name:           perl-Mojo-DOM58
Version:        3.000
Release:        0
Summary:        Minimalistic HTML/XML DOM parser with CSS selectors
License:        Artistic-2.0
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Test::More) >= 0.96
%{perl_requires}

%description
Mojo::DOM58 is a minimalistic and relaxed pure-perl HTML/XML DOM parser
based on Mojo::DOM. It supports the at https://html.spec.whatwg.org/ and at
https://www.w3.org/TR/xml/, and matching based on at
https://www.w3.org/TR/selectors/. It will even try to interpret broken HTML
and XML, so you should not use it for validation.

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
%doc Changes CONTRIBUTING.md examples prereqs.yml README
%license LICENSE

%changelog
