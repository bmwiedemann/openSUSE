#
# spec file for package perl-SGMLS
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-SGMLS
Version:        1.1
Release:        0
Summary:        SGML/XML Parsers
License:        GPL-2.0
Group:          Productivity/Publishing/SGML
Url:            https://metacpan.org/release/RAAB/SGMLSpm-1.1
Source:         https://www.cpan.org/authors/id/R/RA/RAAB/SGMLSpm-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
# workaround the downgrade in version number from 1.03ii to 1.1
Provides:       perl-SGMLS = %{version}0
Provides:       perl(SGMLS) = %{version}0
%{perl_requires}

%description
SGMLSpm is a Perl script that reads ESIS output (from parsers like SP)
and offers an event-based interface to the parser. As long as the
parser can parse XML this also works for XML.

%prep
%setup -q -n SGMLSpm-1.1

%build

%install
mkdir -p %{buildroot}%{perl_vendorlib}
mkdir -p %{buildroot}%{perl_vendorlib}/SGMLS
mkdir -p %{buildroot}%{_bindir}
install lib/SGMLS.pm %{buildroot}%{perl_vendorlib}
install lib/sgmlspl-specs/skel.pl %{buildroot}%{perl_vendorlib}
install lib/SGMLS/Output.pm lib/SGMLS/Refs.pm %{buildroot}%{perl_vendorlib}/SGMLS
install script/sgmlspl.pl %{buildroot}%{_bindir}/sgmlspl
mv DOC/sample.pl DOC/HTML/SGMLSpm/sample.pl

%files
%license COPYING
%doc README BUGS ChangeLog TODO DOC/HTML/*
%dir %{perl_vendorlib}/SGMLS
%{perl_vendorlib}/SGMLS.pm
%{perl_vendorlib}/skel.pl
%{perl_vendorlib}/SGMLS/Output.pm
%{perl_vendorlib}/SGMLS/Refs.pm
%{_bindir}/sgmlspl

%changelog
