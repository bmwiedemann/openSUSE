#
# spec file for package perl-HTML-TreeBuilder-XPath
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


%define cpan_name HTML-TreeBuilder-XPath
Name:           perl-HTML-TreeBuilder-XPath
Version:        0.14
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Add XPath support to HTML::TreeBuilder
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIROD/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         HTML-TreeBuilder-XPath-break.diff
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(XML::XPathEngine) >= 0.12
Requires:       perl(HTML::TreeBuilder)
Requires:       perl(XML::XPathEngine) >= 0.12
%{perl_requires}

%description
This module adds typical XPath methods to HTML::TreeBuilder, to make it
easy to query a document.

%prep
%autosetup  -n %{cpan_name}-%{version} -p1

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

%changelog
