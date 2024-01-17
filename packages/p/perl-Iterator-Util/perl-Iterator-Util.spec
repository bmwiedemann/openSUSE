#
# spec file for package perl-Iterator-Util
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



Name:           perl-Iterator-Util
%define cpan_name Iterator-Util
Summary:        Essential utilities for the Iterator class
Version:        0.02
Release:        1
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Iterator-Util/
#Source:         http://www.cpan.org/authors/id/R/RO/ROODE/Iterator-Util-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Exception::Class) >= 1.21
BuildRequires:  perl(Iterator) >= 0.01
Requires:       perl(Exception::Class) >= 1.21
Requires:       perl(Iterator) >= 0.01
%{perl_requires}

%description
This module implements many useful functions for creating and manipulating
iterator objects.

An "iterator" is an object, represented as a code block that generates the
"next value" of a sequence, and generally implemented as a closure. For
further information, including a tutorial on using iterator objects, see
the the Iterator manpage documentation.

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
%doc Changes README

%changelog
