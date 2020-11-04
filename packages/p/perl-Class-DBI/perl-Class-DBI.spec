#
# spec file for package perl-Class-DBI
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Class-DBI
Version:        3.0.17
Release:        0
%define cpan_name Class-DBI
Summary:        Simple Database Abstraction
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-DBI/
Source:         http://www.cpan.org/authors/id/T/TM/TMTM/%{cpan_name}-v%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor) >= 0.18
BuildRequires:  perl(Class::Data::Inheritable) >= 0.02
BuildRequires:  perl(Class::Trigger) >= 0.07
BuildRequires:  perl(Clone)
BuildRequires:  perl(Ima::DBI) >= 0.33
BuildRequires:  perl(UNIVERSAL::moniker) >= 0.06
BuildRequires:  perl(version)
Requires:       perl(Class::Accessor) >= 0.18
Requires:       perl(Class::Data::Inheritable) >= 0.02
Requires:       perl(Class::Trigger) >= 0.07
Requires:       perl(Clone)
Requires:       perl(Ima::DBI) >= 0.33
Requires:       perl(UNIVERSAL::moniker) >= 0.06
Requires:       perl(version)
%{perl_requires}

%description
Simple Database Abstraction

%prep
%setup -q -n %{cpan_name}-v%{version}
find . -type f -print0 | xargs -0 chmod 644

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
