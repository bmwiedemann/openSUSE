#
# spec file for package perl-DBIx-Simple
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


Name:           perl-DBIx-Simple
Version:        1.37
Release:        0
#Upstream:  Pick your favourite OSI approved license :) http://www.opensource.org/licenses/alphabetical
%define cpan_name DBIx-Simple
Summary:        Very complete easy-to-use OO interface to DBI
License:        MIT
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/DBIx-Simple/
Source0:        https://cpan.metacpan.org/authors/id/J/JU/JUERD/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBI) >= 1.21
Requires:       perl(DBI) >= 1.21
%{perl_requires}

%description
DBIx::Simple provides a simplified interface to DBI, Perl's powerful
database module.

This module is aimed at rapid development and easy maintenance. Query
preparation and execution are combined in a single method, the result
object (which is a wrapper around the statement handle) provides easy
row-by-row and slurping methods.

The 'query' method returns either a result object, or a dummy object. The
dummy object returns undef (or an empty list) for all methods and when used
in boolean context, is false. The dummy object lets you postpone (or skip)
error checking, but it also makes immediate error checking simply
'$db->query(...) or die $db->error'.

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
