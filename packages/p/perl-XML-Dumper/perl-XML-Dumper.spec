#
# spec file for package perl-XML-Dumper
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-XML-Dumper
%define cpan_name XML-Dumper
Summary:        Perl module for dumping Perl objects from/to XML
License:        Artistic-1.0 or GPL-2.0+
Group:          Development/Libraries/Perl
Version:        0.81
Release:        0
Url:            http://search.cpan.org/dist/XML-Dumper
Source:         %{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-XML-Parser >= 2.16
BuildRequires:  perl-macros
Requires:       perl-XML-Parser >= 2.16

%description
XML::Dumper dumps Perl data to XML format. XML::Dumper can also read
XML data that was previously dumped by the module and convert it back
to Perl. You can use the module read the XML from a file and write the
XML to a file. Perl objects are blessed back to their original
packaging; if the modules are installed on the system where the perl
objects are reconstituted from xml, they will behave as expected.
Intuitively, if the perl objects are converted and reconstituted in the
same environment, all should be well. And it is.

  Authors:
		Mike Wong <mike_w3@pacbell.net>
		Jonathan Eisenzopf <eisen@pobox.com>

%prep
%setup -n %{cpan_name}-%{version}

%build
perl Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS -Wall" 
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(-,root,root)
%doc Changes README

%changelog
