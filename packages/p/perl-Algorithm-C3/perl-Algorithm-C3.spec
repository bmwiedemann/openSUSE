#
# spec file for package perl-Algorithm-C3
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Algorithm-C3
Version:        0.10
Release:        0
%define cpan_name Algorithm-C3
Summary:        A module for merging hierarchies using the C3 algorithm
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Algorithm-C3/
Source:         http://www.cpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module implements the C3 algorithm. I have broken this out into it's
own module because I found myself copying and pasting it way too often for
various needs. Most of the uses I have for C3 revolve around class building
and metamodels, but it could also be used for things like dependency
resolution as well since it tends to do such a nice job of preserving local
precedence orderings.

Below is a brief explanation of C3 taken from the the Class::C3 manpage
module. For more detailed information, see the the SEE ALSO manpage section
and the links there.

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
