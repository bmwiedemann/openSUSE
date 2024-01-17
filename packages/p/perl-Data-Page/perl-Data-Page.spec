#
# spec file for package perl-Data-Page
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           perl-Data-Page
Version:        2.03
Release:        0
%define cpan_name Data-Page
Summary:        Help when paging through sets of results
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor::Chained::Fast)
BuildRequires:  perl(Test::Exception)
Requires:       perl(Class::Accessor::Chained::Fast)
%{perl_requires}

%description
When searching through large amounts of data, it is often the case that a
result set is returned that is larger than we want to display on one page.
This results in wanting to page through various pages of data. The maths
behind this is unfortunately fiddly, hence this module.

The main concept is that you pass in the number of total entries, the
number of entries per page, and the current page number. You can then call
methods to find out how many pages of information there are, and what
number the first and last entries on the current page really are.

For example, say we wished to page through the integers from 1 to 100 with
20 entries per page. The first page would consist of 1-20, the second page
from 21-40, the third page from 41-60, the fourth page from 61-80 and the
fifth page from 81-100. This module would help you work this out.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING README
%license LICENCE

%changelog
