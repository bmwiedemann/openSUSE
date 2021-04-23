#
# spec file for package perl-DateTime-Format-ISO8601
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


%define cpan_name DateTime-Format-ISO8601
Name:           perl-DateTime-Format-ISO8601
Version:        0.16
Release:        0
Summary:        Parses ISO8601 formats
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DateTime) >= 1.45
BuildRequires:  perl(DateTime::Format::Builder) >= 0.77
BuildRequires:  perl(Params::ValidationCompiler) >= 0.26
BuildRequires:  perl(Specio) >= 0.18
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Exporter)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::More) >= 1.302015
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(parent)
Requires:       perl(DateTime) >= 1.45
Requires:       perl(DateTime::Format::Builder) >= 0.77
Requires:       perl(Params::ValidationCompiler) >= 0.26
Requires:       perl(Specio) >= 0.18
Requires:       perl(Specio::Declare)
Requires:       perl(Specio::Exporter)
Requires:       perl(Specio::Library::Builtins)
Requires:       perl(namespace::autoclean)
Requires:       perl(parent)
%{perl_requires}

%description
Parses almost all ISO8601 date and time formats. ISO8601 time-intervals
will be supported in a later release.

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md Todo
%license LICENSE

%changelog
