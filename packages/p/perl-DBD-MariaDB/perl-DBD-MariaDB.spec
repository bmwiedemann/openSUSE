#
# spec file for package perl-DBD-MariaDB
#
# Copyright (c) 2022 SUSE LLC
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
Version:        1.22
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        MariaDB and MySQL driver for the Perl5 Database Interface (DBI)
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PA/PALI/%{cpan_name}-%{version}.tar.gz
Source1:        test-setup.sh
Source2:        test-clean.sh
Source3:        cpanspec.yml
Patch0:         perl-DBD-MariaDB-fix_c_32x_test.patch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBI) >= 1.608
BuildRequires:  perl(DBI::Const::GetInfoType)
BuildRequires:  perl(Devel::CheckLib) >= 1.12
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.90
Requires:       perl(DBI) >= 1.608
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  libmariadb-devel
BuildRequires:  mariadb
BuildRequires:  zlib-devel
BuildRequires:  perl(B)
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(Proc::ProcessTable)
BuildRequires:  perl(Storable)
BuildRequires:  perl(TAP::Harness)
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(bigint)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(DynaLoader)
Requires:       perl(strict)
Requires:       perl(warnings)
# MANUAL END

%description
*DBD::MariaDB* is the Perl5 Database Interface driver for MariaDB and MySQL
databases. In other words: DBD::MariaDB is an interface between the Perl
programming language and the MariaDB/MySQL programming API that comes with
the MariaDB/MySQL relational database management system. Most functions
provided by this programming API are supported. Some rarely used functions
are missing, mainly because no-one ever requested them.

%prep
%autosetup  -n %{cpan_name}-%{version} -p1

%build
# fails to detect the paths since perl 5.32
perl Makefile.PL verbose INSTALLDIRS=vendor OPTIMIZE="%{optflags}" --libs="-L%{_libdir} -lmariadb" --cflags="-I%{_includedir}/mysql"
make %{?_smp_mflags}

%check
# Setup environment and start database
. %{SOURCE1}
HARNESS_OPTIONS=j4 make %{?_smp_mflags} test
# Stop database
. %{SOURCE2}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes Changes.historic
%license LICENSE

%changelog
