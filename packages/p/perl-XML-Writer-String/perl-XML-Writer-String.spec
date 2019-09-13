#
# spec file for package perl-XML-Writer-String
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           perl-XML-Writer-String
%define        real_name XML-Writer-String
Summary:        Capture output from XML::Writer
Url:            http://search.cpan.org/perldoc?XML::Writer::String
Group:          Development/Libraries/Perl
License:        Artistic-1.0 or GPL-1.0+
Version:        0.1 
Release:        1
Source:         %{real_name}-%{version}.tar.gz
Requires:       perl-XML-Writer
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
This module implements a bare-bones class specifically for the purpose of
capturing data from the XML::Writer module. XML::Writer expects an IO::Handle
object and writes XML data to the specified object (or STDOUT) via it's print()
method. This module simulates such an object for the specific purpose of
providing the required print() method.

It is recommended that $writer->end() is called prior to calling $s->value() to
check for well-formedness.

Author:
-------
    Simon Oliver <simon.oliver@umist.ac.uk>


%prep
%setup -n %{real_name}-%{version}
for i in Changes README MANIFEST example/eg*; do
	sed -i 's///' $i
done

%build
perl Makefile.PL 
make %{?jobs:-j%jobs}

%check
make test

%install
%perl_make_install
%perl_process_packlist

%clean
rm -rf %{buildroot}

%files 
%defattr(-, root, root)
%doc Changes README MANIFEST example
%doc %{_mandir}/man?/*
%dir %{perl_vendorarch}/auto/XML
%dir %{perl_vendorarch}/auto/XML/Writer
%dir %{perl_vendorarch}/auto/XML/Writer/String
%dir %{perl_vendorlib}/XML
%dir %{perl_vendorlib}/XML/Writer
%{perl_vendorlib}/XML/Writer/*.pm

%changelog
