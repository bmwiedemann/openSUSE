#
# spec file for package perl-HTML-FillInForm
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-HTML-FillInForm
Version:        2.21
Release:        0
#Upstream: CHECK(GPL-1.0+ or Artistic-1.0)
%define cpan_name HTML-FillInForm
Summary:        Populates HTML Forms with data
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTML-FillInForm/
Source0:        http://www.cpan.org/authors/id/M/MA/MARKSTOS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         rt-100926.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CGI)
BuildRequires:  perl(HTML::Parser) >= 3.26
BuildRequires:  perl(HTML::TokeParser) >= 3.26
Requires:       perl(CGI)
Requires:       perl(HTML::Parser) >= 3.26
Requires:       perl(HTML::TokeParser) >= 3.26
%{perl_requires}

%description
This module fills in an HTML form with data from a Perl data structure,
allowing you to keep the HTML and Perl separate.

Here are two common use cases:

1. A user submits an HTML form without filling out a required field. You
want to redisplay the form with all the previous data in it, to make it
easy for the user to see and correct the error.

2. You have just retrieved a record from a database and need to display it
in an HTML form.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
