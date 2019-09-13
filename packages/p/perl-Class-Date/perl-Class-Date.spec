#
# spec file for package perl-Class-Date
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define cpan_name Class-Date
Name:           perl-Class-Date
Version:        1.1.17
Release:        0
Summary:        Class for easy date and time manipulation
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-Date/
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Scalar::Util) >= 1.38
BuildRequires:  perl(Test::More) >= 1.001
BuildRequires:  perl(Test::Warnings)
%{perl_requires}
# MANUAL
BuildRequires:  timezone

%description
This module is intended to provide a general-purpose date and datetime type
for perl. You have a Class::Date class for absolute date and datetime, and
have a Class::Date::Rel class for relative dates.

You can use "+", "-", "<" and ">" operators as with native perl data types.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README.mkdn CONTRIBUTORS doap.xml

%changelog
