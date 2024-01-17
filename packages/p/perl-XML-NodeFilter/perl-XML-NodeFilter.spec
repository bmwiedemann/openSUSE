#
# spec file for package perl-XML-NodeFilter
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

%define cpan_name XML-NodeFilter

Name:           perl-XML-NodeFilter
BuildRequires:  libxml2-devel
Version:        0.01
Release:        175
AutoReqProv:    on
Group:          Development/Libraries/Perl
License:        Artistic-1.0
Url:            http://www.cpan.org/modules/by-module/XML/
Summary:        XML::NodeFilter
Source:         %{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
XML::NodeFilter is a generic node filter class for DOM traversal as
specified in the DOM Level 2 Traversal and Range specification. It
extends that specification, so this class is easier to use for Perl
programmers.



%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL
make %{?_smp_mflags}
#make test

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/XML
%{perl_vendorarch}/auto/XML

%changelog
