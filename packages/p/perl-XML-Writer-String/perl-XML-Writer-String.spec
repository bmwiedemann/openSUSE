#
# spec file for package perl-XML-Writer-String
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


%define cpan_name XML-Writer-String
Name:           perl-XML-Writer-String
Version:        0.100.0
Release:        0
# 0.1 -> normalize -> 0.100.0
%define cpan_version 0.1
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Capture output from XML::Writer
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SO/SOLIVER/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(XML::Writer)
Requires:       perl(XML::Writer)
Provides:       perl(XML::Writer::String) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module implements a bare-bones class specifically for the purpose of
capturing data from the XML::Writer module. XML::Writer expects an
IO::Handle object and writes XML data to the specified object (or STDOUT)
via it's print() method. This module simulates such an object for the
specific purpose of providing the required print() method.

It is recommended that $writer->end() is called prior to calling
$s->value() to check for well-formedness.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes example README

%changelog
