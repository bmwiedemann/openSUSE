#
# spec file for package perl-JavaScript-Minifier-XS
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


%define cpan_name JavaScript-Minifier-XS
Name:           perl-JavaScript-Minifier-XS
Version:        0.160.0
Release:        0
# 0.16 -> normalize -> 0.160.0
%define cpan_version 0.16
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        XS based JavaScript minifier
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GT/GTERMARS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::DiagINC) >= 0.2
BuildRequires:  perl(Test::More) >= 0.96
Provides:       perl(JavaScript::Minifier::XS) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
'JavaScript::Minifier::XS' is a JavaScript "minifier"; its designed to
remove unnecessary whitespace and comments from JavaScript files, which
also *not* breaking the JavaScript.

'JavaScript::Minifier::XS' is similar in function to
'JavaScript::Minifier', but is substantially faster as its written in XS
and not just pure Perl.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README
%license LICENSE

%changelog
