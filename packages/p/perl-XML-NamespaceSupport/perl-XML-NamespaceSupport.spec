#
# spec file for package perl-XML-NamespaceSupport
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


%define cpan_name XML-NamespaceSupport
Name:           perl-XML-NamespaceSupport
Version:        1.120.0
Release:        0
# 1.12 -> normalize -> 1.120.0
%define cpan_version 1.12
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Simple generic namespace processor
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERIGRIN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(XML::NamespaceSupport) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module offers a simple to process namespaced XML names (unames) from
within any application that may need them. It also helps maintain a prefix
to namespace URI map, and provides a number of basic checks.

The model for this module is SAX2's NamespaceSupport class, readable at
http://www.saxproject.org/namespaces.html It adds a few perlisations where
we thought it appropriate.

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
%doc Changes README
%license LICENSE

%changelog
