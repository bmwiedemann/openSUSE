#
# spec file for package perl-DBIx-Connector
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-DBIx-Connector
Version:        0.56
Release:        0
%define cpan_name DBIx-Connector
Summary:        Fast, safe DBI connection and transaction management
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/DBIx-Connector/
Source0:        http://www.cpan.org/authors/id/D/DW/DWHEELER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBI) >= 1.605
BuildRequires:  perl(Module::Build) >= 0.300000
BuildRequires:  perl(Test::MockModule) >= 0.05
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(DBI) >= 1.605
Recommends:     perl(DBI) >= 1.614
%{perl_requires}

%description
Fast, safe DBI connection and transaction management

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README.md

%changelog
