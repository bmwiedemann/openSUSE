#
# spec file for package perl-XML-XSLT
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-XML-XSLT
Version:        0.48
Release:        0
%define cpan_name XML-XSLT
Summary:        Perl module for processing XSLT
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JS/JSTOWE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# MANUAL BEGIN
BuildRequires:  fdupes
# MANUAL END
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(XML::DOM) >= 1.25
BuildRequires:  perl(XML::Parser) >= 2.23
Requires:       perl(XML::DOM) >= 1.25
Requires:       perl(XML::Parser) >= 2.23
%{perl_requires}

%description
This module implements the W3C's XSLT specification. The goal is full
implementation of this spec, but we have not yet achieved that. However, it
already works well. See XML::XSLT Commands for the current status of each
command.

XML::XSLT makes use of XML::DOM and LWP::Simple, while XML::DOM uses
XML::Parser. Therefore XML::Parser, XML::DOM and LWP::Simple have to be
installed properly for XML::XSLT to run.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

# MANUAL BEGIN
%fdupes -s examples
# MANUAL END

%files -f %{name}.files
%defattr(-,root,root,755)
%doc ChangeLog examples README xslt-parser

%changelog
