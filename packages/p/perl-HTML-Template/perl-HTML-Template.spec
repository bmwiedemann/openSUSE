#
# spec file for package perl-HTML-Template
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


Name:           perl-HTML-Template
Version:        2.97
Release:        0
%define cpan_name HTML-Template
Summary:        Perl module to use HTML-like templating language
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTML-Template/
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SAMTREGAR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CGI)
BuildRequires:  perl(Test::Pod)
Requires:       perl(CGI)
%{perl_requires}

%description
This module attempts to make using HTML templates simple and natural. It
extends standard HTML with a few new HTML-esque tags - '<TMPL_VAR>'
'<TMPL_LOOP>', '<TMPL_INCLUDE>', '<TMPL_IF>', '<TMPL_ELSE>' and
'<TMPL_UNLESS>'. The file written with HTML and these new tags is called a
template. It is usually saved separate from your script - possibly even
created by someone else! Using this module you fill in the values for the
variables, loops and branches declared in the template. This allows you to
separate design - the HTML - from the data, which you generate in the Perl
script.

This module is licensed under the same terms as Perl. See the LICENSE
section below for more details.

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
%license LICENSE

%changelog
