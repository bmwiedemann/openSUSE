#
# spec file for package perl-XML-DOM-XPath
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_with pod

Name:           perl-XML-DOM-XPath
%define cpan_name XML-DOM-XPath
Summary:        Perl extension to add XPath support to XML::DOM, using XML::XPath engine
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Version:        0.14
Release:        0
Url:            http://search.cpan.org/dist/XML-DOM-XPath/
Source:         http://www.cpan.org/modules/by-module/XML/XML-DOM-XPath-%{version}.tar.gz
Patch0:         no-more-encoding.diff
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       perl >= 5.16
BuildRequires:  perl >= 5.16
BuildRequires:  perl-macros
%if %{with pod}
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%endif
BuildRequires:  perl(XML::DOM)
BuildRequires:  perl(XML::XPathEngine) >= 0.1
Requires:       perl(XML::DOM)
Requires:       perl(XML::XPathEngine) >= 0.1

%description
XML::DOM::XPath allows you to use XML::XPath methods to query a DOM. This
is often much easier than relying only on getElementsByTagName.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
# do not perl_process_packlist (noarch)
# remove .packlist file
%{__rm} -rf $RPM_BUILD_ROOT%perl_vendorarch
# remove perllocal.pod file
%{__rm} -rf $RPM_BUILD_ROOT%perl_archlib
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,-)
%doc Changes README

%changelog
