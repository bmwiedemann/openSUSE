#
# spec file for package perl-SVG
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


%define cpan_name SVG
Name:           perl-SVG
Version:        2.890.0
Release:        0
# 2.89 -> normalize -> 2.890.0
%define cpan_version 2.89
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl extension for generating Scalable Vector Graphics (SVG) documents
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(parent)
Requires:       perl(parent)
Provides:       perl(SVG) = %{version}
Provides:       perl(SVG::DOM) = %{version}
Provides:       perl(SVG::Element) = %{version}
Provides:       perl(SVG::Extension) = %{version}
Provides:       perl(SVG::XML) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
SVG is a 100% Perl module which generates a nested data structure
containing the DOM representation of an SVG (Scalable Vector Graphics)
image. Using SVG, you can generate SVG objects, embed other SVG instances
into it, access the DOM object, create and access javascript, and generate
SMIL animation content.

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
%doc Changes examples README
%license LICENSE

%changelog
