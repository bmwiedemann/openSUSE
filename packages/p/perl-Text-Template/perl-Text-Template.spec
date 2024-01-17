#
# spec file for package perl-Text-Template
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


%define cpan_name Text-Template
Name:           perl-Text-Template
Version:        1.61
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Expand template text with embedded Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHOUT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More::UTF8)
BuildRequires:  perl(Test::Warnings)
%{perl_requires}

%description
This is a library for generating form letters, building HTML pages, or
filling in templates generally. A `template' is a piece of text that has
little Perl programs embedded in it here and there. When you `fill in' a
template, you evaluate the little programs and replace them with their
values.

You can store a template in a file outside your program. People can modify
the template without modifying the program. You can separate the formatting
details from the main code, and put the formatting parts of the program
into the template. That prevents code bloat and encourages functional
separation.

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
%doc Changes README
%license LICENSE

%changelog
