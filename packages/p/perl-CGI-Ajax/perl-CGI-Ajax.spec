#
# spec file for package perl-CGI-Ajax
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



Name:           perl-CGI-Ajax
%define cpan_name CGI-Ajax
Summary:        A perl-specific System for writing Asynchronous web Apps
Version:        0.707
Release:        1
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/CGI-Ajax/
#Source:         http://www.cpan.org/authors/id/B/BP/BPEDERSE/CGI-Ajax-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CGI)
BuildRequires:  perl(Class::Accessor)
Requires:       perl(CGI)
Requires:       perl(Class::Accessor)
%{perl_requires}

%description
CGI::Ajax is an object-oriented module that provides a unique mechanism for
using perl code asynchronously from javascript- enhanced HTML pages.
CGI::Ajax unburdens the user from having to write extensive javascript,
except for associating an exported method with a document-defined event
(such as onClick, onKeyUp, etc). CGI::Ajax also mixes well with HTML
containing more complex javascript.

CGI::Ajax supports methods that return single results or multiple results
to the web page, and supports returning values to multiple DIV elements on
the HTML page.

Using CGI::Ajax, the URL for the HTTP GET/POST request is automatically
generated based on HTML layout and events, and the page is then dynamically
updated with the output from the perl function. Additionally, CGI::Ajax
supports mapping URL's to a CGI::Ajax function name, so you can separate
your code processing over multiple scripts.

Other than using the Class::Accessor module to generate CGI::Ajax' accessor
methods, CGI::Ajax is completely self-contained - it does not require you
to install a larger package or a full Content Management System, etc.

We have added _support_ for other CGI handler/decoder modules, like the
CGI::Simple manpage or the CGI::Minimal manpage, but we can't test these
since we run mod_perl2 only here. CGI::Ajax checks to see if a header()
method is available to the CGI object, and then uses it. If method() isn't
available, it creates it's own minimal header.

A primary goal of CGI::Ajax is to keep the module streamlined and maximally
flexible. We are trying to keep the generated javascript code to a minimum,
but still provide users with a variety of methods for deploying CGI::Ajax.
And VERY little user javascript.

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

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(644,root,root,755)
%doc Changes LICENSE README

%changelog
