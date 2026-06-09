#
# spec file for package perl-DateTime-Format-Builder
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


%define cpan_name DateTime-Format-Builder
Name:           perl-DateTime-Format-Builder
Version:        0.830.0
Release:        0
# 0.83 -> normalize -> 0.830.0
%define cpan_version 0.83
License:        Artistic-2.0
Summary:        Create DateTime parser classes and objects
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DateTime) >= 1.0
BuildRequires:  perl(DateTime::Format::Strptime) >= 1.40
BuildRequires:  perl(Params::Validate) >= 0.720
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(parent)
Requires:       perl(DateTime) >= 1.0
Requires:       perl(DateTime::Format::Strptime) >= 1.40
Requires:       perl(Params::Validate) >= 0.720
Requires:       perl(parent)
Provides:       perl(DateTime::Format::Builder) = %{version}
Provides:       perl(DateTime::Format::Builder::Parser) = %{version}
Provides:       perl(DateTime::Format::Builder::Parser::Dispatch) = %{version}
Provides:       perl(DateTime::Format::Builder::Parser::Quick) = %{version}
Provides:       perl(DateTime::Format::Builder::Parser::Regex) = %{version}
Provides:       perl(DateTime::Format::Builder::Parser::Strptime) = %{version}
Provides:       perl(DateTime::Format::Builder::Parser::generic) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
DateTime::Format::Builder creates DateTime parsers. Many string formats of
dates and times are simple and just require a basic regular expression to
extract the relevant information. Builder provides a simple way to do this
without writing reams of structural code.

Builder provides a number of methods, most of which you'll never need, or
at least rarely need. They're provided more for exposing of the module's
innards to any subclasses, or for when you need to do something slightly
beyond what I expected.

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md examples README.md
%license LICENSE

%changelog
