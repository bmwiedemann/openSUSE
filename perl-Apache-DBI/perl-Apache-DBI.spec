#
# spec file for package perl-Apache-DBI
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


Name:           perl-Apache-DBI
Version:        1.12
Release:        0
%define cpan_name Apache-DBI
Summary:        Initiate a persistent database connection
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Apache-DBI/
Source0:        http://www.cpan.org/authors/id/P/PH/PHRED/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         Apache-DBI-1.11-path.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBI) >= 1
BuildRequires:  perl(Digest::SHA1) >= 2.01
Requires:       perl(DBI) >= 1
Requires:       perl(Digest::SHA1) >= 2.01
%{perl_requires}

%description
This module initiates a persistent database connection.

The database access uses Perl's DBI. For supported DBI drivers see:

 http://dbi.perl.org/

When loading the DBI module (do not confuse this with the Apache::DBI
module) it checks if the environment variable 'MOD_PERL' has been set and
if the module Apache::DBI has been loaded. In this case every connect
request will be forwarded to the Apache::DBI module. This checks if a
database handle from a previous connect request is already stored and if
this handle is still valid using the ping method. If these two conditions
are fulfilled it just returns the database handle. The parameters defining
the connection have to be exactly the same, including the connect
attributes! If there is no appropriate database handle or if the ping
method fails, a new connection is established and the handle is stored for
later re-use. There is no need to remove the disconnect statements from
your code. They won't do anything because the Apache::DBI module overloads
the disconnect method.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 

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
%doc Changes README TODO traces.txt

%changelog
