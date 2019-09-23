#
# spec file for package perl-Ima-DBI
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


Name:           perl-Ima-DBI
Version:        0.35
Release:        0
%define cpan_name Ima-DBI
Summary:        Database connection caching and organization
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Ima-DBI/
Source:         http://www.cpan.org/authors/id/P/PE/PERRIN/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Data::Inheritable) >= 0.02
BuildRequires:  perl(DBI) >= 1.2
BuildRequires:  perl(DBIx::ContextualFetch) >= 1
#BuildRequires: perl(Ima::DBI)
Requires:       perl(Class::Data::Inheritable) >= 0.02
Requires:       perl(DBI) >= 1.2
Requires:       perl(DBIx::ContextualFetch) >= 1
%{perl_requires}

%description
Ima::DBI attempts to organize and facilitate caching and more efficient use
of database connections and statement handles by storing DBI and SQL
information with your class (instead of as seperate objects). This allows
you to pass around just one object without worrying about a trail of DBI
handles behind it.

One of the things I always found annoying about writing large programs with
DBI was making sure that I didn't have duplicate database handles open. I
was also annoyed by the somewhat wasteful nature of the
prepare/execute/finish route I'd tend to go through in my subroutines. The
new DBI->connect_cached and DBI->prepare_cached helped a lot, but I still
had to throw around global datasource, username and password information.

So, after a while I grew a small library of DBI helper routines and
techniques. Ima::DBI is the culmination of all this, put into a nice(?),
clean(?) class to be inherited from.

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
