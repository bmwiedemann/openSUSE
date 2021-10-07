#
# spec file for package perl-HTML-FillInForm
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name HTML-FillInForm
Name:           perl-HTML-FillInForm
Version:        2.22
Release:        0
#Upstream: Artistic-1.0 or GPL-1.0-or-later
Summary:        Populates HTML Forms with data
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CGI)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(Test::More) >= 0.96
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
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes CONTRIBUTORS README README.md
%license LICENSE

%changelog
