#
# spec file for package perl-Specio-Library-Path-Tiny
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


%define cpan_name Specio-Library-Path-Tiny
Name:           perl-Specio-Library-Path-Tiny
Version:        0.50.0
Release:        0
# 0.05 -> normalize -> 0.50.0
%define cpan_version 0.05
License:        Apache-2.0
Summary:        Path::Tiny types and coercions for Specio
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Temp) >= 0.18
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(Path::Tiny) >= 0.87.0
BuildRequires:  perl(Specio) >= 0.290
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Exporter)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::PartialDump)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Specio)
BuildRequires:  perl(parent)
Requires:       perl(Path::Tiny) >= 0.87.0
Requires:       perl(Specio) >= 0.290
Requires:       perl(Specio::Declare)
Requires:       perl(Specio::Exporter)
Requires:       perl(Specio::Library::Builtins)
Requires:       perl(Specio::PartialDump)
Requires:       perl(parent)
Provides:       perl(Specio::Library::Path::Tiny) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This library provides a set of Path::Tiny types and coercions for Specio.
These types can be used with Moose, Moo, Params::ValidationCompiler, and
other modules.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%license LICENSE

%changelog
