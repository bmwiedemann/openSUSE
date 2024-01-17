#
# spec file for package perl-XML-Structured
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


# define the name from CPAN
%define         cpan_name XML-Structured
Name:           perl-XML-Structured
Version:        1.3
Release:        0
Summary:        Simple conversion API from XML to perl structures and back
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Url:            https://github.com/openSUSE/perl-XML-Structured
Source:         %{cpan_name}-%{version}.tar.gz
BuildRequires:  perl-XML-Parser
BuildRequires:  perl-XML-SAX
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl(Test::More)
%{perl_requires}

%description
Provides a way to convert XML data into a predefined perl data structure and
back to XML. Unlike with modules like XML::Simple, it is an error if the XML
data does not match the provided skeleton (the "DTD").
Another advantage is that the order of the attributes and elements is taken
from the DTD when converting back to xml.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL OPTIMIZE="%{optflags} -Wall"
make %{?_smp_mflags}

%check
PREFERRED_PARSER=XML::Parser make %{?_smp_mflags} test || exit 1
PREFERRED_PARSER=XML::SAX make %{?_smp_mflags} test || exit 1

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root)
%doc MANIFEST README

%changelog
