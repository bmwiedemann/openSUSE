#
# spec file for package perl-Apache-DBI
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Apache-DBI
Name:           perl-Apache-DBI
Version:        1.120.0
Release:        0
# 1.12 -> normalize -> 1.120.0
%define cpan_version 1.12
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Initiate a persistent database connection
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHRED/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Patch0:         Apache-DBI-1.11-path.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBI) >= 1
BuildRequires:  perl(Digest::SHA1) >= 2.10
Requires:       perl(DBI) >= 1
Requires:       perl(Digest::SHA1) >= 2.10
Provides:       perl(Apache::AuthDBI) = %{version}
Provides:       perl(Apache::DBI) = %{version}
Provides:       perl(Apache::DBI::db)
%undefine       __perllib_provides
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
%autosetup -n %{cpan_name}-%{cpan_version} -N

%patch -P0

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
%doc Changes README TODO traces.txt

%changelog
