#
# spec file for package perl-DBD-MariaDB
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


%define cpan_name DBD-MariaDB
Name:           perl-DBD-MariaDB
Version:        1.21
Release:        0
Summary:        MariaDB and MySQL driver for the Perl5 Database Interface (DBI)
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PA/PALI/%{cpan_name}-%{version}.tar.gz
Source1:        test-setup.sh
Source2:        test-clean.sh
BuildRequires:  libmariadb-devel
BuildRequires:  mariadb
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  zlib-devel
BuildRequires:  perl(Config)
BuildRequires:  perl(DBI) >= 1.608
BuildRequires:  perl(DBI::Const::GetInfoType)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::CheckLib) >= 1.12
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(Proc::ProcessTable)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.90
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
Requires:       perl(DBI) >= 1.608
Requires:       perl(DynaLoader)
Requires:       perl(strict)
Requires:       perl(warnings)
%{perl_requires}

%description
*DBD::MariaDB* is the Perl5 Database Interface driver for MariaDB and MySQL
databases. In other words: DBD::MariaDB is an interface between the Perl
programming language and the MariaDB/MySQL programming API that comes with
the MariaDB/MySQL relational database management system. Most functions
provided by this programming API are supported. Some rarely used functions
are missing, mainly because no-one ever requested them.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
# Setup environment and start database
. %{SOURCE1}
make %{?_smp_mflags} test
# Stop database
. %{SOURCE2}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%license LICENSE
%doc Changes Changes.historic

%changelog
